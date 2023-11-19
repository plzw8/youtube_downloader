import time

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service = Service(executable_path='./chromedriver')
driver = webdriver.Chrome(service=service)

url = 'https://www.youtube.com/@OpenAI/videos'  # YouTube video homepage
driver.get(url)

# Simulate scrolling to capture all videos
scroll_script = "window.scrollTo(0, document.documentElement.scrollHeight);"
for i in range(10):
    driver.execute_script(scroll_script)
    time.sleep(1)

# Extract video links
video_links = driver.find_elements(By.ID, "video-title-link")
print(f"find {len(video_links)} videos")

# Save the video links to a text file
with open("urls.txt", "w") as file:
    for video in video_links:
        link = video.get_attribute('href')
        title = video.get_attribute('title')
        print(f'title: {title}, link: {link}')
        file.write(link + "\n")

print(f'save in urls.txt')

driver.quit()
