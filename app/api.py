import requests

class MovieAPI:
    def __init__(self, api_key:str)->None:
        self.headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

    def get_now_playing(self, page:int=1)->list:
        url = f"https://api.themoviedb.org/3/movie/now_playing?language=en-US&page={page}"

        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json().get('results')

        return []
    
    def get_popular(self, page:int=1)->list:
        url = f"https://api.themoviedb.org/3/movie/popular?language=en-US&page={page}"

        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json().get('results')

        return []
    
    def get_top_rated(self, page:int=1)->list:
        url = f"https://api.themoviedb.org/3/movie/top_rated?language=en-US&page={page}"

        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json().get('results')

        return []

    def get_upcoming(self)->list:
        url = f"https://api.themoviedb.org/3/movie/upcoming?language=en-US"

        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json().get('results')

        return []
    
    def get_movie_details(self, movie_id:int)->dict:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"

        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()

        return {}
    
    def get_movie_images(self, movie_id:int)->list:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}/images"

        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json().get('backdrops')

        return []
    
    def get_video_id(self, movie_id:int)->str:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?language=en-US"

        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            data = response.json().get('results')
            for item in data:
                if item.get('type') == 'Trailer' and item.get('official'):
                    return item.get('key')

        return None
    
    def get_similar_movies(self, movie_id:int)->list:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}/similar?language=en-US&page=1"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            data=response.json().get('results')
            items=[item for item in data if item.get('popularity')>15]
            return items

        return []