---
title: "PayPal one-time payments"
source_id: 39127
source_url: https://wiki.genexus.com/commwiki/wiki?39127
genexus_version: "18"
---

# PayPal one-time payments

Steps:

1. Create payment on Paypal
2. Authenticate user on Paypal’s website
3. Execute payment

First, you need to create a payment on PayPal.

You must set up the payment options using CreatePayment SDT: you will setup amount, return URLs (success and cancel), etc.

Then use CreatePaymentAPI procedure, using previously filled SDT to make the API call and create the payment on Paypal. If successful, it will return some information about the payment (which should be loaded to CreatePaymentResponse SDT to be handled).

You will need to get the redirect link, to which you should redirect the payer. This is Paypal’s website, where the payer will authenticate itself (with Paypal account) , and confirm payment.

```
&transaction.amount.currency = "USD"
&transaction.amount.total = "150"

&CreatePayment.intent = "sale"
&CreatePayment.payer.payment_method = "Paypal"
&CreatePayment.redirect_urls.cancel_url = "http://apps5.genexus.com/Idb8236469be2101e927a28340ad5eaaad/executeagreement.aspx"
&CreatePayment.redirect_urls.return_url= "http://apps5.genexus.com/Idb8236469be2101e927a28340ad5eaaad/executepayment.aspx"
&CreatePayment.note_to_payer = "NOTEEEEE"
&CreatePayment.transactions.Add(&transaction)

CreatePaymentAPI(&CreatePayment.ToJson(),&APIResponse,&ErrorCode)

if &ErrorCode = 0
    &CreatePaymentResponse.FromJson(&APIResponse)
    for &i = 1 to &CreatePaymentResponse.links.Count
        if &CreatePaymentResponse.links.Item(&i).method.ToLower() = "redirect"
            &redirectLink = &CreatePaymentResponse.links.Item(&i).href
        endif
    endfor
endif
```

Once the user confirms the payment, the success URL will be called, with a payerId and paymentId as parameters. Those are later used to confirm payment. You should parse them on the start event, execute the payment and show a message to the user.

On the Success WebPanel:

```
Event Start
    Do 'ParseString'    
    ExecutePaymentAPI(&paymentId,&payerId,&APIResponse,&ErrorCode)
    if &ErrorCode = 0
        Msg("Payment Success")
    endif
EndEvent

Sub 'ParseString'
    &Regex = "="
    &Parms = &httpRequest.QueryString
    &Matches = &Parms.SplitRegEx(&Regex)
    &paymentId = &Matches.Item(2).Replace("&token","")
    &token = &Matches.Item(3).Replace("&PayerID","")
    &payerId = &Matches.Item(4)
EndSub
```


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus SDK for PayPal](https://wiki.genexus.com/commwiki/wiki?39115) |

---
