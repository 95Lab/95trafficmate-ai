import sys
sys.path.append('..')
import os
import shutil
import argparse
import cv2 as cv
import pandas as pd
from raster import *

project_data_path=".."
tp = 'congestion'
rt = 'raster'
feature_name = 'avg_length'
parser = argparse.ArgumentParser()
parser.add_argument('-y', '--year', type=int)
args = parser.parse_args()
year = args.year

mesh_full = pd.read_csv(f'{project_data_path}/raster/full_mesh.csv')
nrows = mesh_full['row'].max() + 1
ncols = mesh_full['col'].max() + 1

df = pd.read_csv(f'{project_data_path}/dataframe/{tp}_{year}.csv')

if year == 2020:
    mval, maxval = compute_minmaxval(df, feature_name)
    with open(f'{project_data_path}/{rt}/{tp}/maval.txt', 'w') as f:
        f.write(f'{maxval:.2f}')
else:
    with open(f'{project_data_path}/{rt}/{tp}/maval.txt', 'r') as f:
        maxval = float(f.read())

dfx = pixelize_dataframe(df, feature_name, maxval)
start_time = f"{year}-01-01 00:00:00+09"
end_time = f"{year}-06-30 23:00:00+09"
full_time = make_full_time(start_time, end_time)
output_data_path = f'{project_data_path}/{rt}/{tp}/{year}'
if os.path.exists(output_data_path):
    shutil.rmtree(output_data_path)
os.makedirs(output_data_path)

is_empty = []
file_name = []
for i, tic in enumerate(full_time):
    if i%10 == 0:
        print(f"Processing {i}/{len(full_time)}")
    img, ise = make_raster(tic, nrows, ncols, dfx)
    is_empty.append(ise)
    file_name.append(f'{i}.png')
    cv.imwrite(f'{output_data_path}/{i}.png', img)

dfout = pd.DataFrame(np.array([full_time, file_name, is_empty]).T, columns=['start_datetime', 'file_name', 'is_empty'])
dfout.to_csv(f'{output_data_path}/{year}.csv', index=False)