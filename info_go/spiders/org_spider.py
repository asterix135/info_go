import scrapy
from scrapy.http import Request
import re

class InfoGoOrgSpider(scrapy.Spider):
    '''Spider that goes through all organization pages and pulls id numbers for employee info scraping'''
    name = "org"
    allowed_domains = ["infogo.gov.on.ca"]
    min_num = 2 # should be 2
    max_num = 7356 # should be 7356

    def start_requests(self):
        for page in range(self.min_num, self.max_num + 1):
            yield Request('http://www.infogo.gov.on.ca/infogo/office.do?actionType=telephonedirectory&unitId=%d' % page,
                    callback = self.parse)


    def parse(self, response):
        file_dest = open('employee_numbers.txt', 'a')

        #for sel in response.xpath('//td[@class="content"]'):
        for sel in response.xpath('//body'):
            employee_id = response.xpath('//a[@class="employee"]/@href').extract()
            # print "Employee id"
            # print employee_id
            for item in employee_id:
                id_number = re.match("(.*)Employee\(\'(\d+)(.*)", str(item)).group(2)
                file_dest.write(id_number.encode('utf-8') + '\n')
        file_dest.close()


