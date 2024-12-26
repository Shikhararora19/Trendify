from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

import time

gecko_driver_path = "/Users/shikhararora/Downloads/geckodriver"
service = Service(gecko_driver_path)

# Initialize WebDriver
def initialize_driver():
    options = Options()
    options.add_argument('--headless')  # Enable headless mode
    options.add_argument('--disable-gpu')  # Disable GPU acceleration (optional)
    options.add_argument('--no-sandbox')  # Optional for some environments
    options.add_argument('--window-size=1920,1080')  # Optional, set a default window size
    return webdriver.Firefox(service=service, options=options)

# Scrape Google Trends
def scrape_google_trends(location):
    trends = []
    driver = initialize_driver()
    try:
        url = f"https://trends.google.com/trends/trendingsearches/daily?geo={location}"
        driver.get(url)
        time.sleep(5)
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tbody tr"))
        )
        rows = driver.find_elements(By.CSS_SELECTOR, "tbody tr")
        for row in rows:
            try:
                trend_name_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(2) div")
                trend_name = trend_name_element.text.strip()

                # Find the link to the detailed page
                trend_link_element = row.find_element(By.CSS_SELECTOR, "a")
                trend_link = trend_link_element.get_attribute("href")

                # Append the trend name and link as a dictionary
                trends.append({"name": trend_name, "link": trend_link})
            except Exception as e:
                print(f"Error in row: {e}")
        trends = [trend for trend in trends if trend]  # Remove empty strings   
    except Exception as e:
        print(f"Error scraping Google Trends: {e}")
    finally:
        driver.quit()
    return trends

# Scrape Reddit Trends
def scrape_reddit(location):
    reddit_trends = []
    driver = initialize_driver()
    try:
        # Example: Filter by country-specific subreddits or global content
        url = f"https://www.reddit.com/r/all/"
        driver.get(url)
        time.sleep(10)
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[slot='title']"))
        )
        posts = driver.find_elements(By.CSS_SELECTOR, "a[slot='title']")
        
        # Extract title and link for each post
        for post in posts[:10]:  # Limit to the first 10 posts
            post_title = post.text.strip()  # Extract the title
            post_link = post.get_attribute("href")  # Extract the link
            reddit_trends.append({"name": post_title, "link": post_link})
    except Exception as e:
        print(f"Error scraping Reddit: {e}")
    finally:
        driver.quit()
    return reddit_trends



# Scrape YouTube Trends
def scrape_youtube(location):
    youtube_trends = []
    driver = initialize_driver()
    try:
        # Adjust the URL for localization. For example: `US` for United States
        url = f"https://www.youtube.com/feed/trending?gl={location}"
        driver.get(url)
        time.sleep(5)
        
        # Wait for the video elements to load
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a#video-title"))
        )
        
        # Get the video titles and links
        titles = driver.find_elements(By.CSS_SELECTOR, "a#video-title")
        for title in titles[:10]:  # Limit to the first 10 trends
            video_title = title.text.strip()  # Extract the video title
            video_link = title.get_attribute("href")  # Extract the video link
            youtube_trends.append({"name": video_title, "link": video_link})
    except Exception as e:
        print(f"Error scraping YouTube: {e}")
    finally:
        driver.quit()
    return youtube_trends



# Scrape BBC Headlines
def scrape_bbc(location):
    bbc_trends = []
    driver = initialize_driver()
    try:
        # Modify URL for regional content if available
        region_urls = {
            "US": "https://www.bbc.com/news",
            "GB": "https://www.bbc.com/news/uk",
            "IN": "https://www.bbc.com/news/world/asia/india",
            "AU": "https://www.bbc.com/news/world/australia"
        }
        url = region_urls.get(location, "https://www.bbc.com/news")
        driver.get(url)
        time.sleep(5)
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h2.sc-8ea7699c-3.kwWByH"))
        )
        headlines = driver.find_elements(By.CSS_SELECTOR, "h2.sc-8ea7699c-3.kwWByH")
        bbc_trends = [headline.text.strip() for headline in headlines[:10]]
    except Exception as e:
        print(f"Error scraping BBC News: {e}")
    finally:
        driver.quit()
    return bbc_trends


# Main Function
def main(location='US'):
    google_trends = scrape_google_trends(location)
    reddit_trends = scrape_reddit(location)
    youtube_trends = scrape_youtube(location)
    bbc_trends = scrape_bbc(location)
    return {
        "google_trends": google_trends,
        "reddit_trends": reddit_trends,
        "youtube_trends": youtube_trends,
        "bbc_trends": bbc_trends
    }


if __name__ == "__main__":
    trends_data = main()
    print(trends_data)
