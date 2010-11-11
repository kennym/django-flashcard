#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

app_name = 'flashcard'
version = '0.1.0'

if __name__ == '__main__':
    setup(
        name        = 'django-' + app_name,
        description = 'A flashcard application to practice virtual two-sided cards',
        long_description = open('README', 'r').read(),
        author      = 'Kenny Meyer',
        author_email= 'knny.myer@gmail.com',
        version     = version,
        packages    = ['flashcard'],
        url         = 'http://github.com/km0r3/dvoc',
        license     = 'BSD',
        keywords    = 'django flashcard practice',
        classifiers = [
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'Intended Audience :: Education',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Natural Language :: English',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2',
            'Topic :: Education',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    )
