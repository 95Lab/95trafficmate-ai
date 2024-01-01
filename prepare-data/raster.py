import numpy as np
import pandas as pd


def compute_minmaxval(df, valcol):
    mean, std = df[valcol].apply(['mean', 'std'])
    minval = max(0, mean-3*std)
    maxval = mean + 3*std
    return minval, maxval

def make_full_time(start_time, end_time):
    start_time = pd.to_datetime(start_time)
    end_time = pd.to_datetime(end_time)
    full_time = pd.date_range(start=start_time, end=end_time, freq='1H')    
    full_time = [str(tic)[:-3] for tic in full_time]
    return full_time

def make_raster(tic, nrows, ncols, df):
    img = np.zeros((nrows, ncols), dtype=np.uint8)
    df_ = df[df['start_datetime']==tic]
    if len(df_) == 0:
        return img, 1
    rows = df_['row'].values
    cols = df_['col'].values
    img[rows, cols] = df_['pixel']
    return img, 0

def make_mask_for_test(nrows, ncols, df):
    df_ = df[['row', 'col']].drop_duplicates()
    rows = df_['row'].values
    cols = df_['col'].values
    img = np.zeros((nrows, ncols), dtype=np.uint8)
    img[rows, cols] = 255
    return img

def pixelize_dataframe(df, value_col, maxval):
    pixels = 255 * df[value_col].values / maxval
    pixels = pixels.astype(np.uint8)
    pixels[pixels > 255] = 255
    df['pixel'] = pixels
    return df

def make_row_col_dict(mesh_full):
    mesh_full = mesh_full.set_index('mesh')
    mrc_dict = {}
    for mesh in mesh_full.index:
        row, col = mesh_full.loc[mesh, ['row', 'col']]
        mrc_dict[mesh] = [row, col]
    return mrc_dict