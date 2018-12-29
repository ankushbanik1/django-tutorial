from django.http import HttpResponse

class HttpResponseMixin(object):
    def render_to_httpresponse(self,json_data):
        return HttpResponse(json_data,content_type='application/json')