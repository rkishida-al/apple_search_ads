# github url: https://github.com/BendingSpoons/searchads-api
from search_ads import SearchAds
import datetime
import csv

# set date range for report -- default: current date
todayDate = datetime.datetime.today()
yesterday = datetime.datetime.today() - datetime.timedelta(days=1)
fileDate = todayDate.strftime('%Y-%m-%d_%H-%M-%S')
reportDate = yesterday.strftime('%Y-%m-%d')
# start_date = reportDate
# end_date = reportDate
start_date = '2018-10-23'
end_date = '2018-10-23'

# search ads parameters
api = SearchAds("Apartment List, Inc.")

# open csv file
file_name = 'asa_keyword_report_' + fileDate + '.csv'
report_file = csv.writer(open(file_name, 'w', newline='\n'), delimiter=',', quotechar='"')

# set count to print header only once
count = 0
campaigns = api.get_campaigns()
for camp in campaigns:
    kw_report = api.get_campaign_keywords_report(camp,start_date,end_date,'ORTZ','DAILY',None,[],False,False)
    for kw in kw_report:
        kw["campaignName"] = camp.name # pass campaign_name in final output
        if count == 0:
            report_file.writerow(kw.keys())
            count += 1
        report_file.writerow(kw.values())

