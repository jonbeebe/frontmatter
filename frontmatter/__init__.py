import re
import yaml

__yaml_delim = "^(?:---|\+\+\+)(?:\s+)?\n"
__capture_all = "(.+)"
__re_pattern = (__yaml_delim +
                __capture_all +  # YAML frontmatter
                __yaml_delim +
                __capture_all)   # Remaining content (e.g. markdown)
__regex = re.compile(__re_pattern, re.S | re.M)

def parse(filename):
    """Opens file and returns Dictionary with metadata and content"""
    file_contents = ""
    with open(filename, encoding="utf-8") as f:
        file_contents = f.read()
    
    separated = __separate_yaml_content(file_contents)
    meta = separated[0]
    content = separated[1]
    return { "metadata": meta, "content": content }

def __separate_yaml_content(yaml_content=""):
    """Separates yaml lines from list of strings"""
    result = __regex.search(yaml_content)
    if result:
        metadata = yaml.load(result.group(1))
        content = result.group(2)
        return (metadata, content)
    else:
        return (None, "")
