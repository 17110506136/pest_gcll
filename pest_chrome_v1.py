import pyautogui
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.support.wait import WebDriverWait

# @Author  : li and he

driver = webdriver.Chrome()
# 最大化浏览器窗口
driver.maximize_window()

URL = r"https://ouc.yuketang.cn/pro/lms/7ZXK33nMfxK/15271993/graph/22294488"
# 设置WebDriverWait对象
wait = WebDriverWait(driver, 10)

# 登录
driver.get(URL)
time.sleep(1)
driver.find_element(By.CLASS_NAME, "login-btn").click()
time.sleep(2)
print("扫码登录")

# 创建 ActionChains 对象
actions = ActionChains(driver)

while True:
    try:
        driver.find_element(By.CLASS_NAME,'qr-img')
        print(".",end='')
        time.sleep(1)
    except:
        print("\n登录成功")
        time.sleep(1)
        break
time.sleep(1)


def monitor(driver):
    """
        播放进度监测
        :param driver:
        :return None:
        """
    span_Xpath = "/html/body/div[4]/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/section[1]/div[2]/div/div/span"
    while True:
        WCD = driver.find_element(By.XPATH, span_Xpath).text
        print(WCD)
        WCD = int(WCD.split('：')[1][:-1])
        if WCD == 100:
            print("播放完成\n##################")
            break
        time.sleep(2)

while True:
    # 判断有没有“下一单元”这一按键
    try:
        span_element = driver.find_element(By.XPATH, '//span[@class="f14 color6" and text()="下一单元"]')
        # 获取’下一单元‘的位置
        location4 = span_element.location
        location22 = [location4['x'], 0]
        # 判断有没有视频
        try:
            # 如果有，开始看视频
            print("开始找视频按钮")
            driver.find_element(By.CLASS_NAME, "xt_video_player_big_play_layer")
            print("有视频")
            time.sleep(2)
            driver.find_element(By.CLASS_NAME, "pause_show").click()
            # 监视视频进度
            monitor(driver)
            #点击下一单元
            pyautogui.moveTo(location4['x'] + 15, location4['y'] + 130, 0.5)
            span_element.click()
            # 移动到安全位置
            pyautogui.moveTo(location22[0], location22[1], 0.5)
            # 停两秒
            time.sleep(2)
        except Exception:
            # 点击下一单元按钮
            pyautogui.moveTo(location4['x']+15, location4['y']+130, 0.5)
            span_element.click()
            # 移动到安全位置
            pyautogui.moveTo(location22[0], location22[1], 0.5)
            time.sleep(2)

    except NoSuchElementException:
        print("end")
        break


