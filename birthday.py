#!/usr/local/bin/python

from datetime import date

today = date.today()

#Change this to your birth date
date_of_birth = date(1995, 3, 25)

birthday = date(today.year, date_of_birth.month, date_of_birth.day)
days_until_birthday = (birthday-today).days
days_alive = (today-date_of_birth).days

print( 'You are ' + str(days_alive) + ' days old')

if days_until_birthday > 0:
	print( 'It\'s ' + str(days_until_birthday) + ' days until your Birthday')
elif days_until_birthday == 0:
	print( 'Happy Birthday!')
else:
	print( 'You\'ll have to wait until next year for another birthday')
