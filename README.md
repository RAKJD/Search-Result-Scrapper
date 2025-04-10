
## Search Result Scrapper
### Introduction
A simple Python-based Search Scraper with a graphical interface using Tkinter. It fetches search results from Bing and displays the title, link, and description in an easy-to-use GUI.

### Features
- Fetches search results from Bing (Google has restrictions)
- Displays title, link, and description
- Built-in error handling (timeouts, connection failures, etc.)
- 2-second delay to avoid request blocking
- Simple and interactive Tkinter GUI

### Requirements (including liberaries)
- python
- beautifulsoup4
- requests
- tkinter
- time

### Usage
- Enter search query in search box.
- Click search button
- View results in scrollable search result area.

### Notes
- Bing is used due to Google's strict scrapping policies.
- If results dont appear, Bing's HTML structure may have changed.
- The 2 second delay prevents rate-limiting by Bing.

