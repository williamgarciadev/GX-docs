---
title: "PayPal recurring payments"
source_id: 39129
source_url: https://wiki.genexus.com/commwiki/wiki?39129
genexus_version: "18"
---

# PayPal recurring payments

When selling products that require a subscription (eg: monthly payments), recurring payments are used.

First you need to setup your plan. A plan is the specification of what the user will pay.  
Eg: premium account, $15, monthly.

To do so, you need to create your plan on Paypal and then activate it.  
Use CreateBillingPlan SDT and payment\_definitions to setup your plan, and create it using CreateBillingPlanAPI procedure.  
If created correctly (check error code = 0), map the API Response to CreateBillingPlanResponse SDT and activate the plan using ActivateBillingPlan procedure and the plan Id.

```
&BaseURL = &HttpRequest.BaseUrl

&CreateBillingPlan.name = "Plan 1"
&CreateBillingPlan.description = "Description 1"
&CreateBillingPlan.type = PlanType.INFINITE

&CreateBillingPlan.merchant_preferences.return_url = &BaseURL + CancelAgreement.Link()
&CreateBillingPlan.merchant_preferences.cancel_url = &BaseURL + ExecuteAgreement.Link()
&CreateBillingPlan.merchant_preferences.auto_bill_amount = "no"
&CreateBillingPlan.merchant_preferences.max_fail_attempts = "0" 
&CreateBillingPlan.merchant_preferences.initial_fail_amount_action = "CONTINUE"

&payment_definitions.amount.value = "50"
&payment_definitions.amount.currency = "USD"
&payment_definitions.frequency_interval = "1"
&payment_definitions.frequency = "DAY"
&payment_definitions.cycles = "0"
&payment_definitions.name = "SHIPPING"
&payment_definitions.type = "REGULAR"

&CreateBillingPlan.payment_definitions.Add(&payment_definitions)

CreateBillingPlanAPI(&CreateBillingPlan.ToJson(),&APIResponse,&ErrorCode)

if &ErrorCode = 0
    &CreateBillingPlanResponse.FromJson(&APIResponse)
    &planId = &CreateBillingPlanResponse.id
    ActivateBillingPlan(&planId,&APIResponse,&ErrorCode)
endif

if &ErrorCode = 0
    Msg("Success",status)
endif
```

Billing Agreements create a relationship between the buyer and the plan.  
As with payments, you need to create an agreement, make the user authenticate and execute the agreement.  
To set up an agreement, use CreateBillingAgreement SDT and CreateBillingAgreementAPI procedure. Use CreateBillingAgreementResponse SDT to handle the response and redirect the user to Paypal’s website.

Note: agreements take a minimum of 24 hours to become active (you can set more time if you want)

Afer user authentication, Paypal calls a success URL and sends a token as a parameter. Use that token to execute the agreement. It will become active once the time you indicated before is completed (24 hours minimum).

On the Success WebPanel:

```
Event Start
    Do 'ParseString'
    ExecuteAgreementAPI(&token,&APIResponse,&ErrorCode)
    if &ErrorCode = 0
        Msg("Agreement Success")
    endif
EndEvent

Sub 'ParseString'
    &Regex = "="
    &Parms = &httpRequest.QueryString
    &Matches = &Parms.SplitRegEx(&Regex)
    &token = &Matches.Item(2)
EndSub
```


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus SDK for PayPal](https://wiki.genexus.com/commwiki/wiki?39115) |

---
