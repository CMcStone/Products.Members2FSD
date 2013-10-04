from Extensions import plone_to_facstaffdir
from Products.CMFCore.DirectoryView import registerDirectory
from zope.i18nmessageid import MessageFactory
Members2FSDMessageFactory = MessageFactory('Products.Members2FSD')


GLOBALS = globals()
registerDirectory('skins', GLOBALS)

def initialize(context):
    """Initializer called when used as a Zope 2 product."""

