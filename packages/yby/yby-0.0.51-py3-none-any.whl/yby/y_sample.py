from yby.y_init import y_init
y_init()


###############################################################################

def y_lhs(minv, maxv, layers):
    
    '''
    Generate Latin Hypercube Samples.
    
    PARAMETERS:
    -----------
    minv       - minimum value list
    maxv       - maximum value list
    layers     - layers (points numbers)
    
    RETUNRS:
    --------
    points     - np.ndarray, (layers, len(minv))
    '''
    
    import numpy as np
    from pyDOE import lhs
    
    
    assert len(minv)==len(maxv), 'Minv and max have different length!'
    
    minv = np.array(minv)
    maxv = np.array(maxv)
    dims = len(minv)
    
    points = minv + (maxv - minv) * lhs(dims, layers)
    
    return points

###############################################################################
