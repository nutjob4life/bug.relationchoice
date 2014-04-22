# encoding: utf-8

from setuptools import setup, find_packages

setup(
    name='bug.relationchoice',
    description='Demonstrate bug in RelationChoice/ObjPathSourceBinder',
    entry_points={'z3c.autoinclude.plugin': ['target=plone']},
    extras_require={'test': ['plone.app.testing']},
    include_package_data=True,
    install_requires=[
        'setuptools',
        'Products.CMFPlone',
        'plone.app.dexterity[grok, relations]',
        'plone.app.relationfield',
    ],
    namespace_packages=['bug'],
    packages=find_packages('src', exclude=['bootstrap']),
    package_dir={'': 'src'},
    version='0.0.0',
    zip_safe=False,
)
