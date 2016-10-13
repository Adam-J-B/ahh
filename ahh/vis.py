import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.gridliner import (
                                  LONGITUDE_FORMATTER,
                                  LATITUDE_FORMATTER
                                  )
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator, MonthLocator, DayLocator,\
                             HourLocator, DateFormatter

__author__ = 'huang.andrew12@gmail.com'
__copyright__ = 'Andrew Huang'


class MissingInput(Exception):
    pass


class Unsupported(Exception):
    pass


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
    if subplots == 2 and x2 is None and sharex is False:
        print('\nMissing input "x2" to create second plot!\n')
        raise(MissingInput)
    if subplots == 2 and y2 is None and sharey is False:
        print('\nMissing input "y2" to create second plot!\n')
        raise(MissingInput)
    if ylim_high is not None and ylim_low is None:
        print('\nMissing input "ylim_low" to set upper y limit!\n')
        raise(MissingInput)
    if ylim_low is not None and ylim_high is None:
        print('\nMissing input "ylim_high" to set lower y limit!\n')
        raise(MissingInput)
    if ylim2_high is not None and ylim2_low is None:
        print('\nMissing input "ylim2_low" to set secondary upper y limit!\n')
        raise(MissingInput)
    if ylim2_low is not None and ylim2_high is None:
        print('\nMissing input "ylim2_high" to set secondary lower y limit!\n')
        raise(MissingInput)
    if extra and y2 is None:
        print('\nMissing a "y2" to use "extra" input!\n')
        raise(MissingInput)
    if extray and extra is False:
        print(
            'Input "extra" automatically set to True because "of extray"')
        extra = True
    if subplots > 1:
        if sharey:
            fig, ax = plt.subplots(
                          1, subplots,
                          sharex=sharex,
                          sharey=sharey,
                          figsize=(20, 15)
                          )
        else:
            fig, ax = plt.subplots(
                          subplots,
                          sharex=sharex,
                          sharey=sharey,
                          figsize=(20, 15)
                          )
        if dates:
            ax[0].plot_date(x, y, color)
        else:
            ax[0].plot(x, y, color)

        # Here's some logic to reduce redundancy
        if sharex:
            if xlabel is None:
                if xlabel2 is not None:
                    xlabel = xlabel2
                else:
                    print('No xlabel found, defaulting to "x"')
                    xlabel = 'x'
            elif xlabel2 is None:
                if xlabel is not None:
                    xlabel2 = xlabel
                else:
                    print('No xlabel2 found, defaulting to "x2"')
                    xlabel2 = 'x2'
            ax[0].set_ylabel(ylabel, fontsize=16.5)
            if dates:
                ax[1].plot_date(x, y2, color2)
            else:
                ax[1].plot(x, y2, color2)
            ax[1].set_ylabel(ylabel2, fontsize=16.5)
        elif sharey:
            if ylabel is None:
                if ylabel2 is not None:
                    ylabel = ylabel2
                else:
                    print('No ylabel found, defaulting to "y"')
                    ylabel = 'y'
            elif ylabel2 is None:
                if ylabel is not None:
                    ylabel2 = ylabel
                else:
                    print('No ylabel2 found, defaulting to "y2"')
                    ylabel2 = 'y2'
            ax[0].set_xlabel(xlabel, fontsize=16.5)
            ax[0].set_ylabel(ylabel, fontsize=16.5)
            if dates:
                ax[1].plot_date(x2, y, color2)
            else:
                ax[1].plot(x2, y, color2)
        else:
            if xlabel is None:
                print('No xlabel found, defaulting to "x"')
                xlabel = 'x'
            if xlabel2 is None:
                print('No xlabel2 found, defaulting to "x2"')
                xlabel2 = 'x2'
            if ylabel is None:
                print('No ylabel found, defaulting to "y"')
                ylabel = 'y'
            if ylabel2 is None:
                print('No ylabel2 found, defaulting to "y2"')
                ylabel2 = 'y2'
            ax[0].set_xlabel(xlabel, fontsize=16.5)
            ax[0].set_ylabel(ylabel, fontsize=16.5)
            if dates:
                ax[1].plot_date(x2, y2, color2)
            else:
                ax[1].plot(x2, y2, color2)
            ax[1].set_ylabel(ylabel2, fontsize=16.5)
        ax[1].set_xlabel(xlabel2, fontsize=16.5)
        ax[0].set_title(title, fontsize=23, y=1.03, color='.50')
        if title2 is not None:
            ax[1].set_title(title2, fontsize=23, y=1.03, color='.50')

        if dates:
            if major == 'years':
                major = YearLocator(interval=interval)
                majorFmt = DateFormatter('%Y')
            elif major == 'months':
                major = MonthLocator(interval=interval)
                majorFmt = DateFormatter('%m%Y')
            elif major == 'days':
                major = DayLocator(interval=interval)
                majorFmt = DateFormatter('%m/%d')
            elif major == 'hours':
                major = HourLocator(interval=interval)
                majorFmt = DateFormatter('\n%H')
            if minor is not None:
                if minor == 'years':
                    minor = YearLocator(interval=interval)
                    minorFmt = DateFormatter('\n%Y')
                elif minor == 'months':
                    minor = MonthLocator(interval=interval)
                    minorFmt = DateFormatter('\n%m')
                elif minor == 'days':
                    minor = DayLocator(interval=interval)
                    minorFmt = DateFormatter('\n%d')
                elif minor == 'hours':
                    minor = HourLocator(interval=interval)
                    minorFmt = DateFormatter('\n%H')
            for i in range(subplots):
                if major is not None:
                    ax[i].xaxis.set_major_locator(major)
                    ax[i].xaxis.set_major_formatter(majorFmt)
                if minor is not None:
                    ax[i].xaxis.set_minor_locator(minor)
                    ax[i].xaxis.set_minor_formatter(minorFmt)
            plt.gcf()
            fig.autofmt_xdate()

        if ylim_high is not None and ylim_low is not None:
            ax[0].set_ylim(ylim_low, ylim_high)
        if xlim_high is not None and xlim_low is not None:
            ax[0].set_xlim(xlim_low, xlim_high)

        if ylim2_high is not None and ylim2_low is not None:
            ax[1].set_ylim(ylim2_low, ylim2_high)
        if xlim2_high is not None and xlim2_low is not None:
            ax[1].set_xlim(xlim2_low, xlim2_high)

        # Apply some prettifying
        for i in range(subplots):
            prettify_plot(ax[i])

    elif subplots == 1:
        fig, ax = plt.subplots(figsize=(21, 13))
        if dates:
            ax.plot_date(x, y, color)
            if major == 'years':
                major = YearLocator()
                majorFmt = DateFormatter('%Y')
            elif major == 'months':
                major = MonthLocator()
                majorFmt = DateFormatter('%m')
            elif major == 'days':
                major = DayLocator()
                majorFmt = DateFormatter('%d')
            elif major == 'hours':
                major = HourLocator()
                majorFmt = DateFormatter('%H')
            if minor is not None:
                if minor == 'years':
                    minor = YearLocator()
                    minorFmt = DateFormatter('\n%Y')
                elif minor == 'months':
                    minor = MonthLocator()
                    minorFmt = DateFormatter('\n%m')
                elif minor == 'days':
                    minor = DayLocator()
                    minorFmt = DateFormatter('\n%d')
                elif minor == 'hours':
                    minor = HourLocator()
                    minorFmt = DateFormatter('\n%H')
            ax.xaxis.set_major_locator(major)
            ax.xaxis.set_major_formatter(majorFmt)
            if minor is not None:
                ax.xaxis.set_minor_locator(minor)
                ax.xaxis.set_minor_formatter(minorFmt)
            fig.autofmt_xdate()
        else:
            ax.plot(x, y, color)
        if ylim_high is not None and ylim_low is not None:
            ax.set_ylim(ylim_low, ylim_high)
        if xlim_high is not None and xlim_low is not None:
            ax.set_xlim(xlim_low, xlim_high)
        if xlabel is None:
            print('No xlabel found, defaulting to "x"')
            xlabel = 'x'
        if ylabel is None:
            print('No ylabel found, defaulting to "y"')
            ylabel = 'y'
        ax.set_title(title, fontsize=21, y=1.03, color='.50')
        ax.set_xlabel(xlabel, fontsize=16.5)
        ax.set_ylabel(ylabel, fontsize=16.5)

        if extra:
            if extray:
                ax2 = ax.twinx()
                ax2.plot(x, y2, color2)
                if ylabel2 is None:
                    print('No ylabel2 found, defaulting to "y2"')
                    ylabel2 = 'y2'
                ax2.set_ylabel(ylabel2, fontsize=16.5)
                if ylim2_high is not None and ylim2_low is not None:
                    ax2.set_ylim(ylim2_low, ylim2_high)
                if xlim_high is not None and xlim_low is not None:
                    ax2.set_xlim(xlim_low, xlim_high)
                ax2.spines["top"].set_visible(False)
                ax2.spines["bottom"].set_visible(False)
                ax2.spines["right"].set_visible(False)
                ax2.spines["left"].set_visible(False)
                ax2.get_yaxis().tick_right()
                ax2.yaxis.label.set_color(color2)
                ax2.tick_params(axis='y', colors=color2)
                ax2.grid(b=True, which='major', color=color2, linestyle='--')
            else:
                ax.plot(x, y2, color2)

        # Prettify it!
        prettify_plot(ax)
        if extray:
            ax.yaxis.label.set_color(color)
            ax.tick_params(axis='y', colors=color)
            ax.yaxis.grid(b=True, which='major', color=color, linestyle='--')
        else:
            ax.yaxis.label.set_color('.4')
            ax.tick_params(axis='y', colors='.5')
            ax.yaxis.grid(b=True, which='major', color='.55', linestyle='--')

    else:
        print('Sorry, this function only supports two subplots\n!')
        raise(Unsupported)

    if save is not None:
        fig.savefig(save)

    if show:
        fig.show()

    return fig


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
    if setup_figsize is not None:
        fig = plt.figure(figsize=setup_figsize)
    ax = plt.subplot(sp_rows, sp_cols, sp_pos, projection=projection)
    ax.set_extent([left_lon, right_lon, lower_lat, upper_lat], projection)
    if states:
        feature_name = 'admin_1_states_provinces_lines'
        states_provinces = cfeature.NaturalEarthFeature(category='cultural',
                                                        name=feature_name,
                                                        scale='10m',
                                                        facecolor='none')
        ax.add_feature(states_provinces, edgecolor='black')
    if lakes:
        lakes = cfeature.NaturalEarthFeature(category='physical',
                                             name='lakes',
                                             scale='10m',
                                             facecolor='none')
        ax.add_feature(lakes, edgecolor='black', lw=1)
    if coastlines:
        ax.coastlines()
    gl = ax.gridlines(crs=projection, draw_labels=True,
                      linewidth=0.5, color='black', alpha=0.5, linestyle='--')
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER
    gl.xlabels_top = False

    im = ax.pcolormesh(lon, lat, data,
                       cmap=cmap, vmin=vmin, vmax=vmax)
    plt.colorbar(im)

    if contour is not None:
        im1 = ax.contour(lon2,
                         lat2,
                         data2 / 100,
                         contour, linewidths=1,
                         colors='k', linestyles="solid")
        plt.clabel(im1, fontsize=15, inline=1, fmt='%1.0f')

    if contour2 is not None:
        im2 = ax.contour(lon2,
                         lat2,
                         data2 / 100,
                         contour, linewidths=1,
                         colors='k', linestyles="solid")
        plt.clabel(im2, fontsize=15, inline=1, fmt='%1.0f')

    ax.set_title(title)

    if save != '':
        plt.savefig(save)

    if show:
        plt.show()

    return fig, ax


def prettify_plot(ax):
    """
    Input ax and get a pretty plot back!

    :param: ax (matplotlib.axes) - original axis
    :return: ax (matplotlib.axes) - prettified axis
    """
    ax.spines["top"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.xaxis.label.set_color('.4')
    ax.yaxis.label.set_color('.4')
    ax.tick_params(
        axis='x', which='both', colors='.5', labelsize=12)
    ax.tick_params(
        axis='y', which='both', colors='.5', labelsize=12)
    ax.yaxis.grid(
        b=True, which='major', color='.55', linestyle='--')
    ax.xaxis.grid(
        b=True, which='major', color='.55', linestyle='--')
    return ax


def set_labels(ax, xlabel, ylabel, title=''):
    """
    Input ax and names of xlabel and ylabel to return a
    prettified x axis and y axis label.

    :param: ax (matplotlib.axes) - original axis
    :param: xlabel (str) - x axis label
    :param: ylabel (str) - y axis label
    :param: title (str) - title of plot
    """
    ax.set_xlabel(xlabel, fontsize=16.5)
    ax.set_ylabel(ylabel, fontsize=16.5)
    ax.set_title(title, fontsize=21, y=1.03, color='.50')


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
    leg = ax.legend(loc=loc, ncol=ncol, fontsize=fontsize, frameon=frameon)
    for text in leg.get_texts():
        plt.setp(text, color=color)
