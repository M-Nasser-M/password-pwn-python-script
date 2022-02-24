import requests
from hashlib import sha1
import sys

password = sys.argv[1]
apiUrl = 'https://api.pwnedpasswords.com/range'


def hash_password(password_to_hash: str):
    return sha1(password_to_hash.encode('utf-8')).hexdigest().upper()


def get_hashed_passwords_list(search_hash):
    r = requests.get(f'{apiUrl}/{search_hash}')
    return r.text


password_hashed = hash_password(password)
hashes_text = get_hashed_passwords_list(password_hashed[0:5])
hashes_list = hashes_text.split()
hashes_dic = {}
for element in hashes_list:
    dic_item = element.split(":")
    hashes_dic.update({dic_item[0]: int(dic_item[1])})

print(f" you password:{password} was found {hashes_dic.get(password_hashed[5:])} times")
: