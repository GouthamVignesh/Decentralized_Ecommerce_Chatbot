import random
import requests
import json
def news():
	y = random.randint(1,3)
	if y == 1:
	    r = requests.get('https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=e33b15acbf4c4071bfeb891cd02a99f6')
	    j = r.json()
	    x = j.get('articles')
	    newp = "The headlines are: "+"1. "+x[0]["title"]+"." +" 2. "+x[1]["title"]+"."+" 3. "+x[2]["title"]+"."+" 4. "+x[3]["title"]+"."+" 5. "+x[4]["title"]+"." 
	    talk=""+newp+""
	elif y==2:
	    r = requests.get('https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=e33b15acbf4c4071bfeb891cd02a99f6')
	    j = r.json()
	    x = j.get('articles')
	    newp = "The headlines are: "+"1. "+x[0]["title"]+"." +" 2. "+x[1]["title"]+"."+" 3. "+x[2]["title"]+"."+" 4. "+x[3]["title"]+"."+" 5. "+x[4]["title"]+"." 
	    talk=""+newp+""   
	elif y==3:
	    r = requests.get('https://newsapi.org/v1/articles?source=ars-technica&sortBy=top&apiKey=e33b15acbf4c4071bfeb891cd02a99f6')
	    j = r.json()
	    x = j.get('articles')
	    newp = "The headlines are: "+"1. "+x[0]["title"]+"." +" 2. "+x[1]["title"]+"."+" 3. "+x[2]["title"]+"."+" 4. "+x[3]["title"]+"."+" 5. "+x[4]["title"]+"." 
	    talk=""+newp+""
	return talk