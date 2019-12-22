# -*- coding: utf-8 -*-
import scrapy


class VacanciesSpider(scrapy.Spider):
    name = 'vacancies'
    allowed_domains = ['fontaneljobs.nl']
    start_urls = ['http://fontanel.nl/jobs/bedrijf/acato--2',
                'http://fontanel.nl/jobs/bedrijf/studio-funki',
                'http://fontanel.nl/jobs/bedrijf/stedelijkmuseumamsterdam'
                'http://fontanel.nl/jobs/bedrijf/protocow',
                'http://fontanel.nl/jobs/bedrijf/dotcontrol',
                'http://fontanel.nl/jobs/bedrijf/brandfighters--2',
                'http://fontanel.nl/jobs/bedrijf/aventus' ]

    def parse(self, response):

        d = {}

        d['company-name'] = response.xpath('//*[@id="main"]/article/div[1]/header/h3/text()').extract()[0] 
        d['url'] = response.xpath('//*[@id="main"]/article/div[1]/nav/a[2]/@href').get()
        
        long_description = response.xpath('//*[@id="main"]/article/div[1]/div//text()').getall()[1:-1]
        long_description = ' '.join([str(elem).strip() for elem in long_description]).replace('\xa0','') 
        
        d['long-description'] = long_description

        d['locations'] = []

        locs = response.xpath('//*[@id="maps"]/table/tr//td[2]/text()').extract()

        if len(locs) > 1:
            for l in response.xpath('//*[@id="maps"]/table/tr//td[2]/text()').extract():
                items = l.strip().replace("\n","|").split("|")

                loc = {}


                if(len(items)) == 1:
                    loc['city'] = items[0]
                
                if(len(items)) == 3:
                    loc = {}
                    loc['address'] = items[0]
                    loc['postal-code'] = items[1]
                    loc['city'] = items[2]

                d['locations'].append(loc)

        active_vacancies = response.xpath('//*[@id="active-vacancies"]/ul//li')
        old_vacancies = response.xpath('//*[@id="old-vacancies"]/ul//li')

        self.logger.info('act_vac: %s', len(active_vacancies))
        self.logger.info('old_vac: %s', len(old_vacancies))

        d['vacancies'] = []

        if len(active_vacancies) > 0:
            for item in active_vacancies:
                
                v = {}
        
                v['job-title'] = item.xpath('a/span[1]/text()').get().strip()
                v['job-description'] = item.xpath('a/span[2]/text()').get().strip().replace('\n',' ')
                v['job-type-location'] = item.xpath('a/span[3]/text()[1]').get().strip().replace('\n',' ')
                v['vacancy-date'] = item.xpath('a/span[3]/text()[3]').get().strip().replace('\n',' ') 

                d['vacancies'].append(v)



        if len(old_vacancies) > 0:
            for item in old_vacancies:
                
                v = {}
        
                v['job-title'] = item.xpath('a/span[1]/text()').get().strip()
                v['job-description'] = item.xpath('a/span[2]/text()').get().strip().replace('\n',' ')
                v['job-type-location'] = item.xpath('a/span[3]/text()[1]').get().strip().replace('\n',' ')
                v['vacancy-date'] = item.xpath('a/span[3]/text()[3]').get().strip().replace('\n',' ') 

                d['vacancies'].append(v)

        yield d