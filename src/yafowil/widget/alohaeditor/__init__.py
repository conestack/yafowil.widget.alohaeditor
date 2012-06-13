import os


def register():
    import widget


def get_resource_dir():
    return os.path.join(os.path.dirname(__file__), 'resources')


def get_js():
    return [
        {'resource': 'http://cdn.aloha-editor.org/current/lib/aloha.js',
         'thirdparty': False,
         'order': 20,},
        {'resource': 'widget.js',
         'thirdparty': False,
         'order': 21,}
    ]


def get_css():
    return [
        {'resource': 'http://cdn.aloha-editor.org/current/css/aloha.css',
         'thirdparty': False,
         'order': 20,},
    ]
