from django.shortcuts import render
import requests
import re



def index(request):
	template_name = 'qoutes/index.html'

	#api provider link
	#https://quotesondesign.com/api-v4-0/

	url = 'http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1'

	r = requests.get(url.format()).json()
	
	title = r[0]['title']
	content = r[0]['content']

	content = re.sub('<[^<]+?>', '', content) #remove p tags in the api call on 'contents'

	qoute_values = {
		'title': title,
		'content': content,
	}

	return render(request, template_name, {'qoute':qoute_values} )
