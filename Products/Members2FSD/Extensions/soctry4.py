"""
from the News Item type, the new items will be content copies
of their corresponding Pages (Documents)"""
from zope.app.component.hooks import getSite
from Products.CMFCore.utils import getToolByName

def convert():

     source_contenttype = 'PersonFolder'
     target_contenttype = 'FSDPerson'
     site = getSite()
     peeps = site['people']
     
     

     items = peeps.listFolderContents(
        contentFilter={"portal_type": source_contenttype})
     fsd = site['Directory']

     for item in items:
          middleName, firstName, lastName, classifications, jobTitles, education, department, bibliography, portrait, officePhone, email, OfficeCity, OfficePhone, OfficeState, OfficePostalCode, biography, userpref_ext_editor, officeRoom, officeHours, fullname, names, memcontent = ('',)*22
          id = item.getId()
          jobTitles = item.Description()
          if 'Staff' in item.Subject():
               classifications = 'staff'
               department = 'sociology-staff'
          elif 'Graduate Students' in item.Subject():
               classifications = 'graduate-students'
               department = 'sociology-graduate-students'
          elif 'Affiliated Faculty' in item.Subject():
               classifications = 'affiliated-faculty'
               department = 'sociology-faculty'
          elif 'Emeriti' in item.Subject():
               classifications = 'emeriti' 
               department = 'sociology-faculty'
          elif 'Faculty' in item.Subject():
               classifications = 'faculty'
               deparment = 'sociology-faculty'
          elif 'Graduate Employees' in item.Subject():
               classifications = "graduate-employees"
               department = 'sociology-graduate-students'
          elif 'Lecturers' in item.Subject():
               classifications = "lecturers" 
               department = 'sociology-faculty'
          elif 'Postdoctorates' in item.Subject():
               classifications = 'postdoctorates'
          elif 'Research Professors' in item.Subject():
               classifications = 'research-professors'
               department = 'sociology-faculty'
          else:
               classifications = ""
                             
          education = item.almaMater
          portrait = item.getPortrait()
          officePhone = item.getPhone()
          email = item.getEmail()
          biography = item.biography
          userpref_ext_editor = False
          officeRoom = item.office
          officeHours = item.hours
          fullname = item.Title()
          names = fullname.split(' ')
          if len(names) == 2:
                firstName = names[0]
                lastName = names[1]
          elif len(names) >= 3:
                firstName = names[0]
                middleName = names[1]
                lastName = names[2]
          else:
                raise ValueError, "fullname could not be parsed:" .format(fullname)
           
          if officeHours <> 'N/A':
                quarter = 'Fall 2013'
          else:
                quarter = ''
                
          if not id in fsd.objectIds():
          
               if classifications <> "":
               
                    classificationUID = site.portal_catalog(Title=classifications,portal_type="FSDClassification")[0].UID
                    departmentUID = site.portal_catalog(Title=department, portal_type="FSDDepartment")[0].UID
                    fsd.invokeFactory(
                         type_name='FSDPerson',
                         id=id,
                         firstName=firstName,
                         middleName=middleName,
                         lastName=lastName,
                         classifications=[classificationUID],
                         department=[departmentUID],
                         email=email.strip(),
                         education=education,
                         OfficePhone=OfficePhone,
                         officeRoom=officeRoom,
                         officeHours=officeHours,
                         bibliograph=bibliography,
                         OfficeCity='Davis',
                         OfficeState='CA',
                         OfficePostalCode='95616',
                         userpref_ext_editor=False )
                    
                    fsd[id].at_post_create_script()
                    print "made a person for" + fullname
                    
                     
                  
               else:
                    print "creating fsd person object"
                    fsd.invokeFactory(
                         type_name='FSDPerson', 
                         id=id, 
                         firstName=firstName, 
                         middleName=middleName, 
                         lastName=lastName, 
                         email=email.strip(),
                         portrait=portrait,
                         education=education,
                         OfficePhone=OfficePhone,
                         officeRoom=officeRoom,
                         officeHours=officeHours,
                         bibliograph=bibliography,
                         OfficeCity='Davis',
                         OfficeState='CA',
                         OfficePostalCode='95616',
                         userpref_ext_editor=False)
                    fsd[id].at_post_create_script()
                    print "made a no class person for" + fullname
                    
               
                    
               if hasattr(fsd,id):
                   try:
                       fsd[id].setImage(portrait)
                   except:
                       print "image failed for %s" %id
                   print "image success for %s" % id 
               else:
                   print "fail for %s" % id
                
#               if hasattr(fsd,id):
#                    
               
 #              Assign departments and specialties here
                      
                    
     return "Done"