import utils

from tmdb.constants import TMDB_POSTER_PATH_BASE_URL


def get_movie_details_layout(title, release_date, overview, poster_path):
    formatted_release_dt = utils.reformat_date_str(release_date)
    full_poster_path_url = TMDB_POSTER_PATH_BASE_URL + poster_path
    movie_details_layout = [
        {
            "type": "section",
            "text": {
                "type": "plain_text",
                "text": "Here's the movie info you requested!",
                "emoji": True
            }
        },
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": title,
                "emoji": True
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*Release date:* {formatted_release_dt}\n​{overview}​"
            },
            "accessory": {
                "type": "image",
                "image_url": full_poster_path_url,
                "alt_text": title
            }
        }
    ]
    return movie_details_layout
