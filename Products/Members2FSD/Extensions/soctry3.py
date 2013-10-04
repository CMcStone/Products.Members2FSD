from zope.interface import implements

from Products.Members2FSD.interfaces import IMemberConverter

from Products.CMFCore.utils import getToolByName
from zope.app.component.hooks import getSite
import transaction


class memberConverter(object):
     implements(IMemberConverter)
     source_contenttype = "PersonFolder"
     target_contentype = "FSDPerson"
 
def getOldMemberProperties (self, items):
     items = {}
     site = getSite()
     items = site.people.listFolderContents(contentFilter={"portal_type" : "PersonFolder"}) 
     return items
          
def __call__(self, item):
         site = getSite()
         catalog = getToolByName(site, 'portal_catalog')
         fsd = site['directory'] # wow is this kludgy!
         memberprops = self.getOldMemberProperties(item)
         newprops = self.convertProps(item)
         newid = item.getId()
         portrait = item.getPortrait()
         fsd.invokeFactory(id=newid, type_name="FSDPerson", **newprops)
         if hasattr(fsd,newid):
             try:
                 fsd[newid].setImage(portrait)
             except:
                 print "image failed for %s" %newid
             return "success for %s" % newid 
         else:
             return "fail for %s" % newid
          
          
def convertProps (self, items):
     site = getSite()
     catalog = getToolByName(site, 'portal_catalog')
     newprops = {}
          
          
     fullname = item.Title()
     names = fullname.split(' ')
     if len(names) == 2:
          newprops['firstName'] = names[0]
          newprops['lastName'] = names[1]
                 
     elif len(names) == 3:
          newprops['firstName'] = names[0]
          newprops['middleName'] = names[1]
          newprops['lastName'] = names[2]
     else:
          raise ValueError, 'fullname could not be parsed: %2' % fullname
           
     newprops['classification'] = item.Description()
     newprops['education ']= item.almaMater
     newprops['hours'] = item.hours
     newprops ['phone'] = item.phone
     newprops['email'] = item.email
     newprops['officeAddress'] = item.office
     newprops['biography'] = item.biography + item.cv
     newprops['jobTitles'] = item.profession
             
           #classifications
     brains = catalog(porta_type='FSDClassification')
     classes = {}
     for brain in brains:
          classes[brain.Title] = brain.UID
     newprops['classification'] = item.Description()
            
     return newprops
                
def convert():
    site = getSite()
    items = site.people.listFolderContents(contentFilter={"portal_type" : "PersonFolder"})
    mt = getToolByName(site, 'portal_membership')
    con = memberConverter()
    for item in items:
        m = item.getId()
        site._p_jar.sync()
        con(m)
        transaction.commit()
        try:
            memcontent = site.people[item].objectIds()
            ref = site.people[item].manage_cutObjects(memcontent)
            site._p_jar.sync()
            site.directory[item].manage_pasteObjects(ref)
            transaction.commit()
        except:
            pass
            
def reset():
    site = getSite()
    dir = site['directory']
    persons = dir.objectIds('FSDPerson')
    dir.manage_delObjects(persons)
    transaction.commit()  
          
          
          
     
               
