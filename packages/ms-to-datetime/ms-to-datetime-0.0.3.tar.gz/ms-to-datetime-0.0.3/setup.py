from setuptools import setup, find_packages

setup(
    name='ms-to-datetime',
    version='0.0.3',
    description='Convert from ms to datetime',
    url='',
    author='Felipe Viana',
    author_email='',
    license='MIT',
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent"],
    keywords='',
    packages=find_packages(),
    install_requires=['pytz','datetime']
   
)