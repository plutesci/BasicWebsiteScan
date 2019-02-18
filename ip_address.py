import os
# finds an ip address for the given domain

def get_ip_address(url):
    command = "host " + url
    process = os.popen(command)
    results = str(process.read())
# below adds a character count for the tld.
# in this case an ipv4 000.000.000.000
    marker = results.find('has address') + 12 
    return results[marker:].splitlines()[0]

#print(get_ip_address('reddit.com'))
