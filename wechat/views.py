from django.http import HttpResponse
from django.shortcuts import render


import hashlib

def token_handle(request):
    get_value = lambda dict, key, default: dict[key] if key in dict else default
    if request.method == 'GET':
        dict = request.GET
        signature = get_value(dict, 'signature', '')
        timestamp = get_value(dict, 'timestamp', '')
        nonce = get_value(dict, 'nonce', '')
        echostr = get_value(dict, 'echostr', '')
        token = ''

        list = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, list)
        hashcode = sha1.hexdigest()
        print("handle/GET func: hashcode, signature: ", hashcode, signature)
        
        if hashcode == signature:
            content = echostr
        else:
            content = "Invalid"
        return HttpResponse(content)