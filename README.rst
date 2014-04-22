************************************************************
 Bug in Dexterity and RelationChoice fields in Plone 4.3.3?
************************************************************

I'm getting a stack trace when adding a Dexterity content type that contains a
RelationChoice/ObjPathSourceBinder field.  This small sample package
demonstrates the issue_.  (It works all right with Plone 4.3.2.)


To Reproduce
============

1.  python2.7 bootstrap.py
2.  bin/buildout
3.  bin/plone fg
4.  Visit http://localhost:8080/ and click "Create a new Plone site"
5.  Check box by "bug.relationfield" in the "Add-ons" box; click "Create Plone Site"
6.  From the "Add new" menu, click "Sample" 


Stacktrace
==========

It looks something like the following::

    2014-04-22 09:05:22 ERROR Zope.SiteErrorLog 1398175522.680.167608108016 http://localhost:8080/p2/++add++bug.relationchoice.sample
    Traceback (innermost last):
      Module ZPublisher.Publish, line 138, in publish
      Module ZPublisher.mapply, line 77, in mapply
      Module ZPublisher.Publish, line 48, in call_object
      Module plone.z3cform.layout, line 66, in __call__
      Module plone.z3cform.layout, line 60, in update
      Module z3c.form.form, line 263, in render
      Module z3c.form.form, line 158, in render
      Module zope.browserpage.viewpagetemplatefile, line 51, in __call__
      Module zope.pagetemplate.pagetemplate, line 132, in pt_render
      Module zope.pagetemplate.pagetemplate, line 240, in __call__
      Module zope.tal.talinterpreter, line 271, in __call__
      Module zope.tal.talinterpreter, line 343, in interpret
      Module zope.tal.talinterpreter, line 888, in do_useMacro
      Module zope.tal.talinterpreter, line 343, in interpret
      Module zope.tal.talinterpreter, line 533, in do_optTag_tal
      Module zope.tal.talinterpreter, line 518, in do_optTag
      Module zope.tal.talinterpreter, line 513, in no_tag
      Module zope.tal.talinterpreter, line 343, in interpret
      Module zope.tal.talinterpreter, line 954, in do_defineSlot
      Module zope.tal.talinterpreter, line 343, in interpret
      Module zope.tal.talinterpreter, line 533, in do_optTag_tal
      Module zope.tal.talinterpreter, line 518, in do_optTag
      Module zope.tal.talinterpreter, line 513, in no_tag
      Module zope.tal.talinterpreter, line 343, in interpret
      Module zope.tal.talinterpreter, line 858, in do_defineMacro
      Module zope.tal.talinterpreter, line 343, in interpret
      Module zope.tal.talinterpreter, line 533, in do_optTag_tal
      Module zope.tal.talinterpreter, line 518, in do_optTag
      Module zope.tal.talinterpreter, line 513, in no_tag
      Module zope.tal.talinterpreter, line 343, in interpret
      Module zope.tal.talinterpreter, line 531, in do_optTag_tal
      Module zope.tal.talinterpreter, line 513, in no_tag
      Module zope.tal.talinterpreter, line 343, in interpret
      Module zope.tal.talinterpreter, line 858, in do_defineMacro
      Module zope.tal.talinterpreter, line 343, in interpret
      Module zope.tal.talinterpreter, line 533, in do_optTag_tal
      Module zope.tal.talinterpreter, line 518, in do_optTag
      Module zope.tal.talinterpreter, line 513, in no_tag
      Module zope.tal.talinterpreter, line 343, in interpret
      Module zope.tal.talinterpreter, line 821, in do_loop_tal
      Module zope.tal.talinterpreter, line 343, in interpret
      Module zope.tal.talinterpreter, line 533, in do_optTag_tal
      Module zope.tal.talinterpreter, line 518, in do_optTag
      Module zope.tal.talinterpreter, line 513, in no_tag
      Module zope.tal.talinterpreter, line 343, in interpret
      Module zope.tal.talinterpreter, line 954, in do_defineSlot
      Module zope.tal.talinterpreter, line 343, in interpret
      Module zope.tal.talinterpreter, line 533, in do_optTag_tal
      Module zope.tal.talinterpreter, line 518, in do_optTag
      Module zope.tal.talinterpreter, line 513, in no_tag
      Module zope.tal.talinterpreter, line 343, in interpret
      Module zope.tal.talinterpreter, line 858, in do_defineMacro
      Module zope.tal.talinterpreter, line 343, in interpret
      Module zope.tal.talinterpreter, line 533, in do_optTag_tal
      Module zope.tal.talinterpreter, line 518, in do_optTag
      Module zope.tal.talinterpreter, line 513, in no_tag
      Module zope.tal.talinterpreter, line 343, in interpret
      Module zope.tal.talinterpreter, line 531, in do_optTag_tal
      Module zope.tal.talinterpreter, line 513, in no_tag
      Module zope.tal.talinterpreter, line 343, in interpret
      Module zope.tal.talinterpreter, line 742, in do_insertStructure_tal
      Module zope.tales.tales, line 696, in evaluate
       - URL: /Users/kelly/.buildout/eggs/plone.app.z3cform-0.7.6-py2.7.egg/plone/app/z3cform/templates/macros.pt
       - Line 97, Column 46
       - Expression: <PathExpr standard:u'widget/@@ploneform-render-widget'>
       - Names:
          {'args': (),
           'context': <PloneSite at /p2>,
           'default': <object object at 0x10ba95b70>,
           'loop': {},
           'nothing': None,
           'options': {},
           'repeat': {},
           'request': <HTTPRequest, URL=http://localhost:8080/p2/++add++bug.relationchoice.sample>,
           'template': <zope.browserpage.viewpagetemplatefile.ViewPageTemplateFile object at 0x10fa9a650>,
           'view': <plone.dexterity.browser.add.DefaultAddForm object at 0x111683410>,
           'views': <zope.browserpage.viewpagetemplatefile.ViewMapper object at 0x111729b90>}
      Module zope.tales.expressions, line 217, in __call__
      Module Products.PageTemplates.Expressions, line 155, in _eval
      Module Products.PageTemplates.Expressions, line 117, in render
      Module Products.Five.browser.metaconfigure, line 479, in __call__
      Module zope.browserpage.viewpagetemplatefile, line 83, in __call__
      Module zope.browserpage.viewpagetemplatefile, line 51, in __call__
      Module zope.pagetemplate.pagetemplate, line 132, in pt_render
      Module zope.pagetemplate.pagetemplate, line 240, in __call__
      Module zope.tal.talinterpreter, line 271, in __call__
      Module zope.tal.talinterpreter, line 343, in interpret
      Module zope.tal.talinterpreter, line 858, in do_defineMacro
      Module zope.tal.talinterpreter, line 343, in interpret
      Module zope.tal.talinterpreter, line 954, in do_defineSlot
      Module zope.tal.talinterpreter, line 343, in interpret
      Module zope.tal.talinterpreter, line 531, in do_optTag_tal
      Module zope.tal.talinterpreter, line 513, in no_tag
      Module zope.tal.talinterpreter, line 343, in interpret
      Module zope.tal.talinterpreter, line 742, in do_insertStructure_tal
      Module zope.tales.tales, line 696, in evaluate
       - URL: /Users/kelly/.buildout/eggs/plone.app.z3cform-0.7.6-py2.7.egg/plone/app/z3cform/templates/widget.pt
       - Line 37, Column 4
       - Expression: <PathExpr standard:u'widget/render'>
       - Names:
          {'args': (),
           'context': <ContentTreeWidget 'form.widgets.references'>,
           'default': <object object at 0x10ba95b70>,
           'loop': {},
           'nothing': None,
           'options': {},
           'repeat': {},
           'request': <HTTPRequest, URL=http://localhost:8080/p2/++add++bug.relationchoice.sample>,
           'template': <zope.browserpage.viewpagetemplatefile.ViewPageTemplateFile object at 0x10fb3c750>,
           'view': <Products.Five.metaclass.RenderWidget object at 0x111759e90>,
           'views': <zope.browserpage.viewpagetemplatefile.ViewMapper object at 0x111759f50>}
      Module zope.tales.expressions, line 217, in __call__
      Module zope.tales.expressions, line 211, in _eval
      Module plone.formwidget.contenttree.widget, line 168, in render
      Module zope.browserpage.viewpagetemplatefile, line 83, in __call__
      Module zope.browserpage.viewpagetemplatefile, line 51, in __call__
      Module zope.pagetemplate.pagetemplate, line 132, in pt_render
      Module zope.pagetemplate.pagetemplate, line 240, in __call__
      Module zope.tal.talinterpreter, line 271, in __call__
      Module zope.tal.talinterpreter, line 343, in interpret
      Module zope.tal.talinterpreter, line 533, in do_optTag_tal
      Module zope.tal.talinterpreter, line 518, in do_optTag
      Module zope.tal.talinterpreter, line 513, in no_tag
      Module zope.tal.talinterpreter, line 343, in interpret
      Module zope.tal.talinterpreter, line 742, in do_insertStructure_tal
      Module zope.tales.tales, line 696, in evaluate
       - URL: /Users/kelly/.buildout/eggs/plone.formwidget.contenttree-1.0.7-py2.7.egg/plone/formwidget/contenttree/input.pt
       - Line 3, Column 5
       - Expression: <PathExpr standard:u'view/renderQueryWidget'>
       - Names:
          {'args': (<ContentTreeWidget 'form.widgets.references'>,),
           'context': <PloneSite at /p2>,
           'default': <object object at 0x10ba95b70>,
           'loop': {},
           'nothing': None,
           'options': {},
           'repeat': {},
           'request': <HTTPRequest, URL=http://localhost:8080/p2/++add++bug.relationchoice.sample>,
           'template': <zope.browserpage.viewpagetemplatefile.ViewPageTemplateFile object at 0x10f5e6210>,
           'view': <ContentTreeWidget 'form.widgets.references'>,
           'views': <zope.browserpage.viewpagetemplatefile.ViewMapper object at 0x111760190>}
      Module zope.tales.expressions, line 217, in __call__
      Module zope.tales.expressions, line 211, in _eval
      Module z3c.formwidget.query.widget, line 212, in renderQueryWidget
      Module z3c.form.widget, line 153, in render
      Module zope.browserpage.viewpagetemplatefile, line 51, in __call__
      Module zope.pagetemplate.pagetemplate, line 132, in pt_render
      Module zope.pagetemplate.pagetemplate, line 240, in __call__
      Module zope.tal.talinterpreter, line 271, in __call__
      Module zope.tal.talinterpreter, line 343, in interpret
      Module zope.tal.talinterpreter, line 531, in do_optTag_tal
      Module zope.tal.talinterpreter, line 513, in no_tag
      Module zope.tal.talinterpreter, line 343, in interpret
      Module zope.tal.talinterpreter, line 821, in do_loop_tal
      Module zope.tal.talinterpreter, line 343, in interpret
      Module zope.tal.talinterpreter, line 531, in do_optTag_tal
      Module zope.tal.talinterpreter, line 513, in no_tag
      Module zope.tal.talinterpreter, line 343, in interpret
      Module zope.tal.talinterpreter, line 742, in do_insertStructure_tal
      Module zope.tales.tales, line 696, in evaluate
       - URL: /Users/kelly/.buildout/eggs/z3c.form-3.1.1-py2.7.egg/z3c/form/browser/radio_input.pt
       - Line 8, Column 4
       - Expression: <PythonExpr (view.renderForValue(item['value']))>
       - Names:
          {'args': (),
           'context': <PloneSite at /p2>,
           'default': <object object at 0x10ba95b70>,
           'loop': {},
           'nothing': None,
           'options': {},
           'repeat': {},
           'request': <HTTPRequest, URL=http://localhost:8080/p2/++add++bug.relationchoice.sample>,
           'template': <zope.browserpage.viewpagetemplatefile.ViewPageTemplateFile object at 0x10faf2950>,
           'view': <ContentTreeWidget 'form.widgets.references'>,
           'views': <zope.browserpage.viewpagetemplatefile.ViewMapper object at 0x10c04ef10>}
      Module zope.tales.pythonexpr, line 59, in __call__
       - __traceback_info__: (view.renderForValue(item['value']))
      Module <string>, line 1, in <module>
      Module z3c.form.browser.radio, line 44, in renderForValue
      Module z3c.form.term, line 38, in getTermByToken
      Module zope.schema.vocabulary, line 133, in getTermByToken
    LookupError: --NOVALUE--


.. References:
.. _issue: https://dev.plone.org/ticket/14027


