import requests
import json

response = requests.get('https://iknow.jp/api/v2/goals/566921')
data = json.loads(response.content)

items = data['goal_items']

flashcards = []

for item in items:
    japanese = item['item']['cue']['text']
    english = item['item']['response']['text']
    flashcards.append({ 'japanese': japanese, 'english': english })

with open('flashcards.json', 'w') as file:
    json.dump(flashcards, file)