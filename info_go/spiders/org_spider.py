import scrapy

class InfoGoOrgSpider(scrapy.Spider):
    name = "org"
    allowed_domains = ["infogo.gov.on.ca"]
    start_urls = [
        #"http://www.infogo.gov.on.ca/infogo/office.do?actionType=telephonedirectory&unitid=20",
        #"http://www.infogo.gov.on.ca/infogo/employee.do?actionType=browse&id=10272",
        #"http://www.infogo.gov.on.ca/infogo/employee.do?actionType=browse&id=19667",
        "http://www.infogo.gov.on.ca/infogo/office.do?actionType=telephonedirectory&unitId=294"
    ]

    def parse(self, response):
        #rem'd out stuff just pulls the file and saves it by code number
        #pulls the final number as filename
        #filename = response.url.split("=")[-1]
        #with open(filename, 'wb') as f:
        #    f.write(response.body)

#        employee_name = sel.xpath('//TD class="employeeInfo"')

        #for sel in response.xpath('//body/center/div[3]/div/form/table/tr/td/table/tr/td/table/tr/td/ul/li/a'):
        #    employee_name = sel.xpath('/text()').extract()
        #    employee_id = sel.xpath('').extract()
        #    print employee_name, employee_id

        employee_name = response.xpath('//body/center/div[3]/div/form/table/tr/td/table/tr/td/table/tr/td/ul/li/a/text()').extract()
        employee_id = response.xpath('//body/center/div[3]/div/form/table/tr/td/table/tr/td/table/tr/td/ul/li/a').extract()
        print employee_name, employee_id


                # employee_name = scrapy.Field
                # employee_info = scrapy.Field
                # employee_id = scrapy.Field
