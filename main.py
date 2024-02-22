import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

###############################################################
chrome_driver_path = 'Brain\\chromedriver.exe'
extension_path = 'metamask\\11.9.5_0.crx'
options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--log-level=3')
options.add_argument("--use-fake-ui-for-media-stream")
options.add_argument("--use-fake-device-for-media-stream")
options.add_extension(extension_path)
service = Service(chrome_driver_path)
#################################################################

def createnewaccount(driver):
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.ID, "onboarding__terms-checkbox"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/ul/li[2]/button"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/button[1]"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[1]/label/input"))).send_keys("12345678")
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input"))).send_keys("12345678")
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[3]/label/input"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/button"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/button[1]"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/section/div[1]/div/div/label/input"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/section/div[2]/div/button[2]"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/button"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/button"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/button"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/section/div[1]/div/button/span"))).click()

def metamasklogin(driver):
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.ID, "onboarding__terms-checkbox"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/ul/li[3]/button"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/button[1]"))).click()
    x = ["proud", "prevent", "become", "wage", "minimum", "gadget", "chronic", "number", "dumb", "kidney", "citizen", "clog"]
    for i in range(0,12):
        WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.ID, f"import-srp__srp-word-{i}"))).send_keys(x[i])

    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/button"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[1]/label/input"))).send_keys("12345678")
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input"))).send_keys("12345678")
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[3]/label/input"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/button"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/button"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/button"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/button"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/section/div[1]/div/button/span"))).click()

def metamaskapprove(driver):
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[-1])
    click_button_by_text = """
    var buttons = document.querySelectorAll('button');
    for (var i = 0; i < buttons.length; i++) {
        if (buttons[i].textContent.includes('%s')) {
            buttons[i].click();
            break;
        }
    }
    """
    driver.execute_script(click_button_by_text % 'Next')
    time.sleep(1)
    driver.execute_script(click_button_by_text % 'Connect')
    time.sleep(2)
    driver.execute_script(click_button_by_text % 'Approve')
    time.sleep(1)
    driver.execute_script(click_button_by_text % 'Switch network')

    driver.switch_to.window(driver.window_handles[1])

####################################################################


for i in range(1):
    driver = webdriver.Chrome(service=service, options=options)

    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    driver.refresh()

    metamasklogin(driver)

    driver.get('https://goerli.rio.network/')

    driver.switch_to.window(driver.window_handles[1])

    # taskmonitor(driver)

    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/nav/div[1]/div/div/nav/div[5]/button/span"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div/div[2]/div/label[1]/input"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div/div[3]/button"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div/div/div[2]/div/div/div/div/div/div[2]/div[2]/div[3]/button/div/div/div[2]/div"))).click()
    
    metamaskapprove(driver)

    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/main/div[1]/div/div/div[1]/div/div/div[2]/div[1]/label/div/div[1]/input"))).send_keys('123456')

    input("Press Enter to close the browser...")
    driver.quit()