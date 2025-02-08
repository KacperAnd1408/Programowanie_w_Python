import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
response = requests.get(url=url)

amazon_response = requests.get("https://www.udemy.com/", headers={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Opera GX\";v=\"114\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0",
})

soup = BeautifulSoup(response.text, 'html.parser')
price_whole = soup.find(name='span', class_='a-price-whole').getText()
price_fraction = soup.find(name='span', class_='a-price-fraction').getText()
price = float(price_whole + price_fraction)

title = soup.find(id="productTitle").getText().strip()

target_price = 100

if price < target_price:
    message = f'{title}is on sale for {price}!'

    with smtplib.SMTP(os.environ['SMTP_ADDRESS'], port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ['EMAIL_ADDRESS'], os.environ['EMAIL_PASSWORD'])
        connection.sendmail(
            from_addr=os.environ['EMAIL_ADDRESS'],
            to_addrs=os.environ['EMAIL_ADDRESS'],
            msg=f'Subject:Amazon Price Alert!\n\n{message}\n{url}'.encode("utf-8")
        )

print(soup.prettify())