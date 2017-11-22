

from gtkml.gtkml.stdlib.http_service import HttpService
from gtkml.gtkml.stdlib.object_accessor import ObjectAccessor, OBJECT_POOL



class GtkQueryObject:
    def __init__(self):
        self.http = HttpService()
        self.accessor = ObjectAccessor()

    def __call__(self, *args, **kwargs):
        return self.accessor._get_all()

    def get(self, url):
        return self.http.GET(url)

    def post(self, url):
        return self.http.POST(url)

_ = GtkQueryObject()

if __name__ == '__main__':
    _("asd", 4)
    url1 = "http://httpbin.org/get"
    url2 = "http://httpbin.org/post"
    data1 = _.get(url1)
    data2 = _.post(url2)

    print(data1)
    print()
    print(data2)