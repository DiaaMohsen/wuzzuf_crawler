# -*- coding: utf-8 -*-
import scrapy
from ..items import JobItem

class JobsSpider(scrapy.Spider):
	name = 'jobs'
	allowed_domains = ['wuzzuf.net']
	start_urls = ['https://wuzzuf.net/a/Software-Development-Jobs-in-Egypt?start=0']

	def parse(self, response):
		for u in response.css(".mobile-job-link"):
			job_url = u.css("::attr(href)").extract_first()
			yield scrapy.Request(job_url, callback=self.parse_single_job_page)
		

		next_page_selector = response.css(".pag-next a::attr(href)")
		# print "NEXT:", next_page_selector.extract_first()
		if next_page_selector:
			next_page_link = next_page_selector.extract_first()
			yield scrapy.Request(next_page_link)

	def parse_single_job_page(self, response):

		item = JobItem()

		item['job_title'] = (response.css(".job-title::text").extract()[1] or "").strip()
		item['job_url'] = response.url

		item['posted_on'] = (response.css(".job-post-date::attr(title)").extract_first() or "").strip()
		item['job_roles'] = response.css(".labels-wrapper a.label span::text").extract() or []
		item['keywords'] = response.css(".labels-wrapper meta::attr(content)").extract() or []

		item['company_name'] = (response.css(".job-company-name::text").extract_first() or "").strip()
		item['company_location'] = (response.css(".job-company-location meta::attr(content)").extract_first() or "").strip()
		item['company_website'] = (response.css(".job-company-name::attr(href)").extract_first() or "").strip()
	
		company_industries = response.css(".industries a::text").extract() or []
		item['company_industries'] = list(set([l.strip() for l in company_industries]))

		yield item