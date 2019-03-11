#Playlist Modeling
#### nested dictionaries which has list inside


playlist = {'title': 'patagonia',
            'author': 'colt',
            'songs': [
                {'title': 'ang', 'artist': ['eheads1'], 'duration': 2.5},
                {'title': 'huling', 'artist': ['eheads1', 'eheads2'], 'duration': 3.5},
                {'title': 'elbimbo', 'artist': ['rmaya'], 'duration': 3}
            ]
}

for song in playlist['songs']:
    print(song['title'])

tduration = 0
for min in playlist['songs']:
    tduration += min['duration']
print(tduration)