frontmatter
===========

A very simple Python package for parsing YAML Front Matter from a text file. Supports both Python 2 and 3.

Usage:

    import frontmatter
    
    # assuming 'testfile.md' exists
    post = frontmatter.parse('testfile.md')
    
    print(post['metadata']) # Dictionary
    print(post['content'])  # String

The output would be:

    {'foo': 'bar', 'num': 3, 'list': ['first', 'second', 'third']}
    
    This is the actual post content
    This is a second line



In the above example, the contents of **testfile.md** is:

    ---
    foo: bar
    num: 3
    list:
    - first
    - second
    - third
    
    
    This is the actual post content
    This is a second line

