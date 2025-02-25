import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import scrolledtext
import time

# Function to perform web search
def search_web(query, num_results=10):
    """
    This function sends a search request to Bing, extracts search result titles, links, 
    and descriptions, and returns the results formatted as a string.

    Parameters:
    query (str): The search term entered by the user.
    num_results (int): The number of results to retrieve.

    Returns:
    str: Formatted search results or an error message if something goes wrong.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }

    # We are using Bing because Google's scraping restrictions :(
    search_url = f"https://www.bing.com/search?q={query}&count={num_results}"

    try:
        #send http req to bing with headers
        response = requests.get(search_url, headers=headers, timeout=5)
        response.raise_for_status()  # Raise HTTP error for bad responses

        #parse the html responses
        soup = BeautifulSoup(response.text, "html.parser")
        search_results = []

        #select search results using bing's specific html structure.
        for result in soup.select("li.b_algo"):  
            # bing selector
            title_element = result.select_one("h2 a") 
            # extract title link
            link = title_element["href"] if title_element else "No link"
            title = title_element.text if title_element else "No title"
            # extract description
            desc_element = result.select_one(".b_caption p") 
            description = desc_element.text if desc_element else "No description"
            # Format the result and add it to the list
            search_results.append(f"Title: {title}\nLink: {link}\nDescription: {description}\n\n")

        # Add a delay between requests to avoid being blocked.
        time.sleep(2)  

        #return formatted results or a message if no results wwere found.
        return "".join(search_results) if search_results else "No results found. Try a different query."

    except requests.exceptions.Timeout:
        return "Error: Request timed out."
    except requests.exceptions.ConnectionError:
        return "Error: Unable to connect to Google."
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP Error: {http_err}"
    except requests.exceptions.RequestException as req_err:
        return f"Request Error: {req_err}"
    except Exception as e:
        return f"Unexpected Error: {e}"

# Function to get search query and display results
def search():
    """
    This function retrieves the user's search query from the input box,
    calls the search_web() function, and displays the results in the text area.
    """
    query = entry.get().strip() # gets the user input and removes any extra spaces.
    if query: # proceed is query not empty
        results = search_web(query)
        # enable text area to update content
        text_area.config(state=tk.NORMAL) 
        # clear any previous search results
        text_area.delete(1.0, tk.END)
        # insert a few search results
        text_area.insert(tk.INSERT, results)
        # disable inserting after inserting search results
        text_area.config(state=tk.DISABLED)

# GUI setup
root = tk.Tk()
root.title("Google Search Scraper")  
# set window geometry
root.geometry("500x300")

#label for search input
label = tk.Label(root, text="Enter Search Query:")
label.pack(pady=5)

# input field for entering search query
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

#search button for search function
search_button = tk.Button(root, text="Search", command=search)
search_button.pack(pady=5)

#scrollable search result display area
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=15, state=tk.DISABLED)
text_area.pack(pady=10)

root.mainloop()
