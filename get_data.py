import requests
req = requests.get('http://paste.awesom.eu/hG0O')

with open('fishing_data.csv', 'w', encoding="utf-8") as f:
    f.write(req.content.decode(req.encoding).split('pre>')[1][:-2])