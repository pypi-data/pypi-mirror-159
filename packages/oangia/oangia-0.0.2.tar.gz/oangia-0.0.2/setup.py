from setuptools import setup, find_packages

VERSION = '0.0.2' 
DESCRIPTION = 'My private package'
LONG_DESCRIPTION = 'My private package'

# Setting up
setup(
        name="oangia", 
        version=VERSION,
        author="OG",
        author_email="blogphp.biz@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['numpy', 'pandas'], # add any additional packages that 
        
        keywords=['python', 'utils'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)