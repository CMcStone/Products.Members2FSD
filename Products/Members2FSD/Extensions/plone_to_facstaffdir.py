
from zope.interface import implements
from zope.interface import implements

from Products.Members2FSD.interfaces import IMemberConverter

from Products.CMFCore.utils import getToolByName
from zope.app.component.hooks import getSite
import transaction

class memberConverter(object):
    implements(IMemberConverter)

    def getOldMemberProperties(self, member):
        site = getSite()
        md = getToolByName(site, 'portal_memberdata')
        memberprops = {}
        for prop in md.propertyIds():
            memberprops[prop] = member.getProperty(prop)
        return memberprops

    def __call__(self, member):
        site = getSite()
        mt = getToolByName(site, 'portal_membership')
        md = getToolByName(site, 'portal_memberdata')
	catalog = getToolByName(site, 'portal_catalog')
        fsd = site['directory'] # wow is this kludgy!
        memberprops = self.getOldMemberProperties(member)
        newprops = self.conevertProps(memberprops)
        newid = member.getId()
        portrait = md._getPortrait(member.getId())
        fsd.invokeFactory(id=newid, type_name="FSDPerson", **newprops)
        if hasattr(fsd,newid):
            try:
                fsd[newid].setImage(portrait)
            except:
                print "image failed for %s" %newid
            return "success for %s" % newid 
        else:
            return "fail for %s" % newid

    def convertProps(self, memberprops):
        site = getSite()
        catalog = getToolByName(site, 'portal_catalog')
        newprops = {}
	# fullname to fistName, middleName, lastName
	fullname = memberprops['fullname']
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
        # email to email
        newprops['email'] = memberprops['email']

        # workingtitle, hometitle and department to jobTitles
        newprops['jobTitles'] = [memberprops['workingtitle']]
        if memberprops['hometitle'] != '' or memberprops['homedepartment'] != '':
            newprops['jobTitles'].append(memberprops['hometitle'] + ', ' + memberprops['homedepartment'])

        # location to officeAddress
        newprops['officeAddress'] = memberprops['location']

        # fudge officeCity, officeState, officePostalCode
        newprops['officeCity'] = 'Davis'
        newprops['officeState'] = 'California'
        newprops['officePostalCode'] = '95618'

        # phone to officePhone; note: phoneNumberRegex must be disabled 
        # in fsd_tool
        newprops['officePhone'] = memberprops['phone']

        # member portrait
        
        # punt for now


        # description to biography
        newprops['biography'] = memberprops['description']

        # degree to education
        newprops['education'] = [memberprops['degree'] + ' (' + memberprops['deginstitution'] + ')']

        # home_page = websites
        newprops['websites'] = [memberprops['home_page']]

        # memberid to id
        #newprops['id'] = memberid

        # affiliation to classifications
        brains = catalog(portal_type='FSDClassification')
	classes = {}
        for brain in brains:
            classes[brain.Title] = brain.UID
        newprops['classifications'] = [classes[memberprops['affiliation']]]

        # language to userpref_language
        newprops['userpref_language'] = memberprops['language']

        # wysiwyg_editor to userpref_wysiwyg_editor
        newprops['userpref_wysiwyg_editor'] = memberprops['wysiwyg_editor']

        # ext_editor to userpref_ext_editor set to False
        newprops['userpref_ext_editor'] = False

        # portal_skin to userpref_portal_skin set to blank
        newprops['userpref_portal_skin'] = ''

        return newprops

def convert():
    site = getSite()
    mt = getToolByName(site, 'portal_membership')
    con = memberConverter()
    for memid in mt.listMemberIds():
        m = mt.getMemberById(memid)
        site._p_jar.sync()
        con(m)
        transaction.commit()
        try:
            memcontent = site.people-old[memid].objectIds()
            ref = site.people-old[memid].manage_cutObjects(memcontent)
            site._p_jar.sync()
            site.directory[memid].manage_pasteObjects(ref)
            transaction.commit()
        except:
            pass

def reset():
    site = getSite()
    dir = site['directory']
    persons = dir.objectIds('FSDPerson')
    dir.manage_delObjects(persons)
    transaction.commit()


from Products.Members2FSD.interfaces import IMemberConverter

from Products.CMFCore.utils import getToolByName
from zope.app.component.hooks import getSite
import transaction

class memberConverter(object):
    implements(IMemberConverter)

    def getOldMemberProperties(self, member):
        site = getSite()
        md = getToolByName(site, 'portal_memberdata')
        memberprops = {}
        for prop in md.propertyIds():
            memberprops[prop] = member.getProperty(prop)
        return memberprops

    def __call__(self, member):
        site = getSite()
        mt = getToolByName(site, 'portal_membership')
        md = getToolByName(site, 'portal_memberdata')
	catalog = getToolByName(site, 'portal_catalog')
        fsd = site['directory'] # wow is this kludgy!
        memberprops = self.getOldMemberProperties(member)
        newprops = self.convertProps(memberprops)
        newid = member.getId()
        portrait = md._getPortrait(member.getId())
        fsd.invokeFactory(id=newid, type_name="FSDPerson", **newprops)
        if hasattr(fsd,newid):
            try:
                fsd[newid].setImage(portrait)
            except:
                print "image failed for %s" %newid
            return "success for %s" % newid 
        else:
            return "fail for %s" % newid

    def convertProps(self, memberprops):
        site = getSite()
        catalog = getToolByName(site, 'portal_catalog')
        newprops = {}
	# fullname to fistName, middleName, lastName
	fullname = memberprops['fullname']
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

        # email to email
        newprops['email'] = memberprops['email']

        # workingtitle, hometitle and department to jobTitles
        newprops['jobTitles'] = [memberprops['workingtitle']]
        if memberprops['hometitle'] != '' or memberprops['homedepartment'] != '':
            newprops['jobTitles'].append(memberprops['hometitle'] + ', ' + memberprops['homedepartment'])

        # location to officeAddress
        newprops['officeAddress'] = memberprops['location']

        # fudge officeCity, officeState, officePostalCode
        newprops['officeCity'] = 'Davis'
        newprops['officeState'] = 'California'
        newprops['officePostalCode'] = '95618'

        # phone to officePhone; note: phoneNumberRegex must be disabled 
        # in fsd_tool
        newprops['officePhone'] = memberprops['phone']

        # member portrait
        
        # punt for now


        # description to biography
        newprops['biography'] = memberprops['description']

        # degree to education
        newprops['education'] = [memberprops['degree'] + ' (' + memberprops['deginstitution'] + ')']

        # home_page = websites
        newprops['websites'] = [memberprops['home_page']]

        # memberid to id
        #newprops['id'] = memberid

        # affiliation to classifications
        brains = catalog(portal_type='FSDClassification')
	classes = {}
        for brain in brains:
            classes[brain.Title] = brain.UID
        newprops['classifications'] = [classes[memberprops['affiliation']]]

        # language to userpref_language
        newprops['userpref_language'] = memberprops['language']

        # wysiwyg_editor to userpref_wysiwyg_editor
        newprops['userpref_wysiwyg_editor'] = memberprops['wysiwyg_editor']

        # ext_editor to userpref_ext_editor set to False
        newprops['userpref_ext_editor'] = False

        # portal_skin to userpref_portal_skin set to blank
        newprops['userpref_portal_skin'] = ''

        return newprops

def convert():
    site = getSite()
    mt = getToolByName(site, 'portal_membership')
    con = memberConverter()
    for memid in mt.listMemberIds():
        m = mt.getMemberById(memid)
        site._p_jar.sync()
        con(m)
        transaction.commit()
        try:
            memcontent = site.people-old[memid].objectIds()
            ref = site.people-old[memid].manage_cutObjects(memcontent)
            site._p_jar.sync()
            site.directory[memid].manage_pasteObjects(ref)
            transaction.commit()
        except:
            pass

def reset():
    site = getSite()
    dir = site['directory']
    persons = dir.objectIds('FSDPerson')
    dir.manage_delObjects(persons)
    transaction.commit()
