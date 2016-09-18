import numpy as np
from netCDF4 import Dataset, num2date

__author__ = 'huang.andrew12@gmail.com'
__copyright__ = 'Andrew Huang'


def ahh(variable,
        n='ahh',
        center=0,
        offset=0,
        threshold=15,
        precision=2,
        edgeitems=5,
        suppress=True,
        fillval=9999.):
    """
    Explores type, unnested type, length, and shape of a variable.
    Can optionally include a name to differentiate from other 'ahh's.

    :param: variable (array) - variable to be evaluated
    :param: n (boolean) - name of variable
    :param: center (int) - if not 0, the number*2 to print around the center
    :param: offset (int) - count of indices offset from the center
    :param: threshold (int) - count before abbrieviating the print
    :param: precision (int) - number of decimal places
    :param: edgeitems (int) - how many numbers to print on the edge
    :param: suppress (boolean) - whether to suppress scientific notation
    :param: fillval (float) - anything equal/greater than fill value will
                              not be included in the max and min
    """
    variable = np.array(variable)
    try:
        len_of_var = len(variable)
    except:
        len_of_var = None
    center_of_var = len(variable)/2
    type_of_var = type(variable)
    type_of_var2 = None
    shape_of_var = None
    max_of_var = None
    min_of_var = None

    try:
        shape_of_var = np.array(variable).shape
    except:
        pass

    try:
        fillval_idc = np.where(variable < fillval)
        max_of_var = np.max(variable[fillval_idc])
        min_of_var = np.min(variable[fillval_idc])
    except:
        pass

    if 'Masked' in str(type_of_var):
        variable = variable[~variable.mask]
        center_of_var = len(variable)/2
        print('')
        print('NOTE! This array has been temporarily reshaped to 1D to show')
        print('only non-masked values. Therefore, if you are printing out')
        print('the center, it may show an anomalously large indice!')

    try:
        type_of_var2 = type(variable.flatten()[0])
    except:
        pass

    np.set_printoptions(
                        suppress=suppress,
                        threshold=threshold,
                        precision=precision,
                        edgeitems=edgeitems
                        )

    print('')
    print('            Name: {}'.format(n))
    print('Overarching Type: {}'.format(type_of_var))
    print('   Unnested Type: {}'.format(type_of_var2))
    print('  Original Shape: {}'.format(shape_of_var))
    print('          Length: {}'.format(len_of_var))
    print('         Maximum: {}'.format(max_of_var))
    print('         Minimum: {}'.format(min_of_var))
    print('')

    print('Snippet of values:')
    print(np.array(variable))
    if center != 0:
        try:
            print('Values around indice {}:'
                  .format(center_of_var + offset))
            print(np.array(
                          variable[
                                  center_of_var - center + offset:
                                  center_of_var + center + offset
                                  ]
                          )
                  )
        except:
            print('Unable to get center of variable!')
        print('')


def p(num=1):
    """
    Prints a noticeable mark in the terminal to help debug.

    :param: num (int) - number to differentiate your markers
    """
    print('\n######## MARK {} ########\n'.format(num))


def lonw2e(lon, array=False, reverse=False):
    """
    Converts a west longitude to east longitude, can also do in reverse.
    :param: lon (int) - a west longitude
    :param: reverse (boolean) - indicator whether input is an array
    :param: array (boolean) - indicator whether to go the other direction
    :return: translated_lon (int) - translated longitude
    """
    if not reverse:
        if array:
            translated_lon = np.array(lon)
            west_lon_idc = np.where(translated_lon < 0)
            translated_lon[west_lon_idc] += 360
        else:
            if lon < 0:
                translated_lon = 360 + lon
            else:
                print('Input lon, {}, is already in east coordinates!'
                      .format(lon))
    else:
        if array:
            translated_lon = np.array(lon)
            west_lon_idc = np.where(translated_lon > 180)
            translated_lon[west_lon_idc] -= 360
        else:
            if lon > 180:
                translated_lon = lon - 360
            else:
                print('Input lon, {}, is already in east coordinates!'
                      .format(lon))

    return translated_lon


def get_idc(lats,
            lons,
            lower_lat,
            upper_lat,
            left_lon,
            right_lon,
            maxmin=False,
            w2e=False,
            e2w=False):
    """
    Finds the indices for given latitudes and longitudes boundary.

    :param: lats (list) - array of latitudes
    :param: lons (list) - array of longitudes
    :param: lower_lat (float) - southern latitude boundary
    :param: upper_lat (float) - northern latitude boundary
    :param: left_lon (float) - western longitude boundary
    :param: right_lon (float) - eastern longitude boundary
    :param: maxmin (boolean) - return only the max and min of lat/lon idc
    :param: w2e (boolean) - convert input west longitudes to east longitudes
    :param: e2w (boolean) - convert input east longitudes to west longitudes
    :return: lats_idc, lons_idc (np.array, np.array) - indices of lats/lons
    :return: lat_start_idc, lat_end_idc, lon_start_idc, lon_end_idc -
             (np.int64, np.int64, np.int64, np.int64)
             the lowest and highest lat/lon indices
    """
    lats = np.array(lats)
    lons = np.array(lons)

    if w2e:
        left_lon = lonw2e(left_lon)
        right_lon = lonw2e(right_lon)

    if e2w:
        left_lon = lonw2e(left_lon, reverse=True)
        right_lon = lonw2e(right_lon, reverse=True)

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

    if len(lats_idc) == 0:
        print('Unable to find any lat indices within the range!')
    if len(lons_idc) == 0:
        print('Unable to find any lon indices within the range!')
        print('Perhaps convert west longitudes to east, or vice versa?')

    if maxmin:
        lats_idc = lats_idc[0].min(), lats_idc[0].max()
        lons_idc = lons_idc[0].min(), lons_idc[0].max()
        lat_start_idc = lats_idc[0]
        lat_end_idc = lats_idc[1]
        lon_start_idc = lons_idc[0]
        lon_end_idc = lons_idc[1]
        return lat_start_idc, lat_end_idc, lon_start_idc, lon_end_idc

    return lats_idc[0], lons_idc[0]


def read_nc(file_path,
            lat='lat',
            lon='lon',
            time='time',
            num2date=False,
            peek=False,
            extra=None,
            extra2=None,
            extra3=None,
            original=False):
    """
    Reads the netCDF4 file's lats, lons, and time and returns those
    parameters in addition to an opened netCDF4 dataset.

    :param: file_path (str) - path to file
    :param: peek (boolean) - print out description of netCDF4 dataset
    :param: extra (str) - return an extra variable given name of variable
    :param: num2date (boolean) - converts time to datetime
    :param: extra2 (str) - return a second variable given name of variable
    :param: extra3 (str) - return a third variable given name of variable
    :return: fi_in, time, lats, lons
            (netCDF4.Dataset, np.array, np.array, np.array)
            netCDF4 dataset, time array, latitude array, longitude array
    """
    fi_in = Dataset(file_path, mode='r')
    if peek:
        print(fi_in)
    try:
        lats = fi_in.variables[lat][:]
        lons = fi_in.variables[lon][:]
    except:
        print('Unable to find the given lat, lon variable name!')
        print('Will try the variable names: "latitude" and "longitude"')
        try:
            lats = fi_in.variables['latitude'][:]
            lons = fi_in.variables['longitude'][:]
        except:
            print('Unable to find any lat, lon variable; returning None')
            lats = None
            lons = None
    try:
        if num2date:
            time_var = fi_in.variables[time]
            time = create_dt_arr(time_var)
        else:
            time = fi_in.variables[time][:]
    except:
        print('Unable to create time variable; returning None')
        time = None
    if extra is not None:
        extra_var = fi_in.variables[extra][:]
        if extra2 is not None:
            extra_var2 = fi_in.variables[extra2][:]
            if extra3 is not None:
                extra_var3 = fi_in.variables[extra3][:]
                return time, lats, lons, extra_var, extra_var2, extra_var3
            return time, lats, lons, extra_var, extra_var2
        return time, lats, lons, extra_var
    if original:
        return fi_in, time, lats, lons
    else:
        fi_in.close()
        return time, lats, lons


def create_dt_arr(time_var, calendar='standard'):
    """
    Creates a datetime array based on an unopened time variable.

    :param: time_var (netCDF4.Variable) - unopened time variable
    :param: calendar (str) - type of calendar
    :return: datetime_array (np.array) - array of datetimes
    """
    try:
        datetime_array = num2date(
            time_var[:], units=time_var.units, calendar=time_var.calendar)
    except:
        datetime_array = num2date(
            time_var[:], units=time_var.units, calendar=calendar)
    return datetime_array


def dt2jul(dt):
    """
    Return julian day out of a datetime.

    :param: dt (datetime.datetime/int) - datetime
    :return: jday (int) - julian day
    """
    return dt.timetuple().tm_yday