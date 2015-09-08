Working with Files and Folders
==============================

Python provides a built-in function ``open`` to open a file, which returns a file object. ::

    f = open(filename, 'r') # open a file in read mode
    f = open(filename, 'w') # open a file in write mode
    f = open(filename, 'a') # open a file in append mode

The second argument to open is optional, which defaults to ``'r'`` when not specified.

Unix does not distinguish binary files from text files but Windows does. On Windows ``'rb'``, ``'wb'``, ``'ab'`` should be used to open a binary file in read, write and append modes respectively.

Reading Files
-------------

Easiest way to read contents of a file is by using the ``read`` method.

    >>> open('three.txt').read()
    'one\ntwo\nthree\n'

The ``readlines`` method returns all the lines of the file as a list.

    >>> open('three.txt').readlines()
    ['one\n', 'two\n', 'three\n']

Individual lines of a file can be read using the ``readline`` method. It returns empty string when there is nothing more to read in a file.

::

    >>> f = open('three.txt')
    >>> f.readline()
    'one\n'
    >>> f.readline()
    'two\n'
    >>> f.readline()
    'three\n'
    >>> f.readline()
    ''

**Problem:** Write a program ``cat.py`` that takes a filename as command-line argument and prints all the contents of that file.

::

    $ python cat.py three.txt
    one
    two
    three

Example: Word Count
^^^^^^^^^^^^^^^^^^^

Have you ever used the ``wc`` command, the Unix program to compute number of lines, words and characters in a file?

::

    $ wc numbers.txt
    5      10      34 numbers.txt

Lets try to implement that using Python:

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

Every time we open a file in write mode, the previous contents will be overwritten by the new contents.

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

Instead of explicitly closing the file after writing to it, we can also use a ``with`` statement. The ``with`` statement automatically closes a file object at the end, even in the case of errors.

.. code-block:: python

    with open("b.txt", "w") as f:
        f.write("one\n")
        f.write("two\n")
    # f gets closed automatically

**Problem:** Write a program ``copyfile.py`` to copy one file to another. It should accept two filenames as command-line arguments and copies the first one into the second.::

    $ python copyfile.py a.txt b.txt

*WARNING: Don't call the file copy.py as that conflicts with a built-in module with the same name.*

Working with Directories
------------------------

The ``os`` module provides several functions to work with directories.

For the sake of example, lets us assume that we have a directory tree with the following files.

::

    book/
    |-- chapter1.txt
    |-- chapter2.txt
    |-- chapter3.txt
    |-- chapter4.txt
    |-- notes.txt
    `-- images
        |-- 1.jpg
        |-- 2.jpg
        `-- 3.png

Lets start with listing files in a directory.

    >>> import os
    >>> os.listdir("book")
    ['chapter1.txt', 'chapter2.txt', 'chapter3.txt', 'chapter4.txt', 'notes.txt', 'images']

The ``os.path.join`` function is useful to join two or more path components.

    >>> os.path.join("book", "chapter1.txt")
    'book/chapter1.txt'
    >>> os.path.join("book", "images", "1.jpg")
    'book/images/1.jpg'

The ``os.path.join`` takes care of using the path separator of the underlying system (``/`` on Unix and ``\`` on Windows).

The ``isfile`` and ``isdir`` functions in ``os.path`` module can be used to check if a given path is a file or a directory.

    >>> os.path.isfile("book/chapter1.txt")
    True
    >>> os.path.isfile("book/images")
    False
    >>> os.path.isdir("book/images")
    True


**Problem:** Write a program ``ls.py`` that takes path to a directory as command-line argument and prints all the files in that directory. When no argument is specified, it should list the files in the current directory.

::

  $ python ls.py book
  chapter1.txt
  chapter2.txt
  chapter3.txt
  chapter4.txt
  notes.txt
  images

File Metadata
^^^^^^^^^^^^^

The ``os.stat`` functions provides information about a file.

::

    >>> info = os.stat("a.txt")
    >>> info
    posix.stat_result(st_mode=33188, st_ino=19206704, st_dev=16777217L, st_nlink=1, st_uid=501, st_gid=0, st_size=14, st_atime=1441694498, st_mtime=1441694498, st_ctime=1441694498)

It contains information about the file, including the size, creation time, modified time, access time, permissions, user and group info etc.

For example, here is the file size::

    >>> info.st_size
    14

And the modified time::

    >>> info.st_mtime
    1441694498.0

    >>> import time
    >>> time.ctime(info.st_mtime)
    'Tue Sep  8 12:11:38 2015'

**Problem** Write a program ``largest-file.py`` to find the the largest file in the given directory.The program should accept the directory name as command-line argument and print path to the file (not just filename) that is most recently modified file.

::

    $ python largest-file.py somedir/
    bigfile.txt

**Problem:** Write a program ``most-recent-file.py`` to find the most recently modified file in the given directory. The program should accept the directory name as command-line argument and print path to the file (not just filename) that is most recently modified file.

::

    $ python most-recent-file.py logs/
    logs/access.log

    $ python most-recent-file.py /tmp
    /tmp/a.txt

Matching wildcard patterns in filenames
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you ever need to find filenames matching some pattern, the built-in module ``glob`` makes the job very easy. It uses the Unix wildcard patterns for matching filenames. There are two  wildcard characters and character ranges:

* ``*`` - matches zero or more characters
* ``?`` - matches zero or one character
* ``[a-f]`` - matches all characters from ``a`` to ``f`` (for any two characters)

These look like regular expressions, but these different and quite simpler than regular expressions.

Let us try some examples::

    >>> import glob
    >>> glob.glob("book/*")
    ['book/chapter1.txt', 'book/chapter2.txt', 'book/chapter3.txt', 'book/chapter4.txt', 'book/images', 'book/notes.txt']
    >>> glob.glob("book/*.txt")
    ['book/chapter1.txt', 'book/chapter2.txt', 'book/chapter3.txt', 'book/chapter4.txt', 'book/notes.txt']
    >>> glob.glob("book/chapter?.txt")
    ['book/chapter1.txt', 'book/chapter2.txt', 'book/chapter3.txt', 'book/chapter4.txt']

If we want to find only files, but not sub directories in a directory::

    >>> [f for f in glob.glob("book/*") if os.path.isfile(f)]
    ['book/chapter1.txt', 'book/chapter2.txt', 'book/chapter3.txt', 'book/chapter4.txt', 'book/notes.txt']

And, if we only want the sub directories::

    >>> [f for f in glob.glob("book/*") if os.path.isdir(f)]
    ['book/images']

Internally, the ``glob`` module uses another built-in module ``fnmatch`` for matching the patterns, which can be used directly if we already have paths to be matched against.

    >>> import fnmatch
    >>> fnmatch.fnmatch("chapter1.txt", "chapter?.txt")
    True
    >>> fnmatch.fnmatch("notes.txt", "chapter?.txt")
    False

Traversing Directory Tree
-------------------------

The ``os.walk`` function traverses a directory recursively, and for each directory it generates a tuple containing directory path, names of all sub directories and names of all files in that directory.

::

    >>> for path, dirnames, filenames in os.walk("book/"):
    ...     print path
    ...     print dirnames
    ...     print filenames
    ...     print "---"
    ...
    book/
    ['images']
    ['chapter1.txt', 'chapter2.txt', 'chapter3.txt', 'chapter4.txt', 'notes.txt']
    ---
    book/images
    []
    ['1.jpg', '2.jpg', '3.png']
    ---

Suppose we want the total number of files in a directory tree.
::

    >>> sum([len(filenames) for path, dirnames, filenames in os.walk("book")])
    8


**Problem:** Write a program ``find-matching-files.py`` to find files recursively in a directory tree matching given wildcard pattern. The program should accept the directory and the pattern as command-line argument.

::

    $ python find-matching-files.py book '*.jpg'
    book/images/1.jpg
    book/images/2.jpg

    $ python find-matching-files.py book 'chap*.txt'
    book/chapter1.txt
    book/chapter2.txt
    book/chapter3.txt
    book/chapter4.txt

**Problem** Write a program `find-large-files.py` to find files recursively in a directory tree that are larger than given size. The program should accept the directory and the size as command-line argument. The size can be also be specified with `K`, `M` and `G` suffix for KB, MB and GB respectively.

::

    $ python find-large-files.py logs 100000
    logs/access.log
    logs/error.log

    $ python find-large-files.py logs 100K
    logs/access.log
    logs/error.log

    $ python find-large-files.py logs 2M
    logs/access.log
