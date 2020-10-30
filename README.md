# Slack Movie Info App

**Movie Info** is a slack app that allows you to fetch information regarding your favorite movies. This app can be added to your Slack workspace and it allows you to 
  - Choose movies from available list
  - Get Title, Overview, Release Date and Poster Image as message within Slack

## License
  - This app is released under [GNU GPL v3 License](./LICENSE)

## Tech
  - This app is built using Python 3.6 and [Bolt](https://slack.dev/bolt-python/concepts)
  - The app interacts with [TMDB v3 APIs](https://www.themoviedb.org/documentation/api)

## Env setup
  For local development
  - Setup virtual environment for this project using python3.6
  - Install dependencies mentioned in [requirements.txt](./requirements.txt) using pip3 in the created virtualenv
    ```
    $pip3 install -r requirements.txt
    ```
  - Install and enable [flake8](https://pypi.org/project/flake8/) linter
  - Setup ngrok to expose public endpoint from local as mentioned [here]((https://api.slack.com/start/building/bolt-python#ngrok)). Use port 3000
  - Set below environment variables -
    - **SLACK_BOT_TOKEN** Available from - _Features &rarr; OAuth & Permissions &rarr; OAuth Tokens & Redirect URLs &rarr; Bot User OAuth Access Token_ 
    - **SLACK_SIGNING_SECRET** Available from - _Settings &rarr; Basic Information &rarr; App Credentials &rarr; Signing Secret_
    - **TMDB_API_KEY** - Availble on TMDB web console from - _[Overview](https://www.themoviedb.org/settings/api) &rarr; API Key (v3 auth)_
        ```
        $export SLACK_BOT_TOKEN=<token>
        $export SLACK_SIGNING_SECRET=<secret>
        $export TMDB_API_KEY=<api_key>
        ```
    - Inside the virtual environment,execute below command to start the app 
        ```
        python3 app.py
        ```

## Slack Settings
 Configure the below settings from the Slack App's [web console](https://api.slack.com/apps) -
  - **Enable App Home** from - _Features &rarr; App Home &rarr; Show Tabs &rarr; Home Tab_
  - **Enable Events** from - _Features &rarr; Event Subscriptions &rarr; Enable Events_
    - Set Request Url - `https://<ngrok_public_url>/slack/events`  
  - **Enable Interactivity & Shortcuts** from - _Features &rarr; Interactivity & Shortcuts_
    - Set Request Url - `https://<ngrok_public_url>/slack/events`
  - Subscribe to **app_home_opened** from - _Features &rarr; Event Subscriptions &rarr; Subscribe to events on behalf of users &rarr; Add Workspace Event_
  - Grant **chat:write** permission from - _Features &rarr; OAuth & Permissions
 &rarr; Scopes &rarr; Add an OAuth Scope_
  - Fill in **Display Information** from - _Settings &rarr; Basic Information &rarr; Display Information_
    - Set **App Name**
    - Set **Short Description**
    - Upload **App icon**
    - Set **Background Color**

## Useful Links
  - [Building Slack Apps](https://api.slack.com/start)
  - [TMDB API v3](https://developers.themoviedb.org/3/getting-started/introduction)
  - [ngrok Setup](https://dashboard.ngrok.com/get-started/setup)