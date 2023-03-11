from getpass import getpass
from simple_salesforce import Salesforce
import requests
import sys

if len(sys.argv) != 3:
    sys.exit("usage : %s username login|test" % sys.argv[0])

sfPassword = getpass()

sf = Salesforce(
    username = sys.argv[1],
    password = sfPassword,
    security_token = '',
    domain=sys.argv[2])

result = sf.query('select id, name, email from user')
for row in result['records']:
    print("%s, %s, %s" % (row['Id'], row['Email'], row['Name']))
