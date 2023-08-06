import email
from setuptools import setup, find_packages


setup(
    name='djangorestframework-enhanced',
    description='enhance django rest framework', 
    version='0.0.1', 

    author='Gnix', 
    author_email='madkarl@outlook.com', 
    license='MIT', 

    packages=find_packages(where='.', exclude=('venv', ), include=('*', )), 
    install_requires=[
        'django>=4.0.6', 
        'django-filter>=21.1', 
        'djangorestframework>=3.13.1', 
        'djangorestframework-simplejwt>=5.1.0'
        ], 
    include_package_data=True, 
)