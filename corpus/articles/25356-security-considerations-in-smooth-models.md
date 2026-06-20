---
title: "Security considerations in Smooth models"
source_id: 25356
source_url: https://wiki.genexus.com/commwiki/wiki?25356
genexus_version: "18"
---

# Security considerations in Smooth models

A common scenario for [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836)s which do not use [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) is to include a code for verifying if the user was authenticated or authorized to execute a web page in the Start event of the [Master Page](https://wiki.genexus.com/commwiki/wiki?17088). And consequently, the execution of user events did not include any security check, because it always followed the execution of the Start event where the security had already been checked.

However, programming security checks in the Start event is not a good security solution for applications generated to use [Web Smooth UX](https://wiki.genexus.com/commwiki/wiki?25801,,), and this is due to the [Event Execution Scheme](https://wiki.genexus.com/commwiki/wiki?22472). In such cases, you must consider a different solution.

Despite the fact that using GAM is the best solution for this, GeneXus introduces an automatic solution to help those who haven't [Integrated Security](https://wiki.genexus.com/commwiki/wiki?14706) in their KBs, and are converting from versions prior to GeneXus Evolution 3 to a Smooth model.

### Case Scenario:

[Web User Experience property](https://wiki.genexus.com/commwiki/wiki?22449)= Smooth  
[Integrated Security Level property](https://wiki.genexus.com/commwiki/wiki?15214) = none

When [Web User Experience property](https://wiki.genexus.com/commwiki/wiki?22449)  = Smooth, the Start, Refresh and Load Events are not triggered in the execution of a user event, as explained in the [Event Execution Scheme](https://wiki.genexus.com/commwiki/wiki?22472).

This means that this code is vulnerable as far as security is concerned:

```
Event Start
        &context = LoadContext()
        if (not &context.IsAdministrator)
                  NotAuthorized.Link()
        endif
Endevent

Event 'RemoveData'
    RemoveData.call()
Endevent
```

Note that, in a Smooth model, the execution of user event 'RemoveData' is separated from the Start event. So, the security check inside the Start event is not triggered when the user event is executed.

If security checks were included in every user event, then the problem would not exist but, there is no need to consider the change of user events code because an automatic solution is available to solve such security issues.

## [Solution:](#Solution%3A)

To avoid delegating the responsibility of this task to the GeneXus developer, a solution has been implemented to automatically prevent intruders from executing a user event, without accessing the WebPage (Start Event) at least once. Start Event (Get Method) must be executed, because typically the Authorization code (when not using GAM) is checked here.   
Only when the user has executed the web panel (GET Method) once, a token will be granted to be used in executing the page's user events. If the User does not execute the GET Method of the WebPage, no User Events will be able to be executed, as the Token is mandatory in every Http Request. The token is valid only for that specific web page object.

Since GeneXus 15, the [JWT](https://tools.ietf.org/html/rfc7519) standard is used for the implementation of the token mechanism using advanced cryptography.

Additionally, an automatic security check is also available for each HTTP Post, for detecting whether the read-only data has been changed. In case it has, a 403 Forbidden Error is informed. A more detailed explanation of this mechanism is explained in [Security Web Development tips](https://wiki.genexus.com/commwiki/wiki?31506).

**Note**: The security token will remain valid while the end user is executing a web page, even if a permit for that user is revoked or if the user is deleted. So, depending on the application's strictness and features, we might need to program the security checks for each user event.


|  |
| --- |
| **Backlinks** |
| [Security Web Development tips](https://wiki.genexus.com/commwiki/wiki?31506) |

---
