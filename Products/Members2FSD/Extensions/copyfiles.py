from zope.app.component.hooks import getSite
import transaction



def CopyFiles():
     site = getSite()
     peeps = site['people']
     memcontent = []
     source_contenttype = 'PersonFolder'
     target_contenttype = 'FSDPerson'
     

     items = peeps.listFolderContents(
        contentFilter={"portal_type": source_contenttype})
     fsd = site['Directory']

     for item in items:
          id = item.getId()
          
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