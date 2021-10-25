import urllib
import requests

PRESIDENTS = ['Washington', 'Adams', 'Jefferson', 'Madison', 'Monroe', 'Adams', 
'Jackson', 'Van Buren', 'Harrison', 'Tyler', 'Polk', 'Taylor', 'Fillmore', 'Pierce', 
'Buchanan', 'Lincoln', 'Johnson', 'Grant', 'Hayes', 'Garfield', 'Arthur', 'Cleveland', 
'Harrison', 'Cleveland', 'McKinley', 'Roosevelt', 'Taft', 'Wilson', 'Harding', 
'Coolidge', 'Hoover', 'Roosevelt', 'Truman', 'Eisenhower', 'Kennedy', 'Johnson', 
'Nixon', 'Ford', 'Carter', 'Reagan', 'Bush', 'Clinton', 'Bush', 'Obama', 'Trump', 'Biden']

def query(q):
    base_url = "https://api.duckduckgo.com/?q={}&format=json"
    resp = requests.get(base_url.format(urllib.parse.quote(q)))
    json = resp.json()
    return json

def presidents_search():
    answer = query("presidents of the united states")
    answers_text = [topic['Text'] for topic in answer['RelatedTopics']]
    answer_string = ' '.join(answers_text)
    return answer_string