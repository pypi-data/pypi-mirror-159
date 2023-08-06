import time,os
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import websocket
from threading import Thread
import datetime, time,requests
from webdriver_manager.chrome import ChromeDriverManager


class WhatsAppScraper:
    def __init__(self, url="https://web.whatsapp.com/"):
        self.options = webdriver.ChromeOptions() 
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option("useAutomationExtension", False)
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_argument("disable-infobars")
        self.options.add_argument("--window-size=1280,10000")
        self.options.add_argument("--disable-extensions")
        self.options.add_argument(f'user-data-dir={os.path.realpath("./data")}') 
        self.capabilities = DesiredCapabilities.CHROME
        self.capabilities["goog:loggingPrefs"] = {"performance": "ALL"}
        chrome_service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=chrome_service,options=self.options,desired_capabilities=self.capabilities)
        self.people = []
        self.palavras=['imports','multimarcas','griff','loja','roupa','roupas','masculina','marcas','modas']
        self.url=url
        self.groupWords = ['GROUP', '+', 'GRUPO']
        self.contacts_name=[]

    def login(self):
        '''valid login and wait complete load
        '''
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(3)
        print('wait login')
        #wait for the login to happen
        element = WebDriverWait(self.driver, 60).until_not(EC.presence_of_element_located((By.CLASS_NAME, "landing-header")))
        print('login sucess')
        time.sleep(2)

    def get_all_names_contacts(self):
        '''get all the names of your whatsapp contacts
        :return: self.contacts_name - constains all names
        :rtype: array (1D) 
        '''
        self.contacts_id=[]
        last_round=[]
        while len(self.driver.find_elements(By.XPATH , '//*[@data-testid="back"]')):
            try:self.driver.find_element(By.XPATH , '//*[@data-testid="back"]').click()
            except:break
        self.driver.find_element(By.XPATH , '//*[@data-testid="chat"]').click()
        pane=self.driver.find_element(By.XPATH , '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div[2]')
        for x in range(1000):
            round_=[]
            con_ = self.driver.find_elements(By.XPATH , '//*[@dir="auto" and not(contains(@class, "copyable-text"))]')
            for con in con_[1:]:
                try:name_con=con.get_attribute('title')
                except:continue
                #print(name_con)
                if name_con not in self.contacts_id:
                    self.contacts_id.append(name_con)
                    round_.append(name_con)
            if last_round==round_:break
            else:last_round=round_
            self.driver.execute_script("arguments[0].scrollTop = arguments[1]", pane, 400*(x+1))
        self.contacts_name=self.contacts_id
        return self.contacts_name
            

    def get_my_contacts(self):
        '''get all the numbers of your contacts
        :return: self.contacts [[name, number],...]
        :rtype: array (2D) 
        '''
        if not len(self.contacts_name):
            self.get_all_names_contacts()
        self.contacts=[]
        self.name_number={}
        self.number_name={}
        contacts_id=[]
        while len(self.driver.find_elements(By.XPATH , '//*[@data-testid="back"]')):
            try:self.driver.find_element(By.XPATH , '//*[@data-testid="back"]').click()
            except:break
        time.sleep(1)
 
        for name in self.contacts_name:
            while True:
                try:self.driver.find_element(By.XPATH , '//*[@data-testid="x-alt"]').click()
                except:pass
                try:
                    textbox=self.driver.find_element(By.XPATH , '//*[@role="textbox"]')
                    textbox.send_keys(name)
                    break
                except:
                    try:
                        self.driver.refresh()
                        textbox = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH , '//*[@role="textbox"]')))
                        time.sleep(2)
                        textbox=self.driver.find_element(By.XPATH , '//*[@role="textbox"]')
                        textbox.send_keys(name)
                        break
                    except:pass
                    
            time.sleep(0.5)
            acout=self.driver.find_elements(By.XPATH , f'//*[@title="{name}"]')
            if len(acout):
                acout[0].click()
                time.sleep(0.3)
                head_info = self.driver.find_element(By.XPATH, '//*[@data-testid="conversation-info-header"]')
                head_info.click()
                time.sleep(0.4)
                for number_find in self.driver.find_elements(By.CLASS_NAME , 'copyable-text'):
                    number = number_find.text
                    if '+' in number and '-' in number and len(number)<26:
                        print([name,number])
                        self.contacts.append([name,number])
                        self.name_number[name]=number
                        self.number_name[number]=name
                        break
                textbox.clear()
            
            for x in a.driver.find_elements(By.XPATH , '//*[@data-testid="cell-frame-container"]'):
                if name == x.text:pass
                
        return self.contacts
                    
