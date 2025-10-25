import itertools
import random
import statistics

import pandas as pd
import search
import time
import tracemalloc

# population
max_population = [10, 25, 50, 100]
# mutation_probability
mutation_rate = [0.05, 0.1, 0.2, 0.5]
# number_of_iterations
ngen = [250]

"""
# gene_pool - 8-Queens
gene_pool = [0, 1, 2, 3, 4, 5, 6, 7]
target_len = 8
# f_threshold - 8-Queens
f_thres = 28
# fitness_fn - 8-Queens
def fitness_fn(sample):
    fitness = 0
    n = len(sample)
    for i in range(n):
        for j in range(i + 1, n):
            if sample[i] != sample[j] and abs(sample[i] - sample[j]) != abs(i - j):
                fitness += 1
    return fitness
"""

# gene_pool - 5-Länderproblem
gene_pool = [0, 1, 2, 3, 4, 5] # colors
target_len = 6
# graph - 5-Länderproblem
graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2, 4],
    4: [3],
    5: []
}
# f_threshold - 5-Länderproblem
f_thres = 1
# fitness_fn - 5-Länderproblem
def fitness_fn(sample):
    total_edges = sum(len(neigh) for neigh in graph.values()) / 2
    color_count = len(set(sample))
    conflicts = 0
    for region, neighbors in graph.items():
        for neighbor in neighbors:
            if region < neighbor and sample[region] == sample[neighbor]:
                conflicts += 1
    return 3 / (color_count + conflicts)


overall_results = []
trial_results = []


for max_population, mutation_rate, ngen in itertools.product(max_population, mutation_rate, ngen):
    population = [random.sample(range(target_len), target_len) for i in range(max_population)]

    fitness_values = []
    success_values = []
    evaluations = []
    execution_times = []
    memory_usages = []

    for trial in range(100):
        tracemalloc.start()
        start_time = time.time()
        solution, generations = search.genetic_algorithm(population, fitness_fn, gene_pool, f_thres, ngen,
                                                         mutation_rate)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end_time = time.time()

        fitness_value = fitness_fn(solution)
        execution_time = end_time - start_time
        memory_usage = peak / 1024

        success = False
        if fitness_value == f_thres:
            evaluations.append(generations)
            success = True

        memory_usages.append(memory_usage)
        execution_times.append(execution_time)
        fitness_values.append(fitness_value)
        success_values.append(success)

        print(f"{trial}. ", max_population, mutation_rate, ngen, " ", fitness_value, success, generations,
              f" {execution_time:.2f} {memory_usage:.2f}")

    overall_results.append({
        "max_population": max_population,
        "mutation_rate": mutation_rate,
        "ngen": ngen,
        "avg_fitness": statistics.mean(fitness_values),
        "success_rate": statistics.mean(success_values),
        "avg_evaluations_to_solve": statistics.mean(evaluations) if evaluations else ngen,
        "avg_execution_time": statistics.mean(execution_times),
        "avg_memory_usage": statistics.mean(memory_usages)
    })

df = pd.DataFrame(overall_results)
df.sort_values("avg_execution_time", ascending=False, inplace=True)
print(df.head(df.shape[0]))
df.to_csv("overall_results.csv")

# does not open Images
# plot_NQueens(solution)