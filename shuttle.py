def shuttle():
  import urllib
  import json
  from time import localtime, strftime
  from datetime import datetime
  params = urllib.urlencode({'a': 'Quad', 'b': 'Mass Ave Garden St', 'output': 'json', 'sdt': strftime('%Y-%m-%dT%H:%M:%S', localtime())})
  f = urllib.urlopen("http://shuttleboy.cs50.net/api/1.2/trips?%s" % params)
  all=json.load(f)  
  current=strftime('%H:%M:%S', localtime())
  for i in range(0,3):
    shuttletime=all[i]['departs'][11:];
    print 'Shuttle departs at {}, or {} from now.'.format(shuttletime, datetime.strptime(shuttletime, '%H:%M:%S')-datetime.strptime(current, '%H:%M:%S') );
shuttle();
