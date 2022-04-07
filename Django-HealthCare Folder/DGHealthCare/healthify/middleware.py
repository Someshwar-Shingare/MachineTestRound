from django.http import HttpResponse

class AppMaintainanaceMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        return HttpResponse('<h1>Currently Application is in maintainance stage,Please try after some time')



class ErrorMessageMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        return HttpResponse('<h1>Currently Application is in maintainance stage,Please try after some time')
    def process_exception(self,request,exception):
        return HttpResponse('<h1>Currently facing some technical issue, Please try after some time')



class DemoMiddleware(object):
    def __init__(self,get_response):
        self.get_response = get_response
    def __call__(self,request):
        print('First execution while sending the request')
        response = self.get_response(request)
        print('Second execution while getting the response')
        return response




