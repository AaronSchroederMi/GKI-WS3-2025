from solver import *
from parser_parquet import *

df2 = pd.read_parquet('mc-00000-of-00001.parquet')
df2 = df2.apply(parse_problem, axis=1)
results_df2 = solve_all_puzzles(input_frame=df2, output_file="mc_results.csv")
print("\n" + "="*50)
print("Competition submission file 'mc_results.csv' is ready!")
print("="*50)