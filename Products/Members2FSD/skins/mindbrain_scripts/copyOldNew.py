## Script (Python) "copyOldNew"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
from Products.CMFCore.utils import getToolByName
portal_url = getToolByName(context, "portal_url")
portal = portal_url.getPortalObject()
mt = getToolByName(context, "portal_membership")

o = portal['people-old']
n = portal.directory

for memberid in mt.listMemberIds():


    try:
        ref = o[memberid].manage_copyObjects(o[memberid].objectIds())
        n[memberid].manage_pasteObjects(ref)
    except:
        print 'Failed for %s' % memberid
    print 'Succededfor %s' % memberid

return printed
