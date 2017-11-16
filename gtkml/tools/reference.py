def REF(struct, key):
    return struct[key]

def OBJ_REF(obj, prop):
    return REF(obj.__dict__, "_" + str(obj.__class__.__name__) + prop)