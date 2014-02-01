from workable import *

w = workable()
w.loadJobs()
jobs = []
for job in w.jobs:
    print job
    jobs.append(Job(job))
for job in jobs:
    job.loadJobDetail()
    print "Title: ", job.name, ", ID: ", job.Id
    if job.Id == 4955:
        thePost = "{title: %s, Id: %s}" % (job.name, job.Id)
        postUrl('http://requestb.in/1gqvv9m1', thePost)
        print "Posted: %s, Id: %s" % (job.name, job.Id)
