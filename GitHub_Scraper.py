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

# Chrome will open and get particular data from particular website 

# on = True
# while on:
#     def five_seconds():
#         time.sleep(5)
#         cdp = "/home/yuva/Downloads/chromedriver-linux64/chromedriver" 
#         s = Service(executable_path=cdp)
#         driver = webdriver.Chrome(service=s)
#         # driver.get("https://www.google.com")
#         driver.get("https://www.amazon.in/Lifelong-Dumbbells-Equipment-Exercise-Warranty/dp/B09W5PSTBP/ref=zg_bs_c_sports_d_sccl_1/258-7507423-9619246?pd_rd_w=lsALK&content-id=amzn1.sym.7f3d66f6-5df6-41bc-b3bc-9782a34ce834&pf_rd_p=7f3d66f6-5df6-41bc-b3bc-9782a34ce834&pf_rd_r=M31N9YW7NZNKQCER7CR8&pd_rd_wg=bLXId&pd_rd_r=c9ffa48e-bfcf-40f1-a7f7-3cd7c29c6020&pd_rd_i=B09W5PSTBP&th=1")
#         price =  driver.find_element(By.CLASS_NAME, "a-price-whole")
#         print(price.text)
#         driver.quit()

#     five_seconds()

# ------------------------------------------------------------------------------------------------------------


cdp = "/home/yuva/Downloads/chromedriver-linux64/chromedriver" 
s = Service(executable_path=cdp)
driver = webdriver.Chrome(service=s)

driver.get("https://github.com/UserYourGitAccount")
repo = "https://github.com/UserYourGitAccount"
# time.sleep(4)
res = driver.find_elements(By.CLASS_NAME,"repo")
# time.sleep(4)

links = []
final_links = []

def going_for_raw(second_page):
    driver.get(second_page)
    raw = driver.find_element(By.CLASS_NAME,"prc-Button-Label-pTQ3x")
    raw.click()
    html = driver.page_source
    html = f"{html}"
    # print(html)
    if "Sorting" in html:
        print("found Sorting keyword")


def loop(next_page):
    global a
    driver.get(next_page)
    # time.sleep(4)
    res2 = driver.find_elements(By.CLASS_NAME, "Link--primary")
    for a in res2:
        # print(a.text)
        pass
    if "md" in a.text:
        # print("it worked md is in the text")
        second_page = f"{next_page}/blob/main/{a.text}"
        going_for_raw(second_page)
        # print(second_page)
        # time.sleep(2)


for i in res:
    links.append(i.text)
# print(links)   

for l in links:
    next_page = f"{repo}/{l}" 
    final_links.append(next_page)
    loop(next_page)
# print(final_links)       

driver.quit()


