import scrapy
from scrapy.http import Request
import re

class InfoGoPersSpider(scrapy.Spider):
    name = "person"
    allowed_domains = ["infogo.gov.on.ca"]
    employee_set = set(line.strip() for line in open('file.txt'))
    # min_num = 589 # should be 2
    # max_num = 591 # should be 7356

    def start_requests(self):
        for page in employee_set:
            yield Request('http://www.infogo.gov.on.ca/infogo/employee.do?actionType=browse&Id=%d' % page,
                    callback = self.parse)


    def parse(self, response):
        file_dest = open('employees.txt', 'a')

        for sel in response.xpath('//td[@class="employeeInfo"]'):
            employee_id = response.xpath('//a[@class="employee"]/@href').extract()
            print "Employee id"
            print employee_id
            for item in employee_id:
                #id_step0 = str(item)
                #print id_step0
                id_number = re.match("(.*)Employee\(\'(\d+)(.*)", str(item)).group(2)
                print id_number
                file_dest.write(id_number + '\n')
            #file_dest.write('\n'.join(employee_id))
            #file_dest.write('\n')

