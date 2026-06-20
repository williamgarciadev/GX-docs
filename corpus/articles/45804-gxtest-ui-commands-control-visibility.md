---
title: "GXtest UI Commands - Control Visibility"
source_id: 45804
source_url: https://wiki.genexus.com/commwiki/wiki?45804
genexus_version: "18"
---

# GXtest UI Commands - Control Visibility

This command is useful to check if an element is visible on a webpage.

Returns true if the element is visible and false if it is not.

## [IsControlVisible](#IsControlVisible)

`[imagen omitida: wiki id 46684]`

Checks if a control is visible.

Parameters:

ControlName: the name of the control as defined in the KB.

Example of use:

```
&driver.IsControlVisible("Price")
```

## [IsControlVisible](#IsControlVisible)

`[imagen omitida: wiki id 47918]`

Checks if a control is visible.

Parameters:

ControlName: the name of the control as defined in the KB.

Row: row number to locate the control inside the grid

Example of use:

```
&driver.IsControlVisible("Price", 1)
&driver.IsControlVisible("webComponent1.Price", 2)
```

Also, can be executed using different locators (id, name, CSS, XPath, or LinkText) as follows:

## [IsElementVisibleByID](#IsElementVisibleByID)

`[imagen omitida: wiki id 46685]`

Checks if an element it’s visible using its ID.

Parameters:

ID: the HTML element ID .

Example of use:

```
&driver.IsElementVisibleByID("InvoiceTotal")
```

## [IsElementVisibleByName](#IsElementVisibleByName)

`[imagen omitida: wiki id 46686]`

Checks if an element it’s visible using its 'name' attribute.

Parameters:

Name: the value of the NAME attribute of the element.

Example of use:

```
&driver.IsElementVisibleByName("total")
```

## [IsElementVisibleByCSS](#IsElementVisibleByCSS)

`[imagen omitida: wiki id 46687]`

Checks if an element it’s visible using its CSS selector.

Parameters:

CSS: the CSS selector to the element.

Example of use:

```
&driver.IsElementVisibleByCSS("#vVAR1")
```

## [IsElementVisibleByXPath](#IsElementVisibleByXPath)

`[imagen omitida: wiki id 46688]`

Checks if an element it’s visible using an XPath selector.

Parameters:

XPath: the XPath selector to the element.

Example of use:

```
&driver.IsElementVisibleByXPath("//textarea[@id='vVAR1']")
```

## [IsElementVisibleByLinkText](#IsElementVisibleByLinkText)

`[imagen omitida: wiki id 46689]`

Checks if an element it’s visible using a LinkText selector.

Parameters:

LinkText: the link’s text of the element.

Example of use:

```
&driver.IsElementVisibleByLinkText("Edit")
```


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) | [GXtest UI Test for Web - Supported Commands](https://wiki.genexus.com/commwiki/wiki?40281) |

---
