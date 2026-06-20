---
title: "Procedures as REST: Using SDT as input to the Procedure"
source_id: 15315
source_url: https://wiki.genexus.com/commwiki/wiki?15315
genexus_version: "18"
---

# Procedures as REST: Using SDT as input to the Procedure

In a real-life situation, you will probably need to provide feedback about the operation to the user, so you can use a [Business Component](https://wiki.genexus.com/commwiki/wiki?7344,,) to perform actions in the database tables and return the operation results to the caller consumer.

In the example, "AddCustomer" Procedure is declared as REST web service in GeneXus.

* Expose as web service = true
* Rest protocol = true

`[imagen omitida: wiki id 15318]`

It receives an SDT as a parameter, containing the information of the customer to be added to the Customer table.  
Also, it returns the error and warning messages in the variable &messages, in order to be able to provide feedback about the operation to the user.

**Note**: Rest procedures can receive any type of parameters: simple or SDTs, collections or not.

Parm Rule:

```
parm(in:&Customersdt,out:&messages);
```

Source:

```
&Customer.Load(&Customersdt.CustomerId)

if &Customer.Fail()
 &Customer = new()
 &Customer.CustomerId = &Customersdt.CustomerId
endif

&Customer.CustomerName = &Customersdt.CustomerName
&Customer.CustomerBirthDate = &Customersdt.CustomerBirthDate
&Customer.CustomerPayDate = &Customersdt.CustomerPayDate
&customer.CustomerPhoto = &customersdt.CustomerPhoto

&customer.Save()
&messages = &customer.GetMessages()
commit
```

Variable &Customersdt is based on Customersdt [Structured Data Type](https://wiki.genexus.com/commwiki/wiki?10021):

`[imagen omitida: wiki id 15320]`

A GeneXus client for this REST procedure would be as follows:

```
&httpclient.Host = &host
&httpclient.Port = &port
&httpclient.BaseUrl = &baseurl

&body = '{"Customersdt":' + &customersdt.ToJson() + '}'
 
&httpclient.AddHeader('Content-type','application/json')
&httpclient.AddString(&body)

&httpclient.Execute('POST','AddCustomer')
```

Then process the HTTP Client response.

**Notes:**

* The BaseURL for calling REST Procedures is *<webappname>/rest*.
* Note that the HTTP request is in Json format. Since the Procedure receives an SDT (Structured Data Type), the Json expected is preceded by the name of the SDT, which has to be in the same casing as the parameter of the Procedure (&Customersdt).

So, the HTTP Request is as follows:

```
{"Customersdt":{"CustomerId":129,"CustomerName":"Rodolfo","CustomerBirthDate":"1976-08-05","CustomerPayDate":"1976-08-05T00:31:00","CustomerPhoto":"12356"}}
```

### [See Also](#See+Also)

[Rest web services in GeneXus](https://wiki.genexus.com/commwiki/wiki?28213)


|  |
| --- |
| **Backlinks** |
| [HowTo: Consume a Procedure exposed as a Rest service](https://wiki.genexus.com/commwiki/wiki?15314) | [Procedures as REST: Sending blob data as input to the procedure](https://wiki.genexus.com/commwiki/wiki?15316) | [Toc:Rest web services in GeneXus](https://wiki.genexus.com/commwiki/wiki?28213) |

---
