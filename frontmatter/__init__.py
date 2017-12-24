import yaml

def parse(filename):
    """Opens file and returns Dictionary with metadata and content"""
    lines = []
    with open(filename) as f:
        lines = [line for line in f]

    separated = __separate_yaml_content(lines)
    meta = separated.get('yaml', {})
    contentlines = separated.get('nextlines', [])
    content = ''.join(x for x in contentlines)

    return { 'metadata': meta, 'content': content }

def __separate_yaml_content(lines=[]):
    """Separates yaml lines from list of strings"""
    yaml_content = ''
    marker_reached = False
    linenum = 0

    for line in lines:
        if marker_reached:
            if line.startswith('---') or line.startswith('+++'):
                break;
            yaml_content += line
        elif line.startswith('---') or line.startswith('+++'):
            marker_reached = True
        linenum += 1

    parsedyaml = yaml.load(yaml_content)
    nextline = linenum + 1;

    return { 'yaml': parsedyaml, 'nextlines': lines[nextline:] }