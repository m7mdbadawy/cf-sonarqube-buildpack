import os
import json
import subprocess
import re

vcap = json.loads(os.getenv('VCAP_SERVICES'))

cred = vcap['postgres-cluster'][0]['credentials']

print "loaded cred is " , cred

match_obj = re.match(r"postgres://([^:]+):([^@]+)@(.+)",cred['uri'])
username,password,rest = match_obj.group(1), match_obj.group(2), match_obj.group(3)


os.environ['JDBC_URL'] = "jdbc:postgresql://" + rest
print("jdbc url: ", os.environ['JDBC_URL'])
os.environ['JDBC_USERNAME'] = username
print("jdbc username: ", os.environ['JDBC_USERNAME'])
os.environ['JDBC_PASSWORD'] = password
print("jdbc password: ", os.environ['JDBC_PASSWORD'])

subprocess.call("""perl -p -e 's/\$\{([^}]+)\}/defined $ENV{$1} ? $ENV{$1} : $&/eg; s/\$\{([^}]+)\}//eg' ./sonar.properties > ./sonar_replaced.properties""", shell=True)