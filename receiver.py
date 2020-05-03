import hmac
import hashlib
#message received after transmission
transmitted_message ={
    "Message"         : 'hello there',
    "sha512"         : 'b7e98c78c24fb4c2c7b175e90474b21eae0ccf1b5ea4708b4e0f2d2940004419edc7161c18a1e71b2565df099ba017bcaa67a248e2989b6268ce078b88f2e210',
    "Authentication"  : '3e3e17a3584c75bb0aaaf5dcafd9243f7867f6b2'
}

message=transmitted_message["Message"].encode('utf-8')

#check the integrity
new_hash=hashlib.sha512(message).hexdigest()
if new_hash==reveived_message['hash']:
    print("Integrity check : true")
else:
    print("Integrity check : false")

#Check Authenticity
key=b'21545447'
new_hash_digest=hmac.new(key,message,hashlib.sha1).hexdigest()
if new_hash_digest==transmitted_message['Authentication']:
    print("Authentication : true")
else:
    print("Authentication : false")
