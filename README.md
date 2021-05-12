# Twitch video ID scrapper

Chrome version: 90.0.4430.93
Driver version: 90.0.4430.24 (can be downladed [from this page](https://sites.google.com/a/chromium.org/chromedriver/downloads))
Python version: 3.8

## Env setup

```
python3 -m venv .env
source .env/bin/activate
pip install -U pip
pip install -r requirements.txt
```

## Running

Note: remember to activate your python environment:

```
python scrap_it.py
```

This will create a `twitch_video_ids.json` file when it finishes.

## TODO

- [ ] receive URL as param 
- [ ] receive file name as param (optional)
- [ ] use logging instead of print