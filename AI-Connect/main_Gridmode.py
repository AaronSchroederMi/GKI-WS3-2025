from solver import *
from parser_parquet import *

df1 = pd.read_parquet('Gridmode-00000-of-00001.parquet')
df1 = df1.apply(parse_problem, axis=1)
results_df1 = solve_all_puzzles(input_frame=df1, output_file="gridmode_results.csv")
print("\n" + "="*50)
print("Competition submission file 'gridmode_results.csv' is ready!")
print("="*50)