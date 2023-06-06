import requests
import os
import sys
import time
from art import tprint
import fake_headers
from bs4 import BeautifulSoup
import lxml
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("User-Agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0")
#options.headless=True
#options.add_experimental_option('excludeSwitches', ['enable-logging'])

def drow_main_menu():
    os.system("clear")
    print("-"*42 + " by p4sh4bsc " + "-"*42)
    tprint("GET-FREE-PROXY")
    print("-"*42 + " by p4sh4bsc " + "-"*42)
    print()
    print("00 - get proxy")
    print("01 - update script")
    print("99 - exit")

def main():
    drow_main_menu()
    command = input()

    if command == "00":
        protocol = input("Which protocol of proxy you want (all/http/https/socks): ")
        anon_lvl = input("Which lvl of anon you want ([1] elite/[2] anonymous/[3] transparent ): ")
        for i in range(1, 6):
            

            url = f'https://hidemy.name/ru/proxy-list/?type=s45&anon=34&start=64#list'

            try:
                driver = undetected_chromedriver.Chrome()
                driver.get(url)


                time.sleep(10)
                with open("index.html", "w", encoding="utf-8") as file:
                    file.write(driver.page_source)
                    
            except Exception as ex:
                print(ex)
                
            finally:
                driver.close()
                driver.quit()

            driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
            with open("index.html", encoding="utf-8") as file:
                src = file.read()

            soup = BeautifulSoup(src, "lxml")
        
            table_of_proxy = soup.find("div", class_ = "table_block")
            tbody = table_of_proxy.find("tbody")

            for j in range(500):
                try:
                    line = tbody.find("tr")
                    char = line.find_all("td")
                    speed_full = char[3]
                    speed = str(speed_full.find("p"))
                    speed = speed[3:-7]
                    int_speed = int(speed)
                    
                    if int_speed <= 1000:
                        ip = str(char[0])[4:-5]
                        port = str(char[1])[4:-5]
                        line_for_import = f"{ip}:{port}"
                        print(line_for_import)
                    line.decompose()
                except:
                    pass


    elif command == "01":
        pass
    elif command == "99":
        os.system("clear")
        exit()
    else:
        main()
if __name__ == "__main__":
    main()