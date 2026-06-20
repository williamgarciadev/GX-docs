---
title: "GXtest UI Commands - Alerts"
source_id: 41686
source_url: https://wiki.genexus.com/commwiki/wiki?41686
genexus_version: "18"
---

# GXtest UI Commands - Alerts

JavaScript Alerts and Confirmation messages are not common in GeneXus applications, but in case you need to handle this type of dialogs, you can use the following commands.

**Warning**: GXtest recorder has a bit different model of handling alerts (Canceling or Accepting alerts are commands that need to run before the alert is shown). To understand the full behavior of these commands, try to run [the example](https://wiki.genexus.com/commwiki/wiki?41686).

**Note**: In IE, if more than one alert is displayed during an execution, IE blocks alert contents and execution does not continue as expected. To avoid this problem the site under tests must be added to Trusted Sites on Internet Explorer options (*Internet Options / Security / Trusted Sites / Sites / Add*)

## [AlertAccept](#AlertAccept)

Accepts an Alert or Confirmation message.

Returns: n/a

Example of use:

```
&driver.AlertAccept()
```

## [AlertDismiss](#AlertDismiss)

Dismisses an Alert or Confirmation message.

Returns: n/a

Example of use:

```
&driver.AlertDismiss()
```

## [GetAlertText](#GetAlertText)

Gets the Alert / Confirmation message.

Returns: the message of the Alert / Confirmation

Example of use:

```
//Get AlertText and check the value using Assertions:
AssertStringEquals(&driver.GetAlertText(), "Are you sure?", "unexpected alert text")
```

## [Example](#Example)

```
//Start webdriver
&driver.Start()
&driver.Maximize()

// Open a webpage that handles Alerts and Confirmation messages:
&driver.Go("https://the-internet.herokuapp.com/javascript_alerts")

//Open the alert, Accept it and then check that was accepted 
&driver.ClickByCSS("button")
AssertStringEquals("I am a JS Alert",&driver.GetAlertText(),  "Unexpected alert text")
&driver.AlertAccept()
AssertStringEquals("You successfuly clicked an alert",&driver.GetTextByID("result"),"alert was not accepted")

//Open the confirmation dialog, Accept it and then check that was accepted 
&driver.ClickByXPath("//button[@onclick='jsConfirm()']")
AssertStringEquals("I am a JS Confirm",&driver.GetAlertText(),  "Unexpected confirmation text")
&driver.AlertAccept()
AssertStringEquals("You clicked: Ok",&driver.GetTextByID("result"),"message was not confirmed")

//Open the confirmaion dialog and dismiss it,  then check that was dismissed
&driver.ClickByXPath("//button[@onclick='jsConfirm()']")
AssertStringEquals("I am a JS Confirm",&driver.GetAlertText(),  "Unexpected confirmation text")
&driver.AlertDismiss()
AssertStringEquals("You clicked: Cancel",&driver.GetTextByID("result"),"message was not canceled")

&driver.End()
```


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) | [GXtest UI Commands - Alerts](https://wiki.genexus.com/commwiki/wiki?41686) |
| [GXtest UI Test for Web - Supported Commands](https://wiki.genexus.com/commwiki/wiki?40281) |

---
