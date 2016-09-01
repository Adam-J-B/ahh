__author__ = 'huang.andrew12@gmail.com'
__copyright__ = 'Andrew Huang'

import numpy as np
from netCDF4 import Dataset

def eval(variable, name=None, full=False, head=False, tail=False, output_len=8, unnest=True, unnest_row_len=2, unnest_col_len=5, locate_valid=False):
    """
    Prints a variable summary to screen; includes values, type, values, and shape.

    :param: variable - variable to be evaluated
    :param: name (boolean) - name of variable
    :param: full (boolean) - list out every value
    :param: head (boolean) - list of first values up to output length
    :param: tail (boolean) - list of last values up to output length
    :param: output_len (int) - length of print output
    :param: unnest (boolean) - unnests variable and list out every value
    :param: unnest_row_len (int) - number of unnested rows
    :param: unnest_col_len (int) - number of unnested columns
    :param: locate_valid (boolean) - locates the first valid value and starts there
    """
    len_of_var = len(variable)
    type_of_var = type(variable)
    try:
        shape_of_var = np.array(variable).shape
    except:
        pass
    if name is not None:
        print('Evaluation of {}'.format(name))
    if head:
        print('Head of variable is:\n{}\n'.format(variable[0:output_len]))
    elif tail:
        tail_first = variable[-output_len:-1]
        tail_last = variable[-1]
        tail = np.append(tail_first, tail_last)
        print('Tail of variable is:\n{}\n'.format(variable[-output_len:-1]))
    elif full:
        print('Index, Value')
        for i, val in enumerate(variable):
            print(i, val)
    elif unnest:
        start_row, start_col = 0, 0
        rows = range(shape_of_var[0])
        cols = range(shape_of_var[1])
        if locate_valid:
            start_row, start_col = locate_valid_start(variable, rows, cols)
        rows = range(shape_of_var[0])[start_row:unnest_row_len+start_row]
        cols = range(shape_of_var[1])[start_col:unnest_col_len+start_col]
        print('(Row, Column): Unnested Value')
        for row in rows:
            for col in cols:
                print('({row}, {col}): {var}'.format(row=row,col=col,var=variable[row, col]))
    else:
        print('Data in variable is {}\n'.format(variable))
    print('Type of variable is {}'.format(type_of_var))
    try:
        type_of_val_in_var = type(variable[0])
        print('Type of first unnested value of variable is {}'.format(type_of_val_in_var))
    except:
        pass
    try:
        type_of_val_in_unnested_var = type(variable[0][0])
        print('Type of first unnested of unnested value of variable is {}'.format(type_of_val_in_unnested_var))
    except:
        pass
    try:
        start_row, start_col = locate_valid_start(variable, rows, cols)
        type_of_valid_val_in_unnested_var = type(variable[start_row][start_col])
        print('Type of first valid unnested of unnested value of variable is {}'.format(type_of_valid_val_in_unnested_var))
    except:
        pass
    try:
        print('Length of variable is: {}'.format(len_of_var))
    except:
        pass
    try:
        print('Shape of variable is: {}'.format(shape_of_var))
    except:
        pass


def get_idc(lats, lons, lower_lat, upper_lat, left_lon, right_lon):
    """
    Finds the indices for given latitudes and longitudes boundary.

    :param: lats (list) - array of latitudes
    :param: lons (list) - array of longitudes
    :param: lower_lat (float) - southern latitude boundary
    :param: upper_lat (float) - northern latitude boundary
    :param: left_lon (float) - western longitude boundary
    :param: right_lon (float) - eastern longitude boundary
    :return: lats_idc, lons_idc (np.array, np.array) - indices of latitudes/longitude
    """
    lats = np.array(lats)
    lons = np.array(lons)
    lats_idc = np.where(
                         (lats >= lower_lat)
                         &
                         (lats <= upper_lat)
                         )
    lons_idc = np.where(
                         (lons >= left_lon)
                         &
                         (lons <= right_lon)
                         )
    return lats_idc[0], lons_idc[0]


def read_nc(file_path):
    """
    Reads the netCDF4 file's lats, lons, and time
    and returns those parameters in addition to
    an open netCDF4 dataset.

    :param: file_path (str) - path to file
    :return: fi_in, time, lats, lons (netCDF4.Dataset, np.array, np.array, np.array)
            netCDF4 dataset, time array, latitude array, longitude array
    """

    fi_in = Dataset(file_path, mode='r')
    try:
        lats = fi_in.variables['lat'][:]
        lons = fi_in.variables['lon'][:]
    except:
        lats = fi_in.variables['latitude'][:]
        lons = fi_in.variables['longitude'][:]
    try:
        time = fi_in.variables['time'][:]
    except:
        time = None
    return fi_in, time, lats, lons


def locate_valid_start(variable, num_rows, num_cols):
    """
    Finds the first row and column that isn't zero or masked.

    :param: variable - variable to be evaluated
    :param: rows (int) - number of rows of variable
    :param: cols (int) - number of columns of variable
    :return: start_row, start_col (int, int) - first row/col that isn't zero or masked
    """
    for row in num_rows:
        for col in num_cols:
            if variable[row, col] != 0 and \
                type(variable[row,col]) != np.ma.core.MaskedConstant:
                start_row = row
                start_col = col
                return start_row, start_col
