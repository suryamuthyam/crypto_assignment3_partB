import hmac
import hashlib
#message received after transmission
transmitted_message ={
    "Message"         : 'YQOY]_',
    "sha512"         : '6d8f87664f7e149c6a96641b7a07dcbf60a7e9d0aa474588daf25e8df31fb2aa989a19267873a2041727a425a67df1170854b4a0ea43b97ea50d7fef97d7d9c1',
    "Authentication"  : 'c2445ab3ff4612d32542531f7f8b0956c65987f3'
}
#decryption
encryption_message=transmitted_message["Message"]
key='146146146'
message=''
for i in range(len(encryption_message)):
    message+=chr( ord(encryption_message[i]) ^ ord(key[i%len(key)]) )
message=message.encode('utf-8')
#check the integrity
new_hash=hashlib.sha512(message).hexdigest()
if new_hash==transmitted_message['hash']:
    print("Integrity check : true")
else:
    print("Integrity check : false")

#Check Authenticity
key=b'146146146'
new_hash_digest=hmac.new(key,message,hashlib.sha1).hexdigest()
if new_hash_digest==transmitted_message['Authentication']:
    print("Authentication : true")
else:
    print("Authentication : false")