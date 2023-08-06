from yby.y_init import y_init
y_init()


###############################################################################

def y_filename(time=True, info='', ext='', **var):
    
    '''
    Get filename string.
    
    PARAMETERS:
    -----------
    ext        - extension
    time       - default is True
    *var       - variables
    
    RETURNS:
    --------
    string
    '''
    
    from yby.y_time import y_datetime
    
    assert ext, 'extension is empty'

    if time:
        time_string = y_datetime('second', 'string') + '_'
    else:
        time_string = ''
        
    middle_string = ''
    
    for k,v in var.items():
        tem = k + '_' + str(v) + '_'
        middle_string += tem

    the_string = time_string + middle_string
    if the_string[-1]=='_' and info=='':
        the_string = the_string[:-1]
    
    return the_string + info + ext

###############################################################################

def y_hotpath(title):
    '''
    Get hot path, 0 for input.

    PARAMETERS:
    title      - show as y_display(title)
    '''
    
    from yby.y_control import y_display
    
    common_path = ['Other path not in the list',
                   r'E:',
                   r'F:']

    
    y_display(title)
    for i in range(len(common_path)):
        print(str(i) + ' : ' + common_path[i])
    i = input('Input:')
    if i!='0':
        path = common_path[int(i)]
    else:
        path = input('Please input src path: ')
    
    return path

###############################################################################

def y_hotfile(title):
    '''
    Get hot file, 0 for input.

    PARAMETERS:
    title      - show as y_display(title)
    '''
    
    from yby.y_control import y_display
    
    common_file = ['Other file not in the list',
                   r"D:\颜昺阳\4. 科研项目\2020-颜昺阳-Python\Packages\yby\y_file.py",
                   r"D:\颜昺阳\4. 科研项目\2020-颜昺阳-Python\Packages\yby_project\y_proxy.py"]

    
    y_display(title)
    for i in range(len(common_file)):
        print(str(i) + ' : ' + common_file[i])
    i = input('Input:')
    if i!='0':
        file = common_file[int(i)]
    else:
        file = input('Please input src path: ')
    
    return file

###############################################################################
    
def y_find(files, string):
    
    '''
    Find string in file or files in a folder.
    
    PARAMETERS:
    -----------
    files       - file or directory
    string      - the string to look for
    
    RETURNS:
    --------
    filenames   - name of files that contain particular string
    '''
    
    import os
    
    if os.path.isfile(files):
        with open(files, 'r') as fp:
            if string in fp.read():
                return files
    
    the_list = []
    file = []
    if os.path.isdir(files):
        for r,d,f in os.walk(files):
            for ff in f:
                file.append(os.path.join(r, ff))
        for i in file:
            with open(i, 'r', encoding='utf-8') as fp:
                if string in fp.read():
                    the_list.append(i)
        
        return the_list
            
##############################################################################

def y_replace(file, old, new, max_num=1000):
    '''
    replace old str with new str in file, changeable max_num=1000
    
    PARAMETERS:
    -----------
    file         - file path
    old          - old string
    new          - new string
    max_num      - default is 1000, maximun replace times
    '''
    
    tem = []
    with open(file, 'r+', encoding='utf-8') as fp:
        contents = fp.read()

    new_contents = contents.replace(old, new, max_num)

    with open(file, 'w+', encoding='utf-8') as fp:
        fp.write(new_contents)

##############################################################################
        
def y_append(file,string,position='end'):
    
    '''
    Add string to file.
    
    PARAMETERS:
    -----------
    file       - file abspath
    string    - adding string
    position   - default is 'end', opetional:['start', 'end']
    '''
    
    import os
    
    
    with open(file, 'r+', encoding='UTF-8') as fp:
        content = fp.read()
        if position=='start':
            fp.seek(0,0)
            fp.write(string + content)
        else:
            fp.seek(0,2)
            fp.write(string)
    
    print('Successfully!')

##############################################################################

def y_isdir(path):
    
    '''
    Judge path is dir or file
    If dir, return files in current directory
    If file, return sigle file abspath
    
    PARAMETERS:
    -----------
    path       - directory or file
    
    RETURNS:
    --------
    files      - list format
               - if path is file, return single file, list format
               - if path id dir, retrun files , list format
    '''
    
    import os

    files = []
    
    if os.path.isfile(path):
        files.append(path)
        
    elif os.path.isdir(path):
        for i in os.listdir(path):
            file_path = os.path.join(path, i)
            if os.path.isfile(file_path):
                files.append(file_path)
                
    return files

##############################################################################
    
def y_rename(files, old_str='', new_str='', rena_attr='replace'):
    
    '''
    Rename files in specific mode.
    
    PARAMETERS:
    -----------
    files       - sigle file or files in a folder
    old_str     - old string
    new_str     - new string
    rena_attr   - default if replace
    
    RETURNS:
    --------
    old_path    - old file abspath, list format
    new_path    - new file abspath, list format
    '''
    
    import os
    from yby.y_file import y_isdir
    
    def rename(file, old_str, new_str):
        
        dire = os.path.dirname(file)
        
        old_name = os.path.split(file)[1]
        old_path = os.path.join(dire, old_name)
        
        new_name = old_name.replace(old_str, new_str)
        new_path = os.path.join(dire, new_name)
        
        os.rename(old_path, new_path)
        
        return old_path, new_path
    
    files_list = y_isdir(files)
    
    old_path = []
    new_path = []
    if rena_attr=='replace':
        if old_str!='':
            for i in files_list:
                old_name, new_name = rename(i, old_str, new_str)
                old_path.append(old_name)
                new_path.append(new_name)
                
        return old_path, new_path

##############################################################################

def y_empty():
    '''
    Delete empty folders in dst.
    '''
    
    import os
    from yby.y_file import y_hotpath
    from yby.y_control import y_display
    
    
    path = y_hotpath('Choose a path to remove its empty subfolders:')
    
    def check(mode='check'):
        the_list = []
        for r,d,f in os.walk(path):
            if len(os.listdir(r))==0:
                the_list.append(r)
                if mode=='exe':
                    os.rmdir(r)
                    print(r)
                
        return the_list
    
    empty_list = check('check')
    y_display('Information')
    y_display('Empty folders num: 《{}》'.format(len(empty_list)))
    for j in empty_list:
        print(j)
        
    i = input('Press y to make sure!')
    if i =='y':
        y_display('Deleting...')
        check('exe')

        
##############################################################################

def y_copy(mode=None):
    
    '''
    Copy file, files, or folder to dst path
    
    PARAMETERS:
    -----------
    mode         - optional:[file, files, folder]
                 - file: copy one file from src to dst
                 - files: copy files in src path to dst path
                 - folder: copy src folder to dst folder
    '''
    
    import os
    import shutil
    from yby.y_file import y_hotpath, y_hotfile
    
    if mode=='file':
        src = y_hotfile('Choose src file:')
        dst = y_hotpath('Choose dst path:')
        assert os.path.exists(src) and os.path.exists(dst), 'yby: src or dst not exist!'
        shutil.copy(src, dst)
        
    elif mode=='files':
        src = y_hotpath('Choose src path contain files:')
        dst = y_hotpath('Choose dst path:')
        assert os.path.exists(src) and os.path.exists(dst), 'yby: src or dst not exist!'
        for i in os.listdir(src):
            shutil.copy(os.path.join(src, i), dst)
            
    elif mode=='folder':
        src = y_hotpath('Choose src path:')
        dst = y_hotpath('Choose dst path:')
        if os.path.split(src)[1] in os.listdir(dst):
            shutil.rmtree(os.path.join(dst, os.path.split(src)[1]))
        else:
            shutil.copytree(src, os.path.join(dst, os.path.split(src)[1]))
        
    if mode=='file' or mode=='files' or mode=='folder':
        print('Operate successfully!')
    else:
        print('Wrong mode!')

###############################################################################
        
def y_sync():
    '''
    Sync files from src to dst in mirror mode!
    '''
    
    import os
    import shutil
    import warnings
    from yby.y_control import y_display
    
    def info(path):

        the_dict = {}
        for r,d,f in os.walk(path):
            r = r.replace(path, '')
            if '\\' in r:
                r = r.replace('\\', '', 1)
            the_dict[r] = {}
            the_dict[r]['dirs'] = d
            the_dict[r]['files'] = f

        return the_dict


    def file_num(the_info):

        num  = 0
        for key,value in the_info.items():
            num = num + len(the_info[key]['files'])

        return num


    def reinfo(src, dst):

        src_info = info(src)
        dst_info = info(dst)


        text1 = 'There are {:.0f} folders and {:.0f} files in {}!\n'.format(len(src_info.keys()), file_num(src_info), src)
        text2 = 'There are {:.0f} folders and {:.0f} files in {}!'.format(len(dst_info.keys()), file_num(dst_info), dst)

        y_display('', text1+text2)

        return src_info, dst_info


    def delete(mode='check'):

        the_list = []
        for key,value in dst_info.items():

            # delete single file
            if key in src_info.keys():
                for file in dst_info[key]['files']:
                    if file not in src_info[key]['files']:
                        the_list.append(os.path.join(dst, key, file))
                        if mode=='exe':
                            if not os.path.exists(os.path.join(r_path, key)):
                                os.makedirs(os.path.join(r_path, key))
                                shutil.move(os.path.join(dst, key, file), os.path.join(r_path, key, file))
                                print(os.path.join(dst, key, file))
                            else:
                                shutil.move(os.path.join(dst, key, file), os.path.join(r_path, key, file))
                                print(os.path.join(dst, key, file))
            else:

                # delete files in a folder
                for file in dst_info[key]['files']:
                    the_list.append(os.path.join(dst, key, file))
                    if mode=='exe':
                            if not os.path.exists(os.path.join(r_path, key)):
                                os.makedirs(os.path.join(r_path, key))
                                shutil.move(os.path.join(dst, key, file), os.path.join(r_path, key, file))
                                print(os.path.join(dst, key, file))
                            else:
                                shutil.move(os.path.join(dst, key, file), os.path.join(r_path, key, file))
                                print(os.path.join(dst, key, file))

        # delete empty folders
        if mode=='exe':
            for key,value in dst_info.items():
                if (dst_info[key]['dirs']==[]) and (dst_info[key]['files']==[]):
                    os.rmdir(os.path.join(dst, key))

        return the_list


    def add(mode='check'):

        the_list = []
        for key,value in src_info.items():

            # add src files in a folder
            if key not in dst_info.keys():
                for file in src_info[key]['files']:
                    the_list.append(os.path.join(src, key, file))
                    if mode=='exe':
                        if not os.path.exists(os.path.join(dst, key)):
                            os.makedirs(os.path.join(dst, key))
                            shutil.copy(os.path.join(src, key, file), os.path.join(dst, key, file))
                            print(os.path.join(src, key, file))
                        else:
                            shutil.copy(os.path.join(src, key, file), os.path.join(dst, key, file))
                            print(os.path.join(src, key, file))

            # add single from src to dst
            else:
                for file in src_info[key]['files']:
                    if file not in dst_info[key]['files']:
                        the_list.append(os.path.join(src, key, file))
                        if mode=='exe':
                            if not os.path.exists(os.path.join(dst, key, file)):
                                if not os.path.exists(os.path.join(dst, key)):
                                    os.makedirs(os.path.join(dst, key))
                                shutil.copy(os.path.join(src, key, file), os.path.join(dst, key, file))
                                print(os.path.join(src, key, file))
                            else:
                                shutil.copy(os.path.join(src, key, file), os.path.join(dst, key, file))
                                print(os.path.join(src, key, file))

        return the_list


    def update(mode='check'):

        the_list = []
        for key,value in src_info.items():
            for file in src_info[key]['files']:
                if os.path.exists(os.path.join(src, key, file)) and os.path.exists(os.path.join(dst, key, file)):
                    if os.path.getsize(os.path.join(src, key, file)) != os.path.getsize(os.path.join(dst, key, file)):
                        the_list.append(os.path.join(src, key, file))
                        if mode=='exe':
                            if not os.path.exists(os.path.join(r_path, key)):
                                os.makedirs(os.path.join(r_path, key))
                                shutil.copy(os.path.join(dst, key, file), os.path.join(r_path, key, file))
                            else:
                                shutil.copy(os.path.join(dst, key, file), os.path.join(r_path, key, file))
                            shutil.copy(os.path.join(src, key, file), os.path.join(dst, key, file))
                            print(os.path.join(src, key, file))

        return the_list


    src = y_hotpath('Choose src path:')
    dst = y_hotpath('Choose dst path:')

    ## 创建回收站
    r_path = os.path.join(os.path.split(dst)[0],'Recycle')
    if os.path.exists(r_path):
        shutil.rmtree(r_path)
    else:
        os.mkdir(r_path)

    src_info, dst_info = reinfo(src, dst)                            
    del_list = delete('check')
    add_list = add('check')
    update_list = update('check')

    y_display('Delete files num: 《{}》 '.format(len(del_list)))
    for i in del_list:
        print(i)
    y_display('Add files num: 《{}》 '.format(len(add_list)))
    for i in add_list:
        print(i)
    y_display('Update files num: 《{}》 '.format(len(update_list)))
    for i in update_list:
        print(i)
        
    y_display('','Press y to make sure!')
    i = input()

    if i=='y':
        y_display('Deleting...')
        delete('exe')
        src_info, dst_info = reinfo(src, dst) 

        y_display('Adding...')
        add('exe')
        src_info, dst_info = reinfo(src, dst) 

        if file_num(src_info) != file_num(dst_info):
            warnings.warn('File number in src is different from dst! ', UserWarning)

        y_display('Updating...')
        update('exe')
        src_info, dst_info = reinfo(src, dst)

##############################################################################

def y_txt2csv(txt_name, delimiter = ','):

    '''
    Transform txt file to csv file

    PARAMETERS:
    -----------
    txt_name  -  filename of txt
    delimiter -  comma is default

    RETURNS:
    --------
    generate a csv file that has the same name with txt file
    '''
    
    import csv
    
    new_name = txt_name[:-3] + 'csv'
    with open(txt_name, 'r') as fp1:
        content = []
        for line in fp1.readlines():
            line = line.strip().split(delimiter) #删除每行的空格和定界符
            content.append(line)
        with open(new_name, 'w', newline = '') as fp2: #创建一个同名的csv文件
            w = csv.writer(fp2)
            w.writerows(content)

##############################################################################

