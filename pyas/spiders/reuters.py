import scrapy


class MySpider(scrapy.Spider):
    name = "reuters"
    start_urls = ['http://www.reuters.com/news/archive']

    def parse(self, response):
        for href in response.css(
                "a[href^='/article']::attr(href)"):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_article)

    def parse_article(self, response):
        title = "".join(response.css(
            'h1.article-headline::text').extract())
        content = "\n".join(response.css(
            'span[id=articleText] p::text').extract())
        yield {
            'title': title,
            'content': content,
            'link': response.url,
        }
