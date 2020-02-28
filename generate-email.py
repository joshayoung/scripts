#! /usr/bin/python
from datetime import datetime
from subprocess import Popen, PIPE

def generate_email():
    rdate = datetime.now().strftime("%Y%d%m%H%M%S")
    return "example" + rdate + "@example.com"

def output_email():
    email = generate_email()
    p = Popen(['pbcopy'], stdout=PIPE, stdin=PIPE)
    p.communicate(input=email)
    print email

output_email();
