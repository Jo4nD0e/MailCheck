### How it works
```
  The script is designed to verify the existence of Email address.
  Use IN.csv and OUT.csv for checking LARGE quantities of Email address.
  To check one or more, use #MailCheck_manual.py
```


### Download and Run:
```bash
  # Download
  $ git clone https://github.com/Jo4nD0e/MailCheck
  
  # Requirements
  $ requirements.txt

  # Run
  $ python3 MailCheck.py
  $ python3 MailCheck_manual.py
```


### Important
```
  #1 The good mail server can always answer 250 and then the script will not help
  #2 Beforу use MailCheck, set Email address used for #fromAddress command.
  #3 At the moment, it is possible to check email addresses only for one domain at a time, to check different 
  domains you need to run a script every time.
```