# ahh - Andrew Huang Helps?
Found a bug? Contact me at huang dot andrew12 at gmail dot com!

Functions that I can easily reference, and maybe you too!

Docstrings here: https://github.com/ahuang11/ahh/blob/master/docstrings.py

In-depth example here: https://github.com/ahuang11/ahh/blob/master/examples/example.py

DISCLAIMER: This repo is still in its infancy; I tried to debug as best I could
within a couple days, but may still return  errors or do something unwanted.
Basically don't hold me accountable if something goes wrong; go read the license!

## HOW TO USE:
    - Type "git clone https://github.com/ahuang11/ahh.git"
    - Go into ahh folder (where setup.py is)
    - Type "pip install -e ." (may need to be in bash first!)
    - In a Python script, type "from ahh import vis, sci, ext"
    - Check out example.py in the examples folder for example usage!

### example/basic_example.py - basic example usage:
    from ahh import vis
    x = [1, 2, 3, 4]
    y = [5, 6, 7, 8]
    vis.plot(x, y, show=True)

## CONTAINS:

### ahh/pre.py - pre-analysis fucnctions:
    - wget_fi: downloads multiple files with a common pattern name
        - option to put in username and password
        - option to select directory for files to be downloaded in
    - ncdump: prints out netCDF4 metadata
    - concat_nc: combines multiple netCDF4 files with a common pattern name
        - capability to append/reference record dimension properly
        - option to select directory for files to be read from
### ahh/sci.py - science functions:
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
    - get_norm_anom: get the normalized anomaly of array

### ahh/ext.py - extra functions:
    - ahh: prints out a variable summary
        - prints type, unnested type, length, and shape of a variable.
        - prints max and min of the variable
        - option to control how many numbers are printed
        - option to print the center of the array
        - option to title the print output
    - p: prints a mark in the terminal to help debug
        - option to differentiate marks
    - lonw2e: converts west longitudes to east longitudes
        - option to do reverse
    - get_idc: get the indices for bounding latitudes and longitudes
        - option return only the max and min
        - option to convert input west longitudes to east or vice versa
    - read_nc: read netCDF4 file
        - grabs the opened dataset, time, latitude, and longitude arrays
    - dt2jul: convert datetime to julian day

### vis.py - visualization functions:
    - plot: effortlessly make beautiful plots
        - supports up to two arrays,
        - extra y-axis available,
        - up to two subplots,
        - can share x/y-axis,
        - can limit x/y-axis
        - datetimes supported for x-axis
    - global_map: map out data
    - prettify_plot: effortlessly make your own plot pretty
    - set_labels: set and prettify x and y labels
        - may also set title
    - set_legend: create a legend

## CHANGELOG:
### - v0.0.7
    - Overhauled ext.ahh() to produce more info
    - Renamed ext.ahh(name='old') to ext.ahh(n='new')
    - Can add pretty labels and legends separately
    - If ext.get_idc() is empty, print warning message
    - Added datetime to Julian day conversion function
### - v0.0.6
    - Debug your code easier with ext.p()!
    - Bug fix with xlim not working properly in vis.plot()
    - Cleaned up example.py
### - v0.0.5
    - In-depth example usage is now available!
    - Completely revamped ext.ahh()
    - Fixed sci.convert()
    - Latitude and longitude optional in ext.read_nc
    - New pre.ncdump() which dumps netCDF4 metadata
    - pre.concat_nc() now supports other directories
    - Removed sci.get_atavg and ext.locate_valid_start
    - Renamed lon360 to lonw2e
    - Added ability to convert longitudes from east to west
    - Aesthetic improvements and more error messages
### - v0.0.4
    - Added ext.lon360() which converts west longitudes to east
    - Added "maxmin" and "w2e" inputs to ext.get_idc()
    - Added "directory" input to pre.wget_fi()
    - Added "interval" input to vis.plot()
    - Fixed bug where xlabel and ylabel wasn't set for single plot
### - v0.0.3
    - Added easily accessible docstrings.py for easier referencing
    - Linked the docstrings.py in README.md
    - Reorganized README.md for better logical progression
    - Added requirements to setup.py
### - v0.0.2
    - Added new package: pre.py
    - New functions pre.py: wget_fi() and concat_nc()
    - Renamed ext.eval() to ext.ahh()
    - Function ext.ahh() no longer has unnest=True as default
    - Added "bare" input to ext.ahh
    - Enhanced ext.read_nc() to include more options
    - Enhanced vis.plot() to include exception handling notices
    - Removed "name" input in vis.plot() and changed "save" input
    - New function in vis.py: global_map
    - New function in sci.py: get_norm_anom
    - Aesthetic changes all over
    - Complies with Flake8 and Codacy
### - v0.0.1
    - Creation of ahh with vis, sci, and ext packages.

## TO-DO / UPCOMING:
- Exception handling and display!
- More conversions!
- More scientific/statistical functions!
- Add scalability in vis.plot()
- Remove clutter (if, else) from vis.plot()
- Add more plots functionality in vis.plot()
- Put more work into vis.global_map()
- Replace basemap with cartopy
- Input latitudes and longitudes and locate those values into ahh
- Possibly add read csv capabilities?
- Update sci functions to be more flexible and reflect new changes
- Fix the known issues listed below!

## KNOWN ISSUES:
- vis.plot() "minor" input is useable, but returns inconsistent font and color