import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os


def plot_color():
    # TODO: seperate plot color generation function
    pass


def simple_plot(x, y, x_names, y_names, of_format='png', of_size=False, show_grid=False, show_ptlabels=False,
                approx=False, approx_ord=2):
    # TODO: non DataFrame plotting solution for quick simple plots
    pass


def multi_plot(data, argum, argum_unit='-', of_format='png', of_size=False, od_name='', data_fnames=None, var_ys=None,
               var_unicodes=None, var_units=None, approx=False, approx_ord=2, show_grid=False, show_ptlabels=False,
               xscale='linear', yscale='linear'):
    """
    :param data_fnames: names of files passed via data
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
    :param xscale:
    :param yscale:
    """

    # availible plot size dict
    plot_size = {'A4': [8.3, 11.7], 'A4_l': [11.7, 8.3], 'A5_l': [8.3, 11.7 / 2]}

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

    # temporary color solution
    # TODO: color solution: fix later -> possibly add option to select shades of color for multiple plots
    colors = ['b', 'g', 'm', 'r']  # temporary solution

    # plotting
    for s, suni, jedn in zip(var_ys, var_unicodes, var_units):

        # figure size definition
        if of_size:
            if of_size in plot_size.keys():
                plt.figure(figsize=plot_size[of_size])
            else:
                print(50 * '=' + '\nNot supported plot size: {}\nUsing pyplot default\n'.format(of_size) + 50 * '=')
                plt.figure()
        else:
            plt.figure()

        print("Plotting {} = f({}) to ".format(s, argum) + path)

        # plot for each dataset
        for dat, color, dat_name in zip(data, colors, data_fnames):
            if approx:
                # plotting point graph
                plt.plot(dat[argum], dat[s], '.', color=color, label=None)

                x = dat[argum].to_numpy().astype(np.float)
                y = dat[s].to_numpy().astype(np.float)

                f = np.polyfit(x, y, approx_ord)
                fp = np.poly1d(f)

                xnew = np.linspace(x.min(), x.max(), 100)

                new_label = '{} aproks. st. {}'.format(dat_name, approx_ord)

                plt.plot(xnew, fp(xnew), color=color, label=new_label)

            else:
                plt.plot(dat[argum], dat[s], 'b')

        # global plot formatting
        plt.grid(show_grid)

        plt.xscale(xscale)

        plt.yscale(yscale)

        plt.legend()

        # plot labeling
        plt.xlabel(argum + ' [{}]'.format(argum_unit))
        plt.ylabel("{}  [{}]".format(suni, jedn))
        plt.title("Wykres {} w zależności od {}".format(suni, argum))

        # plot saving
        # path creation
        save_path = path + "plot_{}=f({})".format(s, argum)
        if approx:
            save_path += '_approx={}'.format(approx_ord)

        # saving
        plt.savefig(save_path + '.{}'.format(of_format))

        print("Successfully plotted {} = f({})".format(s, argum))

    print("Plotting Finished")
