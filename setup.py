#!/usr/bin/env python

import os

from setuptools import setup, find_packages

version = '0.1.0'

def read_file(name):
    return open(os.path.join(os.path.dirname(__file__),
                             name)).read()

readme = read_file('README.rst')
changes = read_file('CHANGES.txt')

if __name__ == '__main__':
    setup(
        name        = 'django-flashcard',
        description = 'A flashcard application to practice virtual two-sided cards',
        long_description = ''.join(readme),
        author      = 'Kenny Meyer',
        author_email= 'knny.myer@gmail.com',
        version     = version,
        packages = find_packages('src'),
        package_dir = {'': 'src'},
        url         = 'http://github.com/km0r3/django-flashcard',
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
        install_requires = [
            'setuptools',
            'zc.buildout',
            'zc.recipe.egg',
        ],
        entry_points = """
        # -*- Entry points: -*-
        [zc.buildout]
        default = djangorecipe.recipe:Recipe
        """,
    )
