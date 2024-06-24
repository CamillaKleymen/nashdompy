import scrapy

class RealtyItem(scrapy.Item):
    title = scrapy.Field()
    address = scrapy.Field()
    id = scrapy.Field()
    completion_date = scrapy.Field()
    developer = scrapy.Field()
    company_group = scrapy.Field()
    project_publication_date = scrapy.Field()
    key_handover_date = scrapy.Field()
    average_price_per_m2 = scrapy.Field()
    sold_out_percentage = scrapy.Field()
    property_class = scrapy.Field()
    apartments_count = scrapy.Field()