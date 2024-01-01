import sys
sys.path.append('..')
import os
import shutil
import argparse
import cv2 as cv
import pandas as pd
from raster import *

project_data_path = "../"
parser = argparse.ArgumentParser()
parser.add_argument('-y', '--year', type=int)
args = parser.parse_args()
year = args.year

setagaya_mesh = pd.read_csv(f'{project_data_path}/loc_and_mesh.csv', usecols=['meshcode_250m'])
setagaya_mesh = setagaya_mesh['meshcode_250m'].unique().tolist()
datapath = "../rain_{}_q{}_60.csv"

chunksize = 1e7
dfs = []
cnt = 0
for q in [1, 2, 3, 4]:
    datapath_ = datapath.format(year, q)
    chunks = pd.read_csv(datapath_, chunksize=chunksize, usecols=['start_datetime', 'meshcode', 'avg_value'])
    for chunk in chunks:
        cnt += 1
        print(f"Processing chunk {cnt}")
        df = chunk[chunk['meshcode'].isin(setagaya_mesh)]
        dfs.append(df)

df = pd.concat(dfs, axis=0, ignore_index=True)
df = df.sort_values(by=['start_datetime', 'meshcode'])
df = df.reset_index(drop=True)

mesh_full = pd.read_csv(f'{project_data_path}/raster/full_mesh.csv')
mrc_dict = make_row_col_dict(mesh_full)
df[['row', 'col']] = df['meshcode'].apply(lambda mesh: pd.Series(mrc_dict[mesh]))
df.to_csv(f'{project_data_path}/raster/rain_{year}.csv', index=False)