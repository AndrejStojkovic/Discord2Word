months = ['January', 'February', 'March', 'April', 'May', 'June',
					'July', 'August', 'September', 'October', 'November', 'December']

def get_date(str):
	str = str.split('-')

	year = str[0]
	month = months[int(str[1]) - 1]
	day = ''

	if(str[2][0] == '0'):
		day = str[2][1]
	else:
		day = str[2]

	full_date = month + ' ' + day + ', ' + year

	return full_date
