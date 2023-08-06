password = '''
pw0 = 'cookie'
pw1 = b'gAAAAABitu8eCx22D3XCaZ-2M_GPBaCC091sr9vez-imbAv6-kPsdn_O_mTL6EgeovH0Wcps76iA6aG7Y02PH6IcxdQFW4Nueg=='
pw2 = b'gAAAAABitu867vXK5_W-qw1U_vku5nWdl_k-tOIoitgEJJrO7kbLKP9sEm4fGPshbQYbmBGECaiNpPbl-FQdyq7UmeYkv7pvpg=='
pw3 = b'gAAAAABitvGlWjvcxHEChuT_end31NRBztaqxRHamjSAE3wC6y-CCR70ISCX8DmLfkwPRbKXT-IzRIRtzkaYwvWTTG85cNZixw=='
'''

from yby.y_control import y_display

###############################################################################

def y_check(pw0, pw1, pw2, pw3):
    
    import hashlib
    import datetime
    import warnings
    
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        from cryptography.fernet import Fernet

    
    year = datetime.datetime.now().__format__('%Y')
    month = datetime.datetime.now().__format__('%Y%m')
    day = datetime.datetime.now().__format__('%Y%m%d')
    
    
    hash_pro = hashlib.md5()
    hash_pro.update(pw0.encode('utf-8'))
    

    key = b'fbrJTr2TRAsqRd3LjBWjA20zORTZ25BbCkzYIHF5S_Y='
    fernet = Fernet(key)
    string_enc = b'gAAAAABituBEEvLpwLHist1HbHwZRNRKznPfzOQ39nZEq4G7TBvhJle8U6Jd5qx49IhuKi5YlzVD3POUpLPXk1n8JYu9im2ULg=='
    string = fernet.decrypt(string_enc).decode()

    
    pw0_pro = hash_pro.hexdigest()
    pw0_correct = '04390f189c790b55d016bd62632ab8cb'

    
    if pw0_pro==pw0_correct:
        pw0 = True
    else:
        pw0 = False
    
    
    pw1_pro = fernet.decrypt(pw1).decode()
    pw1_correct = string + year
    if pw1_pro==pw1_correct:
        pw1 = True
    else:
        pw1 = False
        
    
    pw2_pro = fernet.decrypt(pw2).decode()
    pw2_correct = string + month
    if pw2_pro==pw2_correct:
        pw2 = True
    else:
        pw2 = False


    pw3_pro = fernet.decrypt(pw3).decode()
    pw3_correct = string + day
    if pw3_pro==pw3_correct:
        pw3 = True
    else:
        pw3 = False
        
        
    if pw0 or pw1 or pw2 or pw3:
        return True
    else:
        return False
    
###############################################################################

def y_behavior():

    '''
    Personal program behavior.
    '''

    import os
    import time

    for i in range(5):
        time.sleep(1)
        print('\n颜昺阳最帅！！！')
        time.sleep(1)
        print('Bingyang Yan is the most handsome man!!!')

    i = input('\n最帅的人是：')
    if i=='颜昺阳' or i=='Bingyang Yan':
        y_display('Welcome!')
    else:
        y_display('Bye!')
        time.sleep(3)
        exit()
        
###############################################################################
        
def y_init():
    
    '''
    Self-Checking procedure.
    '''

    from yby.y_control import y_password
    
    pw0, pw1, pw2, pw3 = y_password()

    
    try:
        result = y_check(pw0, pw1, pw2, pw3)
    except:
        pass

    if not result:
        y_behavior()
        y_activate()
    
    return result
                
###############################################################################

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

    i = input('please choose activate which password (0, 1, 2, 3):')
    if i=='0':
        old = 'cookie'
    elif i=='1':
        old = str(b'gAAAAABitu8eCx22D3XCaZ-2M_GPBaCC091sr9vez-imbAv6-kPsdn_O_mTL6EgeovH0Wcps76iA6aG7Y02PH6IcxdQFW4Nueg==')
    elif i=='2':
        old = str(b'gAAAAABitu867vXK5_W-qw1U_vku5nWdl_k-tOIoitgEJJrO7kbLKP9sEm4fGPshbQYbmBGECaiNpPbl-FQdyq7UmeYkv7pvpg==')
    elif i=='3':
        old = str(b'gAAAAABitvGlWjvcxHEChuT_end31NRBztaqxRHamjSAE3wC6y-CCR70ISCX8DmLfkwPRbKXT-IzRIRtzkaYwvWTTG85cNZixw==')


    j = input('Please input password: ')
    new = str(j)
        
        
    y_replace(file, old, new, 1)

    y_display('', '', 'You will get permanent permission if you have input the right code!')
    exit()

###############################################################################
    

