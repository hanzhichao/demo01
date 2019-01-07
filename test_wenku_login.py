import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time

class TestGroupSample(object):
    """
    文库测试
    """
    @pytest.mark.run(order=1)
    @allure.step(title='登录')
    def test_login(self):
        """登录百度文库"""
        global driver
        driver = webdriver.Chrome()
        driver.get("https://passport.baidu.com/v2/?login&u=http://wenku.baidu.com/user/mydocs")
        time.sleep(1)
        # 输入帐号密码并登录文库
        driver.find_element_by_id("TANGRAM__PSP_3__userName").click()
        driver.find_element_by_id("TANGRAM__PSP_3__userName").clear()
        driver.find_element_by_id("TANGRAM__PSP_3__userName").send_keys("13129321271")
        driver.find_element_by_id("TANGRAM__PSP_3__password").click()
        driver.find_element_by_id("TANGRAM__PSP_3__password").clear()
        driver.find_element_by_id("TANGRAM__PSP_3__password").send_keys("123456z")
        time.sleep(15)  # 输入验证码
        driver.find_element_by_id("TANGRAM__PSP_3__submit").click()
        time.sleep(3)

        # 初次登录需要清理掉提醒信息
        driver.find_element_by_css_selector("div.btn").click()
        assert driver.title == u"个人中心_百度文库"


    @pytest.mark.run(order=2)
    @allure.step(title='关闭浏览器')
    def test_logout(self):
        u"""退出百度文库"""
        print("logout")
        global driver
        time.sleep(2)

        # 移动鼠标到对应的位置
        above = driver.find_element_by_class_name("text-dec-under")
        time.sleep(5)
        ActionChains(driver).move_to_element(above).perform()

        # 无法直接定位到退出按钮，先move_to_element到设置按钮上
        driver.find_element_by_id("logout").click()
        assert driver.title == u"登录百度帐号"

    @pytest.mark.run(order=3)
    @allure.step(title='关闭浏览器')
    def test_groups_close(self):
        u"""关闭浏览器"""
        print("close")
        global driver
        driver.quit()


if __name__ == '__main__':
    # pytest.main("-s -q test_groups.py")
    # 取当前时间
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    pytest.main("-s -q test_wenku_login.py  --alluredir report-{0}".format(now))
    # 调用命令生成报告（Windows下面的方法）----------需要下载allure.exe
# os.system("C:\\Python27\\Lib\\allure-commandline\\bin\\allure generate report-{0}/ -o report-{0}/html".format(now))
