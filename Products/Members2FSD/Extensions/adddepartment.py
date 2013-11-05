from zope.app.component.hooks import getSite
import transaction
from Products.CMFCore.utils import getToolByName
from Products.Relations.processor import process


def AddDept():
     site = getSite()
     peeps = site['people']
     source_contenttype = 'FSDPerson'
     directory = site['people']
     deptId = ""
     items = director.listFolderContents(
        contentFilter={"portal_type": source_contenttype})
        
     for item in items:
          id = item.getId()
          if id <>"":
          classifications = item.getClassifications()
               if classifications[0].title = 'affiliated-faculty':
                  department = 'mindbrain-faculty'
               elif 'research-staff' in classifications[0].title:
                  department = 'researchers' 
               elif 'trainees' in classifications[0].title:
                  department = 'researchers'
               elif 'undergraduate-research-assistants' in classifications[0].title:
                  department = 'researchers'
               elif 'visiting-scholars' in classifications[0].title:
                    department = 'mindbrain-faculty'
               else:
                    print "skipping department for" % id
          
          
                    
         
                 departmentUID = site.portal_catalog(Title=department, portal_type="FSDDepartment")[0].UID
                 process(site, connect=((directory[id].UID(), departmentUID, departmentRulesetId),))
          
           
     return "done"