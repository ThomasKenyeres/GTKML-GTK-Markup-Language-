class GtkmlException(Exception):
    pass

class GtkmlRuntimeError(GtkmlException):
    pass

class UnsetPropertyError(GtkmlRuntimeError):
    pass