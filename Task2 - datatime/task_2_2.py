import datetime as dt 
from datetime import date
from collections import namedtuple


def get_age_and_sign(birthday):
	today_date = dt.datetime.today()
	birthdate = birthday.split('-')
	differ_days = date(today_date.year, today_date.month, today_date.day) - date(int(birthdate[2]), int(birthdate[1]), int(birthdate[0]))
	differ_years = int(differ_days.days/365)


	my_day = int(birthdate[0])
	my_month = int(birthdate[1])


	if ((int(my_month)==12 and int(my_day) >= 22) or (int(my_month)==1 and int(my_day)<= 19)):
		zodiac_sign = "Capricorn"
	elif ((int(my_month)==1 and int(my_day) >= 20) or (int(my_month)==2 and int(my_day)<= 17)):
		zodiac_sign = "Aquarium"
	elif ((int(my_month)==2 and int(my_day) >= 18) or (int(my_month)==3 and int(my_day)<= 19)):
		zodiac_sign = " Pices"
	elif ((int(my_month)==3 and int(my_day) >= 20) or (int(my_month)==4 and int(my_day)<= 19)):
		zodiac_sign = "Aries"
	elif ((int(my_month)==4 and int(my_day) >= 20) or (int(my_month)==5 and int(my_day)<= 20)):
		zodiac_sign = "Taurus"
	elif ((int(my_month)==5 and int(my_day) >= 21) or (int(my_month)==6 and int(my_day)<= 20)):
		zodiac_sign = "Gemini"
	elif ((int(my_month)==6 and int(my_day) >= 21) or (int(my_month)==7 and int(my_day)<= 22)):
		zodiac_sign = "Cancer"
	elif ((int(my_month)==7 and int(my_day) >= 23) or (int(my_month)==8 and int(my_day)<= 22)): 
		zodiac_sign = "Leo"
	elif ((int(my_month)==8 and int(my_day) >= 23) or (int(my_month)==9 and int(my_day)<= 22)): 
		zodiac_sign = "Virgo"
	elif ((int(my_month)==9 and int(my_day) >= 23) or (int(my_month)==10 and int(my_day)<= 22)):
		zodiac_sign = "Libra"
	elif ((int(my_month)==10 and int(my_day) >= 23) or (int(my_month)==11 and int(my_day)<= 21)): 
		zodiac_sign = "Scorpio"
	elif ((int(my_month)==11 and int(my_day) >= 22) or (int(my_month)==12 and int(my_day)<= 21)):
		zodiac_sign = "Sagittarius"
	

	signs = namedtuple('signs', ('name', 'years'))
	
	my_signature = signs(zodiac_sign, differ_years)
	return my_signature

print(get_age_and_sign('20-11-1997'))