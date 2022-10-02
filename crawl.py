import scrapy


class PostCrawl(scrapy.Spider):
    name = "post_crawl"
    start_urls = ["https://habr.com/ru/all/"]

    def parse(self, response):
        post_url = response.css("a.tm-article-snippet__title-link::attr(href)")
        yield from response.follow_all(post_url, self.post_info)


        next_page = response.xpath("//a[@id='pagination-next-page']/@href")
        yield from response.follow_all(next_page, self.parse)
    




    def post_info(self, response):
        tags = response.css("div.tm-article-presenter__meta-list ul.tm-separated-list__list li a::text").getall()
        yield {
            "title":response.css("h1.tm-article-snippet__title span::text").get(),
            "author":response.css("span.tm-user-info__user a::text").get().strip(),
            "tag":tags
        }








