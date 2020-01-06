import matplotlib.pyplot as plt
import pandas as pd
import numpy as np  
import os

def multi_plot(data, argum, file_format='png', var_s=None, var_s_uni=None, var_jedn=None, show_grid = False, show_ptlabels=False, approx=False, approx_ord=2):
    """ Function plotting multiple plots for given data """
    
    # if var_s not provided use dataframe column values
    if var_s is None:
        var_s = data[0].columns.values

    # if alternate names not provided use dataframe column names
    if var_s_uni is None:
        var_s_uni = var_s

    # if units not porvided use empty string 
    if var_jedn is None:
        var_jedn = ['' for i in range(len(var_s))]

    if not os.path.exists('plots/'):
        os.mkdir('plots')

    # plotting
    for s, suni, jedn in zip(var_s, var_s_uni, var_jedn):
        
        # figure size definition (currently A4 portrait)
        # TODO: multiple size plots
        plt.figure(figsize=[8.3, 11.7])

        print("Ploting {} = f({}) to /plots".format(s, argum))

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

                    plt.annotate(y, # this is the text
                            (x,y), # this is the point to label
                            textcoords="offset points", # how to position the text
                            xytext=(0,10), # distance from text to points (x,y)
                            ha='center') # horizontal alignment can be left, right or center

            else:
                plt.plot(dat[argum], dat[s], 'b')
            
            plt.grid(show_grid)


        # main formatting
        plt.xlabel("I\N{SUBSCRIPT TWO} [A]")
        plt.ylabel("{}  [{}]".format(suni, jedn))
        plt.title("Wykres {} w zależności od I\N{SUBSCRIPT TWO}".format(suni))
            
        # plot saving
        plt.savefig("plots/plot_{}.{}".format(s, file_format), bbox_inches='tight', pad_inches=0.3)

        print("Succesfully plotted {} = f({})".format(s, 'P2'))

    print("Plotting Finished")

