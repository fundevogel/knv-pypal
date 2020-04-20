# ~*~ coding=utf-8 ~*~

from setuptools import setup

setup(
    name='knv_paypal_matcher',
    version='0.2',
    description='Matches KNV online shop invoices with payments received via PayPal™',
    url='http://github.com/Fundevogel/knv-paypal-matcher',
    author='Martin Folkers',
    author_email='hello@twobrain.io',
    maintainer='Fundevogel',
    license='MIT',
    packages=['knv_pypal'],
    zip_safe=False
)
