import os
import urllib
import urllib2
import json
import datetime
import base64

def getApiKey():
    curPath = os.getcwd()
    f = open('%s/workableapi.txt' % curPath, 'rb')
    apikey = f.readline().strip()
    f.close()
    return apikey

### class of Workable instance
class workable(object):
    def __init__(self):
        self.name = "Workable Instance"
        self.jobs = {}
#        self.loadjobs()
### loads all jobs in account
    def loadJobs(self):
        apikey = getApiKey()
        aList = json.loads(getUrl(                                                      'http://www.workable.com/spi/accounts/%s/jobs?phase=published'             % apikey))
        for job in aList['jobs']:
            self.jobs[job['shortcode']] = job

### class of Workable job posting ###
class Job(object):
    def __init__(self, shortCode):
        self.name = ""
        self.Id = ""
        self.shortcode = shortCode
        self.job = {}
        ### Dictionary keys:
           #id, title, code, shortcode, phase, country, location_state,                city, department, created_at, description

    def loadJobDetail(self):
        apikey = getApiKey()
        self.job = json.loads(getUrl(                                                      'http://www.workable.com/spi/accounts/%s/jobs/%s' % (apikey,               self.shortcode)))
        self.name = self.job['title']
        self.Id = self.job['id']
#        self.phase = aDict['phase']
#        self.country = aDict['country']
#        self.state = aDict['location_state']
#        self.city = aDict['city']
        
### GET request to establish parameters
def getUrl(theurl):
    print theurl
    pagehandle = urllib2.urlopen(theurl)
    
    return pagehandle.read()
   
def postUrl(theurl, thePost):

    req = urllib2.Request(theurl)
#    auth = 'Basic ' + base64.urlsafe_b64encode("%s:%s" % (getApiKey(), 'x'))
#    req.add_header('Authorization', auth)
    req.add_header('Content-Type', 'application/json')
    req.add_header('Accept', 'application/json')

    return urllib2.urlopen(req, json.dumps(thePost))

