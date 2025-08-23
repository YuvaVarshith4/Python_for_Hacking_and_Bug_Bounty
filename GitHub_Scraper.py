from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# ------------------------------------------------------------------------------------------------------------

# # Chrome will open and shutdown as well as print the version of it
# Serv = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=Serv)

# driver.get("https://www.google.com")

# chrome_version = driver.capabilities['browserVersion']

# print(f"Chrome Browser Version: {chrome_version}")
# driver.quit()

# ------------------------------------------------------------------------------------------------------------

# Chrome will open and shutdown within seconds 

cdp = "/home/yuva/Downloads/chromedriver-linux64/chromedriver" 
s = Service(executable_path=cdp)
def check_price():
    driver = webdriver.Chrome(service=s)
    # driver.get("https://www.google.com")
    try:
        time.sleep(5)
        driver.get("https://www.amazon.in/Lifelong-Dumbbells-Equipment-Exercise-Warranty/dp/B09W5PSTBP/ref=zg_bs_c_sports_d_sccl_1/258-7507423-9619246?pd_rd_w=lsALK&content-id=amzn1.sym.7f3d66f6-5df6-41bc-b3bc-9782a34ce834&pf_rd_p=7f3d66f6-5df6-41bc-b3bc-9782a34ce834&pf_rd_r=M31N9YW7NZNKQCER7CR8&pd_rd_wg=bLXId&pd_rd_r=c9ffa48e-bfcf-40f1-a7f7-3cd7c29c6020&pd_rd_i=B09W5PSTBP&th=1")
        price =  driver.find_element(By.CLASS_NAME, "a-price-whole")
        print(price.text)
    except Exception as e:
        print("Error:", e)
    finally:
        driver.quit()

on = True
while on:
    check_price()
    # break         


