import requests

class HttpService:
    def __init__(self):
        pass

    def get(self, url):
        return requests.get(url)

    def post(self, url):
        return requests.post(url)

    def GET(self, url, coding="utf-8"):
        return self.get(url).content.decode(coding)

    def POST(self, url, coding="utf-8"):
        return self.post(url).content.decode(coding)

if __name__ == '__main__':
    http = HttpService()
    url1 = "http://httpbin.org/get"
    url2 = "http://httpbin.org/post"
    #data = http.get(url1)
    #print(data.content.decode("utf-8"))

    #pdata = http.post(url2)
    #print(pdata.content.decode("utf-8"))

    data = http.GET(url1)
    pdata = http.POST(url2)

    print(data)
    print(pdata)