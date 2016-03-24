import requests
from lxml import etree
import random

import model

URL = ('https://www.kickstarter.com/discover/advanced?google_chrome_workaround'
       '&category_id=10&woe_id=0&sort=magic&seed={}&page={}')
PAGES_TO_SCRAPE = 20

seed = random.randint(1000000, 9999999)
headers = {}
cookies = {}

for page in range(PAGES_TO_SCRAPE):
    url = URL.format(seed, page+1)

    res = requests.get(
        url,
        headers=headers,
        cookies=cookies)
    parser = etree.HTMLParser()
    root = etree.fromstring(res.content, parser)
    print url
    money_raised = root.xpath('//span[@class="money usd no-code"]')
    for money in money_raised:
        print money.text
