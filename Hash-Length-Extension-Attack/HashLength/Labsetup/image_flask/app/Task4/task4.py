import hmac
import hashlib
key='123456'
message='myname=RushabhPrajapati&uid=1001&lstcmd=1'
mac = hmac.new(bytearray(key.encode('utf-8')),
        msg=message.encode('utf-8','surrogateescape'),
        digestmod=hashlib.sha256).hexdigest()

print(mac)
