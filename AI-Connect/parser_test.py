# Generated from: test-parser-final (2).ipynb
# Converted at: 2025-12-18T09:17:29.197Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# # Specialized Test File Parser for Logic Grid Puzzles
# 
# This notebook provides a specialized parser for the Test CSV file format that differs from the standard grid_mode and mc_mode parquet files.
# 
# **Key Differences:**
# 1. Size is provided in a separate column (`size` field) instead of embedded in the ID
# 2. Categories are extracted differently from the puzzle text
# 3. Constraint parsing has specific handling for test format clues


# Import Required Libraries
import numpy as np
import pandas as pd
import pprint
import re
import json
import os

# ## Load Test CSV File


def print_csv_info():
    # Load the CSV file
    test_file_path = 'Test_100_Puzzles.csv'
    df_test = pd.read_csv(test_file_path)

    print(f"Test CSV shape: {df_test.shape}")
    print(f"Test CSV columns: {df_test.columns.tolist()}")
    print(f"\nFirst row:")
    print(df_test.iloc[0])

    # Test on first few rows
    print("Testing parser on first 5 rows...")
    for idx in range(min(5, len(df_test))):
        try:
            result = parse_problem_test(df_test.iloc[idx])
            print(f"✓ Successfully parsed: {result}")
        except Exception as e:
            print(f"✗ Error parsing row {idx}: {e}")

    # Process all test puzzles in batch
    print(f"Processing {len(df_test)} test puzzles...")
    results = []
    errors = []

    for idx, row in df_test.iterrows():
        try:
            result = parse_problem_test(row)
            results.append(result)
            if (idx + 1) % 10 == 0:
                print(f"Processed {idx + 1}/{len(df_test)} puzzles")
        except Exception as e:
            errors.append({'id': row['id'], 'error': str(e)})
            if (idx + 1) % 10 == 0:
                print(f"Processed {idx + 1}/{len(df_test)} puzzles (with {len(errors)} errors)")

    print(f"\n✓ Successfully processed: {len(results)} puzzles")
    print(f"✗ Failed: {len(errors)} puzzles")

    if errors:
        print("\nFirst 5 errors:")
        for error in errors[:5]:
            print(f"  - {error['id']}: {error['error']}")

    # Generate summary statistics
    print("=" * 60)
    print("TEST FILE PARSER - SUMMARY REPORT")
    print("=" * 60)

    print(f"\nDataset Statistics:")
    print(f"  Total test puzzles: {len(df_test)}")

    size_counts = df_test['size'].value_counts()
    print(f"\nPuzzle size distribution:")
    for size, count in size_counts.sort_index().items():
        h, a = parse_size_from_field(size)
        print(f"  {size} ({h} houses × {a} attributes): {count} puzzles")

    print(f"\n" + "="*60)
    print("KEY DIFFERENCES FROM ORIGINAL PARSER")
    print("="*60)
    print(f"1. Size parsing:")
    print(f"   - Original: Extract from puzzle ID (e.g., 'lgp-test-5x6-16')")
    print(f"   - Test CSV: Parse from 'size' column (e.g., '5*6')")
    print(f"\n2. Categories extraction:")
    print(f"   - Original: Extract from backtick-delimited nodes in text")
    print(f"   - Test CSV: Extract from explicit category headers (Colors:, Pets:, etc.)")
    print(f"\n3. Constraint parsing:")
    print(f"   - Both handle similar constraint types but test CSV has different")
    print(f"     text patterns and clue formatting")
    print(f"\n4. Node extraction:")
    print(f"   - Original: Backtick-enclosed values")
    print(f"   - Test CSV: Comma-separated values from category lines")
    print(f"              + Name extraction from capitalized words in clues")

    print(f"\n" + "="*60)
    print("USAGE EXAMPLE")
    print("="*60)
    print("""
    # Load the test CSV file
    df_test = pd.read_csv('Test_100_Puzzles.csv')

    # Parse all puzzles
    for idx, row in df_test.iterrows():
        parse_problem_test(row)

    # Output: Individual JSONs for each problem
    """)

    print("="*60)

    # Process all test puzzles
    print(f"Processing {len(df_test)} puzzles...")
    print()

    processed_count = 0
    error_count = 0
    error_details = []

    for idx, row in df_test.iterrows():
        try:
            result = parse_problem_test(row)
            processed_count += 1
            if (processed_count) % 20 == 0:
                print(f"Processed {processed_count}/{len(df_test)} puzzles")
        except Exception as e:
            error_count += 1
            error_details.append((row['id'], str(e)))
            if error_count <= 5:  # Show first 5 errors
                print(f"✗ Error for {row['id']}: {e}")

    print()
    print(f"Processing complete!")
    print(f"Successfully parsed: {processed_count}/{len(df_test)}")
    print(f"Errors: {error_count}")

    if error_details:
        print(f"\nFirst few errors:")
        for puzzle_id, error in error_details[:5]:
            print(f"  - {puzzle_id}: {error}")

# ## Helper Functions - Adapted for Test CSV Format
# 
# These functions are adapted from the original parser with modifications for the CSV test format.


def parse_size_from_field(size_field: str) -> tuple[int, int]:
    """
    Parse size field from CSV test file.
    Format: "3*3" -> (3, 3)
    where first number is house_count and second is attribute_count
    
    size_field: string in format "X*Y"
    returns: tuple (house_count, attribute_count)
    """
    match = re.match(r'(\d+)\*(\d+)', size_field)
    if not match:
        raise ValueError(f"Invalid size format: {size_field}")
    house_count = int(match.group(1))
    attribute_count = int(match.group(2))
    return house_count, attribute_count

def create_nodes_test(clues: str, attribute_count: int, house_count: int) -> list[str]:
    """
    Creates nodes from category descriptions and clues in test format.
    For test CSV, nodes are extracted from "Category: item1, item2, item3" lines,
    and names are extracted from capitalized words in the clues section.
    
    clues: natural language description of problem
    attribute_count: amount of unique attributes in each house
    house_count: amount of houses
    
    returns: list of strings (representing each instance of each attribute)
    """
    nodes = []
    categories_dict = {}
    
    lines = clues.split('\n')
    
    # Extract categories and their values
    for line in lines:
        line = line.strip()
        if ':' in line:
            parts = line.split(':', 1)
            if len(parts) == 2:
                category_name = parts[0].strip()
                items_str = parts[1].strip()
                
                # Skip "Clues:" line, numbered lines, and empty items
                if category_name and not category_name[0].isdigit() and category_name.lower() != 'clues' and items_str:
                    # Only process if items_str contains comma-separated values
                    if ',' in items_str:
                        items = [item.strip().rstrip('.') for item in items_str.split(',')]
                        # Filter out empty strings
                        items = [item for item in items if item.strip()]
                        if items:
                            categories_dict[category_name] = items
    
    # Extract names from clues if we don't have a Names category yet
    if 'Names' not in categories_dict and len(categories_dict) < attribute_count:
        # Find the clues section
        clues_text = clues
        if 'Clues:' in clues:
            clues_text = clues.split('Clues:')[1]
        
        # Extract capitalized words (potential names)
        name_pattern = r'\b([A-Z][a-z]+)\b'
        potential_names = re.findall(name_pattern, clues_text)
        
        # Filter unique names, excluding common words
        exclude_words = {'The', 'House', 'Each', 'All', 'No', 'Directly', 'Someone', 'One', 'First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 'Does', 'In', 'Is', 'Not', 'Live', 'Lives', 'Clues', 'Pets', 'Colors', 'Clue'}
        unique_names = []
        seen = set()
        for name in potential_names:
            if name not in exclude_words and name not in seen:
                unique_names.append(name)
                seen.add(name)
        
        # Add names as a category if we found them
        if unique_names:
            if len(unique_names) < house_count:
                unique_names.append('PersonUnknown1')
            if len(unique_names) < house_count:
                unique_names.append('PersonUnknown2')
            categories_dict['Names'] = unique_names[:house_count]
    
    # Build nodes list from categories in a consistent order
    # Order: Names, then other categories alphabetically
    ordered_categories = []
    if 'Names' in categories_dict:
        ordered_categories.append('Names')
    
    # Add other categories in alphabetical order
    for cat_name in sorted(categories_dict.keys()):
        if cat_name != 'Names':
            ordered_categories.append(cat_name)
    
    for cat_name in ordered_categories:
        nodes.extend(categories_dict[cat_name])
    
    if len(nodes) == attribute_count * house_count:
        return nodes
    
    raise ValueError(f"Expected {attribute_count * house_count} nodes, got {len(nodes)}. Categories: {list(categories_dict.keys())}")


def create_categories_test(clues: str, has_names: bool = True) -> list[str]:
    """
    Creates categories by parsing the puzzle description.
    For test format, categories are explicitly listed after labels like "Colors:", "Pets:", etc.
    Categories are identified by lines that end with a colon and contain comma-separated items.
    Returns categories in singular form (Color, Pet, Name) in proper order.
    Also includes 'Name' category if names are extracted from clues.
    
    clues: natural language description of problem
    has_names: whether names were extracted from clues (affects category list)
    
    returns: list of strings (representing each attribute category) in order: Name, Color, Pet, etc.
    """
    categories = []
    lines = clues.split('\n')
    
    # Mapping from plural to singular forms
    singular_map = {
        'Colors': 'Color',
        'Pets': 'Pet',
        'Names': 'Name',
        'People': 'Person',
        'Professions': 'Profession',
        'Ages': 'Age',
        'Hobbies': 'Hobby',
        'Drinks': 'Drink',
        'Houses': 'House',
        'Cars': 'Car',
        'Flowers': 'Flower',
    }
    
    raw_categories = []
    for line in lines:
        line = line.strip()
        # Check if line has category: items format with commas
        if ':' in line and ',' in line and line.lower() != 'clues:':
            parts = line.split(':')
            if len(parts) == 2:
                category_name = parts[0].strip()
                items_str = parts[1].strip()
                # Check if this looks like a category header (not a numbered line)
                if category_name and not category_name[0].isdigit() and items_str:
                    # Apply singular form if available
                    singular_name = singular_map.get(category_name, category_name)
                    raw_categories.append(singular_name)
    
    # Build final category list: Name should come first (if present)
    if has_names:
        categories.append('Name')
    
    # Add other categories in their original order (from puzzle)
    for cat in raw_categories:
        if cat != 'Name':
            categories.append(cat)
    
    return categories


def create_domain_space(nodes: list[str], house_count: int) -> dict:
    """
    Creates the domain space for all nodes from existing nodes and house_count.
    
    nodes: list of strings (representing each instance of each attribute)
    house_count: number of house options (e.g. 1-4, 1-7)
    
    returns: dict with keys for each domain space containing lists of all options
    """
    domain = {}
    for node in nodes:
        domain[node] = list(range(1, house_count + 1))
    
    return domain

def create_all_different_constraints(constraints: list[dict], nodes: list[str], 
                                     house_count: int, attribute_count: int) -> list[dict]:
    """
    Creates ALL_DIFFERENT_CATEGORY constraints for each attribute.
    
    constraints: list that will be returned with appended constraints
    nodes: list of each instance of each attribute
    house_count: number of houses (used here as number of instance of each attribute)
    attribute_count: number of attributes
    
    returns: list of ALL_DIFFERENT_CATEGORY constraints
    """
    for i in range(attribute_count):
        constraints.append({
            'type': 'ALL_DIFFERENT_CATEGORY',
            'vars': nodes[0 + house_count * i:house_count * (i + 1)]
        })
    
    if len(constraints) != attribute_count:
        raise ValueError(f'ALL_DIFFERENT_CATEGORY count mismatch: expected {attribute_count}, got {len(constraints)}')
    
    return constraints

def fix_pattern_typos(pattern: str) -> str:
    """
    Changes certain identifiers that differ between clues and problem description 
    to ensure parity with the clues.
    
    pattern: A string that contains all instances of the attributes
    
    returns: the string with differing items replaced (parity with clues)
    """
    typos = {
        'brit': 'British',
        'hip hop': 'hip-hop',
        'cruise': 'cruises',
        'feb': 'February',
        'jan': 'January',
        'sept': 'September',
        'roses': 'rose bouquet',
        'horse': 'horses',
        'swede': 'Swedish',
        'mar': 'March',
        'painting': 'paints',
        'ford f150': 'Ford F-150'
    }
    
    for old, new in typos.items():
        pattern = pattern.replace(old, new)
    return pattern


def reverse_pattern_typo_fix(vars: list[str]) -> list[str]:
    """
    Changes certain identifiers that differ between clues and problem description 
    to ensure parity with the description.
    
    vars: A list containing all instances of the attributes
    
    returns: the list with differing items replaced (parity with description)
    """
    typos = {
        'British': 'brit',
        'hip-hop': 'hip hop',
        'cruises': 'cruise',
        'February': 'feb',
        'January': 'jan',
        'September': 'sept',
        'rose bouquet': 'roses',
        'horses': 'horse',
        'Swedish': 'swede',
        'March': 'mar',
        'paints': 'painting',
        'Ford F-150': 'ford f150'
    }
    
    new_vars = []
    for var in vars:
        tmp_var = typos.get(var, var)
        new_vars.append(tmp_var)
    
    return new_vars

def house_number_to_integer(token: str) -> int:
    """
    Converts ordinal words ('First', 'Second', etc.) into integer values.
    
    token: This is a string of just one clue with the type (FIXED_SLOT or NOT_AT)
    
    returns: an int representing the house number for the constraint
    """
    param = -1
    tmp = re.findall(r'(First|Second|Third|Fourth|Fifth|Sixth)', token, re.IGNORECASE)
    if len(tmp) != 1:
        raise ValueError(f'HOUSE_NUMBER was recognised incorrectly: {token}')
    
    match tmp[0].lower():
        case 'first':
            param = 1
        case 'second':
            param = 2
        case 'third':
            param = 3
        case 'fourth':
            param = 4
        case 'fifth':
            param = 5
        case 'sixth':
            param = 6
    
    return param

def create_constraints(clues: str, nodes: list[str], house_count: int, attribute_count: int) -> list[dict]:
    """
    Creates the constraints for all clues.
    
    clues: natural language description of problem
    nodes: list of strings (representing each instance of each attribute)
    house_count: number of houses
    attribute_count: number of attributes
    
    returns: list of constraints (each constraint is a dict with type, vars, and optional param)
    """
    constraints = []
    constraints = create_all_different_constraints(constraints, nodes,
                                                   house_count, attribute_count)
    
    # Extract clues from the "Clues:" section only to avoid false positives
    if 'Clues:' in clues:
        clues_section = clues.split('Clues:')[1]
    else:
        clues_section = clues
    
    # Extract numbered clues using a better regex that won't catch false positives
    # This regex matches "1. ..." up to the next number or end of string
    tokens = re.findall(r'^[0-9]+\..+?(?=^[0-9]+\.|$)', clues_section, re.MULTILINE | re.DOTALL)
    
    for token in tokens:
        # Find all variable mentions in this token
        pattern = r'\b(' + '|'.join(nodes) + r')\b'
        pattern = fix_pattern_typos(pattern)
        vars = re.findall(pattern, token, re.IGNORECASE)
        vars = reverse_pattern_typo_fix(vars)

        # Skip constraints with no variables
        if not vars:
            raise ValueError

        # Check for "does not live in" / "not in the" pattern first (more specific)
        if re.search(r'does not live in|not in the', token, re.IGNORECASE):
            try:
                constraints.append({
                    'type': 'NOT_SAME_SLOT',
                    'vars': vars
                })
                continue
            except:
                pass

        # Check for "somewhere to the left"
        if re.search(r'somewhere to the left', token, re.IGNORECASE):
            if len(vars) == 2:
                constraints.append({
                    'type': 'SOMEWHERE_TO_THE_LEFT',
                    'vars': vars
                })
                continue

        # Check for "somewhere to the right"
        if re.search(r'somewhere to the right', token, re.IGNORECASE):
            if len(vars) == 2:
                constraints.append({
                    'type': 'SOMEWHERE_TO_THE_RIGHT',
                    'vars': vars
                })
                continue

        # Check for "lives in house X" or "in the X house" (FIXED_SLOT)
        if re.search(r'lives in house|is in the|in house|House', token, re.IGNORECASE):
            try:
                # Try to extract numeric house number first (e.g., "house 3")
                house_match = re.search(r'house\s+([0-9]+)', token, re.IGNORECASE)
                if house_match:
                    param = int(house_match.group(1))
                    if len(vars) == 1 and 1 <= param <= house_count:
                        constraints.append({
                            'type': 'FIXED_SLOT',
                            'vars': vars,
                            'param': param
                        })
                        continue
                else:
                    # Try ordinal form (First, Second, etc.)
                    param = house_number_to_integer(token)
                    if param != -1 and len(vars) == 1:
                        constraints.append({
                            'type': 'FIXED_SLOT',
                            'vars': vars,
                            'param': param
                        })
                        continue
            except:
                pass

        # Check for "directly left" / "immediately to the left"
        if re.search(r'directly left|immediately to the left', token, re.IGNORECASE):
            if len(vars) == 2:
                constraints.append({
                    'type': 'DIRECTLY_LEFT',
                    'vars': vars
                })
                continue

        # Check for "directly right" / "immediately to the right"
        if re.search(r'directly right|immediately to the right', token, re.IGNORECASE):
            if len(vars) == 2:
                constraints.append({
                    'type': 'DIRECTLY_RIGHT',
                    'vars': vars
                })
                continue

        # Check for "one house between"
        if re.search(r'one house between', token, re.IGNORECASE):
            if len(vars) == 2:
                constraints.append({
                    'type': 'ONE_HOUSE_BETWEEN',
                    'vars': vars
                })
                continue

        # Check for "next to" / "adjacent"
        if re.search(r'next to|adjacent', token, re.IGNORECASE):
            if len(vars) == 2:
                constraints.append({
                    'type': 'NEXT_TO',
                    'vars': vars
                })
                continue

        # Check for "two houses between"
        if re.search(r'two houses between', token, re.IGNORECASE):
            if len(vars) == 2:
                constraints.append({
                    'type': 'TWO_HOUSE_BETWEEN',
                    'vars': vars
                })
                continue

        # Generic "is" constraint for attribute associations (must be 2 variables and no house refs)\
        # Make sure it's not a "is in house" or similar (already handled above)
        if re.search(r'house|contains|lives in the|owns', token, re.IGNORECASE):
            constraints.append({
                'type': 'SAME_SLOT',
                'vars': vars
            })
            continue

    return constraints


# ## Main Parsing Function


def parse_problem_test(row):
    """
    Main parsing function for test CSV format.
    Extracts puzzle data and builds JSON-like structure.
    
    row: a row of the dataframe
    
    returns: problem ID if successful
    """
    # Parse size from size field (CSV column)
    tmp_house_count, tmp_attribute_count = parse_size_from_field(row['size'])
    
    has_names_extracted = False
    
    try:
        tmp_nodes = create_nodes_test(
            clues=row['puzzle'],
            attribute_count=tmp_attribute_count,
            house_count=tmp_house_count
        )
        # If successful, names were extracted if we got attribute_count * house_count nodes
        # and the first house_count nodes are person names
        has_names_extracted = True
    except ValueError as e:
        # If exact node count fails, still proceed with what we have
        # Extract categories and names separately
        lines = row['puzzle'].split('\n')
        tmp_nodes = []
        
        # Extract from explicit categories
        categories_dict = {}
        for line in lines:
            line = line.strip()
            if ':' in line and ',' in line and line.lower() != 'clues:':
                parts = line.split(':', 1)
                if len(parts) == 2:
                    items = [item.strip().rstrip('.') for item in parts[1].split(',')]
                    tmp_nodes.extend([item for item in items if item])
                    # Track which categories we found
                    category_name = parts[0].strip()
                    if not category_name[0].isdigit():
                        categories_dict[category_name] = [item for item in items if item]
        
        # If we don't have enough nodes, try to extract names from clues
        if len(tmp_nodes) < tmp_attribute_count * tmp_house_count:
            clues_text = row['puzzle']
            if 'Clues:' in clues_text:
                clues_text = clues_text.split('Clues:')[1]
            
            name_pattern = r'\b([A-Z][a-z]+)\b'
            potential_names = re.findall(name_pattern, clues_text)
            
            exclude_words = {'The', 'House', 'Each', 'All', 'No', 'Directly', 'Someone', 'One', 'First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 'Does', 'In', 'Is', 'Not', 'Live', 'Lives', 'Clues', 'Pets', 'Colors', 'Clue'}
            unique_names = []
            seen = set()
            for name in potential_names:
                if name not in exclude_words and name not in seen:
                    unique_names.append(name)
                    seen.add(name)
            
            # Add extracted names to the beginning of tmp_nodes
            if unique_names:
                names_to_add = unique_names[:tmp_house_count]
                tmp_nodes = names_to_add + tmp_nodes
                has_names_extracted = True
        
        # If we still don't have enough, leave as is - partial parsing
        if len(tmp_nodes) < tmp_attribute_count * tmp_house_count:
            print(f"Warning: Incomplete node parsing for {row['id']}")
    
    categories = create_categories_test(row['puzzle'], has_names=has_names_extracted)
    
    try:
        constraints = create_constraints(
            clues=row['puzzle'],
            nodes=tmp_nodes,
            house_count=tmp_house_count,
            attribute_count=tmp_attribute_count
        )
    except Exception as e:
        print(f"Error parsing constraints for {row['id']}: {e}")
        constraints = []
    
    data = {
        "metadata": {
            "problem_name": row['id'],
            "attribute_count": tmp_attribute_count,
            "house_count": tmp_house_count,
            "created_at": row['created_at']
        },
        "variables_and_domains": {
            "categories": categories,
            "domain_values": create_domain_space(
                nodes=tmp_nodes,
                house_count=tmp_house_count
            ),
            "nodes": tmp_nodes,
        },
        "constraints": {
            "puzzle_rules": constraints
        },
    }
    
    return data

# ## Compare with Expected Results (sample_result.csv)


# Load sample results to understand expected output format
'''df_sample = pd.read_csv('sample_result.csv')

print("Sample result structure:")
print(f"Shape: {df_sample.shape}")
print(f"Columns: {df_sample.columns.tolist()}")
print("\nFirst row:")
print(df_sample.iloc[0])

print("\n\nExpected grid_solution format:")
solution_json = json.loads(df_sample.iloc[0]['grid_solution'])
pprint.pprint(solution_json)'''

# ## Validate Parsed JSON Structure


# Validate structure of parsed JSON files
def validate_parsed_json(json_file):
    """
    Validates that the parsed JSON has the expected structure.
    
    json_file: path to JSON file
    returns: tuple (is_valid, error_message)
    """
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
        
        # Check required keys
        required_keys = ['metadata', 'variables_and_domains', 'constraints']
        for key in required_keys:
            if key not in data:
                return False, f"Missing key: {key}"
        
        # Check metadata
        metadata = data['metadata']
        required_metadata = ['problem_name', 'attribute_count', 'house_count']
        for key in required_metadata:
            if key not in metadata:
                return False, f"Missing metadata key: {key}"
        
        # Check variables_and_domains
        var_domain = data['variables_and_domains']
        required_var_keys = ['categories', 'domain_values', 'nodes']
        for key in required_var_keys:
            if key not in var_domain:
                return False, f"Missing var_domain key: {key}"
        
        # Check constraints
        constraints = data['constraints']
        if 'puzzle_rules' not in constraints:
            return False, "Missing puzzle_rules in constraints"
        
        return True, "Valid"
    except Exception as e:
        return False, str(e)