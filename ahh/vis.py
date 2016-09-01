__author__ = 'huang.andrew12@gmail.com'
__copyright__ = 'Andrew Huang'

import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator, MonthLocator, DayLocator, HourLocator, DateFormatter

def plot(
        x,
        y,
        x2=None,
        y2=None,
        subplots=1,
        title='Plot',
        title2=None,
        xlabel='x',
        ylabel='y',
        xlabel2=None,
        ylabel2=None,
        xlim_high=None,
        ylim_high=None,
        xlim2_high=None,
        ylim2_high=None,
        xlim_low=None,
        ylim_low=None,
        xlim2_low=None,
        ylim2_low=None,
        color='#ce5f5f',
        color2='#66A7C5',
        sharex=False,
        sharey=False,
        extra=False,
        extray=False,
        show=False,
        save=False,
        name='plot.png',
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
    :param: save (boolean) - saves plot
    :param: name (str) - name of output file
    :param: dates (boolean) - indicates whether x axis are datetime objects
    :param: major (str) - time scale to put tick marks and label
    :param: minor (str) - time scale to put tick marks and label (needs more work)
    :return: fig (matplotlib.figure) - plot figure

    Optional inputs requirements - 
    subplots: x2 (if not sharex), y2 (if not sharey)
    ylim_high: ylim_low (vice-versa)
    xlim_high: xlim_low (vice-versa)
    extra: y2
    extray: extra=True
    save: name
    dates: x=arr. of [datetime.datetime] or x2=arr of [datetime.datetime]
    """
    if subplots > 1:
        if sharey:
            fig, ax = plt.subplots(
                          1, subplots,
                          sharex=sharex,
                          sharey=sharey,
                          figsize=(20,15)
                          )
        else:
            fig, ax = plt.subplots(
                          subplots,
                          sharex=sharex,
                          sharey=sharey,
                          figsize=(20,15)
                          )
        if dates:
            ax[0].plot_date(x, y, color)
        else:
            ax[0].plot(x, y, color)

        # Here's some logic to reduce redundancy
        if sharex:
            if xlabel is None:
                xlabel = xlabel2
            elif xlabel2 is None:
                xlabel2 = xlabel
            ax[0].set_ylabel(ylabel, fontsize=16)
            if dates:
                ax[1].plot_date(x, y2, color2)
            else:
                ax[1].plot(x, y2, color2)
            ax[1].set_ylabel(ylabel2, fontsize=16)
        elif sharey:
            if ylabel is None:
                ylabel = ylabel2
            elif ylabel2 is None:
                ylabel2 = ylabel
            ax[0].set_xlabel(xlabel, fontsize=16)
            ax[0].set_ylabel(ylabel, fontsize=16)
            if dates:
                ax[1].plot_date(x2, y, color2)
            else:
                ax[1].plot(x2, y, color2)
        else:
            ax[0].set_xlabel(xlabel, fontsize=16)
            ax[0].set_ylabel(ylabel, fontsize=16)
            if dates:
                ax[1].plot_date(x2, y2, color2)
            else:
                ax[1].plot(x2, y2, color2)
            ax[1].set_ylabel(ylabel2, fontsize=16)
        ax[1].set_xlabel(xlabel2, fontsize=16)
        ax[0].set_title(title, fontsize=23, y=1.03, color='.50')
        if title2 is not None:
            ax[1].set_title(title2, fontsize=23, y=1.03, color='.50')

        if dates:
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
                majorFmt = DateFormatter('\n%H')
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
            for i in range(subplots):            
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
            ax[i].spines["top"].set_visible(False)
            ax[i].spines["bottom"].set_visible(False)
            ax[i].spines["right"].set_visible(False)
            ax[i].spines["left"].set_visible(False)
            ax[i].get_xaxis().tick_bottom()
            ax[i].get_yaxis().tick_left()
            ax[i].xaxis.label.set_color('.4')
            ax[i].yaxis.label.set_color('.4')
            ax[i].tick_params(axis='x', which='both', colors='.5')
            ax[i].tick_params(axis='y', which='both', colors='.5')
            ax[i].yaxis.grid(b=True, which='major', color='.55', linestyle='--')
            ax[i].xaxis.grid(b=True, which='major', color='.5', linestyle='-')

    elif subplots == 1:
        fig, ax = plt.subplots(figsize=(21,13))
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
                    minor = MonthLocator(e)
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
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_title(title, fontsize=21, y=1.03, color='.50')

        if extra:
            if extray:
                ax2 = ax.twinx()
                ax2.plot(x, y2, color2)
                ax2.set_ylabel(ylabel2)
                if ylim_high is not None and ylim_low is not None:
                    ax2.set_ylim(ylim2_low, ylim2_high)
                if xlim_high is not None and xlim_low is not None:
                    ax2.set_xlim(xlim2_low, xlim2_high)
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
        ax.spines["top"].set_visible(False)
        ax.spines["bottom"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["left"].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()
        ax.xaxis.label.set_color('.4')
        ax.tick_params(axis='x', colors='.5')
        ax.xaxis.grid(b=True, which='major', color='.5', linestyle='-')
        if extray:
            ax.yaxis.label.set_color(color)
            ax.tick_params(axis='y', colors=color)
            ax.yaxis.grid(b=True, which='major', color=color, linestyle='--')
        else:
            ax.yaxis.label.set_color('.4')
            ax.tick_params(axis='x', colors='.5')
            ax.yaxis.grid(b=True, which='major', color='.55', linestyle='--')

    else:
        raise('Sorry, this function only supports two subplots!')

    if save:
        fig.savefig(name)

    if show:
        fig.show()

    return fig
