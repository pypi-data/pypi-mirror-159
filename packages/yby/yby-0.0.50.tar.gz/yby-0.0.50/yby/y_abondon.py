from yby.y_init import y_init
y_init()


'''
Deprecated functions.
'''

##############################################################################

def y_category(csv_name):

    
    '''
    recommand pandas.read_csv, csv package is verbose
    This function is used to get how many kinds of variables by column, and the num of every variable
    
    PARAMETERS:
    -----------
    csv_name - csv filename
    
    RETURN:
    -------
    result   - a dict, sub dict num equal to clolumn num in csv file
    '''

    import numpy as np
    import pandas as pd
    import csv
    
    #读取文件表头
    with open(csv_name) as fp:
        reader  = csv.reader(fp)
        content = [] #将csv文件中的内容存储到content
        for row in reader:
            content.append(row)
            
        print('header:\n', content[0])
    
    
    #将文件所有内容读取为字典，key为表头，value为一列数据组成的列表
    all_content = {}
    for i in range(len(content[0])): #遍历每一列
        with open(csv_name) as fp:
            reader = csv.DictReader(fp)
            column = []
            for row in reader: #遍历csv文件中每一行中的内容
                tem = row[content[0][i]]
                tem.strip().split(',')
                column.append(tem) #将每列的内容存储到一个列表
            all_content[content[0][i]] = column #all_content是csv所有数据的字典，key为首行，value为每列
    
    
    #将上面字典中的value列表替换成set处理后的集合
    set_col = {}
    for key,value in all_content.items():
        set_col[key] = list(set(value)) #列出每列数据中变量的种类
    
    
    #key不变，value集合中添加元素个数信息
    result = {}
    for key,value in set_col.items():
        tem_set_col = {}
        for b in value:  
            tem_set_col[b] = all_content[key].count(b) #临时记录一列数据中变量的个数
        result[key] = tem_set_col

    return result
    print('\nresult:\n', result)

##############################################################################
    
class Y_pkl2data(object):

    def __init__(self, pkl_file):
        
        import pickle as pkl
        
        with open(pkl_file, 'rb') as fp:
            data = pkl.load(fp)
        
        the_list = []
        for i in data['G']['FracGrid'].keys():
            the_list.append(sum(data['G']['FracGrid'][i]['cells']['volumes']))
        
        # 创建实例属性
        self.celldim = data['Y']['G']['celldim']
        self.physdim = data['Y']['G']['physdim']
        self.poro_m = data['G']['rock']['poro']
        self.poro_f = data['Y']['frac']['poro']
        self.perm_m = data['G']['rock']['perm']
        self.perm_f = data['Y']['frac']['perm']
        self.pres = data['Y']['flash']['p_sc']
        self.temp = data['Y']['flash']['T_sc']
        self.num_f = data['Y']['frac']['num']
        self.volu_f = the_list
        self.widt_f = data['Y']['frac']['aperture']
        self.satu_w = data['Y']['state']['saturation'][0]
        self.satu_o = data['Y']['state']['saturation'][1]
        self.satu_g = data['Y']['state']['saturation'][2]
        self.visc_w = data['Y']['fluid']['mu'][0]
        self.visc_o = data['Y']['fluid']['mu'][1]
        self.visc_g = data['Y']['fluid']['mu'][2]
    
        self.file = pkl_file
    
    def get_all(self):
        
        import pickle as pkl
        
        with open(self.file, 'rb') as fp:
            data = pkl.load(fp)

        print('Data from file: ', self.file)
        
        return data

#############################################################################

def y_entropy(*l_prob):
    
    '''
    计算一组和为1的概率的熵
    l_prob: 一组和为1的概率值，输入形式可以是多参数、元组、列表
    result: 熵的值
    '''
    
    import numpy as np
    
    result = 0
    sum_p = 0
    for i in l_prob:
        current = - i * np.log2(i)
        result = result + current
        sum_p += i
    assert sum_p - 1 <= np.power(10.0, -6), 'sum(probability) !=1'
    
    return result

#############################################################################

def y_gini(a, b):
    
    '''
    计算gini系数
    a, b: 只有两个位置参数，分别代表两类事件的个数
    result: gini系数值
    '''

    import numpy as np
    
    sum1 = a + b
    result = 1 - np.power(a / sum1, 2) - np.power(b / sum1, 2)
    assert isinstance(a, int)
    assert isinstance(b, int)
    
    return result

##############################################################################

def y_mat2data(mat_file):
    
    '''
    Prepare proxy model data by extracting data from mat_file.
    Rely on y_mat2pkl in y_mrst,py
    
    PARAMETERS:
    -----------
    mat_file   - mrst simulate result
    
    RETURNS:
    --------
    the_dict   - dict format
    '''
    
    from yby.y_mrst import y_mat2pkl, y_read_t, y_cal_q 
    
    orig_data = y_mat2pkl(mat_file)
    
    the_dict = {}

    if 'Y' in orig_data.keys():
        the_dict['Y'] = orig_data['Y']
    
    the_dict['time'] = {}
    time_argu = ['step_second', 'step_day', 'sum_second', 'sum_day']
    for i in time_argu:
        the_dict['time'][i] = y_read_t(orig_data, i)
    
    the_dict['frac'] = orig_data['fracplanes']
    
    the_dict['prod'] = {}
    prod_argu1 = ['qWr', 'qWs', 'qOr', 'qOs', 'qGr', 'qGs', 'qTr', 'qTs']
    prod_argu2 = ['rate', 'prod', 'sum']
    for i in prod_argu1:
        the_dict['prod'][i] = {}
    for i in prod_argu1:
        for j in prod_argu2:
            the_dict['prod'][i][j] = y_cal_q(orig_data, i, j)
    
    return the_dict

##############################################################################

def y_mrst_check_start(eng, verbose='off'):
    
    '''
    Check if MRST startup has been running or not
    
    PARAMETERS:
    -----------
    eng         - matlab engine
    
    RETURNS:
    --------
    bool        - bool value 
    '''

    from yby.y_control import y_display

    flow = y_start()
    
    try:
        if flow['verbose']=='on':
            y_display('MRST check start')
            print('matlab engine CWD:', eng.cd())
        eng.mrstStartupMessage(nargout=0)
    except:
        if flow['verbose']=='on':
            print('MRST has not been started!')
        return False
    else:
        if flow['verbose']=='on':
            print('MRST has been started!')
        return True
    
##############################################################################

def y_bar(current, total, start_time=None, desc='', symbol='*', symbol_num=50, info={}):
    
    '''
    Display a progress bar which is embedded in a loop.
    
    PARAMETERS:
    -----------
    current      - current length
    total        - total length
    time         - start time
    symbol       - symbol
    symbol_num   - symbol number
    info         - dict format
    '''
    
    import sys
    import time
    import datetime

    
    the_time = datetime.datetime.now()
    
    rate = float(current) / total
    rate_num = int(symbol_num * rate)

    if start_time:
        content = '\r{}: [{}{}] {}%  [{} m {} s]'.format(desc, symbol*rate_num, ' '*(symbol_num - rate_num), int(rate * 100), int((the_time-start_time).seconds//60), int((the_time-start_time).seconds%60))
    else:
        content = '\r{}: [{}{}] {}%'.format(desc, symbol*rate_num, ' '*(symbol_num - rate_num), int(rate * 100))
    
    string = ''
    for k,v in info.items():
        string += ' {}:{}'.format(k,v)
    content = content + string
    
    sys.stdout.write(content)
    sys.stdout.flush()

##############################################################################

def y_activate():

    '''
    Configure cookies and activate this program permanently.
    
    '''
    
    import os
    import yby

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

    y_display('Activate')
    
    file = os.path.join(os.path.dirname(yby.__file__), 'y_control.py')

    i = input('', 'Choose pw', 'please input 0, 1, 2, or 3:')
    if i==0:
        old = 'password0'
    elif i==1:
        old = str(b'gAAAAABitu8eCx22D3XCaZ-2M_GPBaCC091sr9vez-imbAv6-kPsdn_O_mTL6EgeovH0Wcps76iA6aG7Y02PH6IcxdQFW4Nueg==')
    elif i==2:
        old = str(b'gAAAAABitu867vXK5_W-qw1U_vku5nWdl_k-tOIoitgEJJrO7kbLKP9sEm4fGPshbQYbmBGECaiNpPbl-FQdyq7UmeYkv7pvpg==')
    elif old==3:
        old = str(b'gAAAAABitvGlWjvcxHEChuT_end31NRBztaqxRHamjSAE3wC6y-CCR70ISCX8DmLfkwPRbKXT-IzRIRtzkaYwvWTTG85cNZixw==')


    j = input('Please input password: ')
    new = str(j)
        
        
    y_replace(file, old, new)

    y_display('', '', 'You will get permanent permission if you have input the right code!')
    exit()

##############################################################################

