import aiohttp
import json
import asyncio
import getpass
import requests

# This avoids RuntimeErrors
try:
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
except:
    pass

def GetSimumatikApiToken():
    print("[+] Please, select a tenant: '1'(default):Staging, '2':Production")  
    # STAGING
    tenant = input()
    if tenant =='1': 
        auth_provider_url = "https://simumatik-dev.eu.auth0.com/oauth/token"
        audience = "https://api.staging.simumatik.com"
        client_id = "tjQNee6q1yIhPhxQOgTvwThtTu9ibezn"
    # PRODUCTION
    elif tenant=='2': 
        auth_provider_url = f"https://simumatik.eu.auth0.com/oauth/token"
        audience = "https://api.simumatik.com"
        client_id = "bSa7jnCfG3V1NQt7YB1GUSBnoUbrPL8d"
    else:
        print("No valid tenant selected!")
        return None, None

    print("[+] Introduce your username: ")
    username = input()
    print("[+] Introduce your password: ")
    password = getpass.getpass("")
    print("[+] Introduce the Auth0 API Client secret: ")
    client_secret = input()

    print("Getting Auth0 token...")
    r = requests.post(auth_provider_url, data={
        "grant_type": "password",
        "username": username,
        "password": password,
        "audience": audience,
        "client_id": client_id,
        "client_secret": client_secret
    })
    return r.json()['access_token'], audience

async def GetRequestJson(session=None, token=None, url=''):
    s = aiohttp.ClientSession(headers={"Authorization": f"Bearer {token}"}) if session is None else session
    try:
        async with s.get(url, auth=s._default_auth, ssl=False) as resp:
            assert int(resp.status/100) == 2, f"Exception get: {url}"
            res = await resp.text()
        if session is None:
            await s.close()
        return json.loads(res)
    except Exception as e:
        if s: await s.close()
        return None

async def DownloadFile(session=None, token=None, url='', path=''):
    s = aiohttp.ClientSession(headers={"Authorization": f"Bearer {token}"}) if session is None else session
    try:
        res = False
        async with s.get(url, auth=s._default_auth, ssl=False) as resp:
            assert int(resp.status/100) == 2, f"Exception downloading file: {url}, {path}"
            content = await resp.content.read()
            with open(path, 'wb') as f:
                f.write(content)
                res = True
        if session is None:
            await s.close()
        return res

    except Exception as e:
        if s: await s.close()
        return False

async def UploadFile(session=None, token=None, url='', path='', filename=''):
    s = aiohttp.ClientSession(headers={"Authorization": f"Bearer {token}"}) if session is None else session
    data = aiohttp.FormData()
    data.add_field('file',
        open(path+filename, 'rb'),
        filename=filename)
    try:
        async with s.post(url, data=data, ssl=False) as resp:    
            assert int(resp.status/100) == 2, f"Exception Uploading file: {url}, {path+filename}"
            res = await resp.text()
        if session is None:
            await s.close()
        return json.loads(res)
    except Exception as e:
        if s: await s.close()
        return None