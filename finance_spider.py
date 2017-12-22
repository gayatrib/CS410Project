import scrapy


class AuthorSpider(scrapy.Spider):
    name = 'financeforums'

    start_urls = ['http://www.thefinanceforums.com/']

    def parse(self, response):
	link='forumdisplay.php?'
        # follow links to forum pages
        for href in response.xpath('//div/a[@href]/@href').extract():
	    #print(href)
	    if link in href:
                yield response.follow(href, self.parse_forumpage)

    def parse_forumpage(self, response):
        # follow links to forum pages
	finaltext = " "
	finaldate = " "
	finaltime = " "
	finalviews = " "
	finalreplies = " "
	for tr in response.xpath('//tr'):
		for text in tr.xpath('.//td[@id]/div/a[@href]/text()').extract():
		    finaltext = text
	    	    #print(text)
	    	    #yield {
                	#'text': finaltext,
            	    #}
	   	for date in tr.xpath('.//td[@class="alt2"]/div/text()').extract():
	    	    #print(date)
		    date = date.replace('\n','')
		    date = date.replace('\t','')
		    date = date.replace('\r','')
		    date = date.replace(' ','')
		    if date and "by" not in date:
			finaldate = date
			#yield {
                	#	'date': finaldate,
            	    #}	
		for time in tr.xpath('.//td[@class="alt2"]/div/span[@class="time"]/text()').extract():
		    finaltime = time
	    	    #print(time)
	    	    #yield {
                	#'time': finaltime,
            	    #}
		for views in tr.xpath('.//td[@class="alt2"]/text()').extract():
		    views = views.replace('\n','')
		    views = views.replace('\t','')
		    views = views.replace('\r','')
		    if views:
		    	finalviews = views
	    	    #print(views)
	    	    	#yield {
                	#	'views': finalviews,
            	    	#}
		for replies in tr.xpath('.//td[@class="alt1"]/a[@href][@onclick]/text()').extract():
		    replies = replies.replace('Last','')
		    replies = replies.replace('>','')
		    replies = replies.replace(' ','')
		    if replies:
		    	finalreplies = replies
	    	    #print(replies)
	    	    	#yield {
                	#	'replies': finalreplies,
            	    	#}
	    	    if finaltext and finaldate and finaltime and finalviews and finalreplies:
		    	yield {
				'text': finaltext,
                		'date': finaldate,
				'time': finaltime,
				'views': finalviews,
				'replies': finalreplies,
            	 	}	
	for href in response.xpath('//tr/td[@class="alt1"]/a[contains(@title,"Next Page")]/@href').extract():
		yield response.follow(href, self.parse_forumpage)