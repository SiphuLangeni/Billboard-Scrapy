## Web Scraping with Scrapy

Scrapy is a popular Python framework used for efficient web scraping. In this short project, I have created a basic spider to crawl the **Billboard Hot 100** charts from inception until now.

From August 4, 1958 until December 25 1961, charts were catalogued on Monday. They were subsequently catalogued on Saturday. A method was created to use a previous date string to identify the url of the previous chart. 

I have decided that I want to scrape the following data from each week's chart:
* chart date
* song title
* artist
* current week’s rank
* previous week’s rank
* peak position
* number of weeks on the charts

A blog post about the process can be found [here](https://towardsdatascience.com/web-scraping-with-scrapy-8071fd627051).

Scrapy documentation can be found [here](https://docs.scrapy.org/en/latest/).

