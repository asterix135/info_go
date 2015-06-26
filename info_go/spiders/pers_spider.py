import scrapy
from scrapy.http import Request
import re
import os.path

class InfoGoPersSpider(scrapy.Spider):
    name = "person"
    allowed_domains = ["infogo.gov.on.ca"]

    #activate when testing done
    # if os.path.exists('employee_numbers.txt'):
    #     employee_set = set(line.strip() for line in open('employee_numbers.txt'))
    # else:
    #     employee_set = set(['23895'])

    employee_set = set(['27293'])

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


            #testing stuff
            for cnt in range(len(employee_details)):
                print cnt
                print employee_details[cnt] + '\n'


            name_backward = re.match('(.*)\>(.*)\<(.*)', employee_details[0]).group(2)
            name_tokens = [token.strip() for token in name_backward.split(',')]
            person_name = name_tokens[0] + " " + name_tokens[1]

            phone = re.match('(.*)\>(.*)\<(.*)', employee_details[2]).group(2)
            title = re.match('(.*)\>(.*)\<(.*)', employee_details[8]).group(2)
            if re.search('@', email_extract[0]) != None:
                email = re.match('(.*)mailto:(.*?)\"', email_extract[0]).group(2)
            else:
                email = ''
            org_name = re.match('(.*)\>(.*)\<(.*)', org_name_extract[0]).group(2)

            hierarchy = org_name
            for layer in range(1, len(hierarchy_extract)-1):
                layer_name = re.match('(.*)\>(.*)\<(.*)', hierarchy_extract[layer]).group(2)
                hierarchy += " - " + layer_name


            print person_name, phone, title, email, org_name
            print hierarchy

            output_line = ('"' + person_name + '"' + ',' +
                            '"' + title + '"' + ',' +
                            '"' + phone + '"' + ',' +
                            '"' + email + '"' + ',' +
                            '"' + org_name + '"' + ',' +
                            '"' + hierarchy + '"')

            file_dest.write(output_line.encode('utf8') + '\n')

        file_dest.close()


