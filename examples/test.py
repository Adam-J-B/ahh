from ahh import ext

x, y, z, salt = ext.read_nc("/vagrant/ahh/examples/example_data/SALT.1440x720x50.20151212.nc", time='TIME', lat='LATITUDE_T', lon='LONGITUDE_T', extra='SALT')
ext.ahh(salt, center=15, threshold=30, offset=50, precision=1, suppress=True)