# coded with internal modules
# coded by Choyon Ahmed
# donate me : 1LXPCJtyhBxtpE8ULe2ZZAMwSZJiigvTEv
# save your urls to "sitestomirror.txt"
# change line 10 with your defacer name(don't remove quote)
import urllib, urllib2, httplib
def mirror(url):
    try:
        print 'Mirroring', url, 'on z-h'
        data = urllib.urlencode({'defacer':'TeaM_CC', 'domain1':url, 'hackmode':'1', 'reason':'1'})
        req = urllib2.Request('http://www.zone-h.org/notify/single', data)
        response = urllib2.urlopen(req)
        if 'OK' in response.read():
            print '[>>>] z-h DONE!'
        elif 'banned' in response.read():
            print '[X] OMG!you are banned!'
        else:
            print '[X] shit!!!cannot make it on z-h!'
    except:
        pass
try:
    if 'banned' in 'http://www.zone-h.org/notify/single':
        print 'Your IP address was banned by zone-h'
        exit(0)
except:
    pass
go = open('sitestomirror.txt', 'r').readlines()
for i in go:
    i = i.replace('\n','')
    if 'https://' not in i:
        if 'http://' not in i:
            i = 'http://' + i
    mirror(i)
