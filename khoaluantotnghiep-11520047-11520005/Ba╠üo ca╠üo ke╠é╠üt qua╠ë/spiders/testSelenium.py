from demod3js.items import Demod3JsItem
from scrapy.spiders import CrawlSpider
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import copy

attributeList = ["name","region","income","population","lifeExpectancy"]

class RunnerSpider(CrawlSpider):
    name = 'getData'
    allowed_domains = ['ssi.com.vn']
    start_urls = ['http://banggia2.ssi.com.vn/hose.aspx']
    
    def __init__(self):
        self.driver = webdriver.Firefox()
    
    def parse(self, response):
        items = []
        #self.driver.implicitly_wait(10)
        self.driver.get(response.url)
        j=1
        tr_tags = self.driver.find_elements_by_xpath('//*[@id="tableQuote"]/tbody/tr')
        for tr in tr_tags:
            
            item = Demod3JsItem()
            item['region'] = 'Europe & Central Asia'
            code = self.driver.find_element_by_xpath('//*[@id="tableQuote"]/tbody/tr['+str(j)+']/td[1]')
            item['name'] = code.text
            
            starting_year = 1800
            count = 2
            
            total_income = []
            while (count < 10):
                income = self.driver.find_element_by_xpath('//*[@id="tableQuote"]/tbody/tr['+str(j)+']/td['+str(count)+']')
                tmp_income = []
                tmp_income.append(starting_year + (count-2)*5)
                tmp_income.append(income.text)
                total_income.append(list(tmp_income))
                count += 1
        
            item['income'] = total_income
            
            starting_year = 1800
            
            total_population = []
            while (count < 19):
                population = self.driver.find_element_by_xpath('//*[@id="tableQuote"]/tbody/tr['+str(j)+']/td['+str(count)+']')
                tmp_population = []
                tmp_population.append(starting_year + (count - 10)*5)
                tmp_population.append(population.text)
                total_population.append(list(tmp_population))
                count += 1
    
            item['population'] = total_population
        
            starting_year = 1800
            
            total_lifeExpectancy = []
            while (count < 28):
                lifeExpectancy = self.driver.find_element_by_xpath('//*[@id="tableQuote"]/tbody/tr['+str(j)+']/td['+str(count)+']')
                tmp_lifeExpectancy = []
                tmp_lifeExpectancy.append(starting_year + (count - 19)*5)
                tmp_lifeExpectancy.append(lifeExpectancy.text)
                total_lifeExpectancy.append(list(tmp_lifeExpectancy))
                count += 1
        
            item['lifeExpectancy'] = total_lifeExpectancy
            
            items.append(item)
            j+=1
            if j == 21:
                break

        self.driver.close()
        return items