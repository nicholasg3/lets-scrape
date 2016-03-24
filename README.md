# lets-scrape
learn how to scrape a website (kickstarter) by example

### Introduction
http://docs.python-guide.org/en/latest/scenarios/scrape/

When you go to a website, your browser renders an HTML page for you to see. Sometimes, you can "look under the hood" and find the raw data powering the HTML, but other times the data is hidden. In these cases, depending on the structure of the HTML, web scraping may be a viable option to collect this data.

### Scraping may be considered for websites that:
* store information in a structured way (tables, divs)
* have a replicable form of pagination
* have text data rather than images
* don't have anti-bot software
* don't have other anti-scraping measures http://bj.meituan.com/category/

### Common issues encountered:
* the website undergoes a redesign, and tags no longer work
* edge cases: missing fields, "N/A"s, extra fields
* formatting issues (e.g., integers vs strings)
* data integrity / consistency issues
* data storage: the engineer must "know what (s)he's doing"
    * name fields clearly
    * track when processes are run
    * be careful when updating data via overwriting

### Alternatives to web scraping:
* finding what loads the webpage's data, and loading it directly
* using a website's API (e.g. http://open.fda.gov vs. http://www.fda.gov/)

### Scrape responsibly
* rate limit yourself with things like `time.sleep()`
* read the website's terms of service
* minimize the risk of compromising your IP - use [proxies and user agents](http://willdrevo.com/using-a-proxy-with-a-randomized-user-agent-in-python-requests/)