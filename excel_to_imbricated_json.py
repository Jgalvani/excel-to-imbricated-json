import pandas as pd
from datetime import datetime
from tqdm import tqdm
import argparse
import json


# Command line options
parser = argparse.ArgumentParser(prog='Match references', description='match parents and children process references')
parser.add_argument('-i', '--input', type=str, required=True, help='excel file')
parser.add_argument('-o', '--output', type=str, required=True, help='json file')
args = parser.parse_args()


# Variables
begin = datetime.now()
dict_list = []


# Functions
def format_string_date(date):
    return date.replace('/', '-').replace(':', ' ', 1)


def get_hour_diff(start, end):
    start_date = datetime.fromisoformat(format_string_date(start))
    end_date = datetime.fromisoformat(format_string_date(end))
    return str(end_date - start_date)
    

def get_children(row, parent_start):
    row['parentStart'] = parent_start
    row['diff'] =  get_hour_diff(parent_start, row['start'])
    row['children'] = [row[1].to_dict() for row in df.loc[df['parentReference'] == row['reference']].iterrows()]
    
    for child in row['children']:
        get_children(child, row['start'])
    

def main(series):
    row = series.to_dict()
    row['parentReference'] = None
    row['parentStart'] = None
    row['diff'] = None
    row['children'] = [row[1].to_dict() for row in df.loc[df['parentReference'] == row['reference']].iterrows()]
    
    for child in row['children']:
        get_children(child, row['start'])
        
    dict_list.append(row)
    
    
# Script
print('reading file...')
df = pd.read_excel(args.input, usecols=['start', 'reference', 'parentReference', 'role', 'Action', 'end'])
df = df.drop_duplicates()

first_parent_df = df[df['parentReference'].isnull()]

tqdm.pandas(desc='computing time difference from parents to children and building imbricated JSON')
first_parent_df.progress_apply(main, axis=1)

with open(args.output, 'w') as f:
    f.write(json.dumps(dict_list, indent=4)) # "indent" parameter beautifies the JSON but file size grows rapidly

time = datetime.now() - begin
print(f'Execution finished in {str(time)} !\n{args.output} was created.')