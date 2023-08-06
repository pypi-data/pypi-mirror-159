# requests-websub-auth

A micro-library providing [WebSub](https://www.w3.org/TR/websub/) HMAC Signature
authentication for webhooks.

The HMAC signature is generated using a secret and the webhook body. It is placed
in the `X-Hub-Signature` header in the format `<algorithm>=<hmac_signature>`, where the
`hmac_signature` is a hexdigest.

Supports all of the [algorithms](https://www.w3.org/TR/websub/#recognized-algorithm-names) 
detailed in the WebSub specification.

## Installation
``` bash
pip install requests-websub-auth
```

## Usage
``` python
import requests
from requests_websub_auth import WebSubAuth, WebSubAlgorithm

auth = WebSubAuth("secret", WebSubAlgorithm.SHA256)
payload = {
    "foo": 1,
    "bar": 2
}

response = requests.post("https://foobar.com/", auth=auth, json=payload)
response.raise_for_status()
```
