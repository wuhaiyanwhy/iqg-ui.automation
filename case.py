from appium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
from appium.webdriver.common.touch_action import TouchAction


desired_caps = {'platformName': 'Android',
                'platformVersion': '8.1.0',
                'deviceName': 'Honor V8HUAWEI P20-EML-AL00-CLB7N18529009476',
                # 'automationName': 'UiAutomator2',
                'app': "C:\\Users\\dwdtwster\\Desktop\\app-beta-release.apk"
                }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(5)
print(driver.get_window_size())
x = driver.get_window_size()['width']
y = driver.get_window_size()['height']
for i in range(3):
        driver.swipe(9/10*x, 1/2*y, 1/10*x, 1/2*y, 200)
        time.sleep(1)   
driver.find_element_by_id("com.iqianggou.android:id/city_name").click()






# driver.swipe(1/7*x, 1/2*y, 5/7*x, 1/2*y, 300)
# time.sleep(1)
# driver.swipe(1/7*x, 1/2*y, 5/7*x, 1/2*y, 300)
# time.sleep(1)
# driver.swipe(1/7*x, 1/2*y, 5/7*x, 1/2*y, 300)
# time.sleep(1)

class Test(unittest.TestCase):
        def test_login(self):
                driver.find_element_by_android_uiautomator("text(\"我的\")").click()
                driver.find_element_by_android_uiautomator("text(\"注册/登录\")").click()
                driver.find_element_by_id("com.iqianggou.android:id/tv_password_login").click()
                time.sleep(2)
                # driver.find_element_by_id("com.iqianggou.android:id/mobile_field").send_keys('15261875682')
                driver.find_element_by_id("com.iqianggou.android:id/password_field").send_keys('123456')
                driver.find_element_by_id("com.iqianggou.android:id/login_btn").click()
                time.sleep(2)

        def test_activity(self):
                driver.find_element_by_android_uiautomator("text(\"往下拍\")").click()
                time.sleep(2)
                driver.swipe(1/2*x, 1/2*y, 1/2*x, 1/3*y, 200)
                driver.find_element_by_android_uiautomator("text(\"添加活动test\")").click()
                driver.find_element_by_id("com.iqianggou.android:id/btn_buy").click()
                time.sleep(1)
                # driver.find_element_by_android_uiautomator("text(\"确定\")").click()
                # 设定系数
                a = 500/1080
                b = 1200/2244
                driver.tap([(a*x, b*y)],2)  
                time.sleep(3)  
                #点击x号 
                a = 70/1080
                b = 700/2244
                driver.tap([(a*x, b*y)],2) 
                time.sleep(2)
                #点击左上角退出订单
                a = 90/1080
                b = 150/2244
                driver.tap([(a*x, b*y)],2) 
                time.sleep(1)
                driver.find_element_by_android_uiautomator("text(\"狠心抛弃\")").click()
                driver.find_element_by_class_name("android.widget.ImageButton").click()
                time.sleep(2)

        def test_pagedview(self):
                driver.find_element_by_android_uiautomator("text(\"精品套餐\")").click()
                driver.find_element_by_android_uiautomator("text(\"异国风情\")").click() 
                driver.find_element_by_android_uiautomator("text(\"火锅烤串\")").click()
                driver.find_element_by_android_uiautomator("text(\"虾兵蟹将\")").click()
                driver.find_element_by_android_uiautomator("text(\"大牌美食\")").click()
                for i in range(4):
                        driver.swipe(1/7*x, 1/2*y, 5/7*x, 1/2*y, 300)
                        time.sleep(1)

        def test_ticket(self):
                driver.find_element_by_id("com.iqianggou.android:id/tab_discovery_title").click()
                driver.find_element_by_android_uiautomator("#text(\"泉鲤(徐汇日月光店)\")").click()
                driver.find_element_by_id("com.iqianggou.android:id/btn_submit").click()
                driver.find_element_by_android_uiautomator('new UiSelector().textContains(\"金币支付\")').click()
                driver.find_element_by_android_uiautomator('new UiSelector().textContains(\"确认支付\")').click()
                driver.find_element_by_id("com.iqianggou.android:id/btn_order_list").click()
                time.sleep(2)
                a = 900/1080
                b = 500/2244
                x = driver.get_window_size()['width']
                y = driver.get_window_size()['height']
                driver.tap([(a*x, b*y)],2) 
                driver.find_element_by_android_uiautomator("text(\"店码\")").click()
                driver.find_element_by_id("com.iqianggou.android:id/layout_code_view").send_keys('1234')
# if __name__ == "__main__":
#         unittest.main()

from HTMLTestRunner_PY3 import HTMLTestRunner
testcase=unittest.TestSuite()              #实例化对象，创建一个测试集
testcase.addTests([Test('test_login'),Test('test_activity'),Test('test_pagedview'),Test('test_ticket')])    #添加测试用例列表
# testcase.addTests(unittest.TestLoader().loadTestsFromTestCase())
f=open(r"C:\Users\dwdtwster\Desktop\test.html",'wb')    #定义报告生成的路径
runner=HTMLTestRunner(stream=f,title='爱抢购ui自动化测试报告',description='简单描述')
runner.run(testcase)







# class Test(unittest.TestCase):
#     def test_login(self):
        
        # time.sleep(2)
        
        
# if __name__ == "__main__":
#     unittest.main()
    
    




