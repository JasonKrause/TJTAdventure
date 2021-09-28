class Dialog():
    #askText = "Hello, how are you?"
    #responseOptions = [(1,"I'm Good"),(2,"I want to crawl in hole"),(3,"I am angry!")]
    askText = "test?"
    responseOptions = [(1,"t1"),(2,"t2"),(3,"t3!")]

    def __init__(self,ask,respOpts):
        self.askText = ask
        self.responseOptions = respOpts

    def getAskText(self):
        return self.askText

    def getResponseOptions(self):
        return self.responseOptions

class Response():
    responseData = {}
    def getResponseData(self):
        return self.responseData
    def updateResponseData(self, key, value):
        self.responseData[key] = value