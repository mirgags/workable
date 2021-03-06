import urllib2
import ast
import pprint
import json
import os
import unicodedata
import pickle

#start the api work here

curPath = os.getcwd()

f = open('%s/workableapi.txt' % curPath, 'rb')
apikey = f.readline().strip()
f.close()

jobcodes = []
candidates = {}
jsonObjects = []
#url = "http://www.workable.com/spi/accounts/%s/jobs/%s" % (apikey, jobcode)
url = "http://www.workable.com/spi/accounts/%s/jobs?phase=published" % apikey
urlList = [                                                                   "http://www.workable.com/spi/accounts/%s/jobs?phase=published" % apikey,   "http://www.workable.com/spi/accounts/%s/jobs?phase=archived" % apikey,   "http://www.workable.com/spi/accounts/%s/jobs?phase=closed" % apikey
   ]

for url in urlList:
    req = urllib2.Request(url)
    resp = urllib2.urlopen(req)
    
    workabledict = ast.literal_eval(resp.read())
    #print workabledict
    
    for item in workabledict['jobs']:
        jobcodes.append((item['title'], item['shortcode']))

#print jobcodes

for item in jobcodes:
    url = "http://www.workable.com/spi/accounts/%s/jobs/%s/candidates" % (apikey, item[1])
    req = urllib2.Request(url)
    resp = urllib2.urlopen(req)
    candidates[item[0]] = json.load(resp)

#print candidates
#for key in candidates:
#    print key

workablecsv = "sep=|job|name|email|resume"
workableList = ['qualified', 'phone screen', 'assessments', 'interview',                   'presentation', 'offer', 'hired']

for jobtitle in candidates:
    for person in candidates[jobtitle]['candidates']:
#        if any(person['stage'] in l for l in workableList:
        jsonObjects.append([jobtitle, person])
        workablecsv = workablecsv + "^^^" + jobtitle + "|" + unicodedata.normalize('NFKD', person['name']).encode('utf8', 'replace') + "|" + unicodedata.normalize('NFKD', person['email']).encode('utf8', 'replace') + "|" + unicodedata.normalize('NFKD', person['resume_url']).encode('utf8', 'replace') + "|" + unicodedata.normalize('NFKD', person['stage']).encode('utf8', 'replace')
        print "************"
        print jobtitle + "," + str(person)
        for education in person['educations']:
            if education:
                for key in education:
                    try:
                        workablecsv = workablecsv + "|" + key + ": " + unicodedata.normalize('NFKD', education[key]).encode('utf8', 'replace')
                    except (TypeError, AttributeError, UnicodeDecodeError):
                        pass
        for experience in person['experieneces']:
            if experience:
                for key in experience:
                    try:
                        workablecsv = workablecsv + "|" + key + "|" + unicodedata.normalize('NFKD', experience[key]).encode('utf8', 'replace')
                    except (TypeError, AttributeError, UnicodeDecodeError):
                        pass
#        workablecsv = workablecsv + ", " + person['resume_url']

#print workablecsv
workablecsv = unicodedata.normalize('NFKD', workablecsv).encode('utf8', 'replace')
workablecsv = workablecsv.replace('\r', ' ')
workablecsv = workablecsv.replace('\n', ' ')
workablecsv = workablecsv.replace('^^^', '\n')

f = open('%s/workable_candidates.csv' % curPath, 'wb')
f.write(workablecsv)
f.close()

f = open('%s/workable_candidates.pkl' % curPath, 'wb')
pickle.dump(json.dumps(jsonObjects), f)
f.close

f = open('%s/workable_candidates.txt' % curPath, 'wb')
f.writelines(json.dumps(jsonObjects))
f.close
