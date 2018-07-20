"""wechat_token project
wechat URL Configuration
"""

from django.urls import path, re_path

from wechat.views import token_handle

urlpatterns = [
    path('', token_handle),
]