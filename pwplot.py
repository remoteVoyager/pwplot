import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os


def multi_plot(data, argum, argum_unit='-', of_format='png', od_name='', of_size=False, var_ys=None, var_unicodes=None,
               var_units=None, show_grid=False, show_ptlabels=False, approx=False, approx_ord=2):
    """
    :param data: DataFrame containing data for plotting
    :param argum: Plotting argument f(argum)
    :param argum_unit: unit for argum
    :param of_format: output file format
    :param od_name: string added to output directory name
    :param of_size: size of figure, default: None -> standard pyplot size
    :param var_ys: variables to plot
    :param var_unicodes: variable unicode representations
    :param var_units: variable units
    :param show_grid:
    :param show_ptlabels: show points with value at point over them
    :param approx: approximate plots
    :param approx_ord: polynomial order for approximation
    """

    # if var_s not provided use dataframe column values
    if var_ys is None:
        var_ys = data[0].columns.values

    # if alternate names not provided use dataframe column names
    if var_unicodes is None:
        var_unicodes = var_ys

    # if units not porvided use empty string 
    if var_units is None:
        var_units = ['' for i in range(len(var_ys))]

    if od_name is not None:
        path = 'plots_' + of_format + '_' + od_name + '/'
    else:
        path = 'plots_' + of_format + '/'

    if not os.path.exists(path):
        os.mkdir(path)

    # check if arguments were passed as list
    if type(argum) == list:
        # TODO: passing list of arguments
        pass

    # plotting
    for s, suni, jedn in zip(var_ys, var_unicodes, var_units):

        # figure size definition (currently A4 portrait)
        # TODO: multiple size plots

        if of_size:
            if of_size == 'A4':
                plt.figure(figsize=[8.3, 11.7])
            elif of_size == 'A4_l':
                plt.figure(figsize=[11.7, 8.3])
        else:
            plt.figure()

        print("Plotting {} = f({}) to ".format(s, argum) + path)

        # plot for each dataset
        for dat in data:
            if approx:
                plt.plot(dat[argum], dat[s], 'b.')

                x = dat[argum].to_numpy().astype(np.float)
                y = dat[s].to_numpy().astype(np.float)

                f = np.polyfit(x, y, approx_ord)
                fp = np.poly1d(f)

                xnew = np.linspace(x.min(), x.max(), 100)

                plt.plot(xnew, fp(xnew), 'r')

                plt.legend(suni, suni + 'aproksymacja w. st. {}'.format(approx_ord))

            elif show_ptlabels:
                plt.plot(dat[argum], dat[s], 'bo-')

                for x, y in zip(dat[argum], dat[s]):
                    plt.annotate(y,  # this is the text
                                 (x, y),  # this is the point to label
                                 textcoords="offset points",  # how to position the text
                                 xytext=(0, 10),  # distance from text to points (x,y)
                                 ha='center')  # horizontal alignment can be left, right or center

            else:
                plt.plot(dat[argum], dat[s], 'b')

            plt.grid(show_grid)

        # main formatting
        plt.xlabel(argum + ' [{}]'.format(argum_unit))
        plt.ylabel("{}  [{}]".format(suni, jedn))
        plt.title("Wykres {} w zależności od {}".format(suni, argum))

        # plot saving
        plt.savefig(path + "plot_{}=f({}).{}".format(s, argum, of_format), bbox_inches='tight', pad_inches=0.3)

        print("Successfully plotted {} = f({})".format(s, argum))

    print("Plotting Finished")
