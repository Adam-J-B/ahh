__author__ = 'huang.andrew12@gmail.com'
__copyright__ = 'Andrew Huang'

##############################################################################
### https://github.com/ahuang11/ahh - Andrew Huang Helps? ####################
##############################################################################

##############################################################################
### pre.py ###################################################################
##############################################################################

def wget_fi(base_url, glob_str, user=None, pwd=None):
    """
    Wrapper of wget; downloads files that matches the given glob_str. Can input
    username and password if authentication is required.

    :param: base_url (str) - the dir of all the to be downloaded files
    :param: glob_str (str) - the naming pattern of the files
    :param: user (str) - username
    :param: pwd (str) - pwd
    """


def concat_nc(glob_str, output_fi, append_rec_dim=None):
    """
    Wrapper of NCO's ncrcat and optional ncks; concatenates a list of netCDF
    files given a glob_str (i.e. 'THETA.1440x720x50.2010*.nc') and outputs
    concatenated file as the given output_fi. If there's an error complaining
    that there's no record dimension, can give the dimension name to
    concatenate across under append_rec_dim.

    :param: glob_str (str) - the naming pattern of the files
    :param: output_fi (str) - name of concatenated file
    :param: append_rec_dim (str) - name of dimension to act as record dimension
    """

##############################################################################
### ext.py ###################################################################
##############################################################################

def ahh(variable,
        name=None,
        bare=True,
        full=False,
        head=False,
        tail=False,
        output_len=8,
        unnest=False,
        unnest_row_len=2,
        unnest_col_len=5,
        locate_valid=False):
    """
    Explores a variable summary to screen; includes values, type, and shape.

    :param: variable - variable to be evaluated
    :param: name (boolean) - name of variable
    :param: bare (boolean) - only print out shape and types
    :param: full (boolean) - list out every value
    :param: head (boolean) - list of first values up to output length
    :param: tail (boolean) - list of last values up to output length
    :param: output_len (int) - length of print output
    :param: unnest (boolean) - unnests variable and list out every value
    :param: unnest_row_len (int) - number of unnested rows
    :param: unnest_col_len (int) - number of unnested columns
    :param: locate_valid (boolean) - locates the first valid value to start
    """


def get_idc(lats, lons, lower_lat, upper_lat, left_lon, right_lon):
    """
    Finds the indices for given latitudes and longitudes boundary.

    :param: lats (list) - array of latitudes
    :param: lons (list) - array of longitudes
    :param: lower_lat (float) - southern latitude boundary
    :param: upper_lat (float) - northern latitude boundary
    :param: left_lon (float) - western longitude boundary
    :param: right_lon (float) - eastern longitude boundary
    :return: lats_idc, lons_idc (np.array, np.array) - indices of lats/lons
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


def locate_valid_start(variable, num_rows, num_cols):
    """
    Finds the first row and column that isn't zero or masked.

    :param: variable - variable to be evaluated
    :param: rows (int) - number of rows of variable
    :param: cols (int) - number of columns of variable
    :return: start_row, start_col (int, int) -
             first row/col that isn't zero or masked
    """


def create_dt_arr(time_var, calendar='standard'):
    """
    Creates a datetime array based on an unopened time variable.

    :param: time_var (netCDF4.Variable) - unopened time variable
    :param: calendar (str) - type of calendar
    :return: datetime_array (np.array) - array of datetimes
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
            mm2in=True,
            c2f=True,
            c2k=True,
            f2k=True,
            mps2mph=True,
            reverse=True
            ):

def get_atavg(data, time_idc, lats_idc, lons_idc):
    """
    Finds the average over a given area and time

    :param: data (np.array) - array of data to be averaged
    :param: time_idc (np.array) - array of time indices
    :param: lats_idc (np.array) - array of latitude indices
    :param: lons_idc (np.array) - array of longitude indices
    :return: spatial_time_avg (float) - average over time and area
    """


def get_norm_anom(data_avg):
    """
    Finds the normalized anomaly of some averaged data

    :param: data_avg (np.array) - average data values
    :return: data_anom (float) - normalized anomaly
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
         minor=None
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
    :return: fig (matplotlib.figure) - plot figure

    Optional inputs requirements -
    subplots: x2 (if not sharex), y2 (if not sharey)
    ylim_high: ylim_low (vice-versa)
    xlim_high: xlim_low (vice-versa)
    extra: y2
    extray: extra=True
    dates: x=arr. of [datetime.datetime] or x2=arr of [datetime.datetime]
    """


def global_map(
              data, lat, lon, vmin, vmax,
              title='Map',
              show=False,
              save=None,
              proj='cyl',
              center=16.50
              ):
    """
    Wrapper of mpl_toolkits.basemap. Makes a map.

    :param: data (np.array) - data to be mapped
    :param: lat (np.array) - array of latitudes
    :param: lon (np.array) - array of longitudes
    :param: vmin (int) - lower limit of color bar
    :param: vmax (int) - upper limit of color bar
    :param: title (str) - main title
    :param: show (boolean) - shows plot
    :param: save (str) - name of output file
    :param: proj ('str') - abbrieviation of projection
    :param: center (int) - longitude where map will be centered
    :return: fig (matplotlib.figure) - map figure
    """
