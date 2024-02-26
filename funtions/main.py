import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from funtions.metamskall import *
from selenium.common.exceptions import NoSuchWindowException

chrome_driver_path = 'Brain\\chromedriver.exe'
extension_path = 'metamask\\11.9.5_0.crx'
options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--log-level=3')
options.add_argument("--use-fake-ui-for-media-stream")
options.add_argument("--use-fake-device-for-media-stream")
options.add_extension(extension_path)
service = Service(chrome_driver_path)

class MetamaskHandler:
    def __init__(self, driver):
        self.driver = driver

    def create_new_account_save_key(self, savekey=True):
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.ID, "onboarding__terms-checkbox"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/ul/li[2]/button"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/button[1]"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[1]/label/input"))).send_keys("12345678")
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input"))).send_keys("12345678")
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[3]/label/input"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/button"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/button[1]"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/section/div[1]/div/div/label/input"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/section/div[2]/div/button[2]"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/button"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/button"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/button"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/section/div[1]/div/button/span"))).click()
        if savekey == True:
            #copy wallet adress
            WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div[2]/div/div/div/div[1]/button[2]/div"))).click()
            walletadress = WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/section/div[3]/div/div[2]/div/div/button/span[1]/div"))).text
            WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/section/div[1]/div[2]/button/span"))).click()
            #3dot click
            WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div/div/button/span"))).click()
            WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div[2]/button[6]/div/div"))).click()
            WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div[1]/div/button[4]/div/div[2]"))).click()
            WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div[2]/div[2]/button"))).click()

            WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/section/button[1]"))).click()
            WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/section/button[2]"))).click()
            WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/section/button[1]"))).click()
            WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/section/button[1]"))).click()
            WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/section/button[1]"))).click()

            WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div/form/div/input"))).send_keys(12345678)
            WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/button[2]"))).click()

            #hold part
            holdbtn = WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/section/div[2]/button/span")))
            actions = ActionChains(self.driver)
            actions.click_and_hold(holdbtn).perform()
            #save in wallet.txt
            actions.release(holdbtn).perform()
            walletkey = WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div/div/div/p"))).text
            with open('wallets.txt', 'a') as f:
                f.write(f"{walletkey}||{walletadress}\n")
            WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div/div[3]/button"))).click()

    def metamask_login_with_key(self, key=None):
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.ID, "onboarding__terms-checkbox"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/ul/li[3]/button"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/button[1]"))).click()

        if key is None:
            key = ["proud", "prevent", "become", "wage", "minimum", "gadget", "chronic", "number", "dumb", "kidney", "citizen", "clog"]
        else:
            key = key.split()
        
        for i in range(0,12):
            WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.ID, f"import-srp__srp-word-{i}"))).send_keys(key[i])

        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/button"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[1]/label/input"))).send_keys("12345678")
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input"))).send_keys("12345678")
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[3]/label/input"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/button"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/button"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/button"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/button"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/section/div[1]/div/button/span"))).click()   

    def metamask_approve(self):
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        click_button_by_text = """
        var buttons = document.querySelectorAll('button');
        for (var i = 0; i < buttons.length; i++) {
            if (buttons[i].textContent.includes('%s')) {
                buttons[i].click();
                break;
            } else {
            console.log('not found');
        }
        }
        """
        try:
            self.driver.execute_script(click_button_by_text % 'Sign')
            time.sleep(1)
            self.driver.execute_script(click_button_by_text % 'Confirm')
            time.sleep(1)
            self.driver.execute_script(click_button_by_text % 'Next')
            time.sleep(1)
            self.driver.execute_script(click_button_by_text % 'Connect')
            time.sleep(2)
            self.driver.execute_script(click_button_by_text % 'Approve')
            time.sleep(1)
            self.driver.execute_script(click_button_by_text % 'Switch network')
            self.driver.switch_to.window(self.driver.window_handles[1])
        except NoSuchWindowException:
            self.driver.switch_to.window(self.driver.window_handles[1])
            pass

    def login_with_custom_rpc(self, rpc_details, walletkey=None):
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.ID, "onboarding__terms-checkbox"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/ul/li[3]/button"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/button[1]"))).click()
        if walletkey is None:
            walletkey = ["proud", "prevent", "become", "wage", "minimum", "gadget", "chronic", "number", "dumb", "kidney", "citizen", "clog"]
        else:
            walletkey = walletkey.split()

        for i in range(0,12):
            WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.ID, f"import-srp__srp-word-{i}"))).send_keys(walletkey[i])

        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/button"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[1]/label/input"))).send_keys("12345678")
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input"))).send_keys("12345678")
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[3]/label/input"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/button"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/button"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/button"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/button"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/section/div[1]/div/button/span"))).click()

        #going to menu
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[1]/button"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/section/div[5]/button"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[3]/a/h6"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/label/input"))).send_keys(rpc_details[0])
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/label/input"))).send_keys(rpc_details[1])
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/label/input"))).send_keys(rpc_details[2])
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[4]/div/input"))).send_keys(rpc_details[3])
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[5]/label/input"))).send_keys(rpc_details[4])
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[3]/button[2]"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/section/div[2]/div/button[1]/h6"))).click()
        
    def login_with_chainlist(self, rpcurl, walletkey=None):
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.ID, "onboarding__terms-checkbox"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/ul/li[3]/button"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/button[1]"))).click()
        if walletkey is None:
            walletkey = ["proud", "prevent", "become", "wage", "minimum", "gadget", "chronic", "number", "dumb", "kidney", "citizen", "clog"]
        else:
            walletkey = walletkey.split()

        for i in range(0,12):
            WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.ID, f"import-srp__srp-word-{i}"))).send_keys(walletkey[i])

        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/button"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[1]/label/input"))).send_keys("12345678")
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input"))).send_keys("12345678")
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[3]/label/input"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/button"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/button"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/button"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/button"))).click()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/section/div[1]/div/button/span"))).click()

        driver.get(rpcurl)
        
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/header/div/div[2]/button"))).click()
        self.metamask_approve()
        WebDriverWait(self.driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/button"))).click()
        self.metamask_approve()

wallet = []
address = []
with open('wallets.txt', 'r') as f:
    for line in f:
        key, adress = line.strip().split("||")
        wallet.append(key)
        address.append(adress)

for i in range(1):
    driver = webdriver.Chrome(service=service, options=options)
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[1])
    driver.refresh()
    metamask_handler = MetamaskHandler(driver)

    metamask_handler.metamask_login_with_key(wallet[i])
  
    ######################### Do task here ############################
    driver.get('https://beoble.app')
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div[2]/div/div/main/div[1]/div/div[1]/div/div[2]/div/button"))).click()
    #####################################################
    input("Press Enter to close the browser...")

    driver.quit()
