from yafowil.base import (
    factory,
    fetch_value,
)
from yafowil.common import (
    generic_extractor,
    generic_required_extractor,
    textarea_renderer,
)


def alohaeditor_display_renderer(widget, data):
    value = fetch_value(widget, data)
    if not value:
        value = ''
    return data.tag('div', value, **{'class': 'display-alohaeditor'})


factory.register(
    'alohaeditor',
    extractors=[generic_extractor, generic_required_extractor],
    edit_renderers=[textarea_renderer],
    display_renderers=[alohaeditor_display_renderer])

factory.doc['blueprint']['alohaeditor'] = \
"""Add-on blueprint `yafowil.widget.alohaeditor
<http://github.com/bluedynamics/yafowil.widget.alohaeditor/>`_ .
"""

factory.defaults['alohaeditor.default'] = ''
factory.defaults['alohaeditor.wrap'] = None
factory.defaults['alohaeditor.cols'] = 80
factory.defaults['alohaeditor.rows'] = 10
factory.defaults['alohaeditor.readonly'] = None
factory.defaults['alohaeditor.class'] = 'alohaeditor'
