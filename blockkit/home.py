home_layout = {
    "type": "home",
    "callback_id": "home_view",
    "blocks": [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Welcome to Movie Info! :tada:",
                "emoji": True
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Click the button below to pick a movie!"
            }
        },
        {
            "type": "actions",
            "block_id": "buttons",
            "elements": [
                {
                    "type": "button",
                    "action_id": "pick_movie",
                    "text": {
                        "type": "plain_text",
                        "text": "Select a Movie!"
                    }
                }
            ]
        }
    ]
}
