from yby.y_init import y_init
y_init()


###############################################################################

def y_points3d(x, y, z, value, cmap='jet', title=None):
    '''
    plot scatter on mayavi
    
    PARAMETERS:
    -----------
    x        - x array
    y        - y array
    z        - z array
    value    - value at coordinate(x, y, z)
    colot    - color map 
    title    - default is None
    '''
    
    from mayavi import mlab
    
    mlab.points3d(x, y, z, value, colormap=cmap)
    mlab.colorbar(orientation='vertical', nb_labels=6)

    mlab.title(title, height=0.9, size=1.5, color=(1,0,0))
    
    mlab.show()

###############################################################################
