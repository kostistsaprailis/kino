import sqlite3

from datetime import datetime

def return_data(start_date = '2010-01-02 10:00', end_date = ''):
	if (end_date == ""):
		now = datetime.now()
		end_year = now.year
		end_month = now.month
		end_day = now.day
		end_hour = now.hour
		end_minute = now.minute
		end_date = end_year+"-"+end_month+"-"+end_day+" "+end_hour+":"+end_minute

	conn = sqlite3.connect('db/kino.db')
	c = conn.cursor()
	args = [start_date,end_date]
	data = []
	for res in c.execute('select * from entries where draw_date between ? and ?',args):
		draw = []
		for i in range(0,22):
			if (i > 2):
				draw.append(res[i])
		data.append(draw)
	conn.close()
	return data
