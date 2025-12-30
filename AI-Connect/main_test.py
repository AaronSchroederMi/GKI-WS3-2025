from solver import *
from parser_test import *

df3 = pd.read_csv('Test_100_Puzzles.csv')
print_csv_info()
df3 = df3.apply(parse_problem_test, axis=1)
results_df3 = solve_all_puzzles(input_frame=df3, output_file="test_results.csv")
print("\n" + "="*50)
print("Competition submission file 'test_results.csv' is ready!")
print("="*50)