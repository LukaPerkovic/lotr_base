import os
import pandas as pd
import numpy as np
import json
from itertools import groupby
os.chdir(r'C:\Users\Luka\Desktop\Data\Projects\2019_internal_scrapper\lotr')

dict_listing = []

[dict_listing.append(str(x)) for x in os.listdir() if 'list.json' in x]


for dict_name in dict_listing:
    with open(dict_name,'r',encoding="utf8") as l_dict:
            if dict_name.startswith('char'):            
                character_dict = json.loads(l_dict.read())
            elif dict_name.startswith('culture'):            
                culture_dict = json.loads(l_dict.read())
            elif dict_name.startswith('race'):            
                race_dict = json.loads(l_dict.read())
            elif dict_name.startswith('realms'):            
                realms_dict = json.loads(l_dict.read())
            elif dict_name.startswith('titles'):            
                titles_dict = json.loads(l_dict.read())

char_col_names = []
for key in character_dict.keys():
    for key2 in character_dict[key]:
        char_col_names.append(key2)
        
char_col_names = (list(set(char_col_names)))
char_col_names.insert(0,char_col_names.pop(char_col_names.index('Name')))
char_df = pd.DataFrame(columns = char_col_names)


for keys in character_dict:
    if character_dict[keys]['Name'] == 'Missing!':
        character_dict[keys]['Name'] = keys.split('Character_')[1].replace('_',' ')


for key in character_dict.keys():
    for col in char_df.columns:
        if col not in character_dict[key]:
            character_dict[key][col] = ''
        else:
            continue

char_df = char_df.append([k for k in character_dict.values()],ignore_index=True)
char_df.columns

culture_col_names = []
for key in culture_dict.keys():
    for key2 in culture_dict[key]:
        culture_col_names.append(key2)
        
culture_col_names = (list(set(culture_col_names)))
culture_col_names.insert(0,culture_col_names.pop(culture_col_names.index('Name')))
culture_df = pd.DataFrame(columns = culture_col_names)


for keys in culture_dict:
    if culture_dict[keys]['Name'] == 'Missing!':
        culture_dict[keys]['Name'] = keys.split('Culture_')[1].replace('_',' ')


for key in culture_dict.keys():
    for col in culture_df.columns:
        if col not in culture_dict[key]:
            culture_dict[key][col] = ''
        else:
            continue

            
            
culture_df = culture_df.append([k for k in culture_dict.values()],ignore_index=True)
culture_df.rename(columns={'Name':'Culture name'}, inplace=True)
culture_df

race_col_names = []
for key in race_dict.keys():
    for key2 in race_dict[key]:
        race_col_names.append(key2)
        
race_col_names = (list(set(race_col_names)))
race_col_names.insert(0,race_col_names.pop(race_col_names.index('Name')))
race_df = pd.DataFrame(columns = race_col_names)

for keys in race_dict:
    if race_dict[keys]['Name'] == 'Missing!':
        race_dict[keys]['Name'] = keys.split('Race_')[1].replace('_',' ')

for key in race_dict.keys():
    for col in race_df.columns:
        if col not in race_dict[key]:
            race_dict[key][col] = ''
        else:
            continue

race_df = race_df.append([k for k in race_dict.values()],ignore_index=True)
race_df[race_df['Name'] == 'Missing!']
race_df.rename(columns={'Name':'Race name'}, inplace=True)

realms_col_names = []
for key in realms_dict.keys():
    for key2 in realms_dict[key]:
        realms_col_names.append(key2)
        
realms_col_names = (list(set(realms_col_names)))
realms_col_names.insert(0,realms_col_names.pop(realms_col_names.index('Name')))
realms_df = pd.DataFrame(columns = realms_col_names)

for keys in realms_dict:
    if realms_dict[keys]['Name'] == 'Missing!':
        realms_dict[keys]['Name'] = keys.split('Realms_')[1].replace('_',' ')

for key in realms_dict.keys():
    for col in realms_df.columns:
        if col not in realms_dict[key]:
            realms_dict[key][col] = ''
        else:
            continue

realms_df = realms_df.append([k for k in realms_dict.values()],ignore_index=True)
realms_df[realms_df['Name'] == 'Missing!']
realms_df.rename(columns={'Name':'Realms name'}, inplace=True)


titles_col_names = []
for key in titles_dict.keys():
    for key2 in titles_dict[key]:
        titles_col_names.append(key2)
        
titles_col_names = (list(set(titles_col_names)))
titles_col_names.insert(0,titles_col_names.pop(titles_col_names.index('Name')))
titles_df = pd.DataFrame(columns = titles_col_names)

for keys in titles_dict:
    if titles_dict[keys]['Name'] == 'Missing!':
        titles_dict[keys]['Name'] = keys.split('Titles_')[1].replace('_',' ')

for key in titles_dict.keys():
    for col in titles_df.columns:
        if col not in titles_dict[key]:
            titles_dict[key][col] = ''
        else:
            continue

titles_df = titles_df.append([k for k in titles_dict.values()],ignore_index=True)
titles_df[titles_df['Name'] == 'Missing!']
titles_df.rename(columns={'Name':'Titles name'}, inplace=True)


dfs = [char_df,race_df,culture_df,realms_df,titles_df]

unique_cols = []

for df in dfs:
    for col_name in df.columns:
        if col_name not in unique_cols:
            unique_cols.append(col_name)
        else:
            pass

sorted(unique_cols)


titles_df = titles_df.drop([col for col in titles_df.columns if col in char_df.columns],axis=1)
race_df = race_df.drop([col for col in race_df.columns if col in char_df.columns],axis=1)

ch_t_df = char_df.merge(titles_df,how='left',left_on='Titles',right_on='Titles name')
ch_t_ra_df = ch_t_df.merge(race_df,how='left',left_on='Race',right_on='Race name')
realms_df = realms_df.drop([col for col in realms_df.columns if col in ch_t_ra_df.columns],axis=1)

ch_t_ra_re_df = ch_t_ra_df.merge(realms_df,how='left',left_on='Realms',right_on='Realms name')
culture_df = culture_df.drop([col for col in culture_df.columns if col in ch_t_ra_re_df.columns],axis=1)
full_dirty = ch_t_ra_re_df.merge(culture_df,how='left',left_on='Culture',right_on='Culture name')

