# CORS-allowed-hosts
This code allows you to check if a specific host is allowed by a given URL's server. It sends an OPTIONS request to the URL with different origin values and checks if the server responds with the Access-Control-Allow-Origin header.

## Prerequisites
Before running this code, make sure you have the following:

- Python installed on your machine.
- The **`requests`** library installed. You can install it using pip:
```
pip install requests
```

## Explanation
1. The code defines a function **`request_url(url, origin)`** that takes a URL and origin as input and sends an OPTIONS request to the URL with the specified origin. It also includes the authorization token from the **`authorization.txt`** file in the request headers.
2. The function checks if the response contains the **`access-control-allow-origin`** header. If present, it returns **`True`**; otherwise, it returns **`False`**.
3. The code prompts the user to enter a URL to check.
4. It extracts the domain name from the URL and assigns it to **`true_origin`**. It also defines **`false_origin`** as a random URL.
5. The code iterates over the **`origins`** list, calling the **`request_url()`** function for each origin and displaying the result.

## Usage
1. Copy the code into a Python file (e.g., **`main.py`**).
2. Create a file named authorization.txt and add the authorization token you want to use. Make sure the token is on a single line in the file.
3. Run the script using Python: **`python main.py`**.

## Results
```
Please enter a url:
https://{{domain_name}}.com/backend/api/
-----------------------------------
Origin:  https://{{domain_name}}.com
Access Control Allowed: True
-----------------------------------
Origin:  https://random.com
Access Control Allowed: False
```
