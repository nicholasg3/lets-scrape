import requests
from lxml import etree
import random
import time

from model import insert_campaign


URL = ('https://www.kickstarter.com/discover/advanced?google_chrome_workaround'
       '&category_id=10&woe_id=0&sort=magic&seed={}&page={}')
PAGES_TO_SCRAPE = 10

seed = random.randint(1000000, 9999999)
headers, cookies = {}, {}  # we will discuss this during the session

# cycle through the pages
for page in range(PAGES_TO_SCRAPE):

    url = URL.format(seed, page+1)
    print 'scraping url {}'.format(url)
    campaigns = []

    # get the http request and make a html tree object
    res = requests.get(url, headers=headers, cookies=cookies)
    parser = etree.HTMLParser()
    root = etree.fromstring(res.content, parser)

    # get the list of projects as a DOM element
    projects_list = root.xpath('//ul[@id="projects_list"]/div/li')
    for project in projects_list:

        # for every project, get the DOM elements corresponding to the info we want
        campaign_title = project.xpath('.//h6[@class="project-title"]/a')[0].text
        campaign_url = 'http://kickstarter.com{}'.format(
            project.xpath('.//h6[@class="project-title"]/a/@href')[0])
        campaign_id = project.xpath('.//h6[@class="project-title"]/a/@data-pid')[0]
        percent_funded = project.xpath('.//div[@class="project-stats-value"]')[0].text
        money_raised = project.xpath('.//span[contains(@class,"money")]')[0].text

        # format and store the data into our database
        insert_campaign({
            'campaign_title': campaign_title,
            'campaign_url': campaign_url,
            'campaign_id': int(campaign_id),
            'percent_funded': int(percent_funded.strip('%')),
            'money_raised': int(''.join(i for i in money_raised if i.isdigit())),
            })
        print 'inserted campaign_id {}'.format(campaign_id)

        time.sleep(3)  # scrape responsibly

print 'all done'
