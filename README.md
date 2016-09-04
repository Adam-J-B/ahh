# ahh - Andrew Huang Helps?
Found a bug? Contact me at huang dot andrew12 at gmail dot com!

Functions that I can easily reference, and maybe you too!

DISCLAIMER: This repo is still in its infancy; I tried to debug as best I could
within a couple days, but may still return  errors or do something unwanted.
Basically don't hold me accountable if something goes wrong; go read the license!

## HOW TO USE:
    - Type "git clone https://github.com/ahuang11/ahh.git"
    - Go into ahh folder (where setup.py is)
    - Type "pip install -e ." (may need to be in bash first!)
    - In a Python script, type "from ahh import vis, sci, ext"

### example usage:
    from ahh import vis
    x = [1, 2, 3, 4]
    y = [5, 6, 7, 8]
    vis.plot(x, y, show=True)

## CONTAINS:

### pre.py - pre-analysis fucnctions
    - wget_fi: downloads multiple files with a common pattern name
        - option to put in username and password
    - concat_nc: combines multiple netCDF4 files with a common pattern name
        - capability to append/reference record dimension properly

### sci.py - science functions:
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
    - get_norm_anom: get the normalized anomaly of array

### ext.py - extra functions
    - ahh: prints out a variable summary
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

### vis.py - visualization functions:
    - plot: effortlessly make beautiful plots
        - supports up to two arrays,
        - extra y-axis available,
        - up to two subplots,
        - can share x/y-axis,
        - can limit x/y-axis
        - datetimes supported for x-axis

Check individual packages' functions to read the docstrings; more details there...
Or read all the docstrings here: https://github.com/ahuang11/ahh/blob/develop/docstrings.py

## CHANGELOG:
### - v0.0.3
    - Added easily accessible docstrings.py for easier referencing
    - Linked the docstrings.py in README.md
    - Reorganized README.md for better logical progression
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
- Some in-depth usage examples!
- More conversions!
- More scientific/statistical functions!
- Add scalability in vis.plot()
- Put more work into vis.global_map()
- Implement ability for ext.ahh() to read csv.
- Fix the known issues listed below!

## KNOWN ISSUES:
- vis.plot() "minor" input is useable, but returns inconsistent font and color.
- ext.ahh() "unnest" still needs major improvement.
- ext.locate_valid_start() needs major revamp.