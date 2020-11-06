import time
from selenium import webdriver

driver = webdriver.Chrome('PATH_TO_WEBDRIVER')
print("Your credentials are not stored or passed anywhere.\n---------------------------------------------------")
username = input("Enter username : ")
password = input("Enter your password : ")
victimName = input("Enter the victim's username : ")
message = input("Enter the message to send : ")

driver.implicitly_wait(10)
driver.get('https://instagram.com/direct/inbox')

#Provide username and password and clicks proceed
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(username)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()

#Directs to messaging window by dismissing pop-ups
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()

#Clicks search bar and find the person. Then enter the chat
driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(victimName)
driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div[1]/div/div[3]/button').click()
time.sleep(1)
driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/div/button').click()
time.sleep(3)

while(True):
    driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(message)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
