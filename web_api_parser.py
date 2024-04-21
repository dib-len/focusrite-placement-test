import requests

def main():
    url = "https://api.ampifymusic.com/packs"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    # Parse the response and sort it into a set of genres
    genres = set()
        
    for pack in data['packs']:
        for genre in pack['genres']:
            genres.add(genre)

    print(list(genres))

if __name__ == "__main__":
    main()