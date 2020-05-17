import urllib.request
import os.path
from calendar import monthrange
import csv

def string_splitter(raw_string,centre_string):
	centre_string_position = raw_string.find(centre_string)
	left_string = raw_string[:centre_string_position]
	right_string = raw_string[int(centre_string_position+len(centre_string)):]

	return left_string, right_string

def string_extractor(raw_string,start_string,end_string,ignore_end=0):

	extracted_strings = []

	while raw_string.find(start_string) != -1:

		trimmed_string = string_splitter(raw_string,start_string)[1]
		extracted_string, raw_string = string_splitter(trimmed_string,end_string)
		
		ignores = 0
		while ignores < ignore_end:
			extracted_string_temp, raw_string = string_splitter(raw_string,end_string)
			extracted_string = extracted_string+end_string+extracted_string_temp
			ignores = ignores + 1

		extracted_strings.append(extracted_string)

	return extracted_strings

headline_data = []

max_year = 2020
year_int = 2007

num_headlines = 0
while year_int <= max_year:
	month_int = 1
	max_month = 12
	if year_int == 2020:
		max_month = 2
	while month_int <= max_month:
		day_int = 1
		while day_int <= monthrange(year_int,month_int)[1]:
			year = str(year_int)
			month = str(month_int)
			day = str(day_int)
			url = "https://www.express.co.uk/sitearchive/"+year+"/"+month+"/"+day
			file = 'archive/'+year+"_"+month+"_"+day

			if os.path.isfile(file) == False:
				print("Downloading headlines from web: "+year+"/"+month+"/"+day)
				urllib.request.urlretrieve(url, filename=file)
			else: 
				print("Loading headlines from disc   : "+year+"/"+month+"/"+day)

			doc_start_signiture = '<ul class="section-list">'
			doc_end_signiture = '<ul>'

			f = open(file, "r")
			for line in f:
				if doc_start_signiture in line:
					raw_headlines = line

			doc_start_position = int(raw_headlines.find(doc_start_signiture) + len(doc_start_signiture))
			doc_end_position = int(raw_headlines.find(doc_end_signiture) + len(doc_start_signiture))

			raw_headlines = raw_headlines[doc_start_position:doc_end_position]

			catagories = string_extractor(raw_headlines,'<li><a href="/','/',1)
			headlines = string_extractor(raw_headlines,'<span>','</span>')

			num_headlines = num_headlines + len(headlines)

			headline_count = 0
			while headline_count < len(headlines):
				headline_data.append([year_int, month_int, day_int,catagories[headline_count], headlines[headline_count]])
				headline_count = headline_count + 1

			print("Headlines:",len(headlines))
			day_int = day_int + 1
		month_int = month_int + 1
	year_int = year_int + 1

# Write CSV file
kwargs = {'newline': ''}
with open('headline_data.csv', 'w', **kwargs) as fp:
    writer = csv.writer(fp, delimiter=',')
    writer.writerow(["year", "month", "day", "catagory", "headline"])  # write header
    writer.writerows(headline_data)
print("Total headlines  :", num_headlines)