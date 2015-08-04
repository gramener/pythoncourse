# Working with Files and Folders

This section covers the following topics:

* Reading and writing files
* Listing and traversing files in a directory
* Matching files based on wildcards
* Working with temporary files

Suggested reading:

* [Working with Files section in Python Practice Book][1]
* [os module on Python-module-of-the-week][2]
* [os.path module on Python-module-of-the-week][3]
* [glob module on Python-module-of-the-week][4]
* [shutil module on Python-module-of-the-week][5]

[1]: http://anandology.com/python-practice-book/working-with-data.html#working-with-files
[2]: http://pymotw.com/2/os/index.html
[3]: http://pymotw.com/2/ospath/index.html
[4]: http://pymotw.com/2/glob/index.html
[5]: http://pymotw.com/2/shutil/index.html

## Questions

* Write a program `copyfile.py` to copy one file to another. It should accept 2 filenames as arguments and copies the first one into the second.

  $ python copyfile.py a.txt b.txt

* Write a program `head.py` that takes a filename as command-line argument and prints first 5 lines of it.

  $ python head.py one-to-ten.txt
  1
  2
  3
  4
  5

* Write a program `grep.py` that takes a pattern and a filename arguments and prints all the lines in the file that contain given pattern.

  $ python grep.py o numbers.txt
  1 one
  2 two
  4 four

* Write a program `wrap.py` that takes filename and width as command-line arguments and wraps the lines longer than given width.

  $ python wrap.py numbers.txt 5
  1 one
  2 two
  3 thr
  ee
  4 fou
  r
  5 fiv
  e

* Write a program `ls.py` that takes path to a directory as command-line argument and prints all the files in that directory. If no argument is specified, it should list the files in the current directory.

  $ python ls.py

* Write a program `mostrecent.py` to find the most recently modified file in the given directory. The program should accept the directory name as command-line argument and print path to the file (not just filename) that is most recently modified file.

  $ python mostrecent.py logs/
  logs/access.log

  $ python mostrecent.py /tmp
  /tmp/a.txt

* Write a program `find-matching-files.py` to find files recursively in a directory tree matching given wildcard pattern. The program should accept the directory and the pattern as command-line argument.

    $ python find-matching-files.py project '*.py'
    project/__init__.py
    project/a.py
    project/_util.py
    project/submodule/__init__.py
    project/submodule/b.py

    $ python find-matching-files.py project '?.py'
    project/a.py
    project/submodule/b.py

* Write a program `find-large-files.py` to find files recursively in a directory tree that are larger than given size. The program should accept the directory and the size as command-line argument. The size can be also be specified with `K`, `M` and `G` suffix for KB, MB and GB respectively.

    $ python find-large-files.py logs 100000
    logs/access.log
    logs/error.log

    $ python find-large-files.py logs 100K
    logs/access.log
    logs/error.log

    $ python find-large-files.py logs 2M
    logs/access.log

