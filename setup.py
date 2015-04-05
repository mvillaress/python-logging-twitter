import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='python-logging-twitter',
    version='0.3.0',
    description='Python logging handler for Twitter.',
    long_description=(read('README') + '\n\n' +
                      read('CHANGES')),
    author='Marcos Villares',
    author_email='mvillaress@gmail.com',
    url='https://github.com/mvillares/python-logging-twitter',
    packages=['logging_twitter'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Logging',
    ],
    license='GPLv2',
    install_requires=[
        'python-twitter >= 2.2',
    ],
)
