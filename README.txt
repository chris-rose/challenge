Challenge.py


Version
-------

Python 3.4


What is this?
-------------

challenge.py is intended to accept department related data of variable dimensions 
and return the allocation due such a department, given defined cost parameters.
Since a test input object has not been provided, it has been assumed that the 
department objects will follow a json like structure (please see the included unittest 
for several examples of department objects).

How do I use this?
------------------

challenge.py features a globally defined cost dictionary and 2 methods.  

The first method, getAllocation, accepts a department of the same form as our unit test
cases and returns the allocation that department should receive.

e.g.  

department

> {'Manager': 'A', 'Subordinates': [{'Manager': 'B', 'Subordinates': [{'QA Tester': 'C'}]}]}

getAllocation(department)

> 1100

The second method, sliceDepartment, accepts a department + manager name and returns a 
subset of the original department with the passed manager name now recognized as the
highest remaining authority. 

e.g.

sliceDepartment(department, 'B')

> {'Manager': 'B', 'Subordinates': [{'QA Tester': 'C'}]}

getAllocation and sliceDepartment can be nested to identify department allocation by managerial
level.

e.g.

getAllocation(sliceDepartment(department, 'B'))

> 800

License
-------

MIT

Developer Contact Information
-----------------------------

chris.ja.rose@gmail.com
Thank you for your time and I hope to hear from you soon.






