#import warnings
#warnings.filterwarnings("ignore", message='Source ID', category=Warning, module='', lineno=0, append=False)
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['text.usetex'] = True
from adjustText import adjust_text
import numpy as np
import seaborn as sns
palette = sns.color_palette("Paired")
palette[10] = (1.0, 0.5, 0.5)
sns.set(context='paper', palette=palette)
sns.set_style(sns.axes_style("ticks"),
              {'axes.grid': True})
#sns.set_palette(sns.color_palette("Set2"))
#sns.set_palette("muted")

def plot_cryptosystems_seaborn(data, x_col, y_col, type=None, hue_col=None, style_col=None, size_col=None, sizes=(20,150), xlabel='', ylabel='', xscale='linear', yscale='linear', title='', legend_pos=None, markers=True, s=100):
    fig, ax = plt.subplots()
    if type is not None:
        data = data[data['Type'] == type]
    assert(len(set(data[hue_col].values)) <= len(palette))
    sns.scatterplot(data=data,
                         x=x_col, y=y_col,
                         hue=hue_col,
                         style=style_col,
                         sizes=sizes,
                         palette=palette[0:len(set(data[hue_col].values))],
                         size=size_col,
                         ax=ax, markers=markers, s=s)
    ax.set(xscale=xscale, yscale=yscale, xlabel=xlabel, ylabel=ylabel, title=title)
    if legend_pos is not None:
        ax.legend(loc=legend_pos, fontsize="x-small", framealpha=0.8)
    else:
        ax.legend(fontsize="x-small", framealpha=0.8)
    return plt


def plot_cryptosystems_single_dim(data, y_col, x_col='Cipher', hue_col=None, type=None, level=None, xlabel='', ylabel='', xscale='linear', yscale='linear', title='', legend_pos=None, rotation=0, **kwargs):
    fig, ax = plt.subplots()
    if type is not None:
        data = data[data['Type'] == type]
    if level is not None:
        data = data[data['Level'] == level]
        
    g = sns.barplot(data=data,
                x=x_col, y=y_col,
                hue=hue_col,
                ax=ax,
                **kwargs
                )
    g.set_xticklabels(g.get_xticklabels(), rotation=rotation)
    #ax.set(xscale=xscale, yscale=yscale, xlabel=xlabel, ylabel=ylabel, title=title)
    #if legend_pos is not None:
    #    ax.legend(loc=legend_pos, fontsize="x-small", framealpha=0.8)
    #else:
    #    ax.legend(fontsize="x-small", framealpha=0.8)
    return plt


def plot_cryptosystems(xdata, ydata, s=None, sscale='lin', legend=None, annotations=None,xlabel='', ylabel='', xscale='linear', yscale='linear', title=''):
    return plot_cryptosystems_mpl(xdata, ydata, s, sscale, legend, annotations, xlabel, ylabel, xscale, yscale, title)

def plot_cryptosystems_mpl(xdata, ydata, s, sscale, legend, annotations, xlabel='', ylabel='', xscale='linear', yscale='linear', title=''):
    ydata = np.array(ydata)
    xdata = np.array(xdata)
    if s is not None:
        s = np.array(s)
        assert(xdata.shape == s.shape)
        if sscale == 'log':
            s = np.log(s)
    else:
        s = [None]*xdata.shape[0]

    assert(xdata.shape == ydata.shape)
    if annotations is not None:
        annotations = np.array(annotations)
        assert(annotations.shape == xdata.shape)

    fig, ax = plt.subplots()
        
    ax.set_yscale(yscale)
    ax.set_xscale(xscale)   
    for i, x in enumerate(xdata):
        if s[i] is not None:
            for j, x2 in enumerate(s[i]):
                if x2 < mpl.rcParams['lines.markersize']:
                    s[i][j] = mpl.rcParams['lines.markersize']

        ax.scatter(x, ydata[i], s=s[i])

        if annotations is not None:
            texts = []
            for j, x2 in enumerate(x):
                ax.annotate(annotations[i][j], (xdata[i][j]+1000, ydata[i][j]))

    if legend is not None:
        legend = np.array(legend)
        legend = ax.legend(legend)
        for i, x in enumerate(legend.legendHandles):
            legend.legendHandles[i]._sizes = [30]

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    return plt

