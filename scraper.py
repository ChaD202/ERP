import scrapy
from scrapy.crawler import CrawlerProcess
import csv
import os
import random

#reference_data = str(input(" >>> ENTER THE FILENAME OF YOUR REFERENCE CSV (NO .CSV EXTENSION)"))


class scraper(scrapy.Spider):
    name = "est"

    start_urls = ["https://www.scottishepcregister.org.uk/"]

    custom_settings = {"FEEDS": {
                            "scraped_data.csv": {"format": "csv",
                                                 "encoding": "utf-8-sig"}
                        },
                       "LOG_ENABLED": False,
                       "ROBOTSTXT_OBEY": False,
                       "DEFAULT_REQUEST_HEADERS": {
                           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                           'accept-encoding': 'gzip, deflate, br',
                           'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                           'cookie': 'wrawrsatrsrweasrdxsfw2ewasjret=; wrawrsatrsrweasrdxsf=; captchaCookie=1; __ControllerTempData=AAEAAAD/////AQAAAAAAAAAEAQAAAOIBU3lzdGVtLkNvbGxlY3Rpb25zLkdlbmVyaWMuRGljdGlvbmFyeWAyW1tTeXN0ZW0uU3RyaW5nLCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldLFtTeXN0ZW0uT2JqZWN0LCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldXQQAAAAHVmVyc2lvbghDb21wYXJlcghIYXNoU2l6ZQ1LZXlWYWx1ZVBhaXJzAAMAAwgWU3lzdGVtLk9yZGluYWxDb21wYXJlcgjmAVN5c3RlbS5Db2xsZWN0aW9ucy5HZW5lcmljLktleVZhbHVlUGFpcmAyW1tTeXN0ZW0uU3RyaW5nLCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldLFtTeXN0ZW0uT2JqZWN0LCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldXVtdBAAAAAkCAAAAAwAAAAkDAAAABAIAAAAWU3lzdGVtLk9yZGluYWxDb21wYXJlcgEAAAALX2lnbm9yZUNhc2UAAQEHAwAAAAABAAAAAwAAAAPkAVN5c3RlbS5Db2xsZWN0aW9ucy5HZW5lcmljLktleVZhbHVlUGFpcmAyW1tTeXN0ZW0uU3RyaW5nLCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldLFtTeXN0ZW0uT2JqZWN0LCBtc2NvcmxpYiwgVmVyc2lvbj00LjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPWI3N2E1YzU2MTkzNGUwODldXQT8////5AFTeXN0ZW0uQ29sbGVjdGlvbnMuR2VuZXJpYy5LZXlWYWx1ZVBhaXJgMltbU3lzdGVtLlN0cmluZywgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XSxbU3lzdGVtLk9iamVjdCwgbXNjb3JsaWIsIFZlcnNpb249NC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1iNzdhNWM1NjE5MzRlMDg5XV0CAAAAA2tleQV2YWx1ZQECBgUAAAALVmFsaWRTZWFyY2gIAQEB+v////z///8GBwAAAAVUYW5kQwgBAQH4/////P///wYJAAAADEVycm9yTWVzc2FnZQYKAAAANkluY29ycmVjdCB2ZXJpZmljYXRpb24gdGV4dCBlbnRlcmVkLiBQbGVhc2UgdHJ5IGFnYWluLgs=',
                           'dnt': '1',
                           'referer': 'https://www.scottishepcregister.org.uk/CustomerFacingPortal/EPCPostcodeSearchResults?pageNumber=2&pageRecordCount=10&sortBy=InspectionDate&sortDirection=Ascending&postcode=vpWROC8%2FDz7xx7mlcZrcca0oW39CXDsBke7ZJXRA%2BZ0%3D&propertytype=-1',
                           'sec-fetch-dest': 'document',
                           'sec-fetch-mode': 'navigate',
                           'sec-fetch-site': 'same-origin',
                           'sec-fetch-user': '?1',
                           'upgrade-insecure-requests': '1',
                           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
                        }}

    def __init__(self, *args, **kwargs):
        super(scraper, self).__init__(*args, **kwargs)
        self.proxy_pool = ['cjskitwk-dest:fx96whhbpj4b@209.127.191.180:80', 'cjskitwk-dest:fx96whhbpj4b@45.130.255.198:80', 'cjskitwk-dest:fx96whhbpj4b@45.130.255.243:80', 'cjskitwk-dest:fx96whhbpj4b@185.164.56.20:80', 'cjskitwk-dest:fx96whhbpj4b@45.130.255.147:80', 'cjskitwk-dest:fx96whhbpj4b@45.95.96.132:80', 'cjskitwk-dest:fx96whhbpj4b@45.95.96.237:80', 'cjskitwk-dest:fx96whhbpj4b@45.95.96.187:80', 'cjskitwk-dest:fx96whhbpj4b@45.94.47.66:80', 'cjskitwk-dest:fx96whhbpj4b@193.8.56.119:80']

        with open('postcodes.csv', newline='') as f:
            reader = csv.reader(f)
            self.postcode_data = list(reader)

        self.n = 0

    def parse(self, response):
        for postcode in self.postcode_data:
            form_data = {'Postcode': postcode[0], 'CaptchaDeText': 'd30e27ccf2bd4d8b8bcca06033ba6a5b',
                         'CaptchaInputText': '9ywnq3'}

            proxy = random.choice(self.proxy_pool)

            yield scrapy.http.FormRequest('https://www.scottishepcregister.org.uk/CustomerFacingPortal/EPCPostcodeSearchResults', formdata=form_data, meta={'proxy': proxy}, callback=self.parse_results)

    def parse_results(self, response):
        addresses = [u.strip().replace(r"\r\n", "") for u in response.xpath('//tr/td[1]/text()').extract()]
        RRN = [u.strip().replace(r"\r\n", "") for u in response.xpath('//tr/td[2]/text()').extract()]
        pdf_links = ["https://www.scottishepcregister.org.uk{u}".format(u=u) for u in response.xpath('//tr/td/a/@href').extract()]

        data = list(zip(addresses, RRN, pdf_links))

        for d in data:
            path = "{p}.pdf".format(p=d[1])
            proxy = random.choice(self.proxy_pool)
            yield scrapy.Request(d[2], meta={'path': path, 'proxy': proxy}, callback=self.save_pdf)
            yield {'Address': d[0], 'RRN': d[1], 'PDF URL': d[2]}

        next_page = ["https://www.scottishepcregister.org.uk{u}".format(u=u) for u in response.xpath('//li[contains(., "Next")]/a/@href').extract()]

        if len(next_page) > 0:
            yield scrapy.Request(next_page[0], meta=response.meta, callback=self.parse_results)

        else:
            self.n += 1
            print(" >> SCRAPED {n} POSTCODES".format(n=self.n))

    def save_pdf(self, response):
        if not os.path.exists('pdfs'):
            os.makedirs('pdfs')

        if len(response.body) > 0:
            print(' >> Saving PDF to pdfs/{p}'.format(p=response.meta['path']))
            with open("pdfs/{p}".format(p=response.meta['path']), 'wb') as f:
                f.write(response.body)

        else:
            print(' >> Unable to save PDF to pdfs/{p}'.format(p=response.meta['path']))


process = CrawlerProcess()

process.crawl(scraper)
process.start()
