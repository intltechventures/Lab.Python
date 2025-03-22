# https://medium.com/asecuritysite-when-bob-met-alice/1-detects-a-prime-number-468232da1879
# https://asecuritysite.com/primes/regprime

import re
import sys

n=13
if (len(sys.argv)>1):
 n=int(sys.argv[1])

matches=re.match(r'^.?$|^(..+?)\1+$', '1'*n)

print("Use the RegEx of ^.?$|^(..+?)\\1+$\n")
if matches:
 print(f"{n} is not a prime. Match details: {matches.groups()}")
else:
 print(f"{n} is a prime")
