import yaml
import time

from module import Site

'''вынести все локаторы элементов в фикстуры в conftest.py
вынести ожидаемый результат в фикстуру в conftest.py
добавить завершение работы Selenium после теста
вынести время ожидания в конфигурационный файл testdata.yaml
Доработать программу, полученную в предыдущем задании
добавив туда шаг, в котором будет проверяться успешность
входа пользователя при вводе верного имени и пароля.
Имя и пароль должны храниться в конфигурационном файле.
Добавить в наш тестовый проект шаг добавления поста после входа. 
Должна выполняться проверка на наличие названия поста на странице сразу 
после его создания.'''

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)

site = Site(testdata["adress"])

def test_step1(site, log_xpath, pass_xpath, btn_xpath, result_xpath):
    input1 = site.find_element("xpath", log_xpath)
    input1.send_keys("test")
    input2 = site.find_element("xpath", pass_xpath)
    input2.send_keys("test")
    btn = site.find_element("xpath", btn_xpath)
    btn.click()
    err_label = site.find_element("xpath", result_xpath)
    assert err_label.text == "401"

def test_step2(site, log_xpath, pass_xpath, btn_xpath, result_login):
    input1 = site.find_element("xpath", log_xpath)
    input1.send_keys(testdata["login"])
    input2 = site.find_element("xpath", pass_xpath)
    input2.send_keys(testdata["password"])
    btn = site.find_element("xpath", btn_xpath)
    btn.click()
    login = site.find_element("xpath", result_login)
    assert login.text == "Blog"

def test_add_post(log_xpath, pass_xpath, btn_selector, add_post_selector, add_title, add_description,
                  add_content, save_post, check_title, title_name):

    input1 = site.find_element("xpath", log_xpath)
    input1.clear()
    input1.send_keys(testdata["login"])
    input2 = site.find_element("xpath", pass_xpath)
    input2.clear()
    input2.send_keys(testdata["password"])
    btn = site.find_element("css", btn_selector)
    btn.click()

    time.sleep(testdata["sleep_time"])

    btn = site.find_element("xpath", add_post_selector)
    btn.click()

    input3 = site.find_element("xpath", add_title)
    input3.clear()
    input3.send_keys(testdata["title"])
    input4 = site.find_element("xpath", add_description)
    input4.clear()
    input4.send_keys(testdata["description"])
    input5 = site.find_element("xpath", add_content)
    input5.clear()
    input5.send_keys(testdata["content"])
    btn = site.find_element("xpath", save_post)
    btn.click()

    time.sleep(testdata["sleep_time"])

    code_label = site.find_element("xpath", check_title).text
    assert code_label == title_name, "test 'add post' Failed"

    site.driver.close()