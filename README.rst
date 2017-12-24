frontmatter
============

A very simple Python package for parsing YAML Front Matter from a text file. Written for Python 3, but works for 2.

Usage
------

.. code::

    import frontmatter

    # assuming 'testfile.md' exists
    post = frontmatter.parse('testfile.md')

    print(post['metadata']) # Dictionary
    print(post['content'])  # String

The output would be:

.. code::

    {'foo': 'bar', 'num': 3, 'list': ['first', 'second', 'third']}
    
    This is the actual post content
    This is a second line

In the above example, the contents of **testfile.md** is:

.. code::

    ---
    foo: bar
    num: 3
    list:
    - first
    - second
    - third
    ---
    
    This is the actual post content
    This is a second line

LICENSE
--------

This package is licensed under ISC.