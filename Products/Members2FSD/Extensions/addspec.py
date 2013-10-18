       from zope.app.component.hooks import getSite
       import transaction
       from Products.CMFCore.utils import getToolByName
       from Products.Relations.processor import process



       def addspec():
            site = getSite()
            peeps = site['people']
            directory = site['directory']
            memcontent = []
            source_contenttype = 'PersonFolder'
            target_contenttype = 'FSDPerson'
     

            items = peeps.listFolderContents(
               contentFilter={"portal_type": source_contenttype})
            fsd = site['directory']

            for item in items:
                 id = item.getId()
                 if 'Social Transformations' in item.Subject():
                       specialtyId = 'social-transformations'
                       specialtyUID = site.portal_catalog(id=specialtyId, portal_type="FSDSpecialty")[0].UID
                       specialtyRulesetId = getToolByName(site, 'relations_library').getRuleset('people_specialties').getId()

        # You mustmustmust use the Relations API to add references, sayeth Relations/doc/Overview.txt.
                       process(site, connect=((directory[id].UID(), specialtyUID, specialtyRulesetId),))
                       print specialtyId + " assigned"
            return "done"
       