from zope.app.component.hooks import getSite
import transaction



def AddDept():
     site = getSite()
     peeps = site['people']
     source_contenttype = 'PersonFolder'
     target_contenttype = 'FSDPerson'
     

     items = peeps.listFolderContents(
        contentFilter={"portal_type": target_contenttype})
        
     for item in items:
          id = item.getId()
		Get Classification Title
          If classification.title contains "faculty" department title = sociology-faculty
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