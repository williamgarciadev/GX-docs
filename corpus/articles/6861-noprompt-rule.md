---
title: "NoPrompt rule"
source_id: 6861
source_url: https://wiki.genexus.com/commwiki/wiki?6861
genexus_version: "18"
---

# NoPrompt rule

Prevents end-users from selecting/browsing data for a key.

### [Syntax](#Syntax)

**NoPrompt(***att…***);**  
  
**Where:**  
*att…*  
     Is an ordered list of attributes that define an identifier.

### [Scope](#Scope)

**Objects:**[Transaction object](https://wiki.genexus.com/commwiki/wiki?1908), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With for Smart Devices](https://wiki.genexus.com/commwiki/wiki?15974)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), 
[Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

This rule is used to disable the **Prompt** facility (F4) for the indicated list of attributes that are Foreign Keys or **Autoprompt** (Primary Keys) in transaction programs, or the **Browse** facility (used only in Micro/LAN environments). It prevents the end-user from viewing/selecting data from the table identified by this rule's parameters.

### [Samples](#Samples)

It is mostly used to stop the end-user from browsing confidential information, such as passwords, like in the following example:  
  
Invoice [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) structure:

```
Invoice
{
    InvoiceNumber*
    InvoiceDate
    PasswordId
    {
        PrdNbr*
        InvoiceLineQtty
        InvoiceLinePrice
        InvoiceLineAmount
    }
}
```

Invoice Transaction rule:

```
NoPrompt(PassworddId);
```

Password Transaction structure:

```
Password
{
    PasswordId*
    PasswordName
}
```

In this case, the end-user will not be able to see the values of valid passwords. If you consider that the end-user should not have access to clients' data which may come up after working with an Invoice transaction because the client's identification is displayed on the invoice transaction screen, you must include the following line in the Transaction Rules:

```
NoPrompt(ClientId); // ClientId is Client's table Primary key.
```

### [See Also](#See+Also)

[Prompt rule](https://wiki.genexus.com/commwiki/wiki?6863)


|  |
| --- |
| **Backlinks** |
| [Transaction rules](https://wiki.genexus.com/commwiki/wiki?8213) | [Transaction rules when executed as Business Component](https://wiki.genexus.com/commwiki/wiki?2280) |

---
