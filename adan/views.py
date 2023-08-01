# views.py
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def scrape_data(request):
    url = "https://timesprayer.com/prayer-times-in-amman.html"  # Replace with the URL of the website you want to scrape
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find the ul element with class="mat_list"
        ul_element = soup.find("ul", class_="mat_list")
        
        if ul_element:
            # Find all the li elements within the ul element
            li_elements = ul_element.find_all("li")
            
            # Extract the content of the li elements
            scraped_data_list = [{"pray": li.find("strong").text.strip(), "time": li.find("time").text.strip()} for li in li_elements]
            
            return render(request, "scraped_data.html", {"scraped_data_list": scraped_data_list})
        else:
            return render(request, "error.html", {"error_message": "No ul element with class 'mat_list' found on the page."})
    else:
        return render(request, "error.html", {"error_message": "Failed to fetch the website."})

