Building command line applications
==================================

To build a command line application, you need to learn the following modules:

* ``sys`` - `module of the week <http://pymotw.com/2/sys/>`_, specifically the `Runtime environment <http://pymotw.com/2/sys/runtime.html>`_ section.

* ``argparse``
    * `argparse tutorial <https://docs.python.org/2/howto/argparse.html>`_
    * `argparse - module of the week <http://pymotw.com/2/argparse/>`_
* ``fileinput``- `module of the week <http://pymotw.com/2/fileinput/>`_

Problems
--------

**Problem** Write a program ``echo.py`` that takes one or more words as command line arguments and prints them back. If an optional flag ``-r`` or ``--repeats`` is specified followed by number of repeats, the message should be repeated so many times.

::

    $ python echo.py Hello World
    Hello World

    $ python echo.py -r 2 Hello World
    Hello World
    Hello World

    $ python echo.py --repeats 2 Hello World
    Hello World
    Hello World

**Problem** Extend the above ``echo.py`` program by adding additional flag ``-u`` or ``--upper-case``, which converts the message to upper case before printing.

::

    $ python echo.py Hello World
    Hello World

    $ python echo.py -u Hello World
    HELLO WORLD

    $ python echo.py -u -r 2 Hello World
    HELLO WORLD
    HELLO WORLD
