from yby.y_init import y_init
y_init()


###############################################################################

def y_scatter(x, y, z, value, cmap='jet', title=None):
    
    '''
    plot scatter in 3D
    
    PARAMETERS:
    -----------
    x        - x array
    y        - y array
    z        - z array
    value    - value at coordinate(x, y, z)
    color    - color map 
    title    - default is None
    '''
    
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    fig = plt.figure()
    ax = plt.gca(projection="3d") 
    
    p = ax.scatter(x, y, z, c=value, cmap=cmap, marker='.', s=20, alpha=0.5)
    
    ax.grid(False)

    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    #plt.zlabel('z')
    
    plt.colorbar(p)
    plt.show()
      
###############################################################################
 
def y_cmap():
    '''
    Have colormaps separated into categories:
    http://matplotlib.org/examples/color/colormaps_reference.html
    '''
    
    import numpy as np
    import matplotlib.pyplot as plt
    
    cmaps = [('Perceptually Uniform Sequential',
                                ['viridis', 'inferno', 'plasma', 'magma']),
             ('Sequential',     ['Blues', 'BuGn', 'BuPu',
                                 'GnBu', 'Greens', 'Greys', 'Oranges', 'OrRd',
                                 'PuBu', 'PuBuGn', 'PuRd', 'Purples', 'RdPu',
                                 'Reds', 'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd']),
             ('Sequential (2)', ['afmhot', 'autumn', 'bone', 'cool',
                                 'copper', 'gist_heat', 'gray', 'hot',
                                 'pink', 'spring', 'summer', 'winter']),
             ('Diverging',      ['BrBG', 'bwr', 'coolwarm', 'PiYG', 'PRGn', 'PuOr',
                                 'RdBu', 'RdGy', 'RdYlBu', 'RdYlGn', 'Spectral',
                                 'seismic']),
             ('Qualitative',    ['Accent', 'Dark2', 'Paired', 'Pastel1',
                                 'Pastel2', 'Set1', 'Set2', 'Set3']),
             ('Miscellaneous',  ['gist_earth', 'terrain', 'ocean', 'gist_stern',
                                 'brg', 'CMRmap', 'cubehelix',
                                 'gnuplot', 'gnuplot2', 'gist_ncar',
                                 'nipy_spectral', 'jet', 'rainbow',
                                 'gist_rainbow', 'hsv', 'flag', 'prism'])]


    nrows = max(len(cmap_list) for cmap_category, cmap_list in cmaps)
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))


    def plot_color_gradients(cmap_category, cmap_list):
        fig, axes = plt.subplots(nrows=nrows)
        fig.subplots_adjust(top=0.95, bottom=0.01, left=0.2, right=0.99)
        axes[0].set_title(cmap_category + ' colormaps', fontsize=14)

        for ax, name in zip(axes, cmap_list):
            ax.imshow(gradient, aspect='auto', cmap=plt.get_cmap(name))
            pos = list(ax.get_position().bounds)
            x_text = pos[0] - 0.01
            y_text = pos[1] + pos[3]/2.
            fig.text(x_text, y_text, name, va='center', ha='right', fontsize=10)

        # Turn off *all* ticks & spines, not just the ones with colormaps.
        for ax in axes:
            ax.set_axis_off()

    for cmap_category, cmap_list in cmaps:
        plot_color_gradients(cmap_category, cmap_list)

    plt.show()

###############################################################################

def y_marker():
    
    """
    ================================
    Filled and unfilled-marker types
    ================================

    Reference for filled- and unfilled-marker types included with Matplotlib.
    """
    
    from six import iteritems
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D


    points = np.ones(3)  # Draw 3 points for each line
    text_style = dict(horizontalalignment='right', verticalalignment='center',
                      fontsize=12, fontdict={'family': 'monospace'})
    marker_style = dict(linestyle=':', color='cornflowerblue', markersize=10)


    def format_axes(ax):
        ax.margins(0.2)
        ax.set_axis_off()


    def nice_repr(text):
        return repr(text).lstrip('u')


    def split_list(a_list):
        i_half = len(a_list) // 2
        return (a_list[:i_half], a_list[i_half:])


    # Plot all un-filled markers
    # --------------------------

    fig, axes = plt.subplots(ncols=2)

    # Filter out filled markers and marker settings that do nothing.
    # We use iteritems from six to make sure that we get an iterator
    # in both python 2 and 3
    unfilled_markers = [m for m, func in iteritems(Line2D.markers)
                        if func != 'nothing' and m not in Line2D.filled_markers]
    # Reverse-sort for pretty. We use our own sort key which is essentially
    # a python3 compatible reimplementation of python2 sort.
    unfilled_markers = sorted(unfilled_markers,
                              key=lambda x: (str(type(x)), str(x)))[::-1]
    for ax, markers in zip(axes, split_list(unfilled_markers)):
        for y, marker in enumerate(markers):
            ax.text(-0.5, y, nice_repr(marker), **text_style)
            ax.plot(y * points, marker=marker, **marker_style)
            format_axes(ax)
    fig.suptitle('un-filled markers', fontsize=14)


    # Plot all filled markers.
    # ------------------------

    fig, axes = plt.subplots(ncols=2)
    for ax, markers in zip(axes, split_list(Line2D.filled_markers)):
        for y, marker in enumerate(markers):
            ax.text(-0.5, y, nice_repr(marker), **text_style)
            ax.plot(y * points, marker=marker, **marker_style)
            format_axes(ax)
    fig.suptitle('filled markers', fontsize=14)

    plt.show()

###############################################################################

def y_linestyle():
    
    """
    ====================
    Line-style reference
    ====================

    Reference for line-styles included with Matplotlib.
    """
    
    import numpy as np
    import matplotlib.pyplot as plt


    color = 'cornflowerblue'
    points = np.ones(5)  # Draw 5 points for each line
    text_style = dict(horizontalalignment='right', verticalalignment='center',
                      fontsize=12, fontdict={'family': 'monospace'})


    def format_axes(ax):
        ax.margins(0.2)
        ax.set_axis_off()


    def nice_repr(text):
        return repr(text).lstrip('u')


    # Plot all line styles.
    fig, ax = plt.subplots()

    linestyles = ['-', '--', '-.', ':']
    for y, linestyle in enumerate(linestyles):
        ax.text(-0.1, y, nice_repr(linestyle), **text_style)
        ax.plot(y * points, linestyle=linestyle, color=color, linewidth=3)
        format_axes(ax)
        ax.set_title('line styles')

    plt.show()

###############################################################################
