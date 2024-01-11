import requests

class MovieAPI:
    def __init__(self, api_key:str)->None:
        self.headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

    def get_now_playing(self, page:int=1)->dict:
        url = f"https://api.themoviedb.org/3/movie/now_playing?language=en-US&page={page}"

        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json().get('results')

        return {}