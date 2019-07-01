#!/usr/bin/env python
import subprocess

login = 'username'
password = 'somepassword'

# OpenSSL doesn't support stronger hash functions, mkpasswd is preferred
#p = subprocess.Popen(('openssl', 'passwd', '-1', password), stdout=subprocess.PIPE)
p = subprocess.Popen(('mkpasswd', '-m', 'sha-512', password), stdout=subprocess.PIPE)
shadow_password = p.communicate()[0].strip()

if p.returncode != 0:
    print 'Error creating hash for ' + login

r = subprocess.call(('usermod', '-p', shadow_password, login))

if r != 0:
    print 'Error changing password for ' + login
