

class Y():
    
    '''
    Serve the yby package
    '''

    def __init__(self):

        self.verbose = True
        self.the_assert = True
        

    def start(self, name=''):

        '''
        PARAMETERS:
        ----------
        title      - default is ''
        '''

        from yby.y_time import y_datetime
        from yby.y_control import y_display

        
        if self.verbose:
            y_display(name)
        self.start_string, self.start_stamp = y_datetime('second', 'all')


    def end(self):

        from yby.y_time import y_datetime

        self.end_string, self.end_stamp = y_datetime('second', 'all')
        self.run_time = self.end_stamp - self.start_stamp


    def get_report(self, attr_list=None, verbose=None):

        '''
        Report

        PARAMETERS:
        -----------
        attr_list   - default is None, attribute list
        verbose     - default is None
        '''

        from yby.y_control import y_display

        the_report = {}
        for i in attr_list:
            the_report[i] = getattr(self, i, 'NotFound')

        
        if verbose:
            y_display('', '', the_report)

        return the_report
    
###############################################################################
    
def y_password():
    
    pw0 = 'cookie'
    pw1 = b'gAAAAABitu8eCx22D3XCaZ-2M_GPBaCC091sr9vez-imbAv6-kPsdn_O_mTL6EgeovH0Wcps76iA6aG7Y02PH6IcxdQFW4Nueg=='
    pw2 = b'gAAAAABitu867vXK5_W-qw1U_vku5nWdl_k-tOIoitgEJJrO7kbLKP9sEm4fGPshbQYbmBGECaiNpPbl-FQdyq7UmeYkv7pvpg=='
    pw3 = b'gAAAAABitvGlWjvcxHEChuT_end31NRBztaqxRHamjSAE3wC6y-CCR70ISCX8DmLfkwPRbKXT-IzRIRtzkaYwvWTTG85cNZixw=='
    
    return pw0, pw1, pw2, pw3
    
###############################################################################
    
def y_display(title='', description='', text='', symbol='*', sep_line='-'):

    import pprint

    symbol_a = '*'
    for i in range(len(title)+3):
        symbol_a = symbol_a + symbol

    symbol_b = '-'
    for i in range(len(description)+3):
        symbol_b = symbol_b + sep_line


    # 处理title
    if len(title)>0:
        title = ' ' + title + ' '
        print('\n' + symbol_a)
        print(symbol + title + symbol)
        print(symbol_a)

    
    # 处理description
    if len(description)>0:
        description = ' ' + description + ' '
        print('\n' + symbol_b)
        print(sep_line + description + sep_line)
        print(symbol_b)

        
    # 处理text
    if len(text)>0 and text!='end':
        
        if isinstance(text, dict):
            for k,v in text.items():
                y_display('','','{} : {}'.format(k,v))
 
        else:
            print('')
            print(text)
            
    elif text=='end':
        symbol_b = '-'
        for i in range(78):
            symbol_b = symbol_b + sep_line
            
        print('\n' + symbol_b + '\n')

###############################################################################

def y_get():

    import os
    import getpass
    import warnings
    from cryptography.fernet import Fernet
    from yby.y_control import y_display
    
    key = b'fbrJTr2TRAsqRd3LjBWjA20zORTZ25BbCkzYIHF5S_Y='
    fernet = Fernet(key)
    
    the_input = getpass.getpass('Input:')
    the_return = fernet.encrypt(the_input.encode())
    
    y_display(str(the_return))

    os.system('pause')

###############################################################################

