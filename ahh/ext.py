import numpy as np
import pandas as pd
from netCDF4 import Dataset, num2date
from operator import itemgetter
import datetime
import calendar
import os

__author__ = 'huang.andrew12@gmail.com'
__copyright__ = 'Andrew Huang'


class OutOfRange(Exception):
    pass


class FileExists(Exception):
    pass


def ahh(variable,
        n='ahh',
        center=3,
        offset=0,
        threshold=15,
        precision=2,
        edgeitems=5,
        suppress=True,
        fillval_high=99999.,
        fillval_low=-99999.,
        snippet=True,
        time=0,
        level=0,
        ):
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
    :param: fillval_high (float) - anything equal/greater than fill value will
                              not be included in the max
    :param: fillval_low (float) - anything equal/less than fill value will
                          not be included in the min
    :param: snippet (boolean) - whether to exclude snippet of values
    :param: time (integer) - index of time to print in snippet
    :param: level (integer) - index of time to print in snippet
    """
    try:
        variable = np.array(variable)
        try:
            len_of_var = len(variable)
            center_of_var = len(variable)/2
        except:
            len_of_var = None
            center_of_var = None
        type_of_var = type(variable)
        type_of_var2 = None
        shape_of_var = None
        len_shape_of_var = 1
        max_of_var = None
        min_of_var = None

        try:
            shape_of_var = np.array(variable).shape
            len_shape_of_var = len(shape_of_var)
            if len_shape_of_var == 3:
                center_lat_of_var = shape_of_var[1] / 2
                center_lon_of_var = shape_of_var[2] / 2
            elif len_shape_of_var == 4:
                center_lat_of_var = shape_of_var[2] / 2
                center_lon_of_var = shape_of_var[3] / 2
            else:
                center_lat_of_var = None
                center_lon_of_var = None
        except:
            pass

        try:
            variable_ravel = np.ravel(variable)
            fillval_idc = np.where(
                                  (variable_ravel < fillval_high) &
                                  (variable_ravel > fillval_low)
                                  )
            variable_clean = variable_ravel[fillval_idc]
            max_of_var = variable_clean.max()
            min_of_var = variable_clean.min()
        except:
            print('Unable to get the max/min values!')

        try:
            if 'Masked' in str(type_of_var):
                variable = variable[~variable.mask]
                center_of_var = len(variable)/2
                print('')
                print('This array has been temporarily reshaped to 1D to show')
                print('only non-masked values. Therefore, if you are printing out')
                print('the center, it may show an anomalously large indice!')
        except:
            pass

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

        if snippet:
            print('Snippet of values:')
            if len_shape_of_var == 3:
                print(np.array(variable[time, :, :])[0])
            elif len_shape_of_var == 4:
                print(np.array(variable[time, level, :, :])[0])
            else:
                print(np.array(variable))
        else:
            pass
        if center != 0:
            try:

                if len_shape_of_var == 3:
                    print('Values around lat indice {lat}, lon indice {lon}:'
                          .format(lat=center_lat_of_var + offset,
                                  lon=center_lon_of_var + offset
                                  )
                          )
                    print(np.array(
                                  variable[
                                          time,
                                          center_lat_of_var - center + offset:
                                          center_lat_of_var + center + offset,
                                          center_lon_of_var - center + offset:
                                          center_lon_of_var + center + offset,
                                          ][0]
                                  )
                          )
                elif len_shape_of_var == 4:
                    print('Values around lat indice {lat}, lon indice {lon}:'
                          .format(lat=center_lat_of_var + offset,
                                  lon=center_lon_of_var + offset
                                  )
                          )
                    print(np.array(
                                  variable[
                                          time,
                                          level,
                                          center_lat_of_var - center + offset:
                                          center_lat_of_var + center + offset,
                                          center_lon_of_var - center + offset:
                                          center_lon_of_var + center + offset,
                                          ][0]
                                  )
                          )
                else:
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
    except Exception as e:
        print('\nUnable to ahh due to this:')
        print(e)
        print('')


def p(num=1):
    """
    Prints a noticeable mark in the terminal to help debug.

    :param: num (int) - number to differentiate your markers
    """
    print('\n######## MARK {} ########\n'.format(num))


def lonw2e(lon, reverse=False):
    """
    Converts a west longitude to east longitude, can also do in reverse.
    :param: lon (int) - a west longitude
    :param: reverse (boolean) - indicator whether input is an array
    :param: array (boolean) - indicator whether to go the other direction
    :return: translated_lon (int) - translated longitude
    """
    if not reverse:
        if len(lon) > 1:
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
        if len(lon) > 1:
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

    :param: lats (np.array) - array of latitudes
    :param: lons (np.array) - array of longitudes
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


def get_lvl_idc(lvls, lower_lvl, upper_lvl, maxmin=False):
    """
    Finds the level indices for given lower and upper boundary.

    :param: lvls (np.array) - array of levels
    :param: lower_lvl (float) - lower level boundary
    :param: upper_lvl (float) - upper level boundary
    :param: maxmin (boolean) - return only the max and min of level idc
    :return: lvls_idc (np.array) - indices of levels
    :return: lvl_start_idc, lvl_end_idc - (np.int64, np.int64)
             the lowest and highest level indices
    """
    lvls = np.array(lvls)

    lvls_idc = np.where(
                         (lvls >= lower_lvl)
                         &
                         (lvls <= upper_lvl)
                         )

    if len(lvls_idc) == 0:
        print('Unable to find any lat indices within the range!')

    if maxmin:
        lvls_idc = lvls_idc[0].min(), lvls_idc[0].max()
        lvl_start_idc = lvls_idc[0]
        lvl_end_idc = lvls_idc[1]
        return lvl_start_idc, lvl_end_idc

    return lvls_idc[0]


def get_time_idc(times, start_yr, end_yr,
                 start_mth=1, end_mth=12,
                 start_day=1, end_day=31,
                 maxmin=False):
    """
    Finds the time indices for given start time and end time.

    :param: times (np.array) - array of datetimes
    :param: start_yr (int) - lower year boundary
    :param: end_yr (int) - upper year boundary
    :param: start_mth (int) - lower month boundary
    :param: end_mth (int) - upper month boundary
    :param: start_day (int) - lower day boundary
    :param: end_day (int) - upper day boundary
    :param: maxmin (boolean) - return only the max and min of time idc
    :return: times_idc (np.array) - indices of times
    :return: time_start_idc, time_end_idc - (np.int64, np.int64)
             the lowest and highest time indices
    """
    start_dt = datetime.datetime(start_yr, start_mth, start_day)
    while True:
        try:
            end_dt = datetime.datetime(end_yr, end_mth, end_day)
            break
        except Exception as e:
            end_day -= 1
            print('Unable to create end datetime due to this error\n{}'
                  .format(e))
            print('Changing end day to {}!'
                  .format(end_day))

    times_idc = np.where(
                         (times >= start_dt)
                         &
                         (times <= end_dt)
                         )

    if len(times_idc) == 0:
        print('Unable to find any times indices within the range!')

    if maxmin:
        times_idc = times_idc[0].min(), times_idc[0].max()
        time_start_idc = times_idc[0]
        time_end_idc = times_idc[1]
        return time_start_idc, time_end_idc

    return times_idc[0]


def get_closest(data, target_val, type_var='typical'):
    """
    Get the closest value and index to target value.
    :param: data (np.array) - data
    :param: target_val (float/datetime.datetime) - target value
    :param: type_var (str) - typical (float) or datetime (datetime.datetime)

    :return: closest_val, closest_val_idc (datetime.datetime/float, int) -
             the closest value to target value and the index of that
    """
    if type_var == 'typical':
        diff = np.abs(np.array(data) - target_val)
        closest_val_idc = min(enumerate(diff), key=itemgetter(1))[0]
        return data[closest_val_idc], closest_val_idc
    if type_var == 'datetime':
        closest_val = min(data, key=lambda d: abs(d - target_val))
        closest_val_idc = np.where(data == closest_val)[0]
        if len(closest_val_idc) == 0:
            data = np.ma.array(data)
            closest_val_idc = np.where(data == closest_val)[0]
        return closest_val, closest_val_idc

def read_nc(file_path,
            lat='lat',
            lon='lon',
            time='time',
            num2date=False,
            peek=False,
            extra=None,
            extra2=None,
            extra3=None,
            original=False,
            already=False):
    """
    Reads the netCDF4 file's lats, lons, and time and returns those
    parameters in addition to an opened netCDF4 dataset.

    :param: file_path (str) - path to file
    :param: peek (boolean) - print out description of netCDF4 dataset
    :param: extra (str) - return an extra variable given name of variable
    :param: num2date (boolean) - converts time to datetime
    :param: extra2 (str) - return a second variable given name of variable
    :param: extra3 (str) - return a third variable given name of variable
    :param: already (boolean) - whether lat, lon, time is already imported
                                if so, only return the extras
    :return: fi_in, time, lats, lons
            (netCDF4.Dataset, np.array, np.array, np.array)
            netCDF4 dataset, time array, latitude array, longitude array
    """
    fi_in = Dataset(file_path, mode='r')
    if peek:
        print(fi_in)
    if already:
        if extra is not None:
            extra_var = fi_in.variables[extra][:]
            if extra2 is not None:
                extra_var2 = fi_in.variables[extra2][:]
                if extra3 is not None:
                    extra_var3 = fi_in.variables[extra3][:]
                    return extra_var, extra_var2, extra_var3
                return extra_var, extra_var2
            return extra_var
    else:
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


def export_nc(lat, lon, var_list, name_list, units_list,
              out='untitled', time=None, z=None, description=None,
              format='NETCDF3_64BIT', time_name='time', z_name='z',
              lat_units='degrees_north', lon_units='degrees_east',
              time_units='unknown', z_units='unknown',
              time_calendar='unknown'):
    """
    Exports a netCDF3 file.

    :param: lat (np.array) - array of latitudes
    :param: lon (np.array) - array of longitudes
    :param: var_list (list) - list of variables in np.array
    :param: name_list (list) - list of variable names in string
    :param: units_list (list) - list of units names in string
    :param: out (str) - name of output file
    :param: time (np.array) - time/date variable
    :param: z (np.array) - z/level/depth variable
    :param: description (str) - description of data
    :param: format (str) - output format
    :param: time_name (str) - what to name the time variable
    :param: z_name (str) - what to name the z variable
    :param: lat_units (str) - units of latitude
    :param: lon_units (str) - units of longitude
    :param: time_units (str) - units of time
    :param: z_units (str) - units of z
    :param: time_calendar (str) - type of calendar
    """

    output_fi_name = '{}.nc'.format(out)

    if os.path.isfile(output_fi_name):
        print('\nOutput file already exists; please select a out name!\n')
        raise(FileExists)

    fi_out = Dataset(output_fi_name, 'w', format=format)

    if description is not None:
        fi_out.description = description

    if time is not None:
        fi_out.createDimension(time_name, len(time))
        fi_out_time = fi_out.createVariable(time_name, 'f4', (time_name,))
        fi_out_time.units = time_units
        if time_units is 'unknown':
            print('\nPlease set time_units; defaulting to unknown\n')
        if time_calendar is not 'unknown':
            fi_out_time.calendar = time_calendar
        fi_out_time[:] = time

    if z is not None:
        fi_out.createDimension(z_name, len(z))
        fi_out_z = fi_out.createVariable(z_name, 'f4', (z_name,))
        fi_out_z.units = z_units
        if z_units == 'unknown':
            print('\nPlease set z_units; defaulting to unknown\n')
        fi_out_z[:] = z

    fi_out.createDimension('lat', len(lat))
    fi_out_lat = fi_out.createVariable('latitude', 'f4', ('lat',))
    fi_out_lat.units = lat_units
    fi_out_lat[:] = lat

    fi_out.createDimension('lon', len(lon))
    fi_out_lon = fi_out.createVariable('longitude', 'f4', ('lon',))
    fi_out_lon.units = lon_units
    fi_out_lon[:] = lon

    for var, name, units in zip(var_list, name_list, units_list):
        if time is not None and z is not None:
            fi_out_var = fi_out.createVariable(name, 'f4',
                                               (
                                                time_name,
                                                z_name,
                                                'lat',
                                                'lon'
                                                )
                                               )
            fi_out_var.units = units
            fi_out_var[:, :, :, :] = var
        elif z is not None:
            fi_out_var = fi_out.createVariable(name, 'f4',
                                               (z_name, 'lat', 'lon'))
            fi_out_var.units = units
            fi_out_var[:, :, :] = var
        elif time is not None:
            fi_out_var = fi_out.createVariable(name, 'f4',
                                               (time_name, 'lat', 'lon'))
            fi_out_var.units = units
            fi_out_var[:, :, :] = var
        else:
            fi_out_var = fi_out.createVariable(name, 'f4',
                                               ('lat', 'lon'))
            fi_out_var.units = units
            fi_out_var[:, :] = var

    fi_out.close()


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


def jul2dt(jday, year):
    """
    Find the datetime from a julian date.

    :param: jday (int) - julian day
    :param: year (int) - year to determine if leap
    :return: dt (datetime.datetime) - respective datetime
    """
    if calendar.isleap(year):
        cal = pd.read_csv('./data/jd_cal_leap.csv')
        if jday < 1 or jday > 366:
            print('\nInput Julian day is out of 1-366 range!\n')
            raise(OutOfRange)
    else:
        if jday < 1 or jday > 365:
            print('\nInput Julian day is out of 1-365 range!\n')
            raise(OutOfRange)
        cal = pd.read_csv('./data/jd_cal.csv')
    jday_idc = np.where(cal == jday)
    mth = jday_idc[1][0] + 1
    day = jday_idc[0][0] + 1
    return datetime.datetime(year, mth, day)


def dtnow():
    """
    Get current UTC in datetime.

    :return: utcnow (datetime.datetime) - UTC now in datetime
    """
    return datetime.datetime.utcnow()

def clockit(start, n=''):
    """
    Print out elapsed time since start.

    :param: start (datetime.datetime) - start datetime
    :param: n (str) - label/description
    """
    print(n)
    print(datetime.datetime.utcnow() - start)
    print('')