import requests
import os
import sys
import time
from art import tprint
import fake_headers
from bs4 import BeautifulSoup
import lxml

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
        for i in range(1, 2):
            url = f'https://free-proxy.cz/ru/proxylist/country/all/{protocol}/ping/level{anon_lvl}/{i}'
            print(f'!!! for debug {url}')

            f_header = fake_headers.Headers(headers=True)
            head = f_header.generate()

            r = requests.get(url = url, headers=head)
            src = r.text
            
            soup = BeautifulSoup(src, "lxml")
            table_of_proxy = soup.find("table", id = "proxy_list")
            tbody = table_of_proxy.find("tbody")

            for j in range(1):
                line = tbody.find("tr")
                char = line.find_all("td")
                print(char)
                print(type(char))
                print(char[0])

    elif command == "01":
        pass
    elif command == "99":
        os.system("clear")
        exit()
    else:
        main()
if __name__ == "__main__":
    main()