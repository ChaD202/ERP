import scrapy
from scrapy.crawler import CrawlerProcess


class scraper(scrapy.Spider):
    name = "est"

    start_urls = ["https://www.scottishepcregister.org.uk/"]

    def parse(self, response):
        form_data = {'Postcode': 'AB11 6JL', 'CaptchaDeText': 'd30e27ccf2bd4d8b8bcca06033ba6a5b',
                     'CaptchaInputText': '9ywnq3'}

        yield scrapy.http.FormRequest('https://www.scottishepcregister.org.uk/CustomerFacingPortal/EPCPostcodeSearchResults', formdata=form_data, callback=self.parse_results)

    def parse_results(self, response):
        print(response.body)

        addresses = [u.strip().replace(r"\r\n", "") for u in response.xpath('//tr/td[1]/text()').extract()]
        RRN = [u.strip().replace(r"\r\n", "") for u in response.xpath('//tr/td[2]/text()').extract()]
        pdf_links = ["https://www.scottishepcregister.org.uk/{u}".format(u=u) for u in response.xpath('//tr/td/a/@href').extract()]

        data = list(zip(addresses, RRN, pdf_links))

        for d in data:
            path = "{p}.pdf".format(p=d[1])
            yield scrapy.Request(d[2], meta={'path': path}, callback=self.save_pdf)
            yield {'Address': d[0], 'RRN': d[1], 'PDF URL': d[2]}

        next_page = ["https://www.scottishepcregister.org.uk/{u}".format(u=u) for u in response.xpath('//li[contains(., "Next")]/a/@href').extract()]

        if len(next_page) > 0:
            yield scrapy.Request(next_page[0], callback=self.parse_results)

    def save_pdf(self, response):
        self.logger.info('Saving PDF %s', response.meta['path'])
        with open(response.meta['path'], 'wb') as f:
            f.write(response.body)


process = CrawlerProcess(settings={
    "FEEDS": {
        "data.csv": {"format": "csv",
                     "encoding": "utf-8-sig"}
    },
    "DOWNLOAD_DELAY": 1,
    "LOG_ENABLED": True,
    "DEFAULT_REQUEST_HEADERS": {
        'cookie': 'wrawrsatrsrweasrdxsf=d30e27ccf2bd4d8b8bcca06033ba6a5b=WUBEw87awMZXw8L2Ini3Jp4SdZu4Uhl20IeeEgfBvyohT68FYykqQMf0cVQbUBDgsVLOvGLwwm6QrUncrWMTmF1djdNaFHaW+Srf37bESTfNnSnA4oN5PmG28qaiezNpJb5HkYV7hP7Nq91yAAABs+Mz2XWgVugyaV5VhkM1knXLG3yW0u6qeBi5UOLzZsIDWStna+6trwNhExItqWiFYg==; wrawrsatrsrweasrdxsfw2ewasjret='
    }
})

process.crawl(scraper)
process.start()
