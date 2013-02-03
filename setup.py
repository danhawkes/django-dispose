#!/usr/bin/env python
from setuptools import setup

setup(
    name='django-dispose',
    description='Disposes of media files that are no longer referenced in the \
    database.',
    version='1.0',
    author='danhawkes',
    author_email='dan@danhawkes.co.uk',
    license='MIT',
    url='https://bitbucket.org/danhawkes/django-dispose',
    packages=[
        'django_dispose',
        'django_dispose.management',
        'django_dispose.management.commands'],
    classifiers=[
        'Development Status :: 4 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: System :: Installation/Setup'
    ]
)
