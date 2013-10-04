## Script (Python) "getMemberById"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=member
##title=
##
return context.portal_membership.getMemberById(member)