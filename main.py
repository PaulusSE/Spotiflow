import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

cid = '317da785f91a45d3b3e26ae4d051c7ec'  # client ID
secret = '++++++++++++'  # client secret
rur = 'https://vk.com/foxfizeon'  # redirected URI
scope = 'playlist-read-private'  # допуск к возможностям API
user = '31cxvy45dwvj3zr4q2wrolflwraq'  # имя пользователя

# api объект Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cid,
                                               client_secret=secret,
                                               redirect_uri=rur,
                                               scope=scope))

lists_amount = 1

playlist_lib = list()  # dictionary of playlists
# вывод списка инфы плейлистах
results = sp.current_user_playlists(limit=50)
for i, item in enumerate(results['items']):
    playlist_info = dict()  # dictionary of playlist items
    playlistid = item['id']  # id плейлиста
    playlist_img = sp.playlist_cover_image(playlistid)  # обложка листа

    playlist_info['data'] = item['name']
    playlist_info['id'] = item['id']
    playlist_info['img'] = playlist_img[0]['url']

    playlist_lib.append(playlist_info)

    lists_amount += 1

    # вывод названий
    # print("%d%c %s" % ((i+1), ')', item['name']))

    # print(playlistid)
    # print(playlist_img[0]['url'])
    # print()


# num = 1
# while num < lists_amount:
#     try:
#         print(playlist_lib[num])
#         num = num + 1
#     except IndexError:
#         print('Out of lists')
#         break

# info_file = json.dumps(playlist_lib)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(playlist_lib, f, ensure_ascii=False, indent=4)

