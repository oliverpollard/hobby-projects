import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

analysis = 0

headlines_data = pd.read_csv('headline_data.csv')
weather_headlines_data = headlines_data[headlines_data['catagory']=='news/weather']

weather_headlines = weather_headlines_data['headline'].tolist()

print(len(headlines_data))
print(len(weather_headlines))
if analysis == 0:
	caps_words = {}

	headline_count = 0
	while headline_count < len(weather_headlines):
		words = weather_headlines[headline_count].split()
		word_count = 0
		while word_count < len(words):
			if words[word_count].isupper() == True:
				caps_word = ''.join([i for i in words[word_count] if i.isalpha()])

				if caps_word in caps_words:
					caps_words[caps_word] = caps_words[caps_word] + 1
				else:
					caps_words[caps_word] = 1

			word_count = word_count + 1
		headline_count = headline_count + 1

	#print(caps_words)
	caps_words.pop("UK")
	caps_words.pop("BBC")
	caps_words.pop("C")

	ordered_words = sorted(caps_words, key=caps_words.get, reverse=False)

	top_ordered_words = ordered_words[::-1][:20]
	print(top_ordered_words)
	word_freq = sorted(caps_words.values())[::-1][:20]
	print(word_freq)

	fig, ax = plt.subplots()

	#print(sorted(caps_words.values())[:10])
	plt.bar(range(len(top_ordered_words)),word_freq)
	#plt.bar(range(len(top_ordered_words)), list(sorted(caps_words.values())), align='center')
	plt.xticks(range(len(top_ordered_words)), top_ordered_words, rotation='vertical')

	plt.show()
	"""

	ordered_words = sorted(caps_words, key=caps_words.get, reverse=True)

	#top_ordered_words = ordered_words


	text = " ".join([(k + " ")*v for k,v in ordered_words.items()])

	# Generate a word cloud image
	wordcloud = WordCloud().generate(text)


	# Display the generated image:
	# the matplotlib way:
	plt.imshow(wordcloud, interpolation='bilinear')
	plt.axis("off")




	"""

elif analysis == 1:
	#relative number of weather news stories compared with total news stories per year
	years = np.linspace(2007,2020,num=14)
	years_weather_freq = np.zeros(len(years))
	years_freq = np.zeros(len(years))

	count = 0
	while count < len(years):
		year_int = int(years[count])
		years_freq[count] = len(headlines_data[headlines_data['year']==year_int])
		years_weather_freq[count] = len(weather_headlines_data[weather_headlines_data['year']==year_int])
		count = count + 1

	plt.plot(years,100*years_weather_freq/years_freq)
	plt.show()

elif analysis == 2:
	#relative number of weather news stories compared with total news stories per month

	months = np.linspace(2015,2020,num=6*12)
	months_weather_freq = np.zeros(len(months))
	months_freq = np.zeros(len(months))

	count = 0
	while count < len(months):
		year_int = int(np.floor(months[0] + count/12))
		month_int = int(count - (year_int-months[0])*12 + 1)
		print(year_int,month_int,count)
		months_freq[count] = len(headlines_data[headlines_data['year']==year_int][headlines_data['month']==month_int])
		months_weather_freq[count] = len(weather_headlines_data[weather_headlines_data['year']==year_int][weather_headlines_data['month']==month_int])
		count = count + 1

	plt.plot(months,100*months_weather_freq/months_freq)
	plt.show()