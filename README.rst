A simple and reusable flashcard application for the Django web framework
========================================================================

**This project is not being maintained nor is it in a working state. Please consider other projects as an alternative... I'm leaving this project up for educational purposes only**

What is the motivation behind the project?
------------------------------------------

To provide a tool to quickly review new/old vocabulary, definitions
and other stuff which can be resumed in under 200 words.


Installation
------------

Usually:

  $ python setup.py install

should do it. If you don't have root access, then issue the following
command:

  $ python setup.py install --user


Builing it out
--------------

This project is developed with the help of buildout [1], vim, and a lot
of love.

Generally, to replicate my working environment, issue the following commands:

  $ python bootstrap.py && ./bin/buildout

This may take some time, but believe me it's worth it. :-)

[1] http://www.buildout.org


Contribute
----------

You have a great idea, like to report/squash a bug, or write some code? Your my man.

Check out the GitHub project page: https://github.com/km0r3/django-flashcard


Coding guidelines
-----------------

Trying to follow PEP8, and the KISS and DRY principle.
