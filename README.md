Crawling posted Software Engineering jobs from https://wuzzuf.net

NOTE: Before crawling i checked robots.txt and there's no disallows 

What does this spider specifacally do?
- Get all aviable jobs links and crawl some of this vacancies fields:
[job_title, job_url, posted_on, job_roles, keywords, company_name, company_location, company_website, company_industries]
- There are other fields like job description and requirements and other fields
- Write crawled results in csv file


To run this spider run:
- For csv format: scrapy crawl jobs -o jobs.csv -t csv 
- For JL fomat: scrapt crawl jobs -o jobs.jl


I find these tutorials good ones to start with
- https://www.youtube.com/watch?v=4I6Xg6Y17qs&list=PLRYJevdS4CBV1QTNm9UBXbg7mizpkQbjT
- https://www.youtube.com/watch?v=758KrjCgkN8&list=PL51BA5190961CFEE3

ToDo:
- Invest more time on Scrapy Framework and its concepts like pipelines and extractors
- Read Scrapy's documentation
- Add more fields for a job
- Split jobs to be written on multiple files for example: jobs per company or 
														  jobs per industry or 
														  jobs per location

- Index these crawled data into DB (would do it in another repo and use these spider) 
- Build a Job Recommendation Engine

- Whenever something come to mind i'll add it to this list
