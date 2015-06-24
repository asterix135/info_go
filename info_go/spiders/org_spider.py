import scrapy
from scrapy.http import Request
import re

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
        file_dest = open('file.txt', 'a')

        for sel in response.xpath('//td[@class="employeeInfo"]'):
            employee_id = response.xpath('//a[@class="employee"]/@href').extract()
            print "Employee id"
            print employee_id
            for item in employee_id:
                id_step0 = str(item)
                print id_step0
                id_step1 = re.search("browseEmployee\(\'(\n*)", id_step0)
                id_step2 = id_step1.group(1)
                print id_step2

            id_step0 = str(employee_id[0])
            print id_step0
            id_step1 = re.search("browseEmployee\(\'(\n*)", employee_id[0])
            id_number = id_step1.group(1)
            print id_number
            #file_dest.write('\n'.join(employee_id))
            file_dest.write(id_number)
            #return employee_id
        file_dest.write('\n')
        # this part fails
        # for sel in response.path('//a[@class="employee"]'):
        #     employee_id = response.xpath('@href').extract
        #     print employee_id

        # some kind of write to file
        #filename = response.url.split("=")[-1]
        #with open(filename, 'wb') as f:
        #    f.write(response.body)

