README for char_count
=====================

Small command line utility used to count the number of given characters on each line of input

Usage
-----

.. code-block:: bash

    usage: ch_count.py [-h] [-c CHAR]

    optional arguments:
      -h, --help            show this help message and exit
      -c CHAR, --char CHAR  The character that will be counted on each line of input

Example
-------

.. code-block:: bash

    $ echo testing | ch_count.py -c t
    2
    $ echo testing | ch_count.py -c g
    1

