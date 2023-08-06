from yby.y_init import y_init
y_init()

    
if __name__=='yby':

    # y_abondon
    # y_error
    # y_text

    import warnings
    
    from yby.y_alias import *
    from yby.y_control import *
    from yby.y_file import *
    from yby.y_matplotlib import *
    from yby.y_mayavi import *

    try:
        from yby.y_mrst import *
    except:
        warnings.warn('y_mrst.py is not existed.')

    try:
        from yby.y_nn import *
    except:
        warnings.warn('y_nn.py is not existed.')
        
    from yby.y_package import *
    from yby.y_sample import *
    from yby.y_time import *


    

'''
## y_display

    只有驱动类（Y_dirve, Y_mat2data）才可以使用y_display的一级标题，其他类最高只能使用二级标题。

## report
    类的report方法中默认不打印报告，只返回一个报告字典。
    在驱动类的主函数中使用class.report()函数获取报告字典，然后添加到驱动类属性，并进行打印。
    如果是dataloader的report，调用report不建议使用class.dataloader_report， 建议使用class.dataloader.report

## save
    只有驱动类才需要保存self, 默认的文件夹是output
'''
