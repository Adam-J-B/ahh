from ahh import vis, ext

_, slp_lat, slp_lon, slp_arr = ext.read_nc(
                                           './example_data/slp.nc',
                                           extra='slp_pos_nao', peek=True)
_, tmp_lat, tmp_lon, tmp_arr = ext.read_nc('./example_data/tmp.nc',
                                           extra='tmp_pos_nao')

fig, ax = vis.plot_map(tmp_arr, tmp_lat, tmp_lon, -5, 5,
                       data2=slp_arr, lat2=slp_lat, lon2=slp_lon,
                       contour=[2, 4], contour2=[-4, -2], title='NAO (+) Test',
                       setup_figsize=(15, 10), left_lon=-150, right_lon=150)
