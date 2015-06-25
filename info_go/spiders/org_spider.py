import scrapy
from scrapy.http import Request
import re

class InfoGoOrgSpider(scrapy.Spider):
    '''Spider that goes through all organization pages and pulls id numbers for employee info scraping'''
    name = "org"
    allowed_domains = ["infogo.gov.on.ca"]
    min_num = 589 # should be 2
    max_num = 591 # should be 7356

    def start_requests(self):
        for page in range(self.min_num, self.max_num):
            yield Request('http://www.infogo.gov.on.ca/infogo/office.do?actionType=telephonedirectory&unitId=%d' % page,
                    callback = self.parse)


    def parse(self, response):
        file_dest = open('employee_numbers.txt', 'a')

        for sel in response.xpath('//td[@class="content"]'):
            employee_id = response.xpath('//a[@class="employee"]/@href').extract()
            print "Employee id"
            print employee_id
            for item in employee_id:
                id_number = re.match("(.*)Employee\(\'(\d+)(.*)", str(item)).group(2)
                print id_number
                file_dest.write(id_number + '\n')
        file_dest.close()


