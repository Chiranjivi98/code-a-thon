#If you want to scrape a website:
#1.Use the API
#2.HTML WEB Scraping using some tool like bs4

#Step 0:Install all the rquirements if your pip is not added to your path 
#it will show an error no module named so type py -3 -m pip install and after 
#this your tool name
#pip install requests
#pip install bs4
#pip install html5lib

import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
url="https://www.amazon.in/l/21570135031/ref=s9_acss_bw_cg_LFENPC_4a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-1&pf_rd_r=WHVGHKCBRDDK28V1266W&pf_rd_t=101&pf_rd_p=8de60e3c-e172-4965-a5cc-cec2c9fc7fc3&pf_rd_i=21532970031"

#Step1:Get the html
r=requests.get(url)
htmlContent=r.content
#print(htmlContent)

#Step2:Parse the html
soup=BeautifulSoup(htmlContent,'html.parser')
#print(soup.pretiffy)

#Step3:Html tree travsrsal
#
#1.image
#print(type(image)) 
#2.Product Title
#print(type(title))
#3.Product Link
#print(type(title.string))
#4.Price
#print(type(price))
#5.Seller
#print(type(seller))
#6.BeautifulSoup
#print(type(soup)

# Get the title of the HTML page
#title = soup.title

# Get all the paragraphs from the page

# Get first element in the HTML page
# print(soup.find('p') ) 

# Get classes of any element in the HTML page
# print(soup.find('p')['class'])

# Get id of any element in the HTML page
# print(soup.find('p')['id'])

# find all the elements with class lead
# print(soup.find_all("p", class_="lead"))

# Get the text from the tags/soup
#print(soup.find('p').get_text())
#print(soup.get_text())

#Scraping the images
html = urlopen('https://www.amazon.in/l/21570135031/ref=s9_acss_bw_cg_LFENPC_4a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-1&pf_rd_r=WHVGHKCBRDDK28V1266W&pf_rd_t=101&pf_rd_p=8de60e3c-e172-4965-a5cc-cec2c9fc7fc3&pf_rd_i=21532970031')
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', {'src':re.compile('.jpg')})
for image in images: 
    print(image['src']+'\n')

#Scrapping the product link
# Get all the links on the page:
html = urlopen('https://www.amazon.in/l/21570135031/ref=s9_acss_bw_cg_LFENPC_4a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-1&pf_rd_r=WHVGHKCBRDDK28V1266W&pf_rd_t=101&pf_rd_p=8de60e3c-e172-4965-a5cc-cec2c9fc7fc3&pf_rd_i=21532970031')
bs = BeautifulSoup(html, 'html.parser')
for link in links:
    if(link.get('href') != '#'): 
        linkText = "https://www.amazon.com" +link.get('href')
        all_links.add(link)
        print(link)


#Scrapping the title




































































