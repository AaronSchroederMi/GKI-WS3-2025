# Generated from: solver-final (2).ipynb
# Converted at: 2025-12-18T09:17:06.553Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # CSP Solver for Logic Grid Puzzles
# ## AI Connect 2025 - Constraint Satisfaction Problem Solver Challenge
# 
# This notebook implements a complete CSP solver for Zebra/Logic Grid puzzles using:
# - **Backtracking search** with intelligent heuristics
# - **MRV (Minimum Remaining Values)** for variable selection
# - **Forward checking** for early conflict detection
# - **AC-3 algorithm** for arc consistency preprocessing
# - **Step counting** for efficiency evaluation
# 
# ### Competition Evaluation Metrics:
# - **Accuracy:** Percentage of puzzles solved correctly
# - **Efficiency:** Average number of search steps
# - **Composite Score:** `Accuracy (%) - α × (AvgSteps / MaxAvgSteps)` where α = 10


# ## 1. Import Required Libraries


import json
import copy
from collections import deque
from typing import Dict, List, Tuple, Optional, Any
import os
import pandas as pd
from datetime import datetime

print("Libraries imported successfully!")

# ## 2. Load CSP Model from JSON
# 
# The parser team provides JSON files with this structure:
# ```json
# {
#   "metadata": {"problem_name": str, "house_count": int, "attribute_count": int},
#   "variables_and_domains": {
#     "categories": [str],
#     "nodes": [str],
#     "domain_values": {node: [int]}
#   },
#   "constraints": {
#     "puzzle_rules": [{"type": str, "vars": [str], "param": int (optional)}]
#   }
# }
# ```


def load_csp_model(json_path):
    """Load CSP model from JSON file provided by parser team."""
    with open(json_path, 'r') as f:
        data = json.load(f)
    return data

# Test loading
test_file = "zebra_csp_model.json"  # Example file
if os.path.exists(test_file):
    model = load_csp_model(test_file)
    print(f"Loaded: {model['metadata']['problem_name']}")
    print(f"Houses: {model['metadata']['house_count']}")
    print(f"Attributes: {model['metadata']['attribute_count']}")
    print(f"Variables: {len(model['variables_and_domains']['nodes'])}")
    print(f"Constraints: {len(model['constraints']['puzzle_rules'])}")

# ## 3. Constraint Checking Functions
# 
# Each constraint type needs a checking function. Supported constraint types:
# - `ALL_DIFFERENT_CATEGORY`: All variables in a category have different slot assignments
# - `SAME_SLOT`: Two variables must be assigned to the same slot
# - `FIXED_SLOT`: Variable must be at specific slot
# - `NOT_AT`: Variable cannot be at specific slot
# - `NEXT_TO`: Two variables must be in adjacent slots (either order)
# - `DIRECTLY_LEFT`: Var1 must be directly left of Var2 (slot difference = 1)
# - `DIRECTLY_RIGHT`: Var1 must be directly right of Var2 (slot difference = 1)
# - `LEFT_OF`: Var1 must be somewhere left of Var2 (slot1 < slot2)
# - `SOMEWHERE_TO_THE_LEFT`: Same as LEFT_OF
# - `SOMEWHERE_TO_THE_RIGHT`: Var1 must be somewhere right of Var2 (slot1 > slot2)
# - `ONE_HOUSE_BETWEEN`: Exactly 1 slot between two variables (|slot1 - slot2| = 2)
# - `TWO_HOUSE_BETWEEN`: Exactly 2 slots between two variables (|slot1 - slot2| = 3)


def check_constraint(constraint, assignment):
    """Check if a constraint is satisfied given current assignment."""
    ctype = constraint['type']
    vars_list = constraint['vars']
    
    # Check if all variables in constraint are assigned
    if not all(var in assignment for var in vars_list):
        return True  # Can't violate if not all assigned
    
    if ctype == 'ALL_DIFFERENT_CATEGORY':
        # All variables must have different values
        values = [assignment[var] for var in vars_list]
        return len(values) == len(set(values))
    
    elif ctype == 'SAME_SLOT':
        # Two variables must have same value
        return assignment[vars_list[0]] == assignment[vars_list[1]]
    
    elif ctype == 'FIXED_SLOT':
        # Variable must be at specific slot
        return assignment[vars_list[0]] == constraint['param']
    
    elif ctype == 'NOT_AT':
        # Variable cannot be at specific slot
        return assignment[vars_list[0]] != constraint['param']
    
    elif ctype == 'NEXT_TO':
        # Adjacent slots (either order)
        val1, val2 = assignment[vars_list[0]], assignment[vars_list[1]]
        return abs(val1 - val2) == 1
    
    elif ctype == 'DIRECTLY_LEFT':
        # var1 is directly left of var2 (var1 + 1 == var2)
        val1, val2 = assignment[vars_list[0]], assignment[vars_list[1]]
        return val1 + 1 == val2
    
    elif ctype == 'DIRECTLY_RIGHT':
        # var1 is directly right of var2 (var1 - 1 == var2)
        val1, val2 = assignment[vars_list[0]], assignment[vars_list[1]]
        return val1 - 1 == val2
    
    elif ctype in ['LEFT_OF', 'SOMEWHERE_TO_THE_LEFT']:
        # var1 is somewhere left of var2 (var1 < var2)
        val1, val2 = assignment[vars_list[0]], assignment[vars_list[1]]
        return val1 < val2
    
    elif ctype == 'SOMEWHERE_TO_THE_RIGHT':
        # var1 is somewhere right of var2 (var1 > var2)
        val1, val2 = assignment[vars_list[0]], assignment[vars_list[1]]
        return val1 > val2
    
    elif ctype == 'ONE_HOUSE_BETWEEN':
        # Exactly one house between (|val1 - val2| = 2)
        val1, val2 = assignment[vars_list[0]], assignment[vars_list[1]]
        return abs(val1 - val2) == 2
    
    elif ctype == 'TWO_HOUSE_BETWEEN':
        # Exactly two houses between (|val1 - val2| = 3)
        val1, val2 = assignment[vars_list[0]], assignment[vars_list[1]]
        return abs(val1 - val2) == 3
    elif ctype == 'NOT_SAME_SLOT':
        return assignment[vars_list[0]] != assignment[vars_list[1]]
    
    else:
        raise ValueError(f"Unknown constraint type: {ctype}")

def is_consistent(var, value, assignment, constraints):
    """Check if assigning value to var is consistent with current assignment."""
    test_assignment = assignment.copy()
    test_assignment[var] = value
    
    # Check all constraints
    for constraint in constraints:
        if var in constraint['vars']:
            if not check_constraint(constraint, test_assignment):
                return False
    return True

# ## 4. AC-3 Algorithm (Arc Consistency)
# 
# AC-3 preprocesses the CSP by enforcing arc consistency, reducing domain sizes before search.


def ac3(domains, constraints):
    """
    AC-3 algorithm to enforce arc consistency.
    Returns updated domains or None if inconsistency detected.
    """
    domains = {var: set(dom) for var, dom in domains.items()}
    
    # Create queue of all arcs
    queue = deque()
    for constraint in constraints:
        vars_list = constraint['vars']
        if len(vars_list) >= 2:
            # Add arcs in both directions
            queue.append((vars_list[0], vars_list[1], constraint))
            queue.append((vars_list[1], vars_list[0], constraint))
    
    while queue:
        var1, var2, constraint = queue.popleft()
        
        if revise(var1, var2, constraint, domains):
            if len(domains[var1]) == 0:
                return None  # Inconsistency detected
            
            # Add neighbors back to queue
            for other_constraint in constraints:
                if var1 in other_constraint['vars']:
                    for var in other_constraint['vars']:
                        if var != var1:
                            queue.append((var, var1, other_constraint))
    
    return {var: list(dom) for var, dom in domains.items()}

def revise(var1, var2, constraint, domains):
    """
    Revise domain of var1 based on constraint with var2.
    Returns True if domain of var1 was revised.
    """
    revised = False
    to_remove = []
    
    for val1 in domains[var1]:
        # Check if there exists a value in var2's domain that satisfies constraint
        satisfiable = False
        for val2 in domains[var2]:
            assignment = {var1: val1, var2: val2}
            if check_constraint(constraint, assignment):
                satisfiable = True
                break
        
        if not satisfiable:
            to_remove.append(val1)
            revised = True
    
    for val in to_remove:
        domains[var1].discard(val)
    
    return revised

# ## 5. Forward Checking
# 
# Forward checking prunes domains of unassigned variables after each assignment.


def forward_check(var, value, domains, assignment, constraints):
    """
    After assigning value to var, prune domains of unassigned neighbors.
    Returns updated domains or None if any domain becomes empty.
    """
    new_domains = {v: list(d) for v, d in domains.items()}
    
    # Find constraints involving the assigned variable
    for constraint in constraints:
        if var not in constraint['vars']:
            continue
        
        # Check other variables in this constraint
        for other_var in constraint['vars']:
            if other_var == var or other_var in assignment:
                continue
            
            # Prune values from other_var's domain
            valid_values = []
            for val in new_domains[other_var]:
                test_assignment = assignment.copy()
                test_assignment[var] = value
                test_assignment[other_var] = val
                
                if check_constraint(constraint, test_assignment):
                    valid_values.append(val)
            
            new_domains[other_var] = valid_values
            
            # Domain wipeout
            if len(valid_values) == 0:
                return None
    
    return new_domains

# ## 6. MRV Heuristic (Minimum Remaining Values)
# 
# Select the variable with the smallest domain size for assignment.


def select_unassigned_variable(variables, domains, assignment):
    """
    MRV heuristic: Select variable with smallest domain.
    Tie-breaking: Choose first in list.
    """
    unassigned = [var for var in variables if var not in assignment]
    
    if not unassigned:
        return None
    
    # Select variable with minimum remaining values
    return min(unassigned, key=lambda var: len(domains[var]))

# ## 7. Backtracking Search
# 
# Main CSP solver using backtracking with forward checking and MRV.


def backtracking_search(variables, domains, constraints):
    """
    Backtracking search with forward checking and MRV.
    Returns (solution, steps) where solution is assignment dict or None.
    """
    steps = [0]  # Use list to allow modification in nested function
    
    def backtrack(assignment, domains):
        steps[0] += 1
        
        # Check if assignment is complete
        if len(assignment) == len(variables):
            return assignment
        
        # Select variable using MRV heuristic
        var = select_unassigned_variable(variables, domains, assignment)
        
        if var is None:
            return None
        
        # Try each value in the variable's domain
        for value in domains[var]:
            # Check consistency
            if is_consistent(var, value, assignment, constraints):
                # Make assignment
                new_assignment = assignment.copy()
                new_assignment[var] = value
                
                # Forward checking
                new_domains = forward_check(var, value, domains, assignment, constraints)
                
                if new_domains is not None:
                    result = backtrack(new_assignment, new_domains)
                    if result is not None:
                        return result
        
        return None
    
    solution = backtrack({}, domains)
    return solution, steps[0]

# ## 8. CSP Solver Class
# 
# Combines all components into a complete solver.


class CSPSolver:
    def __init__(self, model):
        """Initialize solver with CSP model from JSON."""
        self.metadata = model['metadata']
        self.categories = model['variables_and_domains']['categories']
        self.nodes = model['variables_and_domains']['nodes']
        self.domain_values = model['variables_and_domains']['domain_values']
        self.constraints = model['constraints']['puzzle_rules']
        
    def solve(self):
        """
        Solve the CSP problem.
        Returns (solution_dict, steps) or (None, steps) if no solution.
        """
        # Apply AC-3 preprocessing
        domains = ac3(self.domain_values, self.constraints)
        
        if domains is None:
            return None, 0
        
        # Run backtracking search
        solution, steps = backtracking_search(
            self.nodes,
            domains,
            self.constraints
        )
        
        return solution, steps
    
    def format_solution(self, solution):
        """
        Format solution as grid with header and rows.
        Returns JSON string in competition format.
        """
        if solution is None:
            return None
        
        house_count = self.metadata['house_count']
        
        # Create header row (category names)
        header = ['House']
        [header.append(tmp) for tmp in self.categories.copy()]

        # Create data rows (one per slot/house)
        rows = []
        for slot in range(1, house_count + 1):
            row = [str(slot)]
            for node in self.nodes:
                if solution[node] == slot:
                    row.append(node)
            rows.append(row)

        
        grid = {
            "header": header,
            "rows": rows
        }

        return json.dumps(grid)

# ## 10. Batch Processing
# 
# Process all JSON files in a directory and generate results.


def solve_all_puzzles(input_dir=None, input_frame=pd.DataFrame, output_file="results.csv"):
    """
    Solve all JSON files in input_dir and save results to CSV.
    Output format: id | grid_solution | steps
    """
    import glob
    
    # Find all JSON files or frame
    if input_dir is not None:
        json_files = glob.glob(os.path.join(input_dir, "*.json"))
        if not json_files:
            print("No JSON files found in directory")
            return None
    elif input_frame is not None:
        json_files = list(input_frame)
    else:
        print("No JSON files or Dataframe found")
        return None

    
    print(f"Found {len(json_files)} JSONs to process")
    
    results = []
    
    for i, json_file in enumerate(json_files, 1):
        if input_dir is not None:
            filename = os.path.basename(json_file)
            print(f"[{i}/{len(json_files)}] Processing {filename}...", end=" ")
        
        try:
            # Load model
            if input_dir is not None:
                model = load_csp_model(json_file)
            else:
                model = json_file
            problem_id = model['metadata']['problem_name']
            
            # Create solver and solve
            solver = CSPSolver(model)
            solution, steps = solver.solve()
            
            # Format solution
            grid_json = solver.format_solution(solution)
            
            if grid_json:
                results.append({
                    'id': problem_id,
                    'grid_solution': grid_json,
                    'steps': steps
                })
                print(f"✓ Solved in {steps} steps")
            else:
                results.append({
                    'id': problem_id,
                    'grid_solution': None,
                    'steps': steps
                })
                print(f"✗ No solution found")
                
        except Exception as e:
            print(f"✗ Error: {str(e)}")
            results.append({
                'id': filename,
                'grid_solution': None,
                'steps': 0
            })
    
    # Save results to CSV
    df = pd.DataFrame(results)
    df.to_csv(output_file, index=False)
    print(f"\n✓ Results saved to {output_file}")
    
    # Print summary
    solved = df['grid_solution'].notna().sum()
    total = len(df)
    accuracy = (solved / total) * 100 if total > 0 else 0
    avg_steps = df[df['grid_solution'].notna()]['steps'].mean()
    
    print(f"\nSummary:")
    print(f"  Total puzzles: {total}")
    print(f"  Solved: {solved}")
    print(f"  Accuracy: {accuracy:.2f}%")
    print(f"  Average steps: {avg_steps:.2f}")
    
    return df

# ## 11. Run Batch Processing
# 
# Uncomment and run to process all puzzles in the directory.


# Run batch processing on all JSON files
# Uncomment to execute:

'''results_df = solve_all_puzzles(input_dir="json", output_file="results.csv")
print("\n" + "="*50)
print("Competition submission file 'results.csv' is ready!")
print("="*50)'''

# ## 12. Evaluation Metrics
# 
# Calculate competition metrics from results.


def calculate_metrics(results_df, alpha=10, max_avg_steps=10000):
    """
    Calculate competition evaluation metrics.
    
    Metrics:
    - Accuracy: Percentage of puzzles solved correctly
    - Average Steps: Mean number of backtracking steps for solved puzzles
    - Composite Score: Accuracy - α × (AvgSteps / MaxAvgSteps)
    
    Args:
        results_df: DataFrame with columns [id, grid_solution, steps]
        alpha: Weight parameter for composite score (default: 10)
        max_avg_steps: Maximum average steps for normalization (default: 10000)
    """
    total_puzzles = len(results_df)
    solved_puzzles = results_df['grid_solution'].notna().sum()
    
    # Accuracy (percentage)
    accuracy = (solved_puzzles / total_puzzles * 100) if total_puzzles > 0 else 0
    
    # Average steps (only for solved puzzles)
    solved_df = results_df[results_df['grid_solution'].notna()]
    avg_steps = solved_df['steps'].mean() if len(solved_df) > 0 else 0
    
    # Composite score
    composite_score = accuracy - alpha * (avg_steps / max_avg_steps)
    
    print("="*60)
    print("COMPETITION EVALUATION METRICS")
    print("="*60)
    print(f"Total Puzzles:        {total_puzzles}")
    print(f"Solved Puzzles:       {solved_puzzles}")
    print(f"Unsolved Puzzles:     {total_puzzles - solved_puzzles}")
    print("-"*60)
    print(f"Accuracy:             {accuracy:.2f}%")
    print(f"Average Steps:        {avg_steps:.2f}")
    print(f"Composite Score:      {composite_score:.4f}")
    print("="*60)
    print(f"\nFormula: Composite Score = Accuracy - {alpha} × (AvgSteps / {max_avg_steps})")
    
    return {
        'total_puzzles': total_puzzles,
        'solved_puzzles': solved_puzzles,
        'accuracy': accuracy,
        'avg_steps': avg_steps,
        'composite_score': composite_score
    }

# Example: Load and evaluate results
# df = pd.read_csv('results.csv')
# metrics = calculate_metrics(df)