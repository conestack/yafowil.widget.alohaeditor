import os
from yafowil.base import factory


resourcedir = os.path.join(os.path.dirname(__file__), 'resources')
js = [{
    'group': 'alohaeditor',
    'resource': 'http://cdn.aloha-editor.org/current/lib/aloha.js',
    'order': 20,
}, {
    'group': 'yafowil.widget.alohaeditor',
    'resource': 'widget.js',
    'order': 21,
}]
css = [{
    'group': 'alohaeditor',
    'resource': 'http://cdn.aloha-editor.org/current/css/aloha.css',
    'order': 20,
}, {
    'group': 'yafowil.widget.alohaeditor',
    'resource': 'widget.css',
    'order': 21,
}]


def register():
    import widget
    factory.register_theme('default', 'yafowil.widget.alohaeditor',
                           resourcedir, js=js, css=css)