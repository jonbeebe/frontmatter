from .. import parse

post = parse('./frontmatter/tests/testfile.md')

print("frontmatter.tests.test_simple")

print("\n[metadata]")
print(post['metadata'])

print("\n[content]")
print(post['content'])

print("\nTEST SUCCEEDED.")
