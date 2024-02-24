import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def createnewaccountsavekey(driver):
    #create full
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

    #copy wallet adress
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div/div[2]/div/div/div/div[1]/button[2]/div"))).click()
    walletadress = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/section/div[3]/div/div[2]/div/div/button/span[1]/div"))).text
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/section/div[1]/div[2]/button/span"))).click()
    #3dot click
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div/div/button/span"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div[2]/button[6]/div/div"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div[1]/div/button[4]/div/div[2]"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div[2]/div[2]/button"))).click()

    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/section/button[1]"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/section/button[2]"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/section/button[1]"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/section/button[1]"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/section/button[1]"))).click()

    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div/form/div/input"))).send_keys(12345678)
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/button[2]"))).click()

    #hold part
    holdbtn = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[3]/div/section/div[2]/button/span")))
    actions = ActionChains(driver)
    actions.click_and_hold(holdbtn).perform()
    #save in wallet.txt
    actions.release(holdbtn).perform()
    walletkey = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/div/div[2]/div/div/div/p"))).text
    with open('wallets.txt', 'a') as f:
        f.write(f"{walletkey}||{walletadress}\n")
        
#create new account dont save key
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
#LOGIN METAMASK WITH KEY
def metamaskloginwithkey(driver, key):
    key = key.split()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.ID, "onboarding__terms-checkbox"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/ul/li[3]/button"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div/button[1]"))).click()
    for i in range(0,12):
        WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.ID, f"import-srp__srp-word-{i}"))).send_keys(key[i])

    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/button"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[1]/label/input"))).send_keys("12345678")
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input"))).send_keys("12345678")
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[3]/label/input"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/button"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/button"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/button"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/button"))).click()
    WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/section/div[1]/div/button/span"))).click()
#approve metamask
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
    driver.execute_script(click_button_by_text % 'Sign')
    time.sleep(1)
    driver.execute_script(click_button_by_text % 'Confirm')
    time.sleep(1)
    driver.execute_script(click_button_by_text % 'Next')
    time.sleep(1)
    driver.execute_script(click_button_by_text % 'Connect')
    time.sleep(2)
    driver.execute_script(click_button_by_text % 'Approve')
    time.sleep(1)
    driver.execute_script(click_button_by_text % 'Switch network')
    driver.switch_to.window(driver.window_handles[1])

#sending wallet phrase for login

wallet = []
address = [] 

with open('wallets.txt', 'r') as f:
    for line in f:
        key, adress = line.strip().split("||")
        wallet.append(key)
        address.append(adress)
    
for i in range(1):
    metamaskloginwithkey(driver, wallet[i])
    metamaskloginwithkey(driver, address[i])

#change window
driver.switch_to.window(driver.window_handles[1])
# open a link 
driver.get('https://goerli.rio.network/')
#maximum window size 
driver.maximize_window()


