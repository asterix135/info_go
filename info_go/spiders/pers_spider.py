import scrapy
from scrapy.http import Request
import re
import os.path

class InfoGoPersSpider(scrapy.Spider):
    name = "person"
    allowed_domains = ["infogo.gov.on.ca"]
    if os.path.exists('employee_numbers.txt'):
        employee_set = set(line.strip() for line in open('employee_numbers.txt'))
    else:
        employee_set = set(['23895'])

    def start_requests(self):
        for page in self.employee_set:
            yield Request('http://www.infogo.gov.on.ca/infogo/employee.do?actionType=browse&Id=%s' % page,
                    callback = self.parse)

    def parse(self, response):
        file_dest = open('employees.txt', 'a')
        deleteme = response.xpath('//td[@class="content"]/font').extract()
        print "Deleteme"
        print deleteme
        file_dest.write('\n'.join(deleteme))

        for sel in response.xpath('//td[@class="content"]'):
            employee_details = response.xpath('//font').extract()
            hierarchy_details = response.xpath('//a[@href]').extract()
            #both of these are lists - need to extract info and regex it




            print "Employee details"
            print employee_details
            # for item in employee_id:
            #     #id_step0 = str(item)
            #     #print id_step0
            #     id_number = re.match("(.*)Employee\(\'(\d+)(.*)", str(item)).group(2)
            #     print id_number
            #     file_dest.write(id_number + '\n')
            #file_dest.write('\n'.join(employee_id))
            #file_dest.write('\n')

