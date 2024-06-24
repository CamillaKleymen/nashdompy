import scrapy
from nashdomrf.items import RealtyItem

class RealtySpider(scrapy.Spider):
    name = 'realty'
    allowed_domains = ['xn--80az8a.xn--d1aqf.xn--p1ai']
    start_urls = ['https://xn--80az8a.xn--d1aqf.xn--p1ai/сервисы/каталог-новостроек/список-объектов/список?place=0-1&objStatus=0']

    def parse(self, response):
        for item in response.css('div.NewBuildingItem__Wrapper-sc-o36w9y-0'):
            realty_item = RealtyItem()
            
            realty_item['title'] = item.css('a.NewBuildingItem__MainTitle-sc-o36w9y-6::text').get()
            realty_item['address'] = item.css('p.NewBuildingItem__Text-sc-o36w9y-7::text').get()
            realty_item['id'] = item.css('p.NewBuildingItem__ObjectID-sc-o36w9y-8::text').get().replace('ID: ', '')
            realty_item['completion_date'] = item.css('div.NewBuildingItem__InfoValue-sc-o36w9y-11::text').get()
            realty_item['developer'] = item.css('div.NewBuildingItem__InfoValue-sc-o36w9y-11::text')[-1].get()

            detail_url = item.css('a.NewBuildingItem__MainTitle-sc-o36w9y-6::attr(href)').get()
            yield scrapy.Request(response.urljoin(detail_url), callback=self.parse_detail, meta={'item': realty_item})

        next_page = response.css('a.Pagination__PageLink-sc-pbq2he-2[aria-label="Next page"]::attr(href)').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_detail(self, response):
        item = response.meta['item']
        
        item['company_group'] = response.css('div.Row__Value-sc-13pfgqd-2:contains("Группа компаний") + div::text').get()
        item['project_publication_date'] = response.css('div.Row__Value-sc-13pfgqd-2:contains("Дата публикации проекта") + div::text').get()
        item['key_handover_date'] = response.css('div.Row__Value-sc-13pfgqd-2:contains("Выдача ключей") + div::text').get()
        item['average_price_per_m2'] = response.css('div.Row__Value-sc-13pfgqd-2:contains("Средняя цена за 1 м²") + div::text').get()
        item['sold_out_percentage'] = response.css('div.Row__Value-sc-13pfgqd-2:contains("Распроданность квартир") + div::text').get()
        item['property_class'] = response.css('div.Row__Value-sc-13pfgqd-2:contains("Класс недвижимости") + div::text').get()
        item['apartments_count'] = response.css('div.Row__Value-sc-13pfgqd-2:contains("Количество квартир") + div::text').get()

        yield item