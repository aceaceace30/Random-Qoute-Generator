from django.shortcuts import render
import requests

def index(request):
	template_name = 'qoutes/index.html'

	#api provider link
	#https://quotesondesign.com/api-v4-0/
	url = 'https://quotesondesign.com/wp-json/wp/v2/posts/?orderby=rand'

	r = requests.get(url.format()).json()
	
	title = r[0]['title']['rendered']
	content = r[0]['content']['rendered']

	qoute = {
		'title': title,
		'content': content,
	}

	return render(request, template_name, {'qoute': qoute})
