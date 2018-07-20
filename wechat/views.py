from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import hashlib, os

@csrf_exempt
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
        sha1 = hashlib.sha1(str.encode())
        
        hashcode = sha1.hexdigest()
        print(f"handle/GET func: \n hashcode:{hashcode} \n signature:{signature}")
        
        if hashcode == signature:
            content = echostr
        else:
            content = "invalid"
        return HttpResponse(content)
    
    if request.method == 'POST':
        dict = request.body
        print(dict)
        for key in dict:
            print(f"handle/POST key:{key} value:{dict[key]}")
        return HttpResponse('success')
        