import os
import json

vcap = json.loads(os.getenv('VCAP_SERVICES'))

cred = vcap['p-mysql'][0]['credentials']

print "loaded cred is " , cred
os.environ['JDBC_URL'] = cred['uri']
os.environ['JDBC_USERNAME'] = cred['username']
os.environ['JDBC_PASSWORD'] = cred['password']