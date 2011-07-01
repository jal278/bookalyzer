from mako.template import Template
import sys
import isbn

def postprocess(isbn):
 import os
 import crop
 os.system("convert book%s.png -gravity SouthEast -chop 200x50 pbook%s.png" % (isbn,isbn))
 crop.crop("pbook%s" % isbn)
 os.system("convert pbook%s_crop.png -depth 8 -alpha off -colorspace gray pbook%s.tif" % (isbn,isbn))
 os.system("tesseract pbook%s.tif book%s" % (isbn,isbn))

isbn=isbn.get_isbn(sys.argv[1]) #'0307377334'


height=1400 
page_turns=9
zooms=3

mytemplate=Template(filename="book_template.html")
out=mytemplate.render(ZOOMS=zooms,PAGE_TURNS=page_turns,ISBN=isbn,HEIGHT=height)
open("book.html","w").write(out)


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import selenium
import time

browser = webdriver.Firefox() # Get local session of firefox
browser.get("file:///home/joel/word_count/book.html") # Load page
time.sleep(1.0) # Let the page load, will be added to the API
element = browser.find_element_by_id("viewerCanvas")
element.send_keys(Keys.F11)
time.sleep(1.5) # Let the page load, will be added to the API
browser.get_screenshot_as_file("/home/joel/word_count/book%s.png" % isbn)
browser.close()

postprocess(isbn)
