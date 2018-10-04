frontmatter
============

A very simple Python package for parsing YAML Front Matter from a text file or string. Written for Python 3, but should also work Python 2.

Usage
------

```
from frontmatter import Frontmatter

# assuming 'testfile.md' exists
post = Frontmatter.read_file('testfile.md')

print(post['attributes'], "\n")  # Dictionary
print(post['body'], "\n")        # String
print(post['frontmatter'])       # String
```

The output would be:

```
{'foo': 'bar', 'num': 3, 'list': ['first', 'second', 'third']}

This is the actual post content
This is a second line

foo: bar
num: 3
list:
- first
- second
- third
```

In the above example, the contents of **testfile.md** is:

```
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
```

LICENSE
--------

[ISC License](https://en.wikipedia.org/wiki/ISC_license)
