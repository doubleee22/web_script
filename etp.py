# import time
# import random
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import passes
# import input_list
# import web_list
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Firefox()
#
#
# def login(log, passw):  # clearing, typing log/pass, pressing button
#     EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.controls-Button__wrapper_viewMode-filled'))
#     driver.find_element(By.CSS_SELECTOR, 'input.controls-InputBase__nativeField_caretFilled').clear()
#     driver.find_element(By.CSS_SELECTOR, 'input.controls-InputBase__nativeField_caretFilled').send_keys(log)
#     time.sleep(random.randint(3, 5))  # random sleeps - anticaptcha XD
#     driver.find_element(By.CSS_SELECTOR, '.auth-AdaptiveLoginForm__inputBlock .controls-BaseButton__wrapper').click()
#     time.sleep(random.randint(3, 5))
#     driver.find_element(By.CSS_SELECTOR, 'input.controls-Password__nativeField_caretFilled').clear()
#     time.sleep(random.randint(3, 5))
#     driver.find_element(By.CSS_SELECTOR, 'input.controls-Password__nativeField_caretFilled').send_keys(passw)
#     time.sleep(random.randint(3, 5))
#     driver.find_element(By.CSS_SELECTOR, 'span.controls-Button__wrapper_viewMode-filled').click()
#
#
# def search_sbis(varsbis):  # same for other website - other CSS Selector IDs
#     driver.find_element(By.CSS_SELECTOR, 'input.controls-Field').clear()
#     time.sleep(2)
#     driver.find_element(By.CSS_SELECTOR, 'input.controls-Field').send_keys(varsbis)
#     EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.search-Input__searchButton'))
#     driver.find_element(By.CSS_SELECTOR, 'div.search-Input__searchButton').click()
#
#
# def sbis_full():  # same for other website
#     EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.search-Input__searchButton'))  # essential for this website only
#     search_sbis(input_list.inpl[0])
#     nsb = 1
#     for i in range(8):
#         time.sleep(random.randint(3, 5))
#         driver.switch_to.new_window('tab')
#         driver.get(web_list.sbis)
#         EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.search-Input__searchButton'))
#         search_sbis(input_list.inpl[nsb])
#         nsb = nsb + 1
#
#
# def check_login():  # if not logged in --> login and search, if already logged --> search
#     driver.switch_to.new_window('window')
#     driver.get(web_list.sbis)
#
#     if driver.current_url == web_list.sbislog:
#         login(passes.sbislog, passes.sbispass)
#         time.sleep(10)
#         sbis_full()
#     else:
#         sbis_full()
