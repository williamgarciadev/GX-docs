---
title: "GXtest UI Commands - Get Value"
source_id: 41681
source_url: https://wiki.genexus.com/commwiki/wiki?41681
genexus_version: "18"
---

# GXtest UI Commands - Get Value

Sometimes it is needed to get the Value attribute instead of the text attribute (i.e combo-boxes, numeric values, and others).

In that scenario the right functions to use are GetValue ones, using different locators (control name, id, name, CSS or XPath) as follows:

## [GetValue](#GetValue)

`[imagen omitida: wiki id 47324]`

Gets the value of a control

Parameters

* ControlName: name of the control to retrieve the value

**Example**

```
&driver.GetValue("btn_enter")

&driver.GetValue("CustomerId")
```

## [GetValue](#GetValue)

`[imagen omitida: wiki id 47334]`

Gets the value of a control inside a grid

Parameters

* ControlName: name of the control to retrieve the value
* Row: row number to locate the control inside the grid

**Example**

```
&driver.GetValue("btn_enter", 2)

&driver.GetValue("CustomerId", 1)
```

## [GetValueByID](#GetValueByID)

`[imagen omitida: wiki id 47325]`

Gets the value from an HTML element using its ID.

Returns: The value of the selected element.

Parameters:

* ID: the HTML element ID .

Example of use:

```
&val1 = &driver.GetValueById("InvoiceTotal")
```

## [GetValueByName](#GetValueByName)

`[imagen omitida: wiki id 47326]`

Gets the value from an HTML element using its  'name' attribute.

Returns: The value of the selected element.

Parameters:

* Name: the value of the NAME attribute of the element.

Example of use:

```
&val1 = &driver.GetValueByName("vat_total")
```

## [GetValueByCSS](#GetValueByCSS)

`[imagen omitida: wiki id 47327]`

Gets the value from an HTML element using a CSS selector.

Returns: The value of the selected element.

Parameters:

* CSS: the CSS selector to the element.

Example of use:

```
&val2 = &driver.GetValueByCSS("#vVAR1")
```

## [GetValueByXPath](#GetValueByXPath)

`[imagen omitida: wiki id 47328]`

Gets the value from an HTML element using an XPath selector.

Returns: The value of the selected element.

Parameters:

* XPath: the XPath selector to the element.

Example of use:

```
&text_area_value = &driver.GetValueByXPath("//textarea[@id='vVAR1']")
```


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) | [GXtest UI Commands - Assertions](https://wiki.genexus.com/commwiki/wiki?41682) |
| [GXtest UI Test for Web - Supported Commands](https://wiki.genexus.com/commwiki/wiki?40281) |

---
