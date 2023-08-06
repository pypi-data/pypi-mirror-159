from yby.y_init import y_init
y_init()


##############################################################################

def y_datetime(precision='day', mode='stamp'):

    '''
    Get current datetime string.

    PARAMETERS:
    -----------
    precision  - default is 'day', optional:['year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']
    mode       - default is string, optional: ['string', 'stamp', 'all']
               - string, only return str(time)
               - all, return str(time) and datetime(time)

    RETURNS:
    --------
    string  - datetime string
    '''

    from datetime import datetime

    def str_insert(string, position, content):

        '''
        Insert content at string position.
        '''

        str_list =list(string)
        str_list.insert(position, content)
        string = ''.join(str_list)

        return string

    stamp = datetime.now()

    if precision=='year':
        string = stamp.__format__('%Y')
    elif precision=='month':
        string = stamp.__format__('%Y%m')
    elif precision=='day':
        string = stamp.__format__('%Y%m%d')
    elif precision=='hour':
        string = stamp.__format__('%Y%m%d%H')
    elif precision=='minute':
        string = stamp.__format__('%Y%m%d%H%M')
    elif precision=='second':
        string = stamp.__format__('%Y%m%d%H%M%S')
    elif precision=='microsecond':
        string = stamp.__format__('%Y%m%d%H%M%S') + str(stamp.microsecond)[0:3]

    if precision in ['hour', 'minute', 'second', 'microsecond']:
        string = str_insert(string, 8, '_')
    
    if mode=='string':
        return string
    elif mode=='stamp':
        return stamp
    elif mode=='all':
        return string, stamp


##############################################################################
    
