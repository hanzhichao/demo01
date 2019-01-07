from selenium import webdriver

# dr = webdriver.Chrome()
# dr = webdriver.Ie()
dr = webdriver.Edge()


# chrome_capabilities = {
# 	"browserName": "chrome",
# 	"version": "",
# 	"platform": "ANY",
# 	"javascriptEnabled": True,
# 	# "webdriver.chrome.driver": chrome_driver
# }

# # dr = webdriver.Remote("http://127.0.0.1:5555/wd/hub", desired_capabilities=chrome_capabilities)
# dr = webdriver.Remote("http://{}:{}@ondemand.saucelabs.com:80/wd/hub".format("hanzhichao","9fd534b7-5fa4-4931-ae83-9462704ca4c9"), 
# 	desired_capabilities=chrome_capabilities)

dr.get("http://erp.secoo.com/authorization/index")
dr.maximize_window()
dr.implicitly_wait(10)

dr.find_element_by_id("managerName").send_keys("hanzhichao")
# dr.find_element_by_xpath("//*[text()='用户名']/following::input").send_keys("hanzhichao")
dr.find_element_by_id("managerPwd").send_keys("HANzhichao123")
# dr.find_element_by_xpath("//*[text()='密码']/following::input").send_keys("HANzhichao123")
dr.find_element_by_id("loginBth").click()


