---
title: "Transaction rules when executed as Business Component"
source_id: 2280
source_url: https://wiki.genexus.com/commwiki/wiki?2280
genexus_version: "18"
---

# Transaction rules when executed as Business Component

When you use [Business Component](https://wiki.genexus.com/commwiki/wiki?5846), all [Transaction rules](https://wiki.genexus.com/commwiki/wiki?8213) are executed except:

* Those that include a user interface (i.e. Customer.call() )
* Those that are not applicable:

* [Parm](https://wiki.genexus.com/commwiki/wiki?6862)
* [Prompt](https://wiki.genexus.com/commwiki/wiki?6863)
* [NoPrompt](https://wiki.genexus.com/commwiki/wiki?6861)
* [Color](https://wiki.genexus.com/commwiki/wiki?8348)
* [Accept](https://wiki.genexus.com/commwiki/wiki?6844)

The following specification message: "SPC0097 Rule <Rule> does not apply to Business Component" appears when the mentioned <Rule> is defined in a [Transaction](https://wiki.genexus.com/commwiki/wiki?1908) used in an object as Business Component.

You can specify you want to execute certain rules defined in the Transaction, only when it is executed as Business Component by preceding the rule with the qualifier [BC], as the following example shows:

[BC] Default(InvoiceDate, &today);

Or a set of rules like this example:

[BC]  
{  
     rule1;  
     rule2;  
     ...  
     ruleN;  
}

Likewise, you have the qualifier [WEB] to indicate that a rule or set of rules must be executed only if the transaction is running in web environment with its web form, and not when it is executed as Business Component.


|  |
| --- |
| **Backlinks** |
| [Toc:Business Component](https://wiki.genexus.com/commwiki/wiki?5846) |

---
