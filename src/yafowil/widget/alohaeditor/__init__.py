import os


def register():
    import widget


def get_resource_dir():
    return os.path.join(os.path.dirname(__file__), 'resources')


def get_js():
    return [
        {'resource': 'Aloha-Editor/src/lib/aloha.js',
         'thirdparty': False,
         'order': 20,},
        {'resource': 'widget.js',
         'thirdparty': False,
         'order': 21,}
    ]


def get_css():
    return [
        {'resource': 'Aloha-Editor/src/css/aloha.css',
         'thirdparty': False,
         'order': 20,},
    ]
