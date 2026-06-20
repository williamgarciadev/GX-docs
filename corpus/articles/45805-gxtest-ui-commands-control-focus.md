---
title: "GXtest UI Commands - Control Focus"
source_id: 45805
source_url: https://wiki.genexus.com/commwiki/wiki?45805
genexus_version: "18"
---

# GXtest UI Commands - Control Focus

This command is useful to check if a control is focused on the page.

These commands return true if the control has the focus and false if not.

## [IsControlFocused](#IsControlFocused)

`[imagen omitida: wiki id 46678]`

Checks whether a control is focused.

Parameters:

* ControlName: the name of the control as defined in the KB.

Example of use:

```
&driver.IsControlFocused("Name")
```

## [IsControlFocused](#IsControlFocused)

`[imagen omitida: wiki id 47921]`

Checks whether a control is focused.

Parameters:

* ControlName: the name of the control as defined in the KB.
* Row: the row number to locate the control inside a grid

Example of use:

```
&driver.IsControlFocused("Name", 3)
&driver.IsControlFocused("FilterComp.Search", 1)
```

Also, they can be executed using different HTML locators (id, name, CSS, XPath or LinkText) as follows:

## [IsElementFocusedByID](#IsElementFocusedByID)

`[imagen omitida: wiki id 46679]`

Checks whether an element is focused using its ID.

Parameters:

* ID: the HTML element ID .

Example of use:

```
&driver.IsElementFocusedByID("InvoiceTotal")
```

## [IsElementFocusedByName](#IsElementFocusedByName)

`[imagen omitida: wiki id 46680]`

Checks whether an element is focused using its 'name' attribute.

Parameters:

* Name: the value of the NAME attribute of the element.

Example of use:

```
&driver.IsElementFocusedByName("total")
```

## [IsElementFocusedByCSS](#IsElementFocusedByCSS)

`[imagen omitida: wiki id 46681]`

Checks whether an element is focused using its CSS selector.

Parameters:

* CSS: the CSS selector to the element.

Example of use:

```
&driver.IsElementFocusedByCSS("#vVAR1")
```

## [IsElementFocusedByXPath](#IsElementFocusedByXPath)

`[imagen omitida: wiki id 46682]`

Checks whether an element is focused using an XPath selector.

Parameters:

* XPath: the XPath selector to the element.

Example of use:

```
&driver.IsElementFocusedByXPath("//textarea[@id='vVAR1']")
```

## [IsElementFocusedByLinkText](#IsElementFocusedByLinkText)

`[imagen omitida: wiki id 46683]`

Checks whether an element is focused using a LinkText selector.

Parameters:

* LinkText: the link’s text of the element.

Example of use:

```
&driver.IsElementFocusedByLinkText("Edit")
```


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) | [GXtest UI Test for Web - Supported Commands](https://wiki.genexus.com/commwiki/wiki?40281) |

---
