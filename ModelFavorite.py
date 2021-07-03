import requests, colorama, time

colorama.init()

def GetToken(Cookie):
    Token = requests.post("https://auth.roblox.com/v1/login", cookies = { #When you do botting you need a CSRF Token to login to get actuallaccess and this functions will help with that
        ".ROBLOSECURITY": Cookie
    })

    return Token

ModelID = int(input(f"[+] {colorama.Fore.GREEN}Model ID{colorama.Fore.WHITE}: "))

CookieLine = open("./!Cookies.txt").read().splitlines()
Length = len(CookieLine)
Count = 0

if Length > 0:
    CookiesAmt = 0

    print(f"[+] {colorama.Fore.GREEN}Loading Cookies")

    for Cookie in CookieLine:
        CookiesAmt = 1 + CookiesAmt

    print(f"{colorama.Fore.WHITE}[+] {colorama.Fore.GREEN}Cookies Amount: {CookiesAmt}")

    for Cookie in CookieLine:
        Token = GetToken(Cookie)

        #If its 6x90gJ1NnnBL than its invaild
        if Token.headers['x-csrf-token'] == "6x90gJ1NnnBL":
            print(f"{colorama.Fore.WHITE}[+] {colorama.Fore.RED}Invaild Cookie")
        else:
            FavoriteModel = requests.post(f"https://www.roblox.com/v2/favorite/toggle?itemTargetId={ModelID}&favoriteType=Asset", cookies = {".ROBLOSECURITY": Cookie}, json = {"assetId": ModelID}, headers = {"x-csrf-token": Token.headers['x-csrf-token']}) #Sends Post Request with the Required Data to making it work
            
            #Here we montor the Status Code to check its status
            if FavoriteModel.status_code == 200:
                Count = Count + 1
                print(f"{colorama.Fore.WHITE}[+] {colorama.Fore.GREEN}Botted Model: {Count} | {Token.headers['x-csrf-token']}")
            elif FavoriteModel.status_code == 429:
                print(f"{colorama.Fore.WHITE}[+] {colorama.Fore.RED}Rate Limited: 50 Seconds")
                time.sleep(50)
            else:
                print(f"{colorama.Fore.WHITE}[+] {colorama.Fore.RED}Error")

    print(f"{colorama.Fore.WHITE}[+] {colorama.Fore.GREEN}Finished: {Count} | Closing in 5 Seconds")

    time.sleep(5)
else:
    print("No Cookies: Closing in 5 Seconds")

    time.sleep(5)
