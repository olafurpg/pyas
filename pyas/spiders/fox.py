import scrapy


class MySpider(scrapy.Spider):
    name = "fox"
    start_urls = ['http://www.foxnews.com/world/terrorism/index.html']

    def parse(self, response):
        for href in response.css(
                ".article-ct a[href^='http://www.foxnews.com']::attr(href)"):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_article)

    def parse_article(self, response):
        title = "".join(response.css(
            'h1[itemprop=headline]::text').extract())
        content = "\n".join(response.css(
            'div[itemprop=articleBody] p::text').extract())
        yield {
            'title': title,
            'content': content,
            'link': response.url,
        }
