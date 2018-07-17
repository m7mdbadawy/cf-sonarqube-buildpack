import os
import json

vcap = json.loads(os.getenv('VCAP_SERVICES'))

cred = vcap['p-mysql'][0]['credentials']

print "loaded cred is " , cred
os.putenv('JDBC_URL',cred['uri'])
os.putenv('JDBC_USERNAME',cred['username'])
os.putenv('JDBC_PASSWORD',cred['password'])