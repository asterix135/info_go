import scrapy
from scrapy.http import Request
import re
import os.path

class InfoGoPersSpider(scrapy.Spider):
    name = "person"
    allowed_domains = ["infogo.gov.on.ca"]

    #activate when testing done
    #if os.path.exists('employee_numbers.txt'):
    #    employee_set = set(line.strip() for line in open('employee_numbers.txt'))
    #else:
    #    employee_set = set(['23895'])

    employee_set = set(['23444'])

    def start_requests(self):
        for page in self.employee_set:
            yield Request('http://www.infogo.gov.on.ca/infogo/employee.do?actionType=browse&id=%s' % page,
                    callback = self.parse)

    def parse(self, response):
        file_dest = open('employees.txt', 'a')
        #file_dest.write('\n'.join(deleteme))

        for sel in response.xpath('//table[@title="employeeinfo_frame"]'):
            employee_details = response.xpath('//td[@class="content"]/font').extract()
            email_extract = response.xpath('//td[@class="content"]/a[@href]').extract()
            org_name_extract = response.xpath('//td[@class="content"]/ul/a[@href]').extract()
            hierarchy_extract = response.xpath('//td[@class="content"]//ul/a[@href]').extract()

            person_name = re.match('(.*)\>(.*)\<(.*)', employee_details[7]).group(2)
            phone = re.match('(.*)\>(.*)\<(.*)', employee_details[2]).group(2)
            title = re.match('(.*)\>(.*)\<(.*)', employee_details[8]).group(2)
            if re.search('@', email_extract[0]) != None:
                email = re.match('(.*)mailto:(.*?)\"', email_extract[0]).group(2)
            org_name = re.match('(.*)\>(.*)\<(.*)', org_name_extract[0]).group(2)

            hierarchy = org_name
            for layer in range(1, len(hierarchy_extract)-1):
                print hierarchy_extract[layer]
                layer_name = re.match('(.*)\>(.*)\<(.*)', hierarchy_extract[layer]).group(2)
                hierarchy += " - " + layer_name


            print person_name, phone, title, email, org_name
            print hierarchy

            print '\n'



            output_line = ('"' + person_name + '"' + ',' +
                            '"' + title + '"' + ',' +
                            '"' + phone + '"' + ',' +
                            '"' + email + '"' + ',' +
                            '"' + org_name + '"' + ',' +
                            '"' + hierarchy + '"')
            file_dest.write(output_line + '\n')


        file_dest.close()


