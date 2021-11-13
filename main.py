import json
import time
import random

import requests

get_login_url = "https://qblogin.corrigo.com/login/login.aspx?secure=1"

post_url = "https://qblogin.corrigo.com/login/Login.aspx?secure=1"

secret_page_url = "https://qblogin.corrigo.com/corp/Customers/AddNewCustomer.aspx?backUrl=CustomerList.aspx"

# first_name = input()
first_name_int = str(random.randint(1,1000000000))
last_name = input()
phone = '4074550252'
email = 'tbreutzmann@1pfe.com'
address = '340 Broadway Ave'



# Request data works with the commented portions below..
request_data = {
    # "__EVENTTARGET":"",
    # "__EVENTARGUMENT":"",
    "__VIEWSTATE":"/wEPDwUKLTQwOTIwMDQxOGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFDWNoa1JlbWVtYmVyTWUjPsGCA7BrWO3MBDoRsdWupXiCLGGlLIJZ2ufFXK54dQ==",
    "__VIEWSTATEGENERATOR":"5E7FB4E4",
    "__EVENTVALIDATION":"/wEdAAq/HEBQ46oQaJS9s+v0lVK7bSROi2sBMXLo/aUXSYRI2k8Q6WJCbQMRVdvDM5BdYA1P4q/Xm/muyy5LcNBNytmUWfwQpuK/m5cYCChjI6f8eahXufbhIqPmwKf992GTkd33B/SknYfpkCkJGnZEz9bXop4oRunf14dz2Zt2+QKDEFvv90Pojif5f4vmhiSDFhf3gkRqWeWzvF1d/RMtMlmO16WLGqK6aqDQANN4QG0rfv1TDERejpJl76fdKx9E12E=",
    # "hdnSecureText":"1",
    # "hdnQueryString":"",
    # "hdnPage":"",
    "tbUsername":"mserra@1pfe.com",
    "tbPassword":"treadmills",
    "tbCompany":"first place fitness equipment",
    "btnLogin":"Sign In",
    # "chkRememberMe":"on"
}

secret_form_data = {

"hdModifiedControlsPageConfirmation":"",
"__EVENTTARGET":"",
"__EVENTARGUMENT":"",
"tlbhvctl00_m_crgTaxLabelBehavior":	"ctl00_m_txtTaxCustomer|&|&|&|ctl00_m_lblTaxRateCustomer",
"hdDirtyPageConfirmation":"true",
"tlbhvctl00_m_TaxLabelBehavior1":"ctl00_m_txtTaxSite|&|&|&|ctl00_m_lblTaxRateSite",
"__VIEWSTATE":	"/wEPDwULLTEwODMwNjg4OTIPZBYCZg9kFgICAw8WAh4FY2xhc3MFCWN1c3RvbWVycxYCAgEPZBYEAgMPDxYCHgdWaXNpYmxlaGRkAhUPZBYoAgIPEA9kFgIeB29uY2xpY2sFTVZpZXdSZXNpZGVudGlhbCgpO1NldEhhbmRsZXJSZXNpZGVudGlhbCgpO0N1c3RvbWVyVHlwZUNoYW5nZWQoKTtDbGVhckJveGVzKCk7ZGRkAgQPEA9kFgIfAgVLVmlld0NvbW1lcmNpYWwoKTtTZXRIYW5kbGVyQ29tbWVyY2lhbCgpO0N1c3RvbWVyVHlwZUNoYW5nZWQoKTtDbGVhckJveGVzKCk7ZGRkAgYPD2QWAh4Hb25rZXl1cAVhTW9kaWZ5VGV4dEJveFdpdGhDdXN0RGlzcGxheUFzKCdjdGwwMF9tX3R4dERCQScsJ2N0bDAwX21fdHh0RGlzcGxheUN1c3RBcycpO1NldFZhbHVlVG9TaXRlTmFtZSgpO2QCDA8QFgIeCG9uY2hhbmdlBWJDaGFuZ2VEaXNwbGF5QXMoZXZlbnQsICdjdGwwMF9tX3R4dERpc3BsYXlDb250QXMnLCB0aGlzLCAnY3RsMDBfbV9oZERpc3BsYXlDb250QXMnLCAncm93SGlkZGVuMicpO2RkZAIQD2QWBAIBD2QWAgIBD2QWAmYPDw8WAh4BbQUtZ2V0UGFnZUNvbmZpcm1hdGlvbigpLm9uQ29udHJvbFN0YXRlQ2hhbmdlKCk7ZGRkAgIPZBYCAgEPZBYCZg8PDxYCHwUFLWdldFBhZ2VDb25maXJtYXRpb24oKS5vbkNvbnRyb2xTdGF0ZUNoYW5nZSgpO2RkZAIXDw8WAh4EVGV4dAUESG9tZRYCHwQFE0RvQ2hhbmdlU2l0ZU5hbWUoKTtkAhgPDw8WAh8BaGRkZAIZDw8WBB8GBR9GaXRuZXNzIFN5c3RlbXMgU2VydmljZSBQYWNrYWdlHwFnFgIeB21vZGVsSWQFBDE5MzVkAiAPDxYCHghhbmNob3JpZAUbY3RsMDBfbV90eHRTaXRlU3RhdGVQcm92aWNlZGQCIg8PDxYIHgFwBQVhZG1pbh4BbwKVMh8BaB4BYQUVUGljayBhIHshe1Byb3BlcnR5fSF9ZGRkAiMPDxYEHwYFDUFsbCBXb3JrIFpvbmUfAWcWAh4GY29tbUlkBQQxNzMwZAIlDxYCHwFoZAInD2QWAgIBD2QWAmYPDw8WAh8FBS1nZXRQYWdlQ29uZmlybWF0aW9uKCkub25Db250cm9sU3RhdGVDaGFuZ2UoKTtkZGQCKA9kFgICAQ9kFgJmDw8PFgIfBQUtZ2V0UGFnZUNvbmZpcm1hdGlvbigpLm9uQ29udHJvbFN0YXRlQ2hhbmdlKCk7ZGRkAikPZBYCZg9kFgJmDxYGHgVzdHlsZQUXbWFyZ2luOjBweDtwYWRkaW5nOjBweDseC2NlbGxwYWRkaW5nBQEwHgtjZWxsc3BhY2luZwUBMBYEZg9kFgICAQ9kFgJmDw8WBB4IQ3NzQ2xhc3MFFGNvbW1vbkNmVGV4dEJveFN0eWxlHgRfIVNCAgJkZAIBD2QWAgIBD2QWAmYPDxYEHxAFFGNvbW1vbkNmVGV4dEJveFN0eWxlHxECAmRkAioPEA9kFgIfAgUVU2hvd0JpbGxpbmdBZGRyZXNzKCk7ZGRkAi8PDxYCHwgFHmN0bDAwX21fdHh0QmlsbGluZ1N0YXRlUHJvdmljZWRkAjIPDxYCHg1PbkNsaWVudENsaWNrBUhpZighY2FsZW5kYXJWYWxpZGF0b3IuSXNWYWxpZCgpKXtyZXR1cm4gZmFsc2U7fTtzd2l0Y2hTdGF0dXNGbGFnKHRydWUpOztkZAIzDw8WAh8SBUhpZighY2FsZW5kYXJWYWxpZGF0b3IuSXNWYWxpZCgpKXtyZXR1cm4gZmFsc2U7fTtzd2l0Y2hTdGF0dXNGbGFnKHRydWUpOztkZAI0Dw8WCh4Lc2NvcGVEb21haW4LKXFDb3JyaWdvLkJPLlNjb3BlTG9hZGVyLlNjb3BlRG9tYWluLCBDb3JyaWdvLkJPLlNjb3BlTG9hZGVyLCBWZXJzaW9uPTEuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49bnVsbAAeCWNvbnRleHRJZGYeEGNvbnRleHREaXNwbGF5QXNlHgVpc09mZmceBG1vZGULKWFDb3JyaWdvLldlYi5VSS5TY29wZVNlbGVjdG9yTW9kZSwgQXBwX0NvZGUsIFZlcnNpb249MC4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1udWxsAmRkGAIFHl9fQ29udHJvbHNSZXF1aXJlUG9zdEJhY2tLZXlfXxYEBRZjdGwwMCRtJGJ0blJlc2lkZW50aWFsBRZjdGwwMCRtJGJ0bkNvbW1tZXJjaWFsBRZjdGwwMCRtJGJ0bkNvbW1tZXJjaWFsBRljdGwwMCRtJGNoa0JpbGxpbmdBZGRyZXNzBQ5jdGwwMCR3b1dpZGdldA8UKwADZGhmZGsDo2BvoVil8k6ZLR4WMmCToBEyz3fZ0UEP+XFppM43",
"__VIEWSTATEGENERATOR":	"7FB4AABF",
"__EVENTVALIDATION":"/wEdACl3udLT0YTVW4cZ9QKr/UkuORv6CdGbC9E6qoLTm7pRAl4aHyUCuZFKyIpLA+tqGhEhgOktpm2nwLzoHBrTkfynW9G3yKgmv+E+PxRYKHVMo2lne+7LG7sxi+eVVzAuZ7ZN+35oCLWP+FrO+gT6xANxqLK3apayO748PID5hrZv3KE2yJ9hc80jznjpsRW7MZn8ohQACFr3+WumfEb5bHYgMQgqVXGtuojfzEwJHtcZM0E/jkOGY4VtlNCDvQ25/UwbG28gBGiNY16A2rPNHDAzFAA3zmU4mypCtzRZAWBHtuDmhQuhPfn7lh4uDOBYb+Bxubyo4LUNfNXPGvTwQkBhqPSLXZjlBSm0AUmI4fifCNwf3n4UJogYcB8E7iOxeaz2sIol5PHLGHzslaPuD0/l1j7Bb/yNBU/LJLww1BVkVuzei0WDZ9nPBMKtdp0Edp9l4++vQqPRa2BVknZ2sFSgxTFXzywZ7JZiWVAJJy8noaQld1aigzTuwaRvt+MOD+p4HCFzGgvc8LAbgBYqFz5zqXpBFBxD1D8rgVisYKo9wYvdgYskkG3VB5hdP9+wrvBlGvkDT40Rq8bPjmKCNFtpTSqToHM6PpqYTm6p3H5DD5s8pj7OawO/dIV2NfAl5lVCgoi6hxqpQaPhwrcZTPwUe+C4IEgPTgRvUAI3sBnJ4gfBVTSrssBLVExdSOyZV4OoLzsboFLe3I7cF6hEv2rUFF1hJHF7ciP/ONcZIS0a41+PX5t67I4VnlKAn/g4zXCpw1RMEb4MrkhmCb69YmeCV9HiQ4foMiDiueKot3kxkVYcvFOJwjVStWpcw2H82A3yr8wjKl+ky08Ie09m3ckndD/5F8MHcSNpY5d0D2jRJLT5v80aRS93PK9yOL+Eesv3M/lSRGEfC6OjrojU1kTl",
# "ctl00$searchCombo":"customer_customername",
# "searchStr":"",
# "ctl00$ddlRecent_i":"Recent Items",
# "ctl00$ddlRecent":"",
# "ctl00$ddlRecent_e":"Recent Items",
# "ctl00$m$hdSiteNameManualInput":"false",
"ctl00$m$CustomerType":"btnResidential",
"ctl00$m$hdInit":"R",
"ctl00$m$txtDBA":"",
"ctl00$m$txtDisplayCustAs":	"",
"ctl00$m$txtFirstName":first_name_int,
"ctl00$m$txtLastName":last_name,
"ctl00$m$txtDisplayAs":last_name + ", " + first_name_int,
"ctl00$m$hdDisplayContAs":"false",
"ctl00$m$txtDisplayContAs":last_name + ", " + first_name_int,
"ctl00$m$txtTaxCustomer":"-1",
"ctl00$m$txtTaxCustomer:SecondColumn":"",
"ctl00$m$txtTaxCustomer:Text":"-- Please specify --",
"ctl00$m$txtTaxCodeCustomer":"-1",
"ctl00$m$txtTaxCodeCustomer:SecondColumn":"",
"ctl00$m$txtTaxCodeCustomer:Text":	"",
"ctl00$m$txtPrimaryPhone":phone,
"ctl00$m$txtAlternatePhone":"",
"ctl00$m$txtFax":"",
"ctl00$m$txtContactEmail":email,
"ctl00$m$txtSiteName":first_name_int + last_name,
"ctl00$m$hdModelId":"",
"ctl00$m$txtSiteAddress_1":address,
"ctl00$m$txtSiteAddress_2":"",
"ctl00$m$txtSiteCity":"Orlando",
"ctl00$m$txtSiteStateProvice":"FL",
"ctl00$m$txtSiteZip":"32803",
"ctl00$m$hdCommunityId":"",
"ctl00$m$txtTaxSite":"-1",
"ctl00$m$txtTaxSite:SecondColumn":"",
"ctl00$m$txtTaxSite:Text":"-- Please specify --",
"ctl00$m$txtTaxCodeSite":"-1",
"ctl00$m$txtTaxCodeSite:SecondColumn":"",
"ctl00$m$txtTaxCodeSite:Text":"",
"ctl00$m$cfContainerSpace$2652":"",
"ctl00$m$cfContainerSpace$2392":"",
"ctl00$m$chkBillingAddress":"on",
"ctl00$m$txtBillingAddress_1":"",
"ctl00$m$txtBillingAddress_2":"",
"ctl00$m$txtBillingCity":"",
"ctl00$m$txtBillingStateProvice":"",
"ctl00$m$txtBillingZip":"",
"ctl00$m$btnAdd":"Ok"

}

# This is working completely!

with requests.Session() as s:
    get = s.get(get_login_url)

    post = s.post(post_url, data=request_data)
    print(post.status_code)

    time.sleep(2)
    secret_page = s.get(secret_page_url)
    print(secret_page.status_code)

    time.sleep(2)
    secret_page_send_form = s.post(secret_page_url, data=secret_form_data)
    print(secret_page_send_form.status_code)

    s.close()



