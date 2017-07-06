# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http.response import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
#from zinnia.models.entry import Entry

from wechat_sdk import WechatBasic
from wechat_sdk.exceptions import ParseError
from wechat_sdk.messages import TextMessage, VoiceMessage, ImageMessage, VideoMessage, LinkMessage, LocationMessage, \
    EventMessage
from minicms.settings import WECHAT_TOKEN, WEIXIN_APPID, WEIXIN_APPSECRET

# 首图的URL 900*500
BIGIMAGE_URL = r'http://7xoa4z.com/blog%2Fweixin%2Fhzw200%2F1.jpg'
# 小图的URL 200*200
SMALLIMAGE_URL = r'http://7xoa4z.com/blog%2Fweixin%2Fshuotu.jpg'

wechat_instance = WechatBasic(
    token=WECHAT_TOKEN,
    appid=WEIXIN_APPID,
    appsecret=WEIXIN_APPSECRET
)


@csrf_exempt
def wechat(request):
    if request.method == 'GET':
        # 检验合法性
        # 从 request 中提取基本信息 (signature, timestamp, nonce, xml)
        signature = request.GET.get('signature')
        timestamp = request.GET.get('timestamp')
        nonce = request.GET.get('nonce')

        if not wechat_instance.check_signature(
                signature=signature, timestamp=timestamp, nonce=nonce):
            return HttpResponseBadRequest('Verify Failed')

        return HttpResponse(
            request.GET.get('echostr', ''), content_type="text/plain")

    # 解析本次请求的 XML 数据
    try:
        wechat_instance.parse_data(data=request.body)
    except ParseError:
        return HttpResponseBadRequest('Invalid XML Data')
