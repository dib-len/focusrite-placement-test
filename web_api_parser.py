import requests

def main():
    url = "https://api.ampifymusic.com/packs"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    genres = {}

    for pack in data['packs']:
        for genre in pack['genres']:
            if genre not in genres:
                genres[genre] = []
            genres[genre].append(pack['name'])

    print(sorted(genres.keys())) # prints out a list of all the genres sorted

    if 'hip-hop' in genres:
        print("\nPacks in 'hip-hop' genre:")
        for pack in genres['hip-hop']:
            print(pack) # prints out a list of all the packs in the genre ‘hip-hop’

if __name__ == "__main__":
    main()