# github url: https://github.com/BendingSpoons/searchads-api

from search_ads import SearchAds
import datetime

# get today's date
todayDate = datetime.datetime.today().strftime('%Y-%m-%d')

# search ads parameters
api = SearchAds("Apartment List, Inc.")
start_date = todayDate
end_date = todayDate

campaign = api.get_campaigns()
for camp in campaign:
    kw_report = api.get_campaign_keywords_report(camp,start_date,end_date,'UTC','DAILY',None,[],False,False)
    print(kw_report)





# # get_campaign_keywords_report parameters
# self,
# campaign,
# start_time=_today(),
# end_time=_today(),
# timezone='UTC',
# granularity='DAILY',
# selector=None,
# group_by=[],
# return_records_with_no_metrics=False,
# return_row_totals=False):