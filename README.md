# count_symaccess_inits

This script produces a simple report showing initiator login information from a
VMAX storage array, including unique, total, and logged in initiators. This can
be useful during a tech refresh project for ensuring that replacement solutions
can support the necessary initiator counts for an existing environment.

The script expects the text of the 'symaccess list logins' command as input. To
process a single array, simply save the 'symaccess list logins' command as a
file, and provide that file to the script with the '-f' flag. To process multiple
arrays simultaneously (e.g. for a consolidation project), concatenate multiple
symaccess outputs into a single file, and provide that file to the script.

# Usage

~~~
usage: count_symaccess_inits.py [-h] -f FILE

Count initiators in "symaccess list login" output.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Filename containing symaccess list login output.
~~~


# Example Output

```
$ python ~/Projects/scripts/Python/count_symaccess_inits/count_symaccess_inits.py -f combined_40k.txt


                           Total login table entries: 21120
        Unique WWNs within total login table entries: 2850


                     'Logged in' login table entries: 10039
  Unique WWNs within 'Logged in' login table entries: 1713

```
