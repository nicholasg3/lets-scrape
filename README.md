# lets-scrape
learn how to scrape a website (kickstarter) by example

### Introduction

When you go to a website, your browser renders an HTML page for you to see. Sometimes, you can "look under the hood" and find the raw data powering the HTML, but other times the data is hidden. In the latter case, you may be able to use web scraping to collect this data.
* non-nerdy intro to the DOM: https://css-tricks.com/dom/
* Python's intro to web scraping: http://docs.python-guide.org/en/latest/scenarios/scrape/
* semi-nerdy intro to XPaths: https://en.wikipedia.org/wiki/XPath

### Scraping may be considered for websites that:
* store information in a structured way (tables, divs)
* have a replicable form of pagination
* show data as text rather than images / other media
    * clever example: http://bj.meituan.com/category/
* don't have anti-bot software / other anti-scraping measures

### Common issues we may encounter:
* the website undergoes a redesign, and XPaths no longer work
* edge cases: missing fields, "N/A"s, extra fields
* formatting issues (e.g., integers vs strings)
* data integrity / consistency issues - the site's fault, but your problem :)
* data storage: the engineer must "know what (s)he's doing"
    * name fields clearly
    * be careful when updating data via overwriting
    * keep track of when processes are run / fail

### Alternatives to web scraping:
* finding what loads the webpage's data, and loading it directly
* using a website's API (e.g. http://open.fda.gov vs. http://www.fda.gov/)
* use 3rd parties like http://scrapinghub.com/ (usually costs $$$)

### Scrape responsibly
* rate limit yourself with things like `time.sleep()`
* read the website's terms of service
* minimize the risk of compromising your IP - use [proxies and user agents](http://willdrevo.com/using-a-proxy-with-a-randomized-user-agent-in-python-requests/)