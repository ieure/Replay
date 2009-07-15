from datetime import timedelta
from multiprocessing import Pool
import time, datetime, urllib2, urllib

def hit_url(url):
    print "url: %s" % (url)
    try:
        f = urllib2.urlopen(url)
        f.read()
    except Exception, e:
        pass
    return True
    
f = open("log_data")
next_timestamp = None
pool = Pool(100)

for line in f:
    line = line.strip()
    fields = line.split("\x01")
    time_field = fields[4]
    url_field = fields[5]
    if not url_field.startswith("GET"):
        continue
    
    method, url, http = url_field.split(" ", 2)
    tt = time.strptime(time_field[1:-7], "%d/%b/%Y:%H:%M:%S")
    timestamp = time.mktime(tt)
    
    while 1:
        if next_timestamp and (timestamp + 1 != next_timestamp):
            next_timestamp += 1
            time.sleep(1)
        else:
            break
    next_timestamp = timestamp + 1
    url = "http://localhost/~goffinet/test.php?url=%s" % (urllib.quote(url))
    pool.apply_async(hit_url, [url])
pool.close()
pool.join()