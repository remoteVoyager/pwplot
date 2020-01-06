import matplotlib.pyplot as plt
import pandas as pd
import numpy as np  
import os


data = [pd.read_csv('dane.csv')]
argum = 'I2'    # argument funkcji

file_format = 'pdf'

# plot formatting

approx = False  # czy aproksymować?
approx_ord = 2  # stopień wielomianu do aproksymacji

set_grid = True

show_ptlabels = True


if not os.path.exists('plots/'):
    os.mkdir('plots')

var_s = [ 'P1', 'P2', 'I1', 'U2', 'cosphi', 'ni']
var_s_uni = ['P\N{SUBSCRIPT ONE}', 'P\N{SUBSCRIPT ONE}', 'I\N{SUBSCRIPT ONE}', 'U\N{SUBSCRIPT TWO}', 'cos\N{GREEK SMALL LETTER PHI}', '\u03b7']
var_jedn = ['W', 'W', 'A', 'V', '\N{DEGREE SIGN}', '%']
ascds = []

# dla nie zadanego var_s pobierz nazwy kolumn z danych
if var_s is None:
    var_s = data[0].columns.values

if ascds is None or ascds == []:
    ascds = [None for i in range(len(var_s))]

# wykres
for s, suni, jedn, ascd in zip(var_s, var_s_uni, var_jedn, ascds):
    plt.figure(figsize=[8.3, 11.7])

    print("Ploting {} = f({}) to /plots".format(s, argum))

    for dat in data:

        if approx:
            plt.plot(dat[argum], dat[s], 'b.')

            x = dat[argum].to_numpy().astype(np.float)
            y = dat[s].to_numpy().astype(np.float)

            f = np.polyfit(x, y, 2)
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
        
        plt.grid(set_grid)

    plt.xlabel("I\N{SUBSCRIPT TWO} [A]")
    plt.ylabel("{}  [{}]".format(suni, jedn))
    plt.title("Wykres {} w zależności od I\N{SUBSCRIPT TWO}".format(suni))
        
    plt.savefig("plots/plot_{}.{}".format(s, file_format), bbox_inches='tight', pad_inches=0.3)

    print("Succesfully plotted {} = f({})".format(s, 'P2'))

print("Plotting Finished")

