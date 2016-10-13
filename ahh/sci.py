import numpy as np

__author__ = 'huang.andrew12@gmail.com'
__copyright__ = 'Andrew Huang'


def get_uac(obs, fcst, clim):
    """
    Calculates the uncentered anomaly correlation

    :param: obs (np.array) - observation
    :param: fcst (np.array) - forecast
    :param: clim - (np.array) - climatology
    return: uac - (np.array) - uncentered anomaly correlation
    """
    size_arr = obs.shape
    len_arr = size_arr[0]
    uac = np.zeros(len_arr)

    for i in range(len_arr):
        fcst_prime = np.array(fcst[i, :, :] - clim)
        obs_prime = np.array(obs[i, :, :] - clim)
        numerator = np.sum(fcst_prime * obs_prime)
        denominator = np.sum(
            np.square(fcst_prime)) * np.sum(np.square(obs_prime))
        uac[i] = numerator / np.sqrt(denominator)

    return uac


def get_cac(obs, fcst, clim, idc):
    """
    Calculates the centered anomaly correlation

    :param: obs (np.array) - observation
    :param: fcst (np.array) - forecast
    :param: clim - (np.array) - climatology
    :param: idc - (np.array) - indices of grid points
    return: cac - (np.array) - centered anomaly correlation
    """
    size_arr = obs.shape
    len_arr = size_arr[0]
    cac = np.zeros(len_arr)

    lat_start_idc = idc[0][0]
    lat_end_idc = idc[0][-1]

    lon_start_idc = idc[1][0]
    lon_end_idc = idc[1][-1]

    for i in range(len_arr):
        fcst_prime = np.array(
            fcst[i, lat_start_idc:lat_end_idc, lon_start_idc:lon_end_idc] -
            clim[lat_start_idc:lat_end_idc, lon_start_idc:lon_end_idc])
        obs_prime = np.array(
            obs[i, lat_start_idc:lat_end_idc, lon_start_idc:lon_end_idc] -
            clim[lat_start_idc:lat_end_idc, lon_start_idc:lon_end_idc])

        fcst_prime_avg = np.ma.average(
            np.array(
                fcst[i, lat_start_idc:lat_end_idc, lon_start_idc:lon_end_idc] -
                clim[lat_start_idc:lat_end_idc, lon_start_idc:lon_end_idc])
            )
        obs_prime_avg = np.ma.average(
            np.array(
                obs[i, lat_start_idc:lat_end_idc, lon_start_idc:lon_end_idc] -
                clim[lat_start_idc:lat_end_idc, lon_start_idc:lon_end_idc])
            )

        numerator = np.sum((
            fcst_prime - fcst_prime_avg) * (obs_prime - obs_prime_avg))
        denominator = np.sum(np.square(fcst_prime - fcst_prime_avg)) * \
            np.sum(np.square(obs_prime - obs_prime_avg))
        cac[i] = numerator / np.sqrt(denominator)

    return cac


def get_rmse(obs, fcst, idc):
    """
    Calculates the root mean square error

    :param: obs (np.array) - observation
    :param: fcst (np.array) - forecast
    :param: idc - (np.array) - indices of grid points
    return: rmse - (np.array) - root mean square error
    """
    size_arr = obs.shape
    len_arr = size_arr[0]
    grid_points = size_arr[1] * size_arr[2]
    rmse = np.zeros(len_arr)

    lat_start_idc = idc[0][0]
    lat_end_idc = idc[0][-1]

    lon_start_idc = idc[1][0]
    lon_end_idc = idc[1][-1]

    for i in range(len_arr):
        rmse[i] = np.sqrt(
                    (1 / grid_points) *
                    np.sum(
                        np.square(
                            fcst[
                                i,
                                lat_start_idc:lat_end_idc,
                                lon_start_idc:lon_end_idc] -
                            obs[
                                i,
                                lat_start_idc:lat_end_idc,
                                lon_start_idc:lon_end_idc]
                                )
                            )
                        )
    return rmse


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
    np_var = np.array(variable)
    if not reverse:
        if mm2in:
            conv_var = np_var / 25.4
        elif c2f:
            conv_var = np_var * 1.8 + 32
        elif c2k:
            conv_var = np.var + 273.15
        elif f2k:
            conv_var = np_var * 1.8 + 32 + 273.15
        elif mps2mph:
            conv_var = np_var / 1609.344 * 3600
    elif reverse:
        if mm2in:
            conv_var = np_var * 25.4
        elif c2f:
            conv_var = (np_var - 32) / 1.8
        elif c2k:
            conv_var = np.var - 273.15
        elif f2k:
            conv_var = (np_var - 32) / 1.8 - 273.15
        elif mps2mph:
            conv_var = np_var * 1609.344 / 3600
    return conv_var


def get_norm_anom(data_avg):
    """
    Finds the normalized anomaly of some averaged data

    :param: data_avg (np.ma.array) - average data values
    :return: data_anom (float) - normalized anomaly
    """
    data_std = np.std(data_avg)
    data_clim = np.mean(data_avg)
    data_anom = np.zeros_like(data_avg)
    data_anom = (data_avg - data_clim) / data_std
    return data_anom


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
    data_shp = data.shape

    if len(data_shp) == 2:
        if lats_idc is None:
            lat_start_idc = 0
            lat_end_idc = data_shp[0]
        else:
            lat_start_idc = lats_idc.min()
            lat_end_idc = lats_idc.max()
        if lons_idc is None:
            lon_start_idc = 0
            lon_end_idc = data_shp[1]
        else:
            lon_start_idc = lons_idc.min()
            lon_end_idc = lons_idc.max()
        return np.ma.average(data[
                               lat_start_idc:lat_end_idc,
                               lon_start_idc:lon_end_idc
                               ],
                          axis=axis)

    if len(data_shp) == 3:
        if times_idc is None:
            time_start_idc = 0
            time_end_idc = data_shp[0]
        else:
            time_start_idc = times_idc.min()
            time_end_idc = times_idc.max()
        if lats_idc is None:
            lat_start_idc = 0
            lat_end_idc = data_shp[1]
        else:
            lat_start_idc = lats_idc.min()
            lat_end_idc = lats_idc.max()
        if lons_idc is None:
            lon_start_idc = 0
            lon_end_idc = data_shp[2]
        else:
            lon_start_idc = lons_idc.min()
            lon_end_idc = lons_idc.max()
        return np.ma.average(data[
                               time_start_idc:time_end_idc,
                               lat_start_idc:lat_end_idc,
                               lon_start_idc:lon_end_idc
                               ],
                          axis=axis)

    if len(data_shp) == 4:
        if change_lvl_order:
            if times_idc is None:
                time_start_idc = 0
                time_end_idc = data_shp[0]
            else:
                time_start_idc = times_idc.min()
                time_end_idc = times_idc.max()
            if lats_idc is None:
                lat_start_idc = 0
                lat_end_idc = data_shp[1]
            else:
                lat_start_idc = lats_idc.min()
                lat_end_idc = lats_idc.max()
            if lons_idc is None:
                lon_start_idc = 0
                lon_end_idc = data_shp[2]
            else:
                lon_start_idc = lons_idc.min()
                lon_end_idc = lons_idc.max()
            if lvls_idc is None:
                lvl_start_idc = 0
                lvl_end_idc = data_shp[3]
            else:
                lvl_start_idc = lvl_idc.min()
                lvl_end_idc = lvl_idc.max()
            return np.ma.average(data[
                                   time_start_idc:time_end_idc,
                                   lat_start_idc:lat_end_idc,
                                   lon_start_idc:lon_end_idc,
                                   lvl_start_idc:lvl_end_idc,
                                   ],
                              axis=axis)
        else:
            if times_idc is None:
                time_start_idc = 0
                time_end_idc = data_shp[0]
            else:
                time_start_idc = times_idc.min()
                time_end_idc = times_idc.max()
            if lvls_idc is None:
                lvl_start_idc = 0
                lvl_end_idc = data_shp[1]
            else:
                lvl_start_idc = lvl_idc.min()
                lvl_end_idc = lvl_idc.max()
            if lats_idc is None:
                lat_start_idc = 0
                lat_end_idc = data_shp[2]
            else:
                lat_start_idc = lats_idc.min()
                lat_end_idc = lats_idc.max()
            if lons_idc is None:
                lon_start_idc = 0
                lon_end_idc = data_shp[3]
            else:
                lon_start_idc = lons_idc.min()
                lon_end_idc = lons_idc.max()
            return np.ma.average(data[
                                   time_start_idc:time_end_idc,
                                   lvl_start_idc:lvl_end_idc,
                                   lat_start_idc:lat_end_idc,
                                   lon_start_idc:lon_end_idc,
                                   ],
                              axis=axis)
