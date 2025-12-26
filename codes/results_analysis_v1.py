import pandas as pd

allRace_folder = './races_all'

surnames = pd.read_csv('driver_surname.csv')
overall_results = pd.read_csv('overall_gp_2025.csv')
all_gp = overall_results['Grand Prix'].unique()
all_gp = [gp.lower().replace(' ', '_') for gp in all_gp]
print(all_gp)

all_gp_list = []
grid_gainloss_df = surnames
p3_gainloss_df = surnames
for gp in all_gp:
    print(f'Processing {gp}...')
    races_df = pd.read_csv(f'{allRace_folder}/{gp}_2025.csv', encoding='latin1')
    
    # default to 20 places if position not available or disqualified
    for col in ['race-result', 'qualifying', 'practice/3', 'practice/1']:
        if col in races_df.columns:
            races_df[col] = pd.to_numeric(races_df[col], errors='coerce').fillna(20)
    
    if 'qualifying' in races_df.columns and 'race-result' in races_df.columns:
        races_df['grid_gainloss'] = races_df['qualifying'] - races_df['race-result']
    
    if 'practice/3' in races_df.columns and 'qualifying' in races_df.columns:
        races_df['p3_gainloss'] = races_df['practice/3'] - races_df['qualifying']
    elif 'practice/1' in races_df.columns and 'qualifying' in races_df.columns:
        races_df['p3_gainloss'] = races_df['practice/1'] - races_df['qualifying']
    else:
        print(f'No practice/3 or practice/1 data for {gp}, skipping p3_gainloss calculation.')
        break

    # for each surname, get grid_gainloss and leave the absent surname as NaN
    grid_gainloss_temp = surnames[['Surname']].merge(races_df[['Surname', 'grid_gainloss']], on='Surname', how='left')
    grid_gainloss_df = pd.concat([grid_gainloss_df, grid_gainloss_temp[['grid_gainloss']]], axis=1)
    grid_gainloss_df = grid_gainloss_df.rename(columns={'grid_gainloss': f'{gp}'})

    # for each surname, get p3_gainloss and leave the absent surname as NaN
    p3_gainloss_temp = surnames[['Surname']].merge(races_df[['Surname', 'p3_gainloss']], on='Surname', how='left')
    p3_gainloss_df = pd.concat([p3_gainloss_df, p3_gainloss_temp[['p3_gainloss']]], axis=1)
    p3_gainloss_df = p3_gainloss_df.rename(columns={'p3_gainloss': f'{gp}'})

# Save to CSV
grid_gainloss_df.to_csv('./analysis/grid_gainloss_summary.csv', index=False)
p3_gainloss_df.to_csv('./analysis/p3_gainloss_summary.csv', index=False)