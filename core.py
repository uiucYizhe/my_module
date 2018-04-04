"""
module name: zyz_core
description: Contains the common modules and data paths used in my research.

"""

# common modules
import numpy as np
from tqdm import tqdm


# system modules
import os
import time
import sys


# dataset modules
from netCDF4 import Dataset # netcdf
from struct import unpack   # binary
from pyhdf.SD import SD     # hdf4
import h5py                 # hdf5
import MisrToolkit as mtk   # hdfeos


# statistical modules
import statsmodels.api as sm
from scipy.stats import linregress, norm
#from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegressionCV
from sklearn.metrics import f1_score
from sklearn import svm


# plot modules
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap



"""
some data paths locally, used by zyz_data module
"""
DATA_PATH = '/u/sciteam/smzyz/data'

ocean_mask_1d = DATA_PATH + '/Support/ISLSCP_WaterMasks/land_ocean_mask2_1d.asc'
ocean_mask_hd = DATA_PATH + '/Support/ISLSCP_WaterMasks/land_ocean_mask2_hd.asc'
ocean_mask_qd = DATA_PATH + '/Support/ISLSCP_WaterMasks/land_ocean_mask2_qd.asc'

ceres_dir = DATA_PATH + '/Satellite/Terra/CERES'
misr_dir = DATA_PATH + '/Satellite/Terra/MISR'

nsidc_G02135 = DATA_PATH + '/Satellite/NSIDC/G02135'
nsidc_psn25lats = DATA_PATH + '/Satellite/NSIDC/psn25lats_v3.dat'
nsidc_psn25lons = DATA_PATH + '/Satellite/NSIDC/psn25lons_v3.dat'