---
title: "Stripe Notifications"
source_id: 37966
source_url: https://wiki.genexus.com/commwiki/wiki?37966
genexus_version: "18"
---

# Stripe Notifications

You can be notified when an event happens in your account. It is done using webhooks.

To do so, you must create a new procedure in GeneXus: Main program, and HTTP call protocol.

Then you can get the data sent by Stripe using HTTPRequest variable and load it to a StripeEvent SDT.

Once loaded, you can get the event type, and use a case command to process the notification. In this example, invoice payment success and failure are captured and processed.  
You can add a String Response using HTTPResponse.

```
&NotificationsLog.DateTime = now()
&JSON = &HTTPRequest.ToString()
&StripeEvent.FromJson(&JSON)

&parameters = &StripeEvent.type.SplitRegEx(!"\.")

do case
    case &parameters.Item(1) = "invoice"
        do case
            case &parameters.Item(2) = "payment_succeeded"
                &StripeInvoice.FromJson(&StripeEvent.data.object)
                &NotificationsLog.Data = "Success: " + &StripeInvoice.ToJson()    
            case &parameters.Item(2) = "payment_failed"
                &StripeInvoice.FromJson(&StripeEvent.data.object)
                &NotificationsLog.Data = "Failure: " + &StripeInvoice.ToJson()    
        endcase
endcase

&NotificationsLog.Insert()
commit
&Response = "OK"
&HTTPResponse.AddString(&Response)
```

Important Note: You need to deploy to Cloud so that Stripe is able to reach your URL. Else, an error code will be returned to Stripe and no notification will be processed.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus SDK for Stripe](https://wiki.genexus.com/commwiki/wiki?37967) |

---
