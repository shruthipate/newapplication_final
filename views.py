from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup as BSoup
from news.models import Headline

def scrape(request, category):
    # Clear existing headlines
    Headline.objects.all().delete()

    # Define user agent for web scraping
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.9999.99 Safari/537.36"}

    # Define URL based on category
    url = f"https://www.theonion.com/{category}"

    # Fetch webpage content
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BSoup(response.content, "html.parser")
        articles = soup.find_all("div", class_="sc-1ghoMqc-0 fjQuPs")
        
        # Extract and save headlines
        for article in articles:
            headline_element = article.find("h2", class_="sc-1vrra3l-0 hkgnrk sc-759qgu-0 cvZkKd")
            if headline_element:
                title = headline_element.get_text(strip=True)
                
                link_element = article.find("a", class_="sc-1out364-0 dPMosf js_link", href=True)
                if link_element:
                    link = link_element["href"]
                    
                    img_element = article.find("img", class_="sc-1n4z0lw-1 gfolKV")
                    if img_element:
                        image_url = img_element["src"]

                        # Create and save Headline object
                        Headline.objects.create(title=title, url=link, image=image_url)

    return redirect("../")

def news_list(request):
    # Retrieve headlines
    headlines = Headline.objects.all().order_by('-id')
    context = {"headlines": headlines}
    return render(request, "home.html", context)
