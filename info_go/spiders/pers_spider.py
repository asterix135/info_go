import scrapy
from scrapy.http import Request
import re
import os.path

class InfoGoPersSpider(scrapy.Spider):
    name = "person"
    allowed_domains = ["infogo.gov.on.ca"]

    #activate when testing done

    if os.path.exists('employee_numbers.txt'):
        employee_set = set(line.strip() for line in open('employee_numbers.txt'))
    else:
        employee_set = set(['23895'])

    # test set

    # employee_set = set(['23895'])

    def start_requests(self):
        for page in self.employee_set:
            yield Request('http://www.infogo.gov.on.ca/infogo/employee.do?actionType=browse&id=%s' % page,
                    callback = self.parse)

    def parse(self, response):
        file_dest = open('employees.txt', 'a')

        for sel in response.xpath('//table[@title="employeeinfo_frame"]'):
            employee_details = response.xpath('//td[@class="content"]/font').extract()
            email_extract = response.xpath('//td[@class="content"]/a[@href]').extract()
            org_name_extract = response.xpath('//td[@class="content"]/ul/a[@href]').extract()
            hierarchy_extract = response.xpath('//td[@class="content"]//ul/a[@href]').extract()

            #testing stuff

            # print '\n'
            # print email_extract
            # print len(email_extract)
            # print '\n'

            # for cnt in range(len(employee_details)):
            #     print cnt
            #     print employee_details[cnt] + '\n'

            # end of testing stuff

            name_backward = re.match('(.*)b\>(.*)\</b(.*)', employee_details[0]).group(2)
            name_tokens = [token.strip() for token in name_backward.split(',')]
            person_name = name_tokens[1] + " " + name_tokens[0]

            phone = re.match('(.*)\>(.*)\<(.*)', employee_details[2]).group(2)

            title_ref_no = len(employee_details) - 6

            title_test = re.match('(.*)\>(.*)\<(.*)', employee_details[title_ref_no]).group(2)
            title_test_tokens = [token.strip() for token in title_test.split()]
            if name_tokens[0] == title_test_tokens[-1]:
                title = re.match('(.*)\>(.*)\<(.*)', employee_details[title_ref_no + 1]).group(2)
            else:
                title = title_test

            if len(email_extract) == 0:
                email = ''
            elif re.search('@', email_extract[0]) != None:
                email = re.match('(.*)mailto:(.*?)\"', email_extract[0]).group(2)
            else:
                email = ''

            org_name = re.match('(.*)\>(.*)\<(.*)', org_name_extract[0]).group(2)

            hierarchy = org_name
            for layer in range(1, len(hierarchy_extract)-1):
                layer_name = re.match('(.*)\>(.*)\<(.*)', hierarchy_extract[layer]).group(2)
                hierarchy += " - " + layer_name

            #testing stuff
            # print person_name, phone, title, email, org_name
            # print hierarchy

            output_line = ('"' + person_name + '"' + ',' +
                            '"' + title + '"' + ',' +
                            '"' + phone + '"' + ',' +
                            '"' + email + '"' + ',' +
                            '"' + org_name + '"' + ',' +
                            '"' + hierarchy + '"')

            file_dest.write(output_line.encode('utf-8') + '\n')

        file_dest.close()


