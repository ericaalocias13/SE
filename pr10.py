from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import csv

with open(r'C:\xampp\htdocs\ssbs\assets\data.csv', 'r') as csvinput:
    print("Status:\nInput File opened successfully")
    with open(r'C:\xampp\htdocs\ssbs\assets\result.csv', 'w',newline='') as csvoutput:
        print("Status:\nOutput File opened successfully")
        writer = csv.writer(csvoutput)
        temp = 0

        for row in csv.reader(csvinput):
            writeOutput = []
            if (temp == 0):
                correction = row[0]
                correction = correction.replace("ï»¿", "")
                row[0] = correction

            driver = webdriver.Chrome(ChromeDriverManager().install())
            driver.get('http://localhost/ssbs/assets/login.php')
            driver.find_element_by_xpath("/html/body/div[1]/form/div[1]/input").send_keys(row[0])
            driver.find_element_by_xpath("/html/body/div[1]/form/div[2]/input").send_keys(row[1])
            driver.find_element_by_xpath("/html/body/div[1]/form/div[3]/button").click()
            sleep(0.7)

            try:
                driver.find_element_by_xpath("/html/body/h1")
                writeOutput.append("In Valid")
            except:
                writeOutput.append("Valid")
            
            writer.writerow(row+writeOutput)
