import os
from yafowil.base import factory


resourcedir = os.path.join(os.path.dirname(__file__), 'resources')

js = [{
    'resource': 'http://cdn.aloha-editor.org/current/lib/aloha.js',
    'thirdparty': False,
    'order': 20,
}, {
    'resource': 'widget.js',
    'thirdparty': False,
    'order': 21,
}]

css = [{
    'resource': 'http://cdn.aloha-editor.org/current/css/aloha.css',
    'thirdparty': False,
    'order': 20,
}, {
    'resource': 'widget.css',
    'thirdparty': False,
    'order': 21,
}]


def register():
    import widget
    factory.register_theme('default', 'yafowil.widget.alohaeditor',
                           resourcedir, js=js, css=css)


###############################################################################
# XXX: outdated below
###############################################################################

def get_resource_dir():
    return resourcedir


def get_js():
    return js


def get_css():
    return css
