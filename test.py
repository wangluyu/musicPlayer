import base64
import hashlib
import json
import binascii
import os

import requests
from Crypto.Cipher import AES

TEXT = {'username': '', 'password': '', 'rememberLogin': 'true'}
modulus = ('00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7'
           'b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280'
           '104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932'
           '575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b'
           '3ece0462db0a22b8e7')
nonce = '0CoJUm6Qyw8W8jud'
pubKey = '010001'


def aesEncrypt(text, secKey):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encryptor = AES.new(secKey, 2, '0102030405060708')
    ciphertext = encryptor.encrypt(text)
    ciphertext = base64.b64encode(ciphertext)
    return ciphertext.decode()


def rsaEncrypt(text, pubKey, modulus):
    text = text[::-1].encode()
    rs = int(binascii.hexlify(text), 16)**int(pubKey, 16) % int(modulus, 16)
    return format(rs, 'x').zfill(256)


def createSecretKey(size):
    return ''.join( [ hex(x)[2:] for x in os.urandom(size) ] )[0:16]

# 获取params和encSecKey text为TEXT
def encrypt_request(text):
    text = json.dumps(text)
    secKey = createSecretKey(16)
    encText = aesEncrypt(aesEncrypt(text, nonce), secKey)
    encSecKey = rsaEncrypt(secKey, pubKey, modulus)
    data = {
        'params': encText,
        'encSecKey': encSecKey
    }
    return data

def login(username,password):
    url = 'http://music.163.com/weapi/login/'
    headers = {
        'Cookie': 'appver=2.7.1;',
        'Referer': 'http://music.163.com/'
    }
    text = {
        'username': username,
        'password': hashlib.md5(password.encode()).hexdigest(),
        'rememberLogin': 'true'
    }
    data = encrypt_request(text)
    s = requests.session()
    r = s.post(url, headers=headers, data=data)
    cookies = dict(r.cookies)
    return cookies