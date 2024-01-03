import sys
sys.path.append('../')
import numpy as np

WD = {
    'input': {        
        'sequence_prepdataset': '../dataset/raster_imgs/'    # path to multimodal raster images
    },
    'output': {
        'sequence_prepdataset': '../dataset/raster_imgs_3D/' # path to 3D raster images
    }
}

RASTER_CONFIG = {
    # factor map
    'width'             : 4800,
    'height'            : 4800,
    'offset_lat'        : 0.002083333,
    'offset_long'       : 0.003125,
    'start_lat'         : 33.584375,
    'start_long'        : 134.0015625,
    'pixel_area'        : 0.25 ** 2, # 0.25km
    
    # factor channel index
    'congestion_channel'        : 0,
    'rainfall_channel'          : 1,
    'accident_channel'          : 2,

    'num_factors'               : 3
}

SEQUENCE = {
    'crop' : {
        'xS'    :   560,
        'xE'    :   660,
        'yS'    :   200,
        'yE'    :   450
    },

    'inp_len'    :   6, # 6 steps 
    'inp_delta'  :   6, # 12*5mins=1h
    'out_len'    :   3, # 3 steps
    'out_delta'  :   6, # 12*5mins=3h
    'out_factor' : RASTER_CONFIG['congestion_channel']
}

PROJECTED_SEQUENCE = {
    'width'     : SEQUENCE['crop']['yE'] - SEQUENCE['crop']['yS'],
    'height'    : 20
}

PROJECTION_SHIFT = np.load('handcrafted_skeleton.npy')

projection = {}
