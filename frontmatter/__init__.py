import re
import yaml

class Frontmatter:
    # class properties for internal use that do all the heavy lifting
    _yaml_delim = "^(?:---|\+\+\+)(?:\s+)?\n"
    _capture_all = "(.+)"
    _re_pattern = _yaml_delim + _capture_all + _yaml_delim + _capture_all
    _regex = re.compile(_re_pattern, re.S | re.M)

    @classmethod
    def read_file(cls, path):
        """Reads file at path and returns dict with separated frontmatter.

        Returned dict keys:
        attributes -- extracted YAML attributes in Dictionary form.
        body -- string contents below the YAML separators
        frontmatter -- string representation of YAML
        """
        with open(path, encoding="utf-8") as file:
            file_contents = file.read()
            return cls.read(file_contents)

    @classmethod
    def read(cls, string):
        """Reads string and returns dict with separated frontmatter.

        Returned dict keys:
        attributes: extracted YAML attributes in Dictionary form.
        body: str contents below the YAML separators
        frontmatter: str representation of YAML
        """
        parts = cls.__separate_yaml_content(string)
        fmatter = parts[0]
        body = parts[1]
        attributes = yaml.load(fmatter)
        return {
            "attributes": attributes,
            "body": body,
            "frontmatter": fmatter
        }

    @classmethod
    def __separate_yaml_content(cls, yaml_content=""):
        """Separates yaml lines from list of strings"""
        result = cls._regex.search(yaml_content)
        if result:
            fmatter = result.group(1)
            body = result.group(2)
            return (fmatter, body)
        return (None, "")
