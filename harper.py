import sys, getopt

def main(argv):
    opts, args = getopt.getopt(argv,"u:")
    for opt, arg in opts:
        if opt in ("-u"):
            dxalias = arg

    print ('dx user alias is ', dxalias)

    sf = dxconnect(dxalias)
    result = sf.query_all("select id, email, name from user limit 10")
    for row in result['records']:
        print("%s, %s, %s" % (row['Id'], row['Email'], row['Name']))


def dxconnect(alias):
    import subprocess
    import json
    from simple_salesforce import Salesforce

    sfdx_cmd = subprocess.Popen(f'sfdx force:org:display --targetusername {alias} --json', shell=True, stdout=subprocess.PIPE)
    sfdx_info = json.loads(sfdx_cmd.communicate()[0])

    access_token = sfdx_info['result']['accessToken']
    instance_url = sfdx_info['result']['instanceUrl']

    return Salesforce(instance_url=instance_url,session_id=access_token)

if __name__ == "__main__":
   main(sys.argv[1:])
