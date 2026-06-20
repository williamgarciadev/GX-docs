---
title: "Error handling when Composite command is not used"
source_id: 51603
source_url: https://wiki.genexus.com/commwiki/wiki?51603
genexus_version: "18"
---

# Error handling when Composite command is not used

To handle errors when you don't use the [Composite command](https://wiki.genexus.com/commwiki/wiki?17389), you can evaluate the [&Err variable](https://wiki.genexus.com/commwiki/wiki?51028).

If an error occurs, the &Err variable will take a value greater than 0, and the [&ErrMsg variable](https://wiki.genexus.com/commwiki/wiki?51125) will contain the corresponding error message. Otherwise, if no errors occur the &Err variable value will be 0.

|  |  |
| --- | --- |
| **Value** | **Description** |
| 0 | No error |
| 1 | Unknown error |
| 2 | The user canceled the action |
| 3 | Incorrect parameters |

When the action to be executed invokes a GeneXus object located on the server side—for example, an online [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) or [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270)—the returned value corresponds to the HTTP code returned by this call (for example, 404 or 500). If there is no response from the server, the [&Err variable](https://wiki.genexus.com/commwiki/wiki?51028) will have the value 1.

The code below:

```
Composite
  UpdateEMail(ClientId,&ClientEmail)
  Interop.SendMessage("Your Email has been updated successfully in my database", ClientMobilePhone)
EndComposite
```

is equivalent to:

```
UpdateEMail(ClientId,&ClientEmail)
If &Err <> 0
    msg(&ErrMsg)
Else 
    Interop.SendMessage ("Your Email has been updated successfully in my database", ClientMobilePhone)
EndIf
```

If you don't use the Composite command, no error messages will be displayed automatically but you can use these variables and write the code to do it.

&ErrMsg is an error message for —reachable— end users. The message is the same as the one automatically shown when the [Composite command](https://wiki.genexus.com/commwiki/wiki?17389) is used. It may not be as detailed as you would need to diagnose a problem. In this case, you should see the generated log.

In the cases where there is no message (for example if &ErrMsg comes empty from an external object), the *&ErrMsg* variable will be empty too.

**Note**: For Apple applications, when the Composite command is used, GXM\_ThereWasAnErrorExecuting is shown on the screen.

### [Availability](#Availability)

This feature is available since [GeneXus 17 upgrade 7](https://wiki.genexus.com/commwiki/wiki?49301,,).

### [See Also](#See+Also)

[Interop external object](https://wiki.genexus.com/commwiki/wiki?23734)
