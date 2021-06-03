# tigopesasdk
TigoPesa API wrapper written in python

## installation

```bash

pip install tigopesasdk

```


## usage

```python

from src import tigopesasdk as tigo

# stating the configurations
config = tigo.Config(
    account_name="",
    brand_id="",
    token_url="",
    password="",
    biller_payment_url="",
    biller_code="",
    grant_type="password",
    username="",
    account_msisdn=""
)

# creating a tigo client
client = tigo.TigoClient(
    config,
    True
)

# form a bill request
bill_request = tigo.BillPayRequest(
    reference_id="PYWWTWTW15151718191",
    amount=10000,
    remarks="mt first ever payment from command line tool",
    customer_msisdn="0712915799",
)

# generate token from tigo
token_response = client.generate_token()

if token_response is not None:
    print("access token: " + token_response.access_token)
    print("token type: " + token_response.token_type)
    print("expires date: " + token_response.expires_in)
    bill_response = client.bill_with_token(token_response.access_token, bill_request)
    print("response code " + bill_response.response_code)
    print("response status" + str(bill_response.response_status))
    print("response description " + bill_response.response_description)
    print("reference id " + bill_response.reference_id)

# bill_with_token uses a pre generated token to initiate push pay request
# bill on the other hand request for token internally and use the response to
# initiate the push pay

bill_response = client.bill(bill_request)
if bill_response is not None:
    print("response code " + bill_response.response_code)
    print("response status" + str(bill_response.response_status))
    print("response description " + bill_response.response_description)
    print("reference id " + bill_response.reference_id)
```

## LICENCE
MIT License