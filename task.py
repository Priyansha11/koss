import json
import request






url = "http://quotes.rest/qod.json"
r = json.get(url)
x=r.json()
print(x)






main_api = "http://quotes.rest/qod.json"
url = main_api 






def quoteoftheday

	main_url = "http://quotes.rest/qod.json"
	open_quotes_page = requests.get(main_url).json()
	article = open_quotes_page["quotes"]
	results = []
	results.append(ar["title"])
	print(i+1,results[i])
if _name_=='_main_':
	quoteoftheday()




from urllib.request import urlopen
with urlopen('http:/quotes.rest/qod.json






import urllib.request
response = urllib.request.urlopen('http://quotes.rest/qod.json')
html = response.read()
