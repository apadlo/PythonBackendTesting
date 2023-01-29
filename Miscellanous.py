import requests

test_url = 'http://rahulshettyacademy.com/'
test_cookie = 'https://httpbin.org/cookies'

redir_resp = requests.get(test_url)
print(redir_resp.history, redir_resp.status_code)

redir_resp2 = requests.get(test_url, allow_redirects=False, timeout=1)
print(redir_resp2.status_code)

# 'visit-month'
cookie = {'visit-year': '2021'}

response = requests.get(test_cookie, cookies=cookie)

print(response.status_code, response.text)

se = requests.session()
se.cookies.update({'visit-month': 'June'})

resp = se.get(test_cookie)
print(resp.status_code, resp.text)


# Attachments
url = 'https://petstore.swagger.io/v2/pet/17/uploadImage'
file = {'file': open('C:\\Users\\a.padlo\\Pictures\\FRA.jpg', 'rb')}
attach_resp = requests.post(url, files=file)

print(attach_resp.status_code, attach_resp.text)
