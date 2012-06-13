alohaeditor widget
================

Features
--------

    - renders textarea with alohaeditor css class and provides a alohaeditor
      resources.

Load requirements::

    >>> import yafowil.loader
    >>> import yafowil.widget.alohaeditor

Test widget::

    >>> from yafowil.base import factory

Render widget::

    >>> widget = factory('alohaeditor', 'rt', props={'required': True})
    >>> widget()
    u'<textarea class="alohaeditor" cols="80" id="input-rt" name="rt" required="required" rows="10"></textarea>'

Widget extraction::

    >>> request = {'rt': ''}
    >>> data = widget.extract(request)

No input was given::

    >>> data.errors
    [ExtractionError('Mandatory field was empty',)]

Empty string in extracted::

    >>> data.extracted
    ''

Widget extraction. Returns markup from tinymce::

    >>> request = {'rt': '<p>1</p>'}
    >>> data = widget.extract(request)
    >>> data.errors
    []

    >>> data.extracted
    '<p>1</p>'

    >>> widget(data)
    u'<textarea class="alohaeditor" cols="80" id="input-rt" name="rt" required="required" rows="10"><p>1</p></textarea>'

Display renderer::

    >>> widget = factory('alohaeditor', 'rt', value='<p>foo</p>', mode='display')
    >>> widget()
    u'<div class="display-alohaeditor"><p>foo</p></div>'

    >>> widget = factory('alohaeditor', 'rt', mode='display')
    >>> widget()
    u'<div class="display-alohaeditor"></div>'
