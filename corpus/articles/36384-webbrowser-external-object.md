---
title: "WebBrowser external object"
source_id: 36384
source_url: https://wiki.genexus.com/commwiki/wiki?36384
genexus_version: "18"
---

# WebBrowser external object

The WebBrowser external object allows you to handle events related to web-designed applications, which are embedded in [Apple](https://wiki.genexus.com/commwiki/wiki?14917) and [Android](https://wiki.genexus.com/commwiki/wiki?14453) platform applications.

|  |  |
| --- | --- |
|  |  |

You can find the WebBrowser object in the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210) within the SD module, which in turn is located within the GeneXus module. That is to say, it is part of the [Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288).

## [Methods](#Methods)

### [Open method](#Open+method)

Opens an [inline web browser](https://wiki.genexus.com/commwiki/wiki?36384), displaying the given URL. This method replaces the OpenInBrowser method of [Interop external object](https://wiki.genexus.com/commwiki/wiki?23734).

|  |  |
| --- | --- |
| **Input** | url:[URL](https://wiki.genexus.com/commwiki/wiki?15668) |
| **Output** | None |

### [Close method](#Close+method)

Closes the inline web browser.

|  |  |
| --- | --- |
| **Input** | None |
| **Output** | None |

## [Events](#Events)

### [BeforeNavigate event](#BeforeNavigate+event)

This event lets you capture navigation events started from an embedded web view control before they happen so that you can decide how to handle this navigation.

Note that this event is not triggered from the inline web browser, but from an [embedded web view control](https://wiki.genexus.com/commwiki/wiki?36384). The BeforeNavigate event is not triggered for navigation requests that use the HTTP POST method.   
Only requests performed via <strong>GET</strong> are supported.

In addition, this method only supports internal links via the GET method, which means that POST links are not supported.

If WebBrowser.BeforeNavigate is not present, following a link from an embedded web view control will always open the inline web browser. The reason for this is that the embedded web view control has no navigation controls (like the "back" or "refresh" buttons) required for a smooth navigation experience.

When the WebBrowser.BeforeNavigate is present, you can control if a link is opened in the same embedded web view control or if it should open an inline web browser.

This event receives the URL that will be opened, and an in-out parameter that indicates if the navigation has been handled. If you set the &handled variable to True, the application will not follow the link because it assumes it has been handled in the event. If you set it to False, the navigation is handled as usual and the application will open an inline web browser to show the &url parameter.

|  |  |
| --- | --- |
| **Input** | url:[URL](https://wiki.genexus.com/commwiki/wiki?15668) |
| **In-out** | handled:[Boolean](https://wiki.genexus.com/commwiki/wiki?4374) |
| **Output** | None |

### [OnClose event](#OnClose+event)

This event is triggered when the inline web browser opened within a Native Mobile application is closed. It is very helpful to code communication between mobile and web applications, allowing the execution of custom actions, such as logs, notifications, or specific logic when the browser is closed.

|  |  |
| --- | --- |
| **Input** | url:[URL](https://wiki.genexus.com/commwiki/wiki?15668) |
| **Output** | None |

**Note**: The OnClose event and the Close method only work when the Open method is used to open the browser.

## [Samples](#Samples)

### [Navigating inside the embedded web view control](#Navigating+inside+the+embedded+web+view+control)

To navigate inside the embedded web view control (say you have a &Component variable), the following code can be used:

```
Event GeneXus.SD.WebBrowser.BeforeNavigate(&Url, &Handled)
  composite
    &Component = &Url // assign the new URL to the variable in the form
    &Handled = true
  endcomposite
EndEvent
```

Keep in mind that the typical navigation options (like the "back" or "refresh" actions) will not be available.

### [Implement a payment flow](#Implement+a+payment+flow)

This event is also useful for implementing a payment flow where the web page acts like some kind of wizard with several steps, and after finishing it calls some well-known callback URL to finish the payment process.

This can be implemented as follows:

```
Event GeneXus.SD.WebBrowser.BeforeNavigate(&Url, &Handled)
  composite
    if &Url = &callbackURL
      <your_code>
    endif
    &Handled = true // always force navigation inside the embedded web view
  endcomposite
EndEvent
```

## [See also](#See+also)

[HowTo: Open a Web Page in a New Browser Window from a Smart Devices Application](https://wiki.genexus.com/commwiki/wiki?18555)

## [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

## [Considerations](#Considerations)

Below you can find some precise definitions:

#### [Embedded web view control](#Embedded+web+view+control)

It's a control shown inside the Panel's layout and can show a web page. It can be a read-only attribute, variable, or SDT member based on the [Component](https://wiki.genexus.com/commwiki/wiki?16186) or [HTML](https://wiki.genexus.com/commwiki/wiki?16293) domains.

#### [Inline web browser](#Inline+web+browser)

It is a full-screen web browser with the typical navigation elements (URL, back button, refresh button, etc.) shown inside the application.


|  |
| --- |
| **Backlinks** |
|
| [GeneXus Core module](https://wiki.genexus.com/commwiki/wiki?31268) | [GeneXus Core module (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54413) | [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) | [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) |
| [WebBrowser external object](https://wiki.genexus.com/commwiki/wiki?36384) |

---
