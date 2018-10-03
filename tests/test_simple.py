import frontmatter

post = frontmatter.parse('./tests/testfile.md')

print("frontmatter.tests.test_simple")

print("\n[metadata]")
print(post['metadata'])

print("\n[content]")
print(post['content'])

print("\nTEST SUCCEEDED.")
