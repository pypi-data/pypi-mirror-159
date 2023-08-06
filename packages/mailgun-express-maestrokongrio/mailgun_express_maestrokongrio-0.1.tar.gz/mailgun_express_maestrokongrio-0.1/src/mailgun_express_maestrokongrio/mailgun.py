from xml.dom.pulldom import default_bufsize
import requests

class SimpleMailgun:

    domain=""
    apikey=""
    default_from=""

    def __init__(self,_domain,_apikey,_defaultfrom):
        domain = _domain
        apikey = _apikey
        default_from = _defaultfrom

    def get_endpoint(self):
        return "https://api.mailgun.net/v3/" + self.domain + "/messages"

    def send_simple_message(self,to,name,subject,template,variables):
	    return requests.post(
		self.get_endpoint(),
		auth=("api", self.apikey),
		data={"from": self.default_from,
			"to": name + "<" + to + ">",
			"subject": subject,
			"template": template,
            "h:X-Mailgun-Variables": variables})