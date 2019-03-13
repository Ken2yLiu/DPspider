# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
from time import *
from pyvirtualdisplay import Display

def dazhongdianping_login(phone):
    '''
    大众点评模拟登陆,随机睡眠
    :param phone: 手机号
    :return: 登陆的cookie
    '''

    display = Display(visible=0, size=(800,800))
    display.start()
    driver = webdriver.Chrome('/data/data/dianping/chromedriver')
    driver.get('http://www.dianping.com/')
    # assert "Python" in driver.title
    # elem = driver.find_element_by_id('kw')
    # elem.send_keys("大众点评")
    # elem.send_keys(Keys.RETURN)
    # 自动点击登陆
    sleep(random.uniform(1, 3))
    elem = driver.find_element_by_xpath(r'//*[@id="top-nav"]/div/div[2]/span[2]/a[1]')
    elem.click()
    # 切入网页框架
    sleep(random.uniform(1, 3))
    driver.switch_to.frame(driver.find_element_by_xpath(r'//*[@id="J_login_container"]/div/iframe'))  # 切入
    # 点击账号登录
    driver.find_element_by_xpath(r"/html/body/div/div[2]/div[5]/span").click()

    # print(driver.page_source)
    # 输入验证码
    sleep(random.uniform(1, 3))
    driver.find_element_by_xpath(r'//*[@id="mobile-number-textbox"]').send_keys(phone[:3])
    sleep(random.uniform(0,2))
    driver.find_element_by_xpath(r'//*[@id="mobile-number-textbox"]').send_keys(phone[3:7])
    sleep(random.uniform(0,2))
    driver.find_element_by_xpath(r'//*[@id="mobile-number-textbox"]').send_keys(phone[7:])

    # 点击获取验证码,等待输入
    sleep(random.uniform(1, 3))
    driver.find_element_by_xpath(r'//*[@id="send-number-button"]').click()
    key = input('请输入验证码:')
    driver.find_element_by_xpath(r'//*[@id="number-textbox"]').send_keys(key)
    # 点击登陆
    sleep(random.uniform(0,1))
    driver.find_element_by_xpath(r'//*[@id="login-button-mobile"]').click()
    driver.switch_to.default_content() # 切出框架
    sleep(random.uniform(2,3))
    # 处理cookie
    cookie = driver.get_cookies()
    result = {}
    for each in cookie:
        result[each['name']] = each['value']
    return result

if __name__ == "__main__":
    f = open('login_cookie.txt', 'w')
    phone = '15625153210'
    cookie_dict = dazhongdianping_login(phone)
    cookie_str = ''
    for key,val in cookie_dict.items():
        cookie_str += '{}:{};'.format(key,val)
    f.write(cookie_str)
    f.close()
