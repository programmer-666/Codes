from selenium import webdriver
import time

browser = webdriver.Edge('msedgedriver.exe')
browser.get('https://meet.google.com/vjd-zeuf-ahs')
time.sleep(5)
browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[9]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div/div[1]/span').click()

browser.close()