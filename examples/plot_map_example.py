from ahh import vis, ext

_, slp_lat, slp_lon, slp_arr = ext.read_nc('./example_data/slp.nc', extra='slp_pos_nao', peek=True)
_, tmp_lat, tmp_lon, tmp_arr = ext.read_nc('./example_data/tmp.nc', extra='tmp_pos_nao')

ext.ahh(tmp_arr)

vis.plot_map(slp_arr, slp_lat, slp_lon, -10, 10,
            data2=slp_arr, lat2=slp_lat, lon2=slp_lon,
            contour=[2,4], contour2=[-4,-2], title='NAO (+) Test',
            save='test', setup_figsize=(16, 7))