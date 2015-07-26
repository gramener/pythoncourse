# Building command line apps

To build a command line application, you need to learn the following modules:

- `sys`
    - [Module of the week](http://pymotw.com/2/sys/) -- specifically the
      [Runtime environment](http://pymotw.com/2/sys/runtime.html)
- `argparse`
    - [Argparse tutorial](https://docs.python.org/2/howto/argparse.html)
    - [Module of the week](http://pymotw.com/2/argparse/)
- `fileinput`
    - [Module of the week](http://pymotw.com/2/fileinput/)

## Questions

- The program `alarm.py` pops up a user-specified message after 2 minutes. The
  message can be any piece of text, and is displayed calling the (ficticious)
  function `alert()`. When the user types
  `alarm.py Switch off your laptop`, write a program that calls
  `alert('Switch off your laptop', seconds=120)`.

- We want to allow the user to specify how many seconds later the alarm should
  be set. So, for example, if we type:

        alarm.py --seconds=30 Hello

  ... change the program to call `alert('Hello', seconds=30)`. If `--seconds` is
  not specified, it sets `--seconds` to 120 seconds.

- The user may want the alarm to be specified at multiple times. So, if we type:

        alarm.py --seconds=10 --seconds=20 Hello

  ... change the program to call `alert('Hello', seconds=10)` followed by
  `alert('Hello', seconds=20)`.

