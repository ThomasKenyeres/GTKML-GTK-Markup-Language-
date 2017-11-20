from gtkml.gtkml.static.names import LAYOUT_WIDGETS


def is_layout_widget(gtk_object):
    for gtk_type in LAYOUT_WIDGETS:
        print(gtk_type)
        if isinstance(gtk_object, LAYOUT_WIDGETS[gtk_type]):
            return True
    return False



if __name__ == '__main__':
    is_layout_widget(4)