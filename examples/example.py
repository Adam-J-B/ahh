from ahh import pre, ext, sci, vis
import numpy as np
import os

__author__ = 'huang.andrew12@gmail.com'
__copyright__ = 'Andrew Huang'

###
### Example workflow using ahh repo.
### 
### Read subsurface temperature and salinity data.
### Then plot the relationship between the average of two
### over time as well as over the Eastern Pacific.
### 
### Disclaimer: This uses only nine days of data;
### do not take this as climatology or something...
###

### Prepare for downloading and reading ###
base_url_theta = 'ftp://ecco2.jpl.nasa.gov/data1/cube/cube92/lat_lon/quart_90S_90N/THETA.nc/'
glob_str_theta = 'THETA.1440x720x50.2015121*.nc'
base_url_salt = 'ftp://ecco2.jpl.nasa.gov/data1/cube/cube92/lat_lon/quart_90S_90N/SALT.nc/'
glob_str_salt = 'SALT.1440x720x50.2015121*.nc'

### Build file path ###
this_dir = os.path.dirname(os.path.realpath(__file__))
download_dir = 'example_data'
os.system('mkdir {}'.format(download_dir))
full_dir = os.path.join(this_dir, download_dir)

### Download the files ###
pre.wget_fi(base_url_theta, glob_str_theta, directory=full_dir)
pre.wget_fi(base_url_salt, glob_str_salt, directory=full_dir)

### Will return these files
### "./example_data/THETA.1440x720x50.20151212.nc"
### "./example_data/THETA.1440x720x50.20151215.nc"
### "./example_data/THETA.1440x720x50.20151218.nc"
### "./example_data/SALT.1440x720x50.20151212.nc"
### "./example_data/SALT.1440x720x50.20151215.nc"
### "./example_data/SALT.1440x720x50.20151218.nc"

### Check out the contents of the files ###
pre.ncdump(glob_str_theta, directory=full_dir)
pre.ncdump(glob_str_salt, directory=full_dir)

### We will attempt to concatenate the files into one file ###
output_theta = 'theta_2015_12_1218.nc'
output_salt = 'salt_2015_12_1218.nc'
try:
    pre.concat_nc(glob_str_theta, output_theta, directory=full_dir)
    pre.concat_nc(glob_str_salt, output_salt, directory=full_dir)
except Exception:
    print('Expected error, trying other method now...')

### However, that will result in an error
### ncrcat: ERROR no variables fit criteria for processing
### ncrcat: HINT Extraction list must contain a record variable which to concatenate

### To remedy that, we can append a record dimension by adding an input to concat_nc ###
pre.concat_nc(glob_str_theta, output_theta, directory=full_dir, rec_dim='TIME')
pre.concat_nc(glob_str_salt, output_salt, directory=full_dir, rec_dim='TIME')

### Will return these files
### "./example_data/THETA.1440x720x50.20151212.nc_rd" which was used to concat
### "./example_data/theta_2015_12_1218.nc" the final output of temperature
### "./example_data/SALT.1440x720x50.20151212.nc_rd" which was used to concat
### "./example_data/salt_2015_12_1218.nc" the final output of salinity

### Now we read the concatenated file; we're going to ignore time since our goal
### is to checkout relationship between temperature, salinity, and depth over
### the East Pacific and we will just average over time ###
output_theta_fp = os.path.join(full_dir, output_theta)
time, lat, lon, depth, theta = ext.read_nc(output_theta_fp,
            lat='LATITUDE_T',
            lon='LONGITUDE_T',
            extra='DEPTH_T',
            extra2='THETA')

### Since these are from the same distributor, we will assume lat, lon, depth
### are the same in both files so we don't waste memory
output_salt_fp = os.path.join(full_dir, output_salt)
_, _, _, salt = ext.read_nc(output_salt_fp,
            extra='SALT')

### Do a quick check if it was read in correctly. ###
ext.ahh(theta, name='theta')
ext.ahh(salt, name='salt')

### Define East Pacific region: lower, upper, left, right
    Remember, -130 < -115! ###
ep = [15, 30, -130, -115]

### Get the max min lat and lon indices.
### Since the dataset's lat and lon is defined in east longitude,
### set w2e (west to east) to True. ###
lat_start, lat_end, lon_start, lon_end  = \
    ext.get_idc(lat, lon, ep[0], ep[1], ep[2], ep[3], maxmin=True, w2e=True)

### Average over time first (axis 0) Careful though! It's masked so use np.ma ###
tavg_theta = np.ma.average(theta, axis=0)
tavg_salt = np.ma.average(salt, axis=0)

### Do another quick check ###
ext.ahh(tavg_theta, name='tavg_theta')
ext.ahh(tavg_salt, name='tavg_salt')

### Average over lat (new axis 1) ###
lat_tavg_theta = np.ma.average(tavg_theta, axis=1)
lat_tavg_salt = np.ma.average(tavg_salt, axis=1)

### Average over lon (new axis 1) ###
ep_tavg_theta = np.ma.average(lat_tavg_theta, axis=1)
ep_tavg_salt = np.ma.average(lat_tavg_salt, axis=1)

### Final check! ###
ext.ahh(ep_tavg_theta, name='ep_tavg_theta')
ext.ahh(ep_tavg_salt, name='ep_tavg_salt')

### Convert Celsius to Fahrenheit for Americans ###
ep_tavg_theta_f = sci.convert(ep_tavg_theta, c2f=True)
print(ep_tavg_theta, ep_tavg_theta_f)

### Two methods of plotting: same axes or subplots ###
vis.plot(depth, ep_tavg_theta_f,
            y2=ep_tavg_salt,
            sharex=True,
            extray=True,
            title='East Pacific - Week Average of Temperature and Salinity vs Depth',
            xlabel='Depth (m)',
            ylabel='Temperature (F)',
            ylabel2='Salinity (PSU)',
            xlim_high=2000,
            xlim_low=0,
            save='example_plot_same_axes.png')

vis.plot(depth, ep_tavg_theta_f,
            y2=ep_tavg_salt,
            subplots=2,
            sharex=True,
            title='East Pacific - Week Average of Temperature and Salinity vs Depth',
            xlabel='Depth (m)',
            ylabel='Temperature (F)',
            ylabel2='Salinity (PSU)',
            xlim_high=2000,
            xlim_low=0,
            save='example_plot_subplots.png')
