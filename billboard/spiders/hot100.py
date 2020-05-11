# -*- coding: utf-8 -*-
import scrapy


class Hot100Spider(scrapy.Spider):
    name = 'hot100'
    allowed_domains = ['billboard.com']
    start_urls = ['http://billboard.com/charts/hot-100//']

    def start_requests(self):
        yield scrapy.Request(url='https://billboard.com/charts/hot-100/1984-08-04', callback=self.parse, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        })

    def roll_back_date(self, chart_date):
        if chart_date == date(1976, 7, 4):    
            previous_date = date(1976, 6, 26)

        elif chart_date == date(1962, 1, 6):
            previous_date = date(1961, 12, 25)

        else:
            roll_back = timedelta(weeks=1)
            previous_date = chart_date - roll_back

        previous_date = previous_date.strftime('%Y-%m-%d')
        return previous_date

    def parse(self, response):
        chart_date_string = (response.xpath("//button[starts-with(@class, 'date-selector__button')]/text()").get()).strip()
        chart_date = datetime.strptime(chart_date_string, '%B %d, %Y').date()
        
        hits = response.xpath("//li[starts-with(@class, 'chart-list__element')]")
        for hit in hits:
            yield {
                'date': chart_date,
                'title': hit.xpath(".//span[starts-with(@class, 'chart-element__information__song')]/text()").get(),
                'artist': hit.xpath(".//span[starts-with(@class, 'chart-element__information__artist')]/text()").get(),
                'rank': hit.xpath(".//span[@class='chart-element__rank__number']/text()").get(),
                'last_week': hit.xpath(".//span[contains(@class, 'chart-element__meta ')]/text()")[0].get(),
                'peak': hit.xpath(".//span[contains(@class, 'chart-element__meta ')]/text()")[1].get(),
                'weeks': hit.xpath(".//span[contains(@class, 'chart-element__meta ')]/text()")[2].get()
            }
        
        previous_date_string = self.roll_back_date(chart_date)
        next_page_url = f'https://billboard.com/charts/hot-100/{previous_date_string}'
        yield scrapy.Request(next_page_url, callback=self.parse, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        })



