import os
from base64 import b64encode

# This open() may hang indefinitely
fd = os.open('/dev/urandom', os.O_RDWR)
data = os.read(fd,12)
text = b64encode(data).decode('utf-8')
print(text)
