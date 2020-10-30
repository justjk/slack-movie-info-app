import os

# Use the package we installed
from slack_bolt import App

from blockkit.home import home_layout
from blockkit.movie_details import get_movie_details_layout
from blockkit.movie_picker_modal import modal_layout
from tmdb.get_movie_details import get_movie_details

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)


@app.event("app_home_opened")
def open_app_home(client, event, logger):
    try:
        client.views_publish(
          # the user that opened your app's app home
          user_id=event["user"],
          # the view object that appears in the app home
          view=home_layout
        )
    except Exception as e:
        logger.error(f"Error opening modal: {e}")


@app.action("pick_movie")
def open_movie_picker_modal(body, ack, client, logger):
    try:
        client.views_open(
            trigger_id=body["trigger_id"],
            view=modal_layout)
    except Exception as e:
        logger.error(f"Error opening modal: {e}")
    ack()


@app.view("select_movie")
def handle_submission(ack, body, client, view):
    selected_movie_id = view.get('state', {}).get('values', {}).\
        get('selected_movie', {}).get('static_select-action', {}).\
        get('selected_option', {}).get('value', {})
    user = body["user"]["id"]
    ack()
    movie_details = get_movie_details(selected_movie_id)
    client.chat_postMessage(
        channel=user,
        blocks=get_movie_details_layout(**movie_details))


# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
