---
title: "GXtest UI Commands - Assertions"
source_id: 41682
source_url: https://wiki.genexus.com/commwiki/wiki?41682
genexus_version: "18"
---

# GXtest UI Commands - Assertions

Assertions are not UI commands themselves, but they are used in UI tests to compare two values (like in Unit Testing as well).

You can use assertions by comparing anything you want and determine (based on that verification) if a test is successful or not.

Typically, assertions compares expected values (that you have defined on your test data) against obtained ones using different UI commands (ie. [GetText](https://wiki.genexus.com/commwiki/wiki?41680), [GetValue](https://wiki.genexus.com/commwiki/wiki?41681), [GetTitle](https://wiki.genexus.com/commwiki/wiki?41616), etc). Even if is not common to do so, you can also check database values using assertions in a UI test.

## [Examples of usage](#Examples+of+usage)

The following example shows a UI test using different commands and assertions.

Note that there are examples of assertions to check page title, page source code, and also the Error-message content in a web panel:

```
//Start webdriver
&driver.Start()
&driver.Maximize()

//Get Source and Refresh msg
&driver.Go(photos_wp.Link())
&msg_refreshed_on1 = &driver.GetTextByCSS("span.gx-warning-message")
&wp_source = &driver.GetSource()
//Check the Source is there
AssertBoolEquals(true,&wp_source.Contains("<title>photos_wp</title>"),"not matching PAGE SOURCE.")

//Check the title, change it using JS and then check it again:
AssertStringEquals("photos_wp", &driver.GetTitle(), "not matching title")
&driver.ScriptEval("document.title = 'New Title';")
AssertStringEquals("New Title", &driver.GetTitle(), "not matching title")

//Wait 1 sec to let the function Time() to change.
&dum = sleep(1)
&driver.Refresh()

//Get the message again, and check if it is reloaded with new Time()
&msg_refreshed_on2 = &driver.GetTextByCSS("span.gx-warning-message")
AssertBoolEquals(false,&msg_refreshed_on1=&msg_refreshed_on2, "it seems that didn't refresh")
&wp_source = &driver.getSource()
AssertBoolEquals(true,&wp_source.Contains(&msg_refreshed_on2),"not matching PAGE SOURCE.")
AssertBoolEquals(false,&wp_source.Contains(&msg_refreshed_on1),"matching PAGE SOURCE.")

//Close the browser
&driver.End()
```


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) | [GXtest UI Test for Web - Supported Commands](https://wiki.genexus.com/commwiki/wiki?40281) |

---
