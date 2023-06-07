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


options = undetected_chromedriver.ChromeOptions()
options.headless=True

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
        
        print("You could enter multiple parameters on one line, like s45 and 34)")
        protocol = input("Which protocol of proxy you want ([h] https,[s] https,[4] socks4, [5] socks5): ")
        anon_lvl = input("Which lvl of anon you want ([1] no,[2] low, [3] medium, [4] high): ")
        page = 0
        for i in range(1, 6):
            file_for_proxy = open("proxy.txt", "a")

            url = f'https://hidemy.name/ru/proxy-list/?type={protocol}&anon={anon_lvl}&start={page}#list'

            try:
                driver = undetected_chromedriver.Chrome()
                driver.get(url)


                time.sleep(15)
                with open("index.html", "w", encoding="utf-8") as file:
                    file.write(driver.page_source)
                    
            except Exception as ex:
                print(ex)
                
            finally:
                driver.close()
                driver.quit()

            with open("index.html", encoding="utf-8") as file:
                src = file.read()

            
            soup = BeautifulSoup(src, "lxml")
            try:
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

                            file_for_proxy.write(f"{line_for_import}\n")
                            
                        line.decompose()
                    except Exception as ex:
                        print(ex)
                page+=64
                
            except:
                print("!!! ERROR !!!")
            file_for_proxy.close()

    elif command == "01":
        pass
    elif command == "99":
        os.system("clear")
        exit()
    else:
        main()
    
if __name__ == "__main__":
    main()