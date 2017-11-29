import hashlib
import sys
import pybip38 # pip install pybip38
# Note: The pybip38 is limited to Bitcoin (only) BIP38 encoded keys, NOT other alt-coins that use BIP38. Probably based on validation performed by that library.

# Example BIP38 Key. Password = test
BIP38 = '6PRSDyF92mGmAqG66BpAfo3sPGrHmkqgkriwQevP82satGzVQjWobYCXxc'

for line in open('passwords.txt'):
    passwords = []
    password = line.strip()
    md5 =  hashlib.md5(password).hexdigest()
    sha512 =  hashlib.sha512(password).hexdigest()
    sha256 =  hashlib.sha256(password).hexdigest()
    passwords.append(str(password))
    passwords.append(str(password) + str(password))
    passwords.append(str(md5))
    passwords.append(str(md5) + str(md5))
    passwords.append(str(sha512))
    passwords.append(str(sha512) + str(sha512))
    passwords.append(str(sha256))
    passwords.append(str(sha256) + str(sha256))
    
    for item in passwords:
        print "# Trying password: %s" % item
        if pybip38.bip38decrypt(item, BIP38) != False:
            print "\n## KEY FOUND: %s\n" % item
            sys.exit(0)

print "\n## Password NOT found :-(\n"
