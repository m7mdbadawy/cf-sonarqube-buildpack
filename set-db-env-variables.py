import os
import json
import subprocess

vcap = json.loads(os.getenv('VCAP_SERVICES'))

cred = vcap['postgres-cluster'][0]['credentials']

print "loaded cred is " , cred
os.environ['JDBC_URL'] = "jdbc:" + cred['uri'].replace('postgres','postgresql')

subprocess.call("""perl -p -e 's/\$\{([^}]+)\}/defined $ENV{$1} ? $ENV{$1} : $&/eg; s/\$\{([^}]+)\}//eg' ./sonar.properties > ./sonar_replaced.properties""", shell=True)