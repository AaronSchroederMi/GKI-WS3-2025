# %%
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import pprint # printing the JSON like structure more human friendly
import re # regex functionality

from pyarrow.dataset import parquet_dataset

import json

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside the current session
# %%
'''
creates the nodes from clue string
has security check to secure that the number of nodes read is correct
(e.g. a 6*6 problem has 36 nodes)

clues: natural language description of problem
attribute_count: amount of unique attributes in each house
house_count: amount of houses

returns list of strings (representing each instance of each attribute)
'''
def create_nodes(clues:str, attribute_count:int, house_count:int) -> list[str]:
    tokens = re.findall(r'`.*?`', clues)
    tokens = [match.replace('`', '') for match in tokens]

    if len(tokens) == attribute_count * house_count:
        return tokens
    raise ValueError
# %%
'''
creates the categories by reading the header of the clue file

clues: natural language description of problem

returns list of strings (representing each attribute)

note: does not match a single word per attribute, but rather a longer sentence
'''
def create_categories(clues:str) -> list[str]:
    tokens = re.findall(r'-.*?:', clues)
    tokens = [match.replace('-', '') for match in tokens]
    tokens = [match.replace(':', '') for match in tokens]
    tokens = [match.lstrip() for match in tokens]
    return tokens
# %%
'''
creates the domain space for all nodes from existing nodes and house_count

nodes: list of strings (representing each instance of each attribute)
house_count: number of house options (e.g. 1-4, 1-7)

returns dict with keys for each domain space containing lists of all options
'''
def create_domain_space(nodes:list[str], house_count:int) -> dict:
    domain = {}
    for node in nodes:
        domain[node] = list(range(1, house_count + 1))

    return domain
# %%
'''
creates the constraints for all clues

clues: natural language description of problem
nodes: list of strings (representing each instance of each attribute)

returns list of constraints. Each constraint is a dict with a type, vars and param(if NOT_AT or FIXED_SLOT)
'''
def create_constraints(clues:str, nodes:list[str], house_count:int, attribute_count:int) -> list[dict]:
    constraints = []
    constraints = create_all_different_constraints(constraints, [node.lower() for node in nodes], house_count, attribute_count)
    tokens = re.findall(r'[0-9]+\..+?\.', clues)
    for token in tokens:
        pattern = r'\b(' + '|'.join(nodes) + r')\b'
        pattern = fix_pattern_typos(pattern)
        vars = re.findall(pattern, token, re.IGNORECASE)
        vars = reverse_pattern_typo_fix(vars)
        vars = [var.lower() for var in vars]

        if re.search(r'not in the', token, re.IGNORECASE):
            param = house_number_to_integer(token)
            if param == -1 or len(vars) != 1:
                raise ValueError('NOT_AT was recognised incorrectly', token)
            constraints.append({
                'type': 'NOT_AT',
                'vars': vars,
                'param': param
            })
            continue
        if re.search(r'somewhere to the left', token, re.IGNORECASE):
            if len(vars) != 2:
                raise ValueError('SOMEWHERE_TO_THE_LEFT was recognised incorrectly', token)
            constraints.append({
                'type': 'SOMEWHERE_TO_THE_LEFT',
                'vars': vars
            })
            continue
        if re.search(r'somewhere to the right', token, re.IGNORECASE):
            if len(vars) != 2:
                raise ValueError('SOMEWHERE_TO_THE_RIGHT was recognised incorrectly', token)
            constraints.append({
                'type': 'SOMEWHERE_TO_THE_RIGHT',
                'vars': vars
            })
            continue
        if re.search(r'is in the', token, re.IGNORECASE):
            param = house_number_to_integer(token)
            if param == -1 or len(vars) != 1:
                raise ValueError('FIXED_SLOT was recognised incorrectly', token)
            constraints.append({
                'type': 'FIXED_SLOT',
                'vars': vars,
                'param': param
            })
            continue
        if re.search(r'directly left', token, re.IGNORECASE):
            if len(vars) != 2:
                raise ValueError('DIRECTLY_LEFT was recognised incorrectly', token)
            constraints.append({
                'type': 'DIRECTLY_LEFT',
                'vars': vars
            })
            continue
        if re.search(r'directly right', token, re.IGNORECASE):
            if len(vars) != 2:
                raise ValueError('DIRECTLY_LEFT was recognised incorrectly', token)
            constraints.append({
                'type': 'DIRECTLY_RIGHT',
                'vars': vars
            })
            continue
        if re.search(r'one house between', token, re.IGNORECASE):
            if len(vars) != 2:
                raise ValueError('ONE_HOUSE_BETWEEN was recognised incorrectly', token)
            constraints.append({
                'type': 'ONE_HOUSE_BETWEEN',
                'vars': vars
            })
            continue
        if re.search(r'next to', token, re.IGNORECASE):
            if len(vars) != 2:
                raise ValueError('NEXT_TO was recognised incorrectly', token)
            constraints.append({
                'type': 'NEXT_TO',
                'vars': vars
            })
            continue
        if re.search(r'two houses between', token, re.IGNORECASE):
            if len(vars) != 2:
                raise ValueError('TWO_HOUSE_BETWEEN was recognised incorrectly', token)
            constraints.append({
                'type': 'TWO_HOUSE_BETWEEN',
                'vars': vars
            })
            continue
        if re.search(r'is', token, re.IGNORECASE):
            if len(vars) != 2:
                raise ValueError('SAME_SLOT was recognised incorrectly', token)
            constraints.append({
                'type': 'SAME_SLOT',
                'vars': vars
            })
            continue
    return constraints

'''
This helper function creates the ALL_DIFFERENT_CATEGORY constraints

constraints: list that will be returned with appended constraints
nodes: list of each instance of each attribute
house_count: number of houses (used here as number of instance of each attribute)
attribute_count: number of attributes

returns list of ALL_DIFFERENT_CATEGORY constraints. Each constraint is represented as a dict with a type and vars
'''
def create_all_different_constraints(constraints:list[dict], nodes:list[str], house_count:int, attribute_count:int) -> list[dict]:
    for i in range(attribute_count):
        constraints.append({
            'type': 'ALL_DIFFERENT_CATEGORY',
            'vars': nodes[0 + house_count * i:house_count * (i + 1)]
        })
    if len(constraints) != attribute_count:
        raise ValueError('ALL_DIFFERENT_CATEGORY was recognised incorrectly', constraints)
    return constraints

'''
This helper function changes certain identifiers that differ between clues and problem description to ensure parity with the description

vars: A list containing all instances of the attributes of the current problem present in the current clue

returns the string with the differing items replaced (parity with description))
'''
def reverse_pattern_typo_fix(vars:list[str]) -> list[str]:
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

'''
This helper function changes certain identifiers that differ between clues and problem description to ensure parity with the clues

pattern: A string that contains all instances of the attributes of the current problem

returns the string with the differing items replaced (parity with clues)
'''
def fix_pattern_typos(pattern:str) -> str:
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

'''
This helper function is used for converting the ('first', 'second', etc.) into integer values

token: This is a string of just one clue with the type (FIXED_SLOT or NOT_AT)

returns an int representing the house number for the constraint
'''
def house_number_to_integer(token:str) -> int:
    param = -1
    tmp = re.findall(r'(First|Second|Third|Fourth|Fifth|Sixth)', token, re.IGNORECASE)
    if len(tmp) != 1:
        raise ValueError('HOUSE_NUMBER was recognised incorrectly', token)
    match tmp[0]:
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
# %%
'''
building JSON like structure

meant to be used with the apply function of pandas dataframes

row: a row of the dataframe it is executed on
'''
def parse_problem(row:pd.Series):
    print(row['id'])

    tmp_house_count = int(row['id'][9])
    tmp_attribute_count = int(row['id'][11])
    
    tmp_nodes = create_nodes(
        clues=row['puzzle'],
        attribute_count=tmp_attribute_count,
        house_count=tmp_house_count
    )
    lower_tmp_nodes = [node.lower() for node in tmp_nodes]
    
    data = {
        "metadata": {
            "problem_name": row['id'],
            "attribute_count": tmp_attribute_count,
            "house_count": tmp_house_count,
        },
        "variables_and_domains": {
            "categories": 
                create_categories(
                    clues=row['puzzle']
                ),
            "domain_values":
                create_domain_space(
                    nodes=lower_tmp_nodes,
                    house_count=tmp_house_count
                ),
            "nodes": lower_tmp_nodes,
        },
        "constraints": {
            "puzzle_rules": create_constraints(
                clues=row['puzzle'],
                nodes=tmp_nodes,
                house_count=tmp_house_count,
                attribute_count=tmp_attribute_count
            )
        },
    }
    return data