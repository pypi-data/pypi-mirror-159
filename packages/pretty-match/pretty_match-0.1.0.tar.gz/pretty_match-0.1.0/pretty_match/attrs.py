class AttrIsNone:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"<AttrIsNone: {self.name}>"

    def __repr__(self):
        return f"<AttrIsNone: {self.name}>"

    def __eq__(self, other):
        return other.name == self.name


def FirstNoneAttr(*attr_names, instance):
    for attr_name in attr_names:
        if getattr(instance, attr_name) is None:
            return AttrIsNone(attr_name)
