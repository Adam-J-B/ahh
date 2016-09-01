# ahh - Andrew Huang Helps?
Contact: huang.andrew12@gmail.com

Functions that I can easily reference, and maybe you too!

DISCLAIMER: This repo is still in its infancy; I tried to debug as best I could
within a couple days, but may still return  errors or do something unwanted.
Basically don't hold me accountable if something goes wrong; go read the license!

# CONTAINS:
vis.py - visualization functions:
    - plot: effortlessly make beautiful plots
        - supports up to two arrays,
        - extra y-axis available,
        - up to two subplots,
        - can share x/y-axis,
        - can limit x/y-axis
        - datetimes supported for x-axis

sci.py - science functions:
    - get_uac: get the uncentered anomaly correlation of grid
    - get_cac: get the centered anomaly correlation of grid
    - get_rmse: get root mean square error of grid
    - convert: does some common conversions ** UNTESTED
        - millmeters to inches
        - Celsius to Fahrenheit
        - Celsius to Kelvin
        - Fahrenheit to Kelvin
        - meters per second to miles per hour
        - All that in reverse
    - get_atavg: get the areal and time average

ext.py - extra functions
    - eval: prints out a variable summary
        - prints out type of variable, length, shape
        - prints out type of unnested, unnested of unnested, and valid value
        - option to title the print output
        - option to print out the head/tail of variable up to length
        - control the length of output/how many values get printed out
        - supports unnesting arrays
        - control the rows and columns unnested
    - get_idc: get the indices for bounding latitudes and longitudes
    - read_nc: read netCDF4 file
        - grabs the opened dataset, time, latitude, and longitude arrays
    - locate_valid_start: finds the first row and column that isn't zero or masked

Check individual packages' functions to read the docstrings; more details there...

# TO-DO / UPCOMING:
- Exception handling and display!
- More in-depth documentation!
- More conversions!
- More scientific/statistical functions!
- Fix the known issues listed below!
- Plot world maps off netCDF4 files

# KNOWN ISSUES:
- In vis.py, plot's "minor" input is useable, but returns inconsistent font and color