from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'A nice and sweet API wrapper made for Maple'
LONG_DESCRIPTION = 'A nice and sweet API wrapper made for Maple'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="maple-syrup", 
        version=VERSION,
        author="Aditya Priyadarshi",
        author_email="adityapriyadarshi669@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['requests'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'API'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)