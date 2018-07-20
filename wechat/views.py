from django.http import HttpResponse
from django.shortcuts import render


import hashlib, os

def token_handle(request):
    get_value = lambda dict, key, default: dict[key] if key in dict else default
    if request.method == 'GET':
        dict = request.GET
        signature = get_value(dict, 'signature', '')
        timestamp = get_value(dict, 'timestamp', '')
        nonce = get_value(dict, 'nonce', '')
        echostr = get_value(dict, 'echostr', '')
        token = os.getenv('WX_TOKEN', '508EE8A6BEED4DB78068960627D763A3')

        list = [token, timestamp, nonce]
        list.sort()
        str = ''.join(list)
        sha1 = hashlib.sha1(str)
        
        hashcode = sha1.hexdigest()
        print(f"handle/GET func: \n hashcode:{hashcode} \n signature:{signature}")
        
        if hashcode == signature:
            content = echostr
        else:
            content = "Invalid"
        return HttpResponse(content)