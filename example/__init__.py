#  MIT License
#
#  Copyright (c) 2021 Pius Alfred
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
#


import tigopesasdk as tigo

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


# create a callback handler


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
