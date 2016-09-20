import requests
from time import sleep
Notifier = raw_input('Enter your Notifier Name:\n')
file_prompt = raw_input('Enter the file name to import(ex. list.txt):\n')
file_open = open(file_prompt, 'r').readlines()
for Domain in file_open:
    with requests.Session() as c:
	    print 'Submitting', Domain, 'as', Notifier, '...'
        url = 'http://www.zone-h.org/notify/single'
        c.get(url)
        post_data = dict(defacer=Notifier, domain1=Domain, hackmode=1, reason=1)
        c.post(url, data=post_data, headers={"Referer": "http://www.zone-h.org/"})
        page = c.get('http://www.zone-h.org/notify/single')
print 'All submission has been accomplished!'
print 'Exiting ...'
sleep(3)
