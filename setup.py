import os
c = input("Choose your environment: [0] pip / [1] pip3 : ")

if c == "0":
    os.system("pip install cloudscraper")
    os.system("pip install socks")
    os.system("pip install pysocks")
    os.system("pip install colorama")
    os.system("pip install httpx")
    os.system("pip install undetected_chromedriver")
elif c == "1":
    os.system("pip3 install cloudscraper")
    os.system("pip3 install socks")
    os.system("pip3 install pysocks")
    os.system("pip3 install colorama")
    os.system("pip3 install undetected_chromedriver")
    os.system("pip3 install httpx")


print("Done.")
