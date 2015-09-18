Getting Started
===============

First Steps
-----------

Running Python Interpreter
^^^^^^^^^^^^^^^^^^^^^^^^^^

Python comes with an interactive interpreter. When you type ``python`` in your
shell or command prompt, the python interpreter becomes active with a ``>>>``
prompt and waits for your commands.

.. code-block:: python

    $ python
    Python 2.7.8 (default, Aug 24 2014, 21:26:19)
    [GCC 4.2.1 Compatible Apple LLVM 5.1 (clang-503.0.40)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Now you can type any valid python expression at the prompt. python reads the
typed expression, evaluates it and prints the result.

.. code-block:: python

    >>> 42
    42
    >>> 4 + 2
    6

**Problem** Open a new Python interpreter and use it to find the value of ``2 + 3``.

We can also print something explicitly using the `print` statement.

::

    >>> print "hello world"
    hello world

Running Python Scripts
^^^^^^^^^^^^^^^^^^^^^^

Open your text editor, type the following text and save it as ``hello.py``.

.. code-block:: python

    print "hello, world!"

And run this program by calling ``python hello.py``. Make sure you change to
the directory where you saved the file before doing it.

.. code-block:: python

    $ python hello.py
    hello, world!

**Problem**: Create a python script to print  ``hello, world!`` four times.

Code
----

Comments
^^^^^^^^

Text after ``#`` character in any line is considered as comment.

.. code-block:: python

    # This is helloworld program
    # run this as:
    #    python hello.py
    print "hello, world!"

Variables
^^^^^^^^^

One of the building blocks of programming is associating a name to a value.
This is called assignment. The associated name is usually called a *variable*.

.. code-block:: python

    >>> x = 4
    >>> x * x
    16

In this example ``x`` is a variable and it's value is ``4``.

If you try to use a name that is not associated with any value, python gives an error message.

.. code-block:: python

    >>> foo
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    NameError: name 'foo' is not defined
    >>> foo = 4
    >>> foo
    4

If you re-assign a different value to an existing variable, the new value
overwrites the old value.

.. code-block:: python

    >>> x = 4
    >>> x
    4
    >>> x = 'hello'
    >>> x
    'hello'

It is possible to do multiple assignments at once.

.. code-block:: python

    >>> a, b = 1, 2
    >>> a
    1
    >>> b
    2
    >>> a + b
    3

Swapping values of 2 variables in python is very simple.

.. code-block:: python

    >>> a, b = 1, 2
    >>> a, b = b, a
    >>> a
    2
    >>> b
    1

Datatypes
^^^^^^^^^

Python has numbers.

    >>> 1 + 2
    3

Python has floating point numbers to represent decimal numbers.

    >>>  2.5 * 1.1
    2.75

Python has strings to represent text.

    >>> print "hello"
    hello

String can be enclosed either in double quotes or single quotes.

    >>> "hello" + 'world'
    'helloworld'

Python has lists.

    >>> x = ['a', 'b', 'c']
    >>> x
    ['a', 'b', 'c']

The individual elements of the list can be accessed using the `[]` operator.

    >>> x[0]
    'a'
    >>> x[1]
    'b'
    >>> x[2]
    'c'

Elements of a list can be of different type.

    >>> [1, 'a', 3.14]
    [1, 'a', 3.14]

In Python, the variable do not have any type.

    >>> x = 1
    >>> x = "hello"

Python has boolean type too. The built-in values ``True`` and ``False`` represent boolean true and false.

    >>> True
    True
    >>> False
    False

There are more datatypes like tuple, set and dictionary, but we'll look at them later.

Functions
---------

Python has many built-in functions. Lets see some of them.

The built-in function ``len`` provides length of a string or a list.

    >>> len("hello")
    5
    >>> len([1, 2, 3])
    3

The ``min`` and ``max`` functions compute minimim and maximum of given 2 values.

    >>> min(2, 3)
    2
    >>> max(2, 3)
    3
    >>> max(12, 3)
    12

The ``int`` function coverts a string to an integer.

    >>> int('2')
    2
    >>> 1 + int('2')
    3

The ``str`` function takes any value and converts it into a string.

    >>> str(4)
    '4'

Function calls can be nested or used in any other expressions.

    >>> len("hello") + 1
    6
    >>> min(3, len("hello"))
    3

Now lets see how to write our own functions.

.. code-block:: python

    >>> def square(x):
    ...    return x * x
    ...
    >>> square(5)
    25

The ``...`` is the secondary prompt, which the Python interpreter uses to
denote that it is expecting some more input.

It is important to notice that the body of the function is indented. Indentation is the Python's way of grouping statements.

We can also write this in a new file. Lets create a file ``square.py`` with the following code:

.. code-block:: python

    def square(x):
        return x * x

    print square(5)

and try running it::

    $ python square.py
    25

Existing functions can be used in creating new functions.

.. code-block:: python

    >>> def sum_of_squares(x, y):
    ...    return square(x) + square(y)
    ...
    >>> sum_of_squares(2, 3)
    13

**Problem** Write a function ``cube`` to compute cube of a number.

    >>> cube(2)
    8
    >>> cube(3)
    27

**Problem** Write a function ``count_digits`` that takes a number as argument and returns the number of digits it has.

    >>> count_digits(1234)
    4
    >>> count_digits(789)
    3

``print`` vs. ``return``
^^^^^^^^^^^^^^^^^^^^^^^^

Consider the following two functions.

.. code-block:: python

    def square1(x):
        y = x*x
        return y

    def square2(x):
        y = x*x
        print y

    print square1(4)
    square2(4)

output::

    16
    16

Both of these seems to be doing the same thing. The ``square1`` function is returning the result and the ``square2`` function is printing it. While the output in both these cases look exactly the same, their abilities differ quite a lot.

::

    >>> square1(4) + 1
    17
    >>> square1(square1(4))
    256

The result of calling the ``square1`` function can be used in other expressions, but the ``square2`` function can't be used that way because it is not returning anything back.

Functions are values too
^^^^^^^^^^^^^^^^^^^^^^^^

Functions are just like other values, they can assigned, passed as arguments to
other functions etc.

.. code-block:: python

    >>> f = square
    >>> f(4)
    16

Lets try an example.

.. code-block:: python

    def sum_of_squares(x, y):
        return square(x) + square(y)

    print sum_of_squares(3, 4) # prints 25

The ``sum_of_squares`` function is taking two numbers as arguments and computing sum of their squares.
Now lets try to implement similar function to compute sum of cubes of 2 numbers.

.. code-block:: python

    def cube(x):
        return x*x*x

    def sum_of_cubes(x, y):
        return cube(x) + cube(y)

    print sum_of_cubes(3, 4) # prints 91

If you see the ``sum_of_squares`` and ``sum_of_cubes`` functions, there are almost the same except the function they are calling on each number. It would be nice if we can generalize this idea and write a generic function that can compute sum of square, cube or any other function applied on two numbers. We can acheive that by passing the function as argument.

.. code-block:: python

    def sum_of(f, x, y):
        return f(x) + f(y)

    # assuming square and cube are already defined
    print sum_of(square, 3, 4)
    print sum_of(cube, 3, 4)

    # we can also use sum_of on functions as well
    print sum_of(len, "hello", "python")

Outut::

    25
    91
    11

Passing functions as arguments is so useful operation that there are some built-in functions that accept functions as arguments.

    >>> max(['one', 'two', 'three', 'four', 'five'])
    'two'
    >>> max(['one', 'two', 'three', 'four', 'five'], key=len)
    'three'

The first one finds the last word when compared using alphabetical order. The last one tries find the longest word instead as we've asked the ``max`` function to compare the words on their ``len``.



Methods
^^^^^^^

Methods are special kind of functions that work on an object.

For example, ``upper`` is a method available on string objects.

.. code-block:: python

    >>> x = "Hello"
    >>> print x.upper()
    HELLO
    >>> print x.lower()
    hello

The string objects have many more useful methods.

    >>> "mathematics".count("mat")
    2

**Problem**: Write a function ``icount`` to count the number of occurances of a substring in a string ignoring the case.

    >>> icount("mathematics", "mat")
    2
    >>> icount("Mathematics", "mat")
    2
    >>> icount("Mathematics", "MAT")
    2

A string can be split into multiple parts using the ``split`` method.

::

    >>> sentence = "good morning everyone"
    >>> sentence.split()
    ['good', 'morning', 'everyone']
    >>> sentence.split("o")
    ['g', '', 'd m', 'rning every', 'ne']

When no arguments are provided, the ``split`` method split the string at every white space. If a delimiter is passed as argument, the string is split whereever that delimiter is present.

**Problem:** Write a function ``count_words`` to count the number of words in sentence.

    >>> count_words("good morning everyone")
    3
    >>> count_words("one two three four five six")
    6

**Problem:** Write a function ``longest_word`` that takes a sentence as argument and returns the longest word in it.

    >>> longest_word('one two three four five')
    'three'

Modules
-------

TODO

Conditional Expressions
-----------------------

Python provides various operators for comparing values. The result of a comparison is a boolean value, either ``True`` or ``False``.

.. code-block:: python

    >>> 2 < 3
    False
    >>> 2 > 3
    True

Here is the list of available conditional operators.

* ``==`` equal to
* ``!=`` not equal to
* ``<`` less than
* ``>`` greater than
* ``<=`` less than or equal to
* ``>=`` greater than or equal to

It is even possible to combine these operators.

.. code-block:: python

    >>> x = 5
    >>> 2 < x < 10
    True
    >>> 2 < 3 < 4 < 5 < 6
    True

The conditional operators work even on strings - the ordering being the lexical order.

.. code-block:: python

    >>> "python" > "perl"
    True
    >>> "python" > "java"
    True

There are few logical operators to combine boolean values.

* ``a and b`` is ``True`` only if both ``a`` and ``b`` are True.
* ``a or b`` is True if either ``a`` or ``b`` is True.
* ``not a`` is True only if ``a`` is False.

.. code-block:: python

    >>> True and True
    True
    >>> True and False
    False
    >>> 2 < 3 and 5 < 4
    False
    >>> 2 < 3 or 5 < 4
    True

**Problem**: What will be output of the following program?

.. code-block:: python

    print 2 < 3 and 3 > 1
    print 2 < 3 or 3 > 1
    print 2 < 3 or not 3 > 1
    print 2 < 3 and not 3 > 1

**Problem**: What will be output of the following program?

.. code-block:: python

    x = 4
    y = 5
    p = x < y or x < z
    print p

**Problem**: What will be output of the following program?

.. code-block:: python

    True, False = False, True
    print True, False
    print 2 < 3

The if statement
^^^^^^^^^^^^^^^^

The ``if`` statement is used to execute a piece of code only when a boolean expression is true.

.. code-block:: python

    >>> x = 42
    >>> if x % 2 == 0: print 'even'
    even
    >>>

In this example, ``print 'even'`` is executed only when ``x % 2 == 0`` is ``True``.

The code associated with ``if`` can be written as a separate indented block of code, which is often the case when there is more than one statement to be executed.

.. code-block:: python

    >>> if x % 2 == 0:
    ...     print 'even'
    ...
    even
    >>>


The ``if`` statement can have optional ``else`` clause, which is executed when the boolean expression is ``False``.

.. code-block:: python

    >>> x = 3
    >>> if x % 2 == 0:
    ...     print 'even'
    ... else:
    ...     print 'odd'
    ...
    odd
    >>>

The ``if`` statement can have optional ``elif`` clauses when there are more
conditions to be checked. The ``elif`` keyword is short for ``else if``, and is
useful to avoid excessive indentation.

.. code-block:: python

    >>> x = 42
    >>> if x < 10:
    ...        print 'one digit number'
    ... elif x < 100:
    ...     print 'two digit number'
    ... else:
    ...     print 'big number'
    ...
    two digit number
    >>>

**Problem**: What happens when the following code is executed? Will it give any
   error? Explain the reasons.

.. code-block:: python

    x = 2
    if x == 2:
        print x
    else:
        print y

**Problem**: What happens the following code is executed? Will it give any error? Explain the reasons.

.. code-block:: python

    x = 2
    if x == 2:
        print x
    else:
        x +

Lists
-----

Lists are one of the great datastructures in Python. We are going to learn a
little bit about lists now. Basic knowledge of lists is requrired to be able to
solve some problems that we want to solve in this chapter.

Here is a list of numbers.

.. code-block:: python

    >>> x = [1, 2, 3]

And here is a list of strings.

.. code-block:: python

    >>> x = ["hello", "world"]

List can be heterogeneous. Here is a list containings integers, strings and another list.

.. code-block:: python

    >>> x = [1, 2, "hello", "world", ["another", "list"]]

The built-in function ``len`` works for lists as well.

.. code-block:: python

    >>> x = [1, 2, 3]
    >>> len(x)
    3

The ``[]`` operator is used to access individual elements of a list.

.. code-block:: python

    >>> x = [1, 2, 3]
    >>> x[1]
    2
    >>> x[1] = 4
    >>> x[1]
    4

The first element is indexed with ``0``, second with ``1`` and so on.

We'll learn more about lists in the next chapter.

Modules
-------

Modules are libraries in Python. Python ships with many standard library modules.

A module can be imported using the ``import`` statement.

Lets look at ``time`` module for example:

.. code-block:: python

    >>> import time
    >>> time.asctime()
    'Tue Sep 11 21:42:06 2012'

The ``asctime`` function from the ``time`` module returns the current time of
the system as a string.

The ``sys`` module provides access to the list of arguments passed to the
program, among the other things.

The ``sys.argv`` variable contains the list of arguments passed to the program.
As a convention, the first element of that list is the name of the program.

Lets look at the following program ``echo.py`` that prints the first argument
passed to it.

.. code-block:: python

    import sys
    print sys.argv[1]

Lets try running it.

.. code-block:: python

    $ python echo.py hello
    hello
    $ python echo.py hello world
    hello

There are many more interesting modules in the standard library. We'll learn
more about them in the coming chapters.

**Problem**: Write a program ``add.py`` that takes 2 numbers as command line
   arguments and prints its sum.

.. code-block:: python

    $ python add.py 3 5
    8
    $ python add.py 2 9
    11
