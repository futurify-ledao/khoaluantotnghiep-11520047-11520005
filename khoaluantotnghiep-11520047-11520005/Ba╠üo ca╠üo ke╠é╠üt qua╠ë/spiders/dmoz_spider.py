import scrapy
from scrapy.spider import Spider
from scrapy.http import Request, Response
from tutorial.items import DmozItem

#class DmozSpider(scrapy.Spider):
class DmozSpider(Spider):
        name = "dmoz"
        allowed_domains = ["priceonline.hsc.com.vn"]
        start_urls = [
            "http://priceonline.hsc.com.vn/Process.aspx?Type=MS"
        ]
        download_delay = 10
        def start_requests(self):
            yield Request('http://priceonline.hsc.com.vn/Process.aspx?Type=MS',
                          cookies={'ASP.NET_SessionId':'cvg20tmdr0uqhs45fdjbza45',
                                   '_kieHoSESF':'HAG|GTN|GTT|HAG|HAH|HAI|HAP|HAR|HAS|HAX|HBC|HCM|HDC|HDG|HHS|HLG|HMC|HNG|HOT|HPG|HQC|HRC|HSG|HT1|HTI|HTL|HTV|HU1|HU3|HVG|HVX|ICF|IDI|IJC|IMP|ITA|ITC|ITD|JVC|KAC|KBC|KDC|KDH|KHA|KHP|KMR|KSA|KSB|KSH|KSS|'})

            for url in self.start_urls:
                yield Request(url, callback=self.parse)
        
        def parse(self, response):
            item = DmozItem()
            item['data'] = response.body
            yield item