modal_layout = {
  "type": "modal",
  "callback_id": "select_movie",
  "title": {
    "type": "plain_text",
    "text": "Movie Info",
    "emoji": True
  },
  "submit": {
    "type": "plain_text",
    "text": "Submit",
    "emoji": True
  },
  "close": {
    "type": "plain_text",
    "text": "Cancel",
    "emoji": True
  },
  "blocks": [
    {
      "type": "input",
      "block_id": "selected_movie",
      "element": {
        "type": "static_select",
        "placeholder": {
          "type": "plain_text",
          "text": "Select an item",
          "emoji": True
        },
        "options": [
          {
            "text": {
              "type": "plain_text",
              "text": "Star Wars",
              "emoji": True
            },
            "value": "11"
          },
          {
            "text": {
              "type": "plain_text",
              "text": "Star Wars: The Rise of Skywalker",
              "emoji": True
            },
            "value": "181812"
          },
          {
            "text": {
              "type": "plain_text",
              "text": "Solo: A Star Wars Story",
              "emoji": True
            },
            "value": "348350"
          },
          {
            "text": {
              "type": "plain_text",
              "text": "Star Wars: The Force Awakens",
              "emoji": True
            },
            "value": "140607"
          },
          {
            "text": {
              "type": "plain_text",
              "text": "Rogue One: A Star Wars Story",
              "emoji": True
            },
            "value": "330459"
          },
          {
            "text": {
              "type": "plain_text",
              "text": "The Empire Strikes Back",
              "emoji": True
            },
            "value": "1891"
          },
          {
            "text": {
              "type": "plain_text",
              "text": "Star Wars: The Last Jedi",
              "emoji": True
            },
            "value": "181808"
          }
        ],
        "action_id": "static_select-action"
      },
      "label": {
        "type": "plain_text",
        "text": "Select a movie:",
        "emoji": True
      }
    }
  ]
}
