from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep
from test2 import first_comment

def check_for_new_video(channel_url):
    
    chrome_options = Options()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('disable-gpu')
    chrome_options.add_argument('log-level=3')
    
    # Launch the Chrome browser
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        previous_link = None
        while True: 
            # Open the YouTube channel URL
            driver.get(channel_url)
            
            #print("hi")
            # Wait for the videos to load (increased timeout to 30 seconds)
            result = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.yt-simple-endpoint.focus-on-expand.style-scope.ytd-rich-grid-slim-media')))
            # print(result)
            # #log.debug(result)
            
            # # Find the first video element
            # video_element = driver.find_element(By.CSS_SELECTOR, 'ytd-rich-grid-media')
            # print("video element:", video_element)
            # Get the title of the first video
           

            video_link = None

            for element in result:
                video_link = element.get_attribute('href')
                break
            #print(video_link)
            if video_link != previous_link:
                print("New video title:", video_link)
                previous_link = video_link
                first_comment()

        
            sleep(1)
            #print("checking...")
            driver.refresh()
        # You can implement further logic here to compare the latest video title with a previously stored title to check for new uploads
        
    finally:
        # Close the browser
        driver.quit()

# Example usage: provide the URL of the YouTube channel you want to check
channel_url = "https://www.youtube.com/@bokyemtv/shorts"
check_for_new_video(channel_url)
