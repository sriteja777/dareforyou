import requests
import bs4
import json
import random
from time import sleep
fruits = ["Açaí", "Akee", "Apple", "Apricot", "Avocado", "Banana", "Bilberry", "Blackberry", "Blackcurrant", "Black sapote", "Blueberry", "Boysenberry",
"Buddha's hand (fingered citron)", "Cactus pear", "Crab apple", "Currant", "Cherry", "Cherimoya (Custard Apple)","Chico fruit", "Cloudberry", "Coconut",
"Cranberry", "Damson", "Date", "Dragonfruit (or Pitaya)","Durian", "Elderberry", "Feijoa", "Fig", "Goji berry", "Gooseberry", "Grape", "Raisin", "Grapefruit",
"Guava", "Honeyberry", "Huckleberry", "Jabuticaba", "Jackfruit", "Jambul", "Japanese plum", "Jostaberry", "Jujube", "Juniper berry", "Kiwano (horned melon)",
"Kiwifruit", "Kumquat", "Lemon", "Lime", "Loganberry", "Loquat", "Longan", "Lychee", "Mango", "Mangosteen", "Marionberry", "Melon", "Cantaloupe", "Galia melon",
"Honeydew", "Watermelon", "Miracle fruit", "Mulberry", "Nectarine", "Nance", "Orange", "Blood orange", "Clementine", "Mandarine", "Tangerine", "Papaya", "Passionfruit",
"Peach", "Pear", "Persimmon", "Plantain", "Plum", "Prune (dried plum)", "Pineapple", "Pineberry", "Plumcot (or Pluot)", "Pomegranate", "Pomelo", "Purple mangosteen", "Quince",
"Raspberry", "Salmonberry", "Rambutan (or Mamin Chino)", "Redcurrant", "Salal berry", "Salak", "Satsuma", "Soursop", "Star apple", "Star fruit", "Strawberry", "Surinam cherry",
"Tamarillo", "Tamarind", "Tangelo", "Tayberry", "Ugli fruit", "White currant", "White sapote", "Yuzu"]

random.shuffle(fruits)
ses = requests.Session()

pg = ses.get("https://buzzbuddy.site/en/d/198768")
sp = bs4.BeautifulSoup(pg.text, "lxml")
token = sp.find("meta", {"name": "csrf-token"}).get('content')

data= {"qdata": json.dumps({'qid': 198768, 'pname': 'santras', 'score': 7})}
headers={
	'X-CSRF-TOKEN': token,
	"Referer": "https://buzzbuddy.site/en/d/198768",
	'X-Requested-With': 'XMLHttpRequest',
	'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'
}
print(len(fruits))
for idx,fruit in enumerate(fruits):
	data['qdata'] = json.dumps({'qid': 198768, 'pname': fruit, 'score': random.randint(-20,30)})
	res = ses.post("https://buzzbuddy.site/submit",data=data, headers=headers)
	print(fruit, res.text,type(json))
	print(idx)
	sleep(0.5)