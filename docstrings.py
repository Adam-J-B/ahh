__author__ = 'huang.andrew12@gmail.com'
__copyright__ = 'Andrew Huang'

##############################################################################
### https://github.com/ahuang11/ahh - Andrew Huang Helps? ####################
##############################################################################

##############################################################################
### pre.py ###################################################################
##############################################################################


def wget_fi(base_url, glob_str, user=None, pwd=None, directory=None):
    """
    Wrapper of wget; downloads files that matches the given glob_str. Can input
    username and password if authentication is required.

    :param: base_url (str) - the dir of all the to be downloaded files
    :param: glob_str (str) - the naming pattern of the files
    :param: user (str) - username
    :param: pwd (str) - password
    :param: directory (str) - name of directory for files to be saved
    """


def ncdump(glob_str, directory='./'):
    """
    Wrapper of ncdump; prints out netCDF metadata.

    :param: glob_str (str) - the naming pattern of the files
    :param: directory (str) - directory of file
    """


def concat_nc(glob_str, output_fi, directory='./', rec_dim=None):
    """
    Wrapper of NCO's ncrcat and optional ncks; concatenates a list of netCDF
    files given a glob_str (i.e. 'THETA.1440x720x50.2010*.nc') and outputs
    concatenated file as the given output_fi. If there's an error complaining
    that there's no record dimension, can give the dimension name to
    concatenate across under rec_dim.

    :param: glob_str (str) - the naming pattern of the files
    :param: output_fi (str) - name of concatenated file
    :param: directory (str) - directory of both input and output files
    :param: rec_dim (str) - name of dimension to act as record dimension
    """


##############################################################################
### ext.py ###################################################################
##############################################################################


def ahh(variable,
        n='ahh',
        center=3,
        offset=0,
        threshold=15,
        precision=2,
        edgeitems=5,
        suppress=True,
        fillval_high=9999.,
        fillval_low=-9999.,
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


def get_closest(data, target_val, type_var='typical'):
    """
    Get the closest value and index to target value.
    :param: data (np.array) - data
    :param: target_val (float/datetime.datetime) - target value
    :param: type_var (str) - typical (float) or datetime (datetime.datetime)

    :return: closest_val, closest_val_idc (datetime.datetime/float, int) -
             the closest value to target value and the index of that
    """


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
            already=True):
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


def create_dt_arr(time_var, calendar='standard'):
    """
    Creates a datetime array based on an unopened time variable.

    :param: time_var (netCDF4.Variable) - unopened time variable
    :param: calendar (str) - type of calendar
    :return: datetime_array (np.array) - array of datetimes
    """


def dt2jul(dt):
    """
    Return julian day out of a datetime.

    :param: dt (datetime.datetime/int) - datetime
    :return: jday (int) - julian day
    """


def jul2dt(jday, year):
    """
    Find the datetime from a julian date.

    :param: jday (int) - julian day
    :param: year (int) - year to determine if leap
    :return: dt (datetime.datetime) - respective datetime
    """


def dtnow():
    """
    Get current UTC in datetime.

    :return: utcnow (datetime.datetime) - UTC now in datetime
    """


def clockit(start, n=''):
    """
    Print out elapsed time since start.

    :param: start (datetime.datetime) - start datetime
    :param: n (str) - label/description
    """


##############################################################################
### sci.py ###################################################################
##############################################################################


def get_uac(obs, fcst, clim):
    """
    Calculates the uncentered anomaly correlation

    :param: obs (np.array) - observation
    :param: fcst (np.array) - forecast
    :param: clim - (np.array) - climatology
    return: uac - (np.array) - uncentered anomaly correlation
    """


def get_cac(obs, fcst, clim, idc):
    """
    Calculates the centered anomaly correlation

    :param: obs (np.array) - observation
    :param: fcst (np.array) - forecast
    :param: clim - (np.array) - climatology
    :param: idc - (np.array) - indices of grid points
    return: cac - (np.array) - centered anomaly correlation
    """


def get_rmse(obs, fcst, idc):
    """
    Calculates the root mean square error

    :param: obs (np.array) - observation
    :param: fcst (np.array) - forecast
    :param: idc - (np.array) - indices of grid points
    return: rmse - (np.array) - root mean square error
    """


def convert(variable,
            mm2in=False,
            c2f=False,
            c2k=False,
            f2k=False,
            mps2mph=False,
            reverse=False
            ):
    """
    Converts the variable from one unit to another.

    :param: variable (np.array) - variable values
    :param: mm2in (boolean) - millimeters to inches
    :param: c2f (boolean) - Celsius to Fahrenheit
    :param: c2k (boolean) - Celsius to Kelvin
    :param: f2k (boolean) - Fahrenheit to Kelvin
    :param: mps2mph (boolean) - meters per second to miles per hour
    :param: reverse (boolean) - reverses the conversions (mm2in becomes in2mm)
    :return: conv_var (np.array) - converted variable values
    """


def get_norm_anom(data_avg):
    """
    Finds the normalized anomaly of some averaged data

    :param: data_avg (np.ma.array) - average data values
    :return: data_anom (float) - normalized anomaly
    """


def get_avg(data, axis=(0),
            times_idc=None,
            lats_idc=None,
            lons_idc=None,
            lvls_idc=None,
            change_lvl_order=False):
    """
    Finds the areal and/or time average and/or level, but first,
    data dimensions must be in these orders:
    lat, lon
    time, lat, lon
    time, level, lat, lon OR time, lat, lon, level (if change_lvl_order)

    :param: data (np.ma.array) - input data
    :param: axis (tuple) - axis to average over
    :param: times_idc (np.array) - time indices
    :param: lats_idc (np.array) - latitude indices
    :param: lons_idc (np.array) - longitude indices
    :param: lvls_idc (float) - level indices
    :param: change_lvl_order (boolean) - changes order of level dimension

    :return: avg (np.array) - average over given parameters
    """


##############################################################################
### vis.py ###################################################################
##############################################################################


def plot(
         x,
         y,
         x2=None,
         y2=None,
         subplots=1,
         title='Plot',
         title2=None,
         xlabel=None,
         ylabel=None,
         xlabel2=None,
         ylabel2=None,
         xlim_low=None,
         ylim_low=None,
         xlim2_low=None,
         ylim2_low=None,
         xlim_high=None,
         ylim_high=None,
         xlim2_high=None,
         ylim2_high=None,
         color='#ce5f5f',
         color2='#66A7C5',
         sharex=False,
         sharey=False,
         extra=False,
         extray=False,
         show=False,
         save=None,
         dates=False,
         major='days',
         minor=None,
         interval=1,
         ):
    """
    Wrapper of matplotlib.pyplot. Makes a plot.
    Only two inputs are required: x and y.
    However, some inputs require other inputs.

    :param: x (list/np.array) - main x array
    :param: y (list/np.array) - main y array
    :param: x2 (list/np.array) - secondary x array
    :param: y2 (list/np.array) - secondary y array
    :param: subplots (int) - number of subplots (max 2)
    :param: title (str) - main title
    :param: title2 (str) - secondary title
    :param: xlabel (str) - main x axis label
    :param: ylabel (str) - main y axis label
    :param: xlabel2 (str) - secondary x axis label
    :param: ylabel2 (str) - secondary y axis label
    :param: xlim_low (int/float) - main x axis lower limit
    :param: ylim_low (int/float) - main y axis lower limit
    :param: xlim2_low (int/float) - secondary x axis lower limit
    :param: ylim2_low (int/float) - secondary y axis lower limit
    :param: xlim_high (int/float) - main x axis upper limit
    :param: ylim_high (int/float) - main y axis upper limit
    :param: xlim2_high (int/float) - secondary x axis upper limit
    :param: ylim2_high (int/float) - secondary y axis upper limit
    :param: color (str) - main line color, hexcode or matplotlib color
    :param: color2 (str) - secondary line color, hexcode or matplotlib color
    :param: sharex (boolean) - share x axis trigger
    :param: sharey (boolean) - share y axis trigger
    :param: extra (boolean) - plot y2 on same plot
    :param: extray (boolean) - plot y2 on secondary axis
    :param: show (boolean) - shows plot
    :param: save (str) - name of output plot
    :param: dates (boolean) - indicates whether x axis are datetime objects
    :param: major (str) - time scale to put tick marks and label
    :param: minor (str) - time scale to put tick marks and label (buggy)
    :param: interval (int) - intervals between tick marks
    :return: fig (matplotlib.figure) - plot figure

    Optional inputs requirements -
    subplots: x2 (if not sharex), y2 (if not sharey)
    ylim_high: ylim_low (vice-versa)
    xlim_high: xlim_low (vice-versa)
    extra: y2
    extray: extra=True
    dates: x=arr. of [datetime.datetime] or x2=arr of [datetime.datetime]
    """


def plot_map(
             data, lat, lon,
             vmin, vmax,
             setup_figsize=None,
             sp_rows=1,
             sp_cols=1,
             sp_pos=1,
             data2=None,
             lat2=None,
             lon2=None,
             lower_lat=-90,
             upper_lat=90,
             left_lon=-180,
             right_lon=180,
             projection=ccrs.PlateCarree(),
             states=False,
             lakes=False,
             coastlines=True,
             cmap='gist_earth_r',
             contour=None,
             contour2=None,
             title='',
             show=False,
             save='',
             ):
    """
    Makes a map.

    :param: data (np.array) - data to be mapped
    :param: lat (np.array) - array of latitudes
    :param: lon (np.array) - array of longitudes
    :param: vmin (int) - lower limit of color bar
    :param: vmax (int) - upper limit of color bar
    :param: sp_rows (int) - subplot rows
    :param: sp_cols (int) - subplot columns
    :param: sp_pos (int) - subplot position
    :param: data2 (np.array) - contour data to be mapped
    :param: lat2 (np.array) - array of contour latitudes
    :param: lon2 (np.array) - array of contour longitudes
    :param: lower_lat (int) - lower latitude boundary
    :param: upper_lat (int) - upper latitude boundary
    :param: left_lon (int) - left latitude boundary
    :param: right_lon (int) - right latitude boundary
    :param: projection (ccrs) - map projection
    :param: states (boolean) - display states boundary
    :param: lakes (boolean) - display lakes boundary
    :param: coastlines (boolean) - display coastlines
    :param: cmap (str) - color map
    :param: contour (list) - list of positive values to contour
    :param: contour2 (list) - list of negative values to contour
    :param: title (str) - main title
    :param: save (str) - name of output file
    :param: show (boolean) - shows plot
    :return: fig, ax (matplotlib.figure, matplotlib.ax) - map figure and axis
    """


def prettify_plot(ax):
    """
    Input ax and get a pretty plot back!

    :param: ax (matplotlib.axes) - original axis
    :return: ax (matplotlib.axes) - prettified axis
    """


def set_labels(ax, xlabel, ylabel, title=''):
    """
    Input ax and names of xlabel and ylabel to return a
    prettified x axis and y axis label.

    :param: ax (matplotlib.axes) - original axis
    :param: xlabel (str) - x axis label
    :param: ylabel (str) - y axis label
    :param: title (str) - title of plot
    """


def set_legend(ax,
               color='0.5',
               fontsize='16.5',
               loc='best',
               ncol=4,
               frameon=False):
    """
    Input ax and plt to return a prettified legend. Must set
    names of labels separately though.

    :param: ax (matplotlib.axes) - original axis\
    :param: color (str) - matplotlib abbrieviation of color
    :param: fontsize (str) - font size of legend text
    :param: loc (str) - matplotlib names of locations
    :param: ncol (int) - number of legend columns
    :param: frameon (boolean) - switch for having a box around legend
    """