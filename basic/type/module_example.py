import math

print(round(3.14))
print(math.floor(3.6))
print(math.ceil(3.6))

import random
print(random.random)
print(random.uniform(10, 20))
print(round(random.uniform(10, 20)))
print(random.randrange(10))
print(random.choice([1,2,3,4,5]))
print(random.choices([1,2,3,4,5]), 2, 10)
print(random.shuffle([1,2,3,4,5]))
print()
print(random.sample([1,2,3,4,5], k=4))

import sys
print(sys.argv)
print(sys.getcheckinterval)
print(sys.getdefaultencoding)
print(sys.getdlopenflags)

import datetime
now = datetime.datetime.now()
print(now)
print(now.second)

after = now + datetime.timedelta(
    days=1,
    hours=1
)
print(after.strftime("%Y{} %m{} %d{} %H{}").format(*"년월일시"))