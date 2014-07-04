import json
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.context_processors import csrf
from DjangoCaptcha import Captcha
from shadowsocks.web.models import Account
from shadowsocks.web.models import Link

def index(req):
    return render_to_response('index.html',)

def code(req):
    ca =  Captcha(req)
    ca.type = 'number'
    return ca.display()

def get(req):
    accounts = Account.objects.order_by('-id').filter(status='1')
    return render_to_response('get.html',{'accounts':accounts})

def share(req):
    if req.method == 'POST':
        ca = Captcha(req)
        if ca.check(req.POST['code']):
            try:
                Account.objects.create(ip=req.POST['ip'],port=req.POST['port'],password=req.POST['password'],encryption=req.POST['encryption'],country=req.POST['country'],etime=req.POST['etime'],email=req.POST['email'],name=req.POST['name'])
                return HttpResponse(u'\u003C\u0021\u0044\u004f\u0043\u0054\u0059\u0050\u0045\u0020\u0068\u0074\u006d\u006c\u003E\u000A\u003C\u0068\u0074\u006d\u006c\u0020\u006c\u0061\u006e\u0067\u003D\u0022\u007a\u0068\u002d\u0063\u006e\u0022\u003E\u000A\u003C\u0068\u0065\u0061\u0064\u003E\u000A\u003C\u006d\u0065\u0074\u0061\u0020\u0068\u0074\u0074\u0070\u002d\u0065\u0071\u0075\u0069\u0076\u003D\u0022\u0043\u006f\u006e\u0074\u0065\u006e\u0074\u002d\u0054\u0079\u0070\u0065\u0022\u0020\u0063\u006f\u006e\u0074\u0065\u006e\u0074\u003D\u0022\u0074\u0065\u0078\u0074\u002f\u0068\u0074\u006d\u006c\u003B\u0020\u0063\u0068\u0061\u0072\u0073\u0065\u0074\u003D\u0075\u0074\u0066\u002d\u0038\u0022\u0020\u002f\u003E\u000A\u003C\u0074\u0069\u0074\u006c\u0065\u003E\u5206\u4EAB\u5E10\u53F7\u0020\u007C\u0020\u0053\u0068\u0061\u0064\u006f\u0077\u0053\u006f\u0063\u006b\u0073\u516C\u76CA\u7EC4\u7EC7\u0020\u007C\u0020\u0053\u0068\u0061\u0064\u006f\u0077\u0053\u006f\u0063\u006b\u0073\u516C\u76CA\u7EC4\u7EC7\u662F\u4E00\u4E2A\u7531\u6C11\u95F4\u56E2\u4F53\u53D1\u8D77\u7684\uFF0C\u65E8\u5728\u5206\u4EAB\u0053\u0068\u0061\u0064\u006f\u0077\u0053\u006f\u0063\u006b\u0073\u5E10\u53F7\u003C\u002f\u0074\u0069\u0074\u006c\u0065\u003E\u000A\u003C\u002f\u0068\u0065\u0061\u0064\u003E\u000A\u000A\u003C\u0062\u006f\u0064\u0079\u003E\u000A\u003C\u0070\u003E\u003C\u0073\u0074\u0072\u006f\u006e\u0067\u003E\u63D0\u4EA4\u6210\u529F\uFF01\u6211\u4EEC\u5C06\u5C3D\u5FEB\u5BA1\u6838\u60A8\u7684\u5E10\u53F7\uFF01\u003C\u002f\u0073\u0074\u0072\u006f\u006e\u0067\u003E\u003C\u002f\u0070\u003E\u000A\u003C\u0070\u003E\u003C\u0061\u0020\u0068\u0072\u0065\u0066\u003D\u0022\u002f\u0022\u003E\u8FD4\u56DE\u9996\u9875\u003C\u002f\u0061\u003E\u003C\u002f\u0070\u003E\u000A\u003C\u002f\u0062\u006f\u0064\u0079\u003E\u000A\u003C\u002f\u0068\u0074\u006d\u006c\u003E\u000A')
            except:
                return HttpResponse(u'\u003C\u0021\u0044\u004f\u0043\u0054\u0059\u0050\u0045\u0020\u0068\u0074\u006d\u006c\u003E\u000A\u003C\u0068\u0074\u006d\u006c\u0020\u006c\u0061\u006e\u0067\u003D\u0022\u007a\u0068\u002d\u0063\u006e\u0022\u003E\u000A\u003C\u0068\u0065\u0061\u0064\u003E\u000A\u003C\u006d\u0065\u0074\u0061\u0020\u0068\u0074\u0074\u0070\u002d\u0065\u0071\u0075\u0069\u0076\u003D\u0022\u0043\u006f\u006e\u0074\u0065\u006e\u0074\u002d\u0054\u0079\u0070\u0065\u0022\u0020\u0063\u006f\u006e\u0074\u0065\u006e\u0074\u003D\u0022\u0074\u0065\u0078\u0074\u002f\u0068\u0074\u006d\u006c\u003B\u0020\u0063\u0068\u0061\u0072\u0073\u0065\u0074\u003D\u0075\u0074\u0066\u002d\u0038\u0022\u0020\u002f\u003E\u000A\u003C\u0074\u0069\u0074\u006c\u0065\u003E\u5206\u4EAB\u5E10\u53F7\u0020\u007C\u0020\u0053\u0068\u0061\u0064\u006f\u0077\u0053\u006f\u0063\u006b\u0073\u516C\u76CA\u7EC4\u7EC7\u0020\u007C\u0020\u0053\u0068\u0061\u0064\u006f\u0077\u0053\u006f\u0063\u006b\u0073\u516C\u76CA\u7EC4\u7EC7\u662F\u4E00\u4E2A\u7531\u6C11\u95F4\u56E2\u4F53\u53D1\u8D77\u7684\uFF0C\u65E8\u5728\u5206\u4EAB\u0053\u0068\u0061\u0064\u006f\u0077\u0053\u006f\u0063\u006b\u0073\u5E10\u53F7\u003C\u002f\u0074\u0069\u0074\u006c\u0065\u003E\u000A\u003C\u002f\u0068\u0065\u0061\u0064\u003E\u000A\u000A\u003C\u0062\u006f\u0064\u0079\u003E\u000A\u003C\u0070\u003E\u003C\u0073\u0074\u0072\u006f\u006e\u0067\u003E\u63D0\u4EA4\u5931\u8D25\uFF01\u8BF7\u91CD\u65B0\u63D0\u4EA4\uFF01\u003C\u002f\u0073\u0074\u0072\u006f\u006e\u0067\u003E\u003C\u002f\u0070\u003E\u000A\u003C\u0070\u003E\u003C\u0061\u0020\u0068\u0072\u0065\u0066\u003D\u0022\u0073\u0068\u0061\u0072\u0065\u0022\u003E\u8FD4\u56DE\u003C\u002f\u0061\u003E\u003C\u002f\u0070\u003E\u000A\u003C\u002f\u0062\u006f\u0064\u0079\u003E\u000A\u003C\u002f\u0068\u0074\u006d\u006c\u003E\u000A')
        else:
            return HttpResponse(u'\u003C\u0021\u0044\u004f\u0043\u0054\u0059\u0050\u0045\u0020\u0068\u0074\u006d\u006c\u003E\u000A\u003C\u0068\u0074\u006d\u006c\u0020\u006c\u0061\u006e\u0067\u003D\u0022\u007a\u0068\u002d\u0063\u006e\u0022\u003E\u000A\u003C\u0068\u0065\u0061\u0064\u003E\u000A\u003C\u006d\u0065\u0074\u0061\u0020\u0068\u0074\u0074\u0070\u002d\u0065\u0071\u0075\u0069\u0076\u003D\u0022\u0043\u006f\u006e\u0074\u0065\u006e\u0074\u002d\u0054\u0079\u0070\u0065\u0022\u0020\u0063\u006f\u006e\u0074\u0065\u006e\u0074\u003D\u0022\u0074\u0065\u0078\u0074\u002f\u0068\u0074\u006d\u006c\u003B\u0020\u0063\u0068\u0061\u0072\u0073\u0065\u0074\u003D\u0075\u0074\u0066\u002d\u0038\u0022\u0020\u002f\u003E\u000A\u003C\u0074\u0069\u0074\u006c\u0065\u003E\u5206\u4EAB\u5E10\u53F7\u0020\u007C\u0020\u0053\u0068\u0061\u0064\u006f\u0077\u0053\u006f\u0063\u006b\u0073\u516C\u76CA\u7EC4\u7EC7\u0020\u007C\u0020\u0053\u0068\u0061\u0064\u006f\u0077\u0053\u006f\u0063\u006b\u0073\u516C\u76CA\u7EC4\u7EC7\u662F\u4E00\u4E2A\u7531\u6C11\u95F4\u56E2\u4F53\u53D1\u8D77\u7684\uFF0C\u65E8\u5728\u5206\u4EAB\u0053\u0068\u0061\u0064\u006f\u0077\u0053\u006f\u0063\u006b\u0073\u5E10\u53F7\u003C\u002f\u0074\u0069\u0074\u006c\u0065\u003E\u000A\u003C\u002f\u0068\u0065\u0061\u0064\u003E\u000A\u000A\u003C\u0062\u006f\u0064\u0079\u003E\u000A\u003C\u0070\u003E\u003C\u0073\u0074\u0072\u006f\u006e\u0067\u003E\u9A8C\u8BC1\u7801\u9519\u8BEF\uFF0C\u8BF7\u91CD\u65B0\u8F93\u5165\uFF01\u003C\u002f\u0073\u0074\u0072\u006f\u006e\u0067\u003E\u003C\u002f\u0070\u003E\u000A\u003C\u0070\u003E\u003C\u0061\u0020\u0068\u0072\u0065\u0066\u003D\u0022\u0073\u0068\u0061\u0072\u0065\u0022\u003E\u8FD4\u56DE\u003C\u002f\u0061\u003E\u003C\u002f\u0070\u003E\u000A\u003C\u002f\u0062\u006f\u0064\u0079\u003E\u000A\u003C\u002f\u0068\u0074\u006d\u006c\u003E\u000A')
    else:
        c = {}
        c.update(csrf(req))
        return render_to_response('share.html', c)

def link(req):
    links = Link.objects.all()
    return render_to_response('link.html',{'links':links})

def api(req):
    accounts = Account.objects.filter(status='1',spdy='0')
    list = []
    for account in accounts:
        dist = {}
        dist['id'] = account.id
        dist['country'] = account.country
        dist['name'] = account.name
        dist['qr'] = str(account.qr)
        dist['api'] = account.api
        dist['online'] = account.is_on
        list.append(dist)
    return HttpResponse(json.dumps(list))
