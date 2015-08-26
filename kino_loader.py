###################
# Library imports

# Import sqlite3 library used to access a sqlite3 db
import sqlite3

# Import the datetime library.
from datetime import datetime

# The dataLoader class is used to retrieve the kino results from the database
class dataLoader(object):
	# Constructor
	def __init__(self, database='db/kino.db'):
		'''class constructor to create and initialize the database path.'''
		self.database = database

	# The returnData method used to return db data.
	def returnData(self,start_date = '2010-01-02 10:00', end_date = ''):
		'''Function that queries the database the the draw results on between the 
		   provided dates. Includes default values.'''

		# Check to see if the end date has not been provided.
		# If so use the current date.
		if (end_date == ""):
			now = datetime.now()
			end_year = now.year
			end_month = now.month
			end_day = now.day
			end_hour = now.hour
			end_minute = now.minute
			end_date = end_year+"-"+end_month+"-"+end_day+" "+end_hour+":"+end_minute
		
		# Initialiaze a connection to the database,
		# an
		conn = sqlite3.connect(self.database)
		c = conn.cursor()
		
		# Creating the list of arguments to pass to the query
		args = [start_date,end_date]
		
		# The data list is used to store the total results to be returned.
		data = []
		for res in c.execute('select * from entries where draw_date between ? and ?',args):
			# The draw list is used to store the results form each result line returned from the query.
			draw = []
			# We don't want the first three columns from the result set
			for i in range(0,22):
				if (i > 2):
					draw.append(res[i])
			data.append(draw)
		conn.close()
		return data
