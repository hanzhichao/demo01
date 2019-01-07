from appium import webdriver
from time import sleep
import os

desired_caps = {
	"platformName": "Android",
	"platformVersion": "8.0.0",
	"deviceName": "0e41dda7",
	"appPackage": "com.secoo",
	"appActivity": "com.secoo.app.mvp.ui.activity.LauncherActivity",
	# "unicodeKeyboard": True,
	"resetKeyboard": True,
	"noReset": True
}

d = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
d.implicitly_wait(30)
search = d.find_element_by_id("com.secoo:id/home_search_input")
search.click()
sleep(1)
# hot = d.find_element_by_android_uiautomator('new UiSelector().text("热门搜索")')
# print(hot.text)
search2 = d.find_element_by_id("com.secoo:id/et_title_search")

# os.system("adb shell ime set com.sec.android.inputmethod/.SamsungKeypad")
# os.system("adb shell ime set com.baidu.input/.ImeService")
search2.send_keys("lv")
sleep(2)
d.find_element_by_android_uiautomator('new UiSelector().text("进入品牌")').click()
sleep(5)
print(d.contexts)
# search2.send_keys("\n")
# sleep(3)
# d.press_keycode(66)
# sleep(1)
# d.press_keycode(84)
# os.system("adb shell ime set io.appium.android.ime/.UnicodeIME")
# d.keyevent(3)
sleep(40)
d.quit()