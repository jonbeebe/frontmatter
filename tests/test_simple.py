from frontmatter import Frontmatter

post = Frontmatter.read_file('./tests/testfile.md')

print("\n[attributes]")
print(post['attributes'])

print("\n[body]")
if post['body'] == "":
    print("ERROR: body not captured properly.")
    print("TEST FAILED.")
    exit(1)

print(post['body'])

print("\n[frontmatter]")
if post['frontmatter'] == "":
    print("ERROR: frontmatter not captured properly.")
    print("TEST FAILED.")
    exit(1)

print(post["frontmatter"])

print("TEST SUCCEEDED.")
exit(0)
