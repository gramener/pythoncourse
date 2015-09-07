Working with Files and Folders
==============================

Python provides a built-in function ``open`` to open a file, which returns a file object. ::

    f = open(filename, 'r') # open a file in read mode
    f = open(filename, 'w') # open a file in write mode
    f = open(filename, 'a') # open a file in append mode

The second argument to open is optional, which defaults to ``'r'`` when not specified.

Unix does not distinguish binary files from text files but Windows does. On Windows ``'rb'``, ``'wb'``, ``'ab'`` should be used to open a binary file in read, write and append mode respectively.

Reading Files
-------------

Easiest way to read contents of a file is by using the ``read`` method.

    >>> open('three.txt').read()
    'one\ntwo\nthree\n'

The ``readlines`` method returns all the lines of the file as a list.

    >>> open('three.txt').readlines()
    ['one\n', 'two\n', 'three\n']

Indivual lines of a file can be read using the ``readline`` method. It returns empty string when there is nothing more to read in a file.

    >>> f = open('three.txt')
    >>> f.readline()
    'one\n'
    >>> f.readline()
    'two\n'
    >>> f.readline()
    'three\n'
    >>> f.readline()
    ''

**Problem** Write a program ``cat.py`` that takes a filename as command-line argument and prints all the contents of that file. ::

    $ python cat.py three.txt
    one
    two
    three

Example: Word Count
^^^^^^^^^^^^^^^^^^^

Have you ever used the ``wc`` command, the unix program to compute number of lines, words and characters in a file? ::

    $ wc numbers.txt
    5      10      34 numbers.txt

Lets try to implment that using Python:

.. code-block:: python

    """wc.py - program to count number of lines, words and chars
    in a file.
    """
    import sys

    def linecount(f):
        """Returns number of lines a file.
        """
        # read lines and count them
        return len(open(f).readlines())

    def wordcount(f):
        """Returns the number of words in a file."""
        # Get the words by doing split() on the contents
        return len(open(f).read().split())

    def charcount(f):
        """Returns the number of charaters in a file.
        """
        # The number of characters in a file is same as the length
        # of its contents.
        return len(open(f).read())

    def main():
        f = sys.argv[1]
        print linecount(f), wordcount(f), charcount(f), f

    if __name__ == "__main__":
        main()

Lets try it on our sample file::

    $ python wc.py numbers.txt
    5 10 34 numbers.txt

**Problem:** Write a program ``head.py`` that takes a filename as command-line argument and prints the first 5 lines of it.

::

    $ python head.py one-to-ten.txt
    1
    2
    3
    4
    5

**Problem:** Write a program ``sumfile.py`` that takes a filename as argument and prints sum of all numbers in that file. It is assumed that the file will only have one number in every line.

::

    $ python sumfile.py one-to-ten.txt
    55

**Problem:** Write a program ``grep.py`` that takes a pattern and a filename as command-line argument and prints all the lines in the file that contain given pattern.

::

    $ python grep.py o numbers.txt
    1 one
    2 two
    4 four

**Problem** Write a program ``wrap.py`` that takes filename and width as command-line arguments and wraps the lines longer than given width.

::

    $ python wrap.py numbers.txt 5
    1 one
    2 two
    3 thr
    ee
    4 fou
    r
    5 fiv
    e

Writing to Files
----------------

To writing something to a file, we first open it in write mode, write something and finally close it.

.. code-block:: python

    f = open("a.txt", "w")
    f.write("one\n")
    f.write("two\n")
    f.close()

Everytime we open a file in write mode, the previous contents would be overwritten by the new contents.

.. code-block:: python

    >>> open("a.txt").read()
    'one\ntwo\n'

To add more contents to an existing file, the file must be opened in the append mode.

.. code-block:: python

    f = open("a.txt", "a")
    f.write("three\n")
    f.close()

Lets see what is there in the file now.

    >>> open("a.txt").read()
    'one\ntwo\nthree\n'

The ``with`` Statement
^^^^^^^^^^^^^^^^^^^^^^

Instead of explicitly closing the file after writing to it, we can also use a ``with`` statement. The ``with`` statement automatically closes a file object at the end, even if in presence of errors.

.. code-block:: python

    with open("b.txt", "w") as f:
        f.write("one\n")
        f.write("two\n")
    # f gets closed automatically

**Problem:** Write a program ``copyfile.py`` to copy one file to another. It should accept two filenames as command-line arguments and copies the first one into the second.::

    $ python copyfile.py a.txt b.txt

*WARNING: Don't call the file copy.py as that conflicts with a built-in module with the same name.*
