from frontmatter import Frontmatter

post = Frontmatter.read_file('./tests/testfile.md')

print("\n[attributes]")
print(post['attributes'])

print("\n[body]")
print(post['body'])

print("\n[frontmatter]")
print(post["frontmatter"])

print("\nTEST SUCCEEDED.")
