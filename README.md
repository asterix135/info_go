#Webscraper - Scrapy

to execute the crawler, either:

1) call `execute_scrape.sh` from bash console

or 

a) Ensure that employees.txt and employee_numbers.txt have been deleted from your active directory
b) From the command line, enter the following two commands:

```bash
scrapy crawl org
scrapy crawl person
```

The first routine - `scrapy crawl org` - generates a list of employee numbers from departmental
listing pages.  This list is saved to the active directory as employee_numbers.txt and is used 
in the second routine.

The second routine - `scrapy crawl person` - pulls relevant contact information from individual
contact pages.  This accesses the file employee_numbers.txt and goes through all unique entries in
this list.
The results are saved in comma-delimited format in the file employees.txt

XPath guidance: http://www.w3schools.com/XPath/default.asp

Scrapy tutorial: http://doc.scrapy.org/en/latest/intro/tutorial.html#intro-tutorial

