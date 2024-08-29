import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import warnings
warnings.filterwarnings('ignore')
import urllib.request 

# browser EDGE 
driver = webdriver.Edge();
# browser CHROME
# driver = webdriver.Chrome();

# input data fixed argument (cat)
driver.get('https://www.flickr.com/search/?text=cats')
# input data member setting up 
driver.get('https://www.flickr.com/search/?text=cats')

time.sleep(2)
driver.maximize_window()
time.sleep(3)

# initialzation of current height.
temp_height = 0

while True:
    #Looping down the scroll bar
    driver.execute_script("window.scrollBy(0,1000)")
    #sleep and let the scroll bar react
    time.sleep(3)
    #Get the distance of the current scroll bar from the top
    check_height = driver.execute_script("return document.documentElement.scrollTop || window.pageYOffset || document.body.scrollTop;")
    #If the two are equal to the end
    print("temp_height",temp_height)
    print("check_height",check_height)
    if check_height==temp_height:
        break
    temp_height=check_height
    print("page scollled")

soup = BeautifulSoup(driver.page_source, 'html.parser')
all_div_tag = soup.find_all('div', 'photo-list-photo-container')

print(len(all_div_tag))
    
card = all_div_tag[0]
print(card)

imgTest = card.find('img')
print(imgTest)
print(imgTest['src'])

all_images = []
for everyTag in all_div_tag :
    img_tag = everyTag.find('img')
    img_tag = 'https:' + img_tag['src']
    all_images.append(img_tag)


pic_num = 1

for images in all_images :
    try :
        print(images)
        urllib.request.urlretrieve(images,'URL'+str(pic_num)+'.jpg')
        pic_num += 1
    except Exception as err :
        print("ERROR FOUND :" ,err)

'''
   / \__
  (    @\___
  /         O
 /   (_____/
/_____/   U

'''
