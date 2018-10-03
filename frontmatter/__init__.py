import re
import yaml

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
    yaml_delim = "^(?:---|\+\+\+)(?:\s+)?\n" # +++ or --- to start/end YAML
    everything = "(.+)"
    yaml_pattern = (yaml_delim +
                    everything +  # YAML frontmatter
                    yaml_delim +
                    everything)   # Remaining content (e.g. markdown)
    result = re.search(yaml_pattern, yaml_content, re.S | re.M)
    if result:
        metadata = yaml.load(result.group(1))
        content = result.group(2)
        return (metadata, content)
    else:
        return (None, "")
