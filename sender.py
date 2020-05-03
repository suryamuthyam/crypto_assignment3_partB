import hmac
import hashlib

#message
message=b'hello there'

#Integrity check
hash_of_msg=hashlib.sha512(message).hexdigest()
print(hash_of_msg)

#Authentication
key=b'21545447'
hexdigest = hmac.new(key,message,hashlib.sha1).hexdigest()
print(hexdigest)

#final_message to transmit
final_message = {
    "Message"         : message,
    "sha512"          : hash_of_msg,
    "Authentication"  : hexdigest
}
