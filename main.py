import requests

def request_url(url, origin):
  payload = {}
  headers = {
    'Origin': origin,
    'Authorization': open("authorization.txt","r").read()
  }

  response = requests.request("OPTIONS", url, headers=headers, data=payload)

  # for key, value in response.headers.items():
  #   print(f"{key}: {value}")

  if 'access-control-allow-origin' in response.headers:
        return True
  else:
        return False

url = input("Please enter a url:\n")
true_origin = input("Please enter a true origin:\n")
# substring = url.find(".com")
# true_origin = url[:substring+4]
flase_origin = 'https://random.com'
origins = [true_origin, flase_origin]

for origin in origins:
  print('-----------------------------------')
  print('Origin: ',origin)
  result = request_url(url, origin)
  print(f"Access Control Allowed: {result}")
