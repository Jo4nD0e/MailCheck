import re
import smtplib
import dns.resolver
import csv
# Address used for SMTP MAIL FROM command
fromAddress = 'Jhon.Doe@gmail.com'
# Open .csv file with list of email
# Read file without \n
data = []
with open('IN.csv') as File:
    for row in File:
        data = [x.rstrip("\n") for x in File.readlines()]
        print('Reading from file - DONE')
# Get domain for DNS lookup
addressToVerify = data[0]
domain = addressToVerify.split('@')[1]
print('Domain:', domain)
# MX record lookup
records = dns.resolver.query(domain, 'MX')
mxRecord = records[0].exchange
mxRecord = str(mxRecord)
# SMTP lib setup (use debug level for full output)
server = smtplib.SMTP()
server.set_debuglevel(0)
# SMTP Conversation
server.connect(mxRecord)
server.helo(server.local_hostname)
server.mail(fromAddress)
# Write to .csv file SMTP response code
with open('OUT.csv', 'w') as FileOUT:
    fieldnames = ['Addresses', 'Exists/Not exists']
    writer = csv.DictWriter(FileOUT, fieldnames=fieldnames)
    writer.writeheader()
    for addressToVerify in data:
    	code, message = server.rcpt(str(addressToVerify))
        # Assume SMTP response 250 is success
    	if code == 250:
    		writer.writerow({'Addresses': addressToVerify, 'Exists/Not exists': 'Exists'})
    	else:
    		writer.writerow({'Addresses': addressToVerify, 'Exists/Not exists': 'Not exists'})
    print('Writing to file - DONE')
server.quit()