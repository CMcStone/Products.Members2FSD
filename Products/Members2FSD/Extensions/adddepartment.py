from zope.app.component.hooks import getSite
import transaction
from Products.CMFCore.utils import getToolByName
from Products.Relations.processor import process


def AddDept():
     site = getSite()
     peeps = site['people']
     source_contenttype = 'PersonFolder'
     target_contenttype = 'FSDPerson'
     directory = 
     deptId = ""
     items = peeps.listFolderContents(
        contentFilter={"portal_type": target_contenttype})
        
     for item in items:
          id = item.getId()
          classifications = item.getClassifications()
               if classifications[0].title = 'Staff':
                  department = 'sociology-staff'
               elif 'faculty' in classifications[0].title:
                  department = 'sociology-faculty' 
               elif 'graduate' in classifications[0].title:
                  department = 'sociology-graduate-students'
               elif 'emeriti' in classifications[0].title:
                  department = 'sociology-faculty'
               else:
                    print "skipping department for" % id
          
          if specialtyId <> "":
            # get all the specialties assigned to this person
            specialtiesTuple = directory[id].getSpecialties()
            specialties = [eachSpecialtiesTuple[0].getObject().UID() for eachSpecialtiesTuple in specialtiesTuple]

            # see if the specialty we are assigning is already assigned
            if specialtyUID not in specialties:
              print "Specialty not assigned, assigning it"

              # You mustmustmust use the Relations API to add references, sayeth Relations/doc/Overview.txt.
              process(self, connect=((directory[id].UID(), specialtyUID, specialtyRulesetId),))
                    
          print "Looking up the department"
          departmentUID = self.portal_catalog(Title=department, portal_type="FSDDepartment")[0].UID
          
          
           
                   
          get sociology-faculty uid
          assign department to member as "Sociology Faculty"
          
          
          try:
            memcontent = site.people[id].objectIds()
            ref = site.people[id].manage_cutObjects(memcontent)
            site._p_jar.sync()
            site.Directory[id].manage_pasteObjects(ref)
            transaction.commit()
            print 'files copied'
          except:
            print 'no file copy'
     return "done"