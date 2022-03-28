from selenium import webdriver
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(ChromeDriverManager().install())

url = 'https://ehandboken.ous-hf.no/Printing/PrintDocument?documentId=14633'

driver.get(url)
texts = []
#tables = ui.WebDriverWait(driver, 50).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "document-name")))
driver.find_elements(By.CLASS_NAME, 'text-ellipsis')
#rows = []
#for table in tables:
#    #row = table.find_element(By.TAG_NAME, 'td')
#    rows.append(table.text())
#print(rows)


#%%
