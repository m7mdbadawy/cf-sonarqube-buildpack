import os
import json

vcap = json.loads(os.getenv('VCAP_SERVICES'))

cred = vcap['p-mysql'][0]['credentials']

print "loaded cred is " , cred
os.environ['JDBC_URL'] = cred['uri']
os.environ['JDBC_USERNAME'] = cred['username']
os.environ['JDBC_PASSWORD'] = cred['password']

subprocess.call("""perl -p -e 's/\$\{([^}]+)\}/defined $ENV{$1} ? $ENV{$1} : $&/eg; s/\$\{([^}]+)\}//eg' ./sonar.properties > ./sonar_replaced.properties""", shell=True)