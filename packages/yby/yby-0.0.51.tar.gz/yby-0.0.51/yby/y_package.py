from yby.y_init import y_init
y_init()


##########################################################################

def y_addpath():
    
    '''
    Import project function instead of using functions defined in class
    '''
    
    import os
    import sys
    from yby.y_control import y_display
    
    y_display('','addpath')
    project_dir = input('Please input project function directory:')
    project_dir = project_dir.replace('"', '')
    
    sys.path.append(project_dir)
    
    assert os.path.exists(sys.path[-1]), 'Project function directory failed to append to sys.path.'

    y_display('','', '{} has been add to sys.path'.format(project_dir))
    y_display('','','end')
    
##############################################################################

def y_upload():

    '''
    Guide through upload packages to Pypi.

    PARAMETERS:
    -----------
    folder       - an empty root folder
    package      - a folder contains lots of modules
    '''

    from yby.y_text import y_license, y_readme, y_setup
    from yby.y_file import y_hotpath
    import shutil
    import os

    package = y_hotpath('Choose an uploading module:')
    folder = y_hotpath('Choose an empty folder:')
    
    assert os.listdir(folder)==[], 'yby: Root folder is not empty!'
    shutil.copytree(package,os.path.join(folder,os.path.split(package)[1]))

    license = y_license()
    readme = y_readme()

    name = os.path.split(package)[1]
    version = input('Please input version value:')
    setup = y_setup()
    setup = setup.replace('name="yby"', 'name="'+str(name)+'"')
    setup = setup.replace('version="0.0.0"', 'version="'+str(version)+'"')

    with open(os.path.join(folder, 'LICENSE.txt'), 'w', encoding='UTF-8') as fp:
        fp.write(license)
    with open(os.path.join(folder, 'README.md'), 'w', encoding='UTF-8') as fp:
        fp.write(readme)
    with open(os.path.join(folder, 'setup.py'), 'w', encoding='UTF-8') as fp:
        fp.write(setup)
            
    os.chdir(folder)
    #os.system('python setup.py check')
    os.system('python setup.py sdist bdist_wheel')
    #os.system('python -m pip install --user --upgrade twine')
    os.system('python -m twine upload dist/*')

##############################################################################
