from setuptools import setup

with open('README.md') as f:
    long_desc = f.read()

setup(
    name='mvp_msr8',
    version='0.0.2',
    description='hi!',
    py_modules=['mvp_msr8'],
    long_description=long_desc,
    long_description_content_type='text/markdown',
    install_requires=['rich'],
    package_dir={'': 'src'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent'
    ]
)



'''
name:        what you will pip install, not import
py_modules:  what they will import

!! NAME OF THE MAIN FILE IN THE src DIR SHOULD BE SAME AS PACKAGE NAME
'''


