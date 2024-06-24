BOT_NAME = "nashdomrf"

SPIDER_MODULES = ["nashdomrf.spiders"]
NEWSPIDER_MODULE = "nashdomrf.spiders"

ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 1
CONCURRENT_REQUESTS = 8

ITEM_PIPELINES = {
    "nashdomrf.pipelines.JsonWriterPipeline": 300,
}