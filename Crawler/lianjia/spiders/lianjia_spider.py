import scrapy
import sys
from lianjia.items import LianjiaItem

class LianjiaSpider(scrapy.Spider):
  reload(sys)
  sys.setdefaultencoding('utf-8')
  name = 'lianjia'
  allowed_domains = ["sh.lianjia.com"]
  start_urls = ["http://sh.lianjia.com/chengjiao/fengxian/"]

  def parse(self, response):
    for info in response.xpath('//div[@class="content"]/div[@class="m-list cj-list"]/ul/li'):
      try:
        item = LianjiaItem()
        item['community'] = info.xpath('div[@class="info"]/div[@class="info-table"]/div[@class="info-row"]/a/span/text()').extract()[0]
        item['otherInfo'] = info.xpath('div[@class="info"]/div[@class="info-table"]/div[@class="info-row"]/a/@title').extract()[0]
        item['room'] = item['otherInfo'].split(' ')[1]
        item['space'] = item['otherInfo'].split(' ')[2]
        item['floor'] = info.xpath('div[@class="info"]/div[@class="info-table"]/div[@class="info-row"]/div[@class="row1-text"]/text()').extract()[1].replace('\n','').replace('\t','')
        item['direction'] = info.xpath('div[@class="info"]/div[@class="info-table"]/div[@class="info-row"]/div[@class="row1-text"]/text()').extract()[2].replace('\n','').replace('\t','')
        item['decoration'] = info.xpath('div[@class="info"]/div[@class="info-table"]/div[@class="info-row"]/div[@class="row1-text"]/text()').extract()[3].replace('\n','').replace('\t','')
        item['date'] = info.xpath('div[@class="info"]/div[@class="info-table"]/div[@class="info-row"]/div[@class="info-col deal-item main strong-num"]/text()').extract()[0]
        item['totalPrice'] = info.xpath('div[@class="info"]/div[@class="info-table"]/div[@class="info-row"]/div[@class="info-col price-item main"]/span[@class="strong-num"]/text()').extract()[0]
        item['district'] = info.xpath('div[@class="info"]/div[@class="info-table"]/div[@class="info-row"]/span[@class="row2-text"]/a[2]/text()').extract()[0]
        item['unitPrice'] = info.xpath('div[@class="info"]/div[@class="info-table"]/div[@class="info-row"]/div[@class="info-col price-item minor"]/text()').extract()[0]
        item['href'] = "http://sh.lianjia.com" + info.xpath('div[@class="info"]/div[@class="info-table"]/div[@class="info-row"]/a/@href').extract()[0]
        yield item
      except Exception as err:
        self.log(str(err))
      
    #next page
    next_page = response.xpath('//div[@class="c-pagination"]/a[@gahref="results_next_page"]/@href')
    if next_page:
      url = response.urljoin(next_page[0].extract())
      yield scrapy.Request(url, self.parse)
