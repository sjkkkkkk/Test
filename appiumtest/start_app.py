from appium import webdriver
desired_caps = {
'platformName': 'Android',
'deviceName':'cdcbe9be',
'platformVersion':'8.1.0',
'appPackage':'com.wm.getngo',
'appActivity' : 'com.wm.getngo.ui.activity.AppNavigateActivity'
}

driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)

