import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import frontmatter

post = frontmatter.parse('testfile.md')
print(post['metadata'])
print(post['content'])