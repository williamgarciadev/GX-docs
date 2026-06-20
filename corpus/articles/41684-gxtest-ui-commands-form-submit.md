---
title: "GXtest UI Commands - Form Submit"
source_id: 41684
source_url: https://wiki.genexus.com/commwiki/wiki?41684
genexus_version: "18"
---

# GXtest UI Commands - Form Submit

Submitting forms is usually the action of pressing the Return/Enter key on a form or clicking a button. If you don't want to click on a form and want to simulate the form submit action from a user, use the following functions over an element:

## [SubmitByID](#SubmitByID)

Submits the form of an element locating it by ID.

Parameters:

* ID: the HTML element ID of the form to submit.

Example of use:

```
&driver.SubmitById("InvoiceTotal")
```

## [SubmitByLinkText](#SubmitByLinkText)

Submits the form of link of some specific text.

Parameters:

* LinkText: the link text inside the form to locate.

Example of use:

```
&driver.SubmitByLinkText("buy flight 1")
```

## [SubmitByName](#SubmitByName)

Submits the form of an element with a specific 'name' attribute.

Parameters:

* Name: the NAME attribute of the control to locate.

Example of use:

```
&driver.SubmitByName("CountryName")
```

## [SubmitByCSS](#SubmitByCSS)

Submits the form's element, by using a CSS selector.

Parameters:

* CSS: the CSS selector to the element you want to submit.

Example of use:

```
&driver.SubmitByCSS("#var1")
```

## [SubmitByXPath](#SubmitByXPath)

Submits the form of an element, locating it with an XPath selector.

Parameters:

* XPath: the XPath selector to the element that wants to be submitted.

Example of use:

```
&driver.SubmitByXPath("//span/input1")
```


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) | [GXtest UI Test for Web - Supported Commands](https://wiki.genexus.com/commwiki/wiki?40281) |

---
