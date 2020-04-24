# ~*~ coding=utf-8 ~*~

from setuptools import setup

setup(
    name='knv_paypal_matcher',
    version='0.3',
    description='Matches KNV online shop invoices with payments received via PayPal™',
    url='http://github.com/Fundevogel/knv-paypal-matcher',
    author='Martin Folkers',
    author_email='hello@twobrain.io',
    maintainer='Fundevogel',
    maintainer_email='dev@fundevogel.de',
    license='MIT',
    packages=['knv_pypal'],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Office/Business :: Financial :: Accounting'
        ],
    zip_safe=False
)
