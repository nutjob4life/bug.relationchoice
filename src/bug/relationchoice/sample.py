# encoding: utf-8

'''Sample content'''

from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.supermodel import model
from z3c.relationfield.schema import RelationChoice
from zope import schema

class ISample(model.Schema):
    '''A sample content type'''
    title = schema.TextLine(
        title=u'Title',
        required=True,
    )
    description = schema.Text(
        title=u'Description',
        required=False,
    )
    references = RelationChoice(
        title=u'References',
        source=ObjPathSourceBinder(portal_type='Document'),
        required=False,
    )
