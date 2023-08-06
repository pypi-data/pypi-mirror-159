from yby.y_init import y_init
y_init()


'''
Alias of basic functions.
'''
        
##############################################################################

def y_inspect(module):
    
    '''
    Get module source code.

    PARAMETERS:
    -----------
    module     - module name

    RETURN:
    -------
    text       - module source code 
    '''

    import inspect

    text = inspect.getsource(module)

    return text

##############################################################################

def y_read(file):
    
    '''
    Get file content.

    PARAMETERS:
    -----------
    file       - file path

    RETURN:
    -------
    text       - file content
    '''

    with open(file, 'r') as fp:
        text = fp.read()

    return text

##############################################################################

def y_compile(file, py_ver='39'):
    
    '''
    Compile single file or files in a folder to pyc.
    Move
    
    PARAMETERS:
    -----------
    file       - a py file or a directory contains py files
    py_ver     - python version num, default is '39'
    
    RETURNS:
    --------
    the_list   - pyc abspath, list format
    '''
    
    import os
    import shutil
    import py_compile
    from yby.y_file import y_rename, y_isdir
    
    def move(file, dire):
        
        filename = os.path.split(file)[1]
        new_path = os.path.join(dire, filename)
        shutil.move(file, new_path)
        
        return file, new_path
    
    files = y_isdir(file)
    
    the_list = []
    
    for i in files:
        py_compile.compile(i)
        pyc_name = os.path.join(os.path.dirname(i), '__pycache__',  os.path.splitext(os.path.split(i)[1])[0]+'.cpython-'+py_ver+'.pyc')
        old_name, new_name = y_rename(pyc_name, '.cpython-'+py_ver, '', 'replace')
        old_name = old_name[0]
        new_name = new_name[0]
        file, new_path = move(new_name, os.path.dirname(os.path.dirname(new_name)))
        the_list.append(new_path)
        
    return the_list

##############################################################################

