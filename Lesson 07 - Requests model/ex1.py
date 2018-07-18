import requests
import json

url = 'https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=5'
r = requests.get(url)
f = open('music_show.json','w')
music_list   = json.loads(r.text)  # music_list is a list
music_string = json.dumps(music_list)  # music_string is a string
f.write(music_string) 
f.close()

with open( 'music_show.json', 'r' , encoding='utf-8-sig' ) as ff:
    txtfile = open( 'music_show.txt' , 'w' , encoding='utf-8-sig' )
    music = json.load(ff)
    for i in music:
        event_date_string = i['title'] + " : " + i['startDate']+ " ~ " + i['startDate']
        txtfile.write( event_date_string +'\n' )
    txtfile.close()