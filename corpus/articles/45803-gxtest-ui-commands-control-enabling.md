---
title: "GXtest UI Commands - Control Enabling"
source_id: 45803
source_url: https://wiki.genexus.com/commwiki/wiki?45803
genexus_version: "18"
---

# GXtest UI Commands - Control Enabling

This command is useful to check if a control is enabled on the page, without checking if it is visible or not.

This command returns true if the element is enabled and false if not, and can be executed using different locators (control name, id, name, CSS, XPath, or LinkText) as follows:

## [IsControlEnabled](#IsControlEnabled)

`[imagen omitida: wiki id 46746]`

Checks whether a control is present and enabled or not.

**Parameters**

* ControlName: name of the control

**Example**

```
&driver.IsControlEnabled("LoginButton")
```

## [IsControlEnabled](#IsControlEnabled)

`[imagen omitida: wiki id 47920]`

Checks whether a control is present and enabled or not.

**Parameters**

* ControlName: name of the control
* Row: the row number where the control is located inside the grid

**Example**

```
&driver.IsControlEnabled("Delete", 2)
&driver.IsControlEnabled("Component2.Add", 1)
```

## [IsElementEnabledByID](#IsElementEnabledByID)

`[imagen omitida: wiki id 46740]`

Checks if an element is enabled using its ID.

Parameters:

* ID: the HTML element ID .

Example of use:

```
&driver.IsElementEnabledByID("InvoiceTotal")
```

## [IsElementEnabledByName](#IsElementEnabledByName)

`[imagen omitida: wiki id 46741]`

Checks if an element is enabled using its 'name' attribute.

Parameters:

* Name: the value of the NAME attribute of the element.

Example of use:

```
&driver.IsElementEnabledByName("total")
```

## [IsElementEnabledByCSS](#IsElementEnabledByCSS)

`[imagen omitida: wiki id 46742]`

Checks if an element is enabled using its CSS selector.

Parameters:

* CSS: the CSS selector to the element.

Example of use:

```
&driver.IsElementEnabledByCSS("#vVAR1")
```

## [IsElementEnabledByXPath](#IsElementEnabledByXPath)

`[imagen omitida: wiki id 46743]`

Checks if an element is enabled using an XPath selector.

Parameters:

* XPath: the XPath selector to the element.

Example of use:

```
&driver.IsElementEnabledByXPath("//textarea[@id='vVAR1']")
```

## [IsElementEnabledByLinkText](#IsElementEnabledByLinkText)

`[imagen omitida: wiki id 46744]`

Checks if an element is enabled using a LinkText selector.

Parameters:

* LinkText: the link’s text of the element.

Example of use:

```
&driver.IsElementEnabledByLinkText("Edit")
```


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) | [GXtest UI Test for Web - Supported Commands](https://wiki.genexus.com/commwiki/wiki?40281) |

---
