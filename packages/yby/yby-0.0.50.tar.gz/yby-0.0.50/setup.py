import setuptools
 
with open("README.md", "r", encoding="utf-8") as fp:
    long_description = fp.read()
    
with open("LICENSE.txt", "r", encoding="utf-8") as fp:
    long_license = fp.read()
    
setuptools.setup(
    name="yby",
    version="0.0.50",
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
                      'cryptography'],
    
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

    