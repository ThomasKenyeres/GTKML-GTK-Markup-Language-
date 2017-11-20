def get_attribute(tag, attr):
    if attr in tag.attributes:
        return tag.attributes[attr]
    else:
        return None

def get_bool_attribute(tag, attr):
    val = get_attribute(tag, attr)
    if val is True:
        return True
    return False

def get_str_bool_attribute(tag, attr):
    val = get_attribute(tag, attr)
    if val == "True":
        return True
    return False