#<0>
import random
import time
random.seed(time.time())
c=['edit', 'me'] #<1>
print(c[random.randint(0, len(c)-1)])