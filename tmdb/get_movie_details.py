import requests

from tmdb.constants import MAX_TIMEOUT_SEC, TMDB_API_KEY, TMDB_V3_API_BASE_URL


def get_movie_details(movie_id):
    movie_details = {}
    API_URL = TMDB_V3_API_BASE_URL + f"/movie/{movie_id}"
    query_params = {
        "api_key": TMDB_API_KEY
    }
    try:
        response = requests.get(
            API_URL, params=query_params, timeout=MAX_TIMEOUT_SEC)
        response.raise_for_status()
        movie_details = {
            "title": response.json().get("title"),
            "release_date": response.json().get("release_date"),
            "overview": response.json().get("overview"),
            "poster_path": response.json().get("poster_path")
        }
    except requests.exceptions.RequestException as e:
        print(str(e))
    return movie_details


if __name__ == "__main__":
    print(get_movie_details(140607))
