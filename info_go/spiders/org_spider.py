import scrapy
from scrapy.http import Request

class InfoGoOrgSpider(scrapy.Spider):
    name = "org"
    allowed_domains = ["infogo.gov.on.ca"]
    min_num = 589 # should be 2
    max_num = 591 # should be 7356
    start_urls = [
        #"http://www.infogo.gov.on.ca/infogo/office.do?actionType=telephonedirectory&unitid=250",
        #"http://www.infogo.gov.on.ca/infogo/employee.do?actionType=browse&id=10272",
        #"http://www.infogo.gov.on.ca/infogo/employee.do?actionType=browse&id=19667",
        "http://www.infogo.gov.on.ca/infogo/office.do?actionType=telephonedirectory&unitId=2"
    ]

    def start_requests(self):
        for page in range(self.min_num, self.max_num):
            yield Request('http://www.infogo.gov.on.ca/infogo/office.do?actionType=telephonedirectory&unitId=%d' % page,
                    callback = self.parse)


    def parse(self, response):

        for sel in response.xpath('//td[@class="employeeInfo"]'):
            employee_id = response.xpath('//a[@class="employee"]/@href').extract()
            print "Employee id"
            print employee_id
            return employee_id

        # this part fails
        # for sel in response.path('//a[@class="employee"]'):
        #     employee_id = response.xpath('@href').extract
        #     print employee_id

        # some kind of write to file
        #filename = response.url.split("=")[-1]
        #with open(filename, 'wb') as f:
        #    f.write(response.body)

