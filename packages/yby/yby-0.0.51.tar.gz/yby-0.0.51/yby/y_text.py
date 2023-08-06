from yby.y_init import y_init
y_init()

        
##############################################################################

def y_license():

    content = '''Copyright (c) 2022 The Python Packaging Authority
 
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
 
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
 
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
    '''
    print('\nLICENSE.txt')
    print(content)

    return content

##############################################################################

def y_readme():

    content = 'Only for testing.'

    print('\nREADME.md')
    print(content)
        
    return content

##############################################################################

def y_setup():

    '''
    Setep for y_upload for Pypi
    '''

    content = '''import setuptools
 
with open("README.md", "r", encoding="utf-8") as fp:
    long_description = fp.read()
    
with open("LICENSE.txt", "r", encoding="utf-8") as fp:
    long_license = fp.read()
    
setuptools.setup(
    name="yby",
    version="0.0.0",
    description='yanbingyang personal packages',
    url='https://pypi.org/user/Flyby_98/',
    author="Bingyang Yan",
    author_email="yanbingyang1998@outlook.com",
    license=long_license,
    install_requires=['setuptools',
                      'wheel',
                      'twine',
                      'numpy',
                      'pandas',
                      'scipy',
                      'matplotlib',
                      'cryptography',
                      'tqdm',
                      'glob2'],
    
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

    '''

    print('\nsetup.py')
    print(content)


    return content

##############################################################################








