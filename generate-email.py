#! /usr/bin/python
import sys
from datetime import datetime
from subprocess import Popen, PIPE

try:
    email_name = sys.argv[1]
except IndexError:
    email_name = "example"

try:
    email_host = sys.argv[2]
except IndexError:
    email_host = "example.com"

def generate_email():
    rdate = datetime.now().strftime("%Y%d%m%H%M%S")
    return email_name + rdate + "@" + email_host

def output_email():
    email = generate_email()
    p = Popen(['pbcopy'], stdout=PIPE, stdin=PIPE)
    p.communicate(input=email)
    print email

output_email();
