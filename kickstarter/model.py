import dataset
import datetime


# create a database and a table
db = dataset.connect('mysql://root@localhost/kickstarter')
table = db['campaign_basics']


def now():
    return datetime.datetime.now()


# insert time-stamped campaign info into the database
def insert_campaign(campaign_info):
    campaign_info['date_observed'] = now()
    table.insert(campaign_info)
