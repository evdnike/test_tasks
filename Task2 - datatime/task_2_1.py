import datetime as dt

date_time_now = dt.date.today()
today_year, today_month = date_time_now.year, date_time_now.month


def get_this_year(fridays13 = 0):
	months = range(today_month, 13)
	years = range(today_year, today_year+1)
	
	for year in years :
		for month in months:
			if dt.datetime(year, month, 13).weekday() == 4: # weekday() == 4(Friday), 0 - Monday.
				fridays13 += 1
		
	return fridays13


def get_rest_years():
	fridays = get_this_year()

	for year in range(today_year+1, 2200):
		if fridays == 10:
			break
		for month in range(1, 13):
			if dt.datetime(year, month, 13).weekday() == 4:
				fridays += 1
				
				print(year, month, 13)

get_rest_years()