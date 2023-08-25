from selenium import webdriver
from selenium.webdriver.common.by import By
import web_list
from to_change import input_list
from to_change import passes
import sbis

driver = webdriver.Firefox()


def search_fabr(varfabr):
    driver.find_element(By.XPATH, 'id("search_query")').clear()  # clearing input field
    driver.find_element(By.XPATH, 'id("search_query")').send_keys(varfabr)  # typing in input field
    driver.find_element(By.XPATH, 'id("search_submit")').click()  # pressing 'search' button


def fabr_full():
    driver.get(web_list.fabr)  # open up website
    search_fabr(input_list.inpl[0])  # search for 1st keyword fom input_list
    nf = 1  # var for iteration
    for i in range(8):
        driver.switch_to.new_window('tab')  # creating new tab
        driver.get(web_list.fabr)  # opening a search page
        search_fabr(input_list.inpl[nf])  # search for next keyword from input_list
        nf = nf + 1  # iteration


def search_rost(varros):  # same for other website - other XPath IDs
    driver.find_element(By.XPATH, 'id("keywords")').clear()
    driver.find_element(By.XPATH, 'id("keywords")').send_keys(varros)
    driver.find_element(By.XPATH, 'id("start-search-button")').click()


def rost_full():  # same for other website
    driver.switch_to.new_window('window')  # creating a new window
    driver.get(web_list.rost)
    search_rost(input_list.inpl[0])
    nrt = 1
    for i in range(8):
        driver.switch_to.new_window('tab')
        driver.get(web_list.rost)
        search_rost(input_list.inpl[nrt])
        nrt = nrt + 1


def search_rosa(varrosa):  # same for other website - other XPath IDs
    driver.find_element(By.XPATH, 'id("f_keyword")').clear()
    driver.find_element(By.XPATH, 'id("f_keyword")').send_keys(varrosa)
    driver.find_element(By.XPATH, 'id("search_button")').click()


def rosa_full():  # same for other website
    driver.switch_to.new_window('window')
    driver.get(web_list.rosa)
    search_rosa(input_list.inpl[0])
    nra = 1
    for i in range(8):
        driver.switch_to.new_window('tab')
        driver.get(web_list.rosa)
        search_rosa(input_list.inpl[nra])
        nra = nra + 1


def sbis_full():  # need to authorise before searching, so sbis.py file created
    sbis.check_login()
