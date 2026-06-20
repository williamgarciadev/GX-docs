---
title: "GXtest UI Commands - Get Text"
source_id: 41680
source_url: https://wiki.genexus.com/commwiki/wiki?41680
genexus_version: "18"
---

# GXtest UI Commands - Get Text

Getting the visible text from controls is very useful for several purposes.

Typically is used combined with [assertions](https://wiki.genexus.com/commwiki/wiki?38336) to let GXtest check for expected conditions. Another common usage is to retrieve web panel data that needs to be used in other test case steps.

## [GetText](#GetText)

`[imagen omitida: wiki id 47321]`

Gets the text of a control

**Parameters**

* ControlName: name of the control to retrieve the text

**Example**

```
&driver.GetText("ControlLabel") 
&driver.GetText("webComponent1.control1")
```

## [GetText](#GetText)

`[imagen omitida: wiki id 47322]`

Gets the text of a control

**Parameters**

* ControlName: name of the control to retrieve the text
* Row: row number inside the grid

**Example**

```
&driver.GetText("ControlLabel", 3)
&driver.GetText("webComponent1.control1", 1)
```

## [GetTextByID](#GetTextByID)

`[imagen omitida: wiki id 47913]`

Gets the text from an HTML element using its ID.

Returns: The text of the selected element.

Parameters:

* ID: the HTML element ID to retrieve the text.

Example of use:

```
&txt1 = &driver.GetTextById("CountryName")
```

## [GetTextByName](#GetTextByName)

`[imagen omitida: wiki id 47914]`

Gets the text from an HTML element using its  'name' attribute.

Returns: The text of the selected element.

Parameters:

* Name: the value of the NAME attribute of the element.

Example of use:

```
&txt1 = &driver.GetTextByName("CustomerName")
```

## [GetTextByCSS](#GetTextByCSS)

`[imagen omitida: wiki id 47915]`

Gets the text from an HTML element using a CSS selector.

Returns: The text of the selected element.

Parameters:

* CSS: the CSS selector to the element.

Example of use:

```
&txt1 = &driver.GetTextByCSS("label.gx-label.col-sm-3.AttributeLabel.control-label")
```

## [GetTextByXPath](#GetTextByXPath)

`[imagen omitida: wiki id 47916]`

Gets the text from an HTML element using an XPath selector.

Returns: The text of the selected element.

Parameters:

* XPath: the XPath selector to the element.

Example of use:

```
&txt1 = &driver.GetTextByXPath("//label")
```


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) | [GXtest UI Commands - Assertions](https://wiki.genexus.com/commwiki/wiki?41682) |
| [GXtest UI Test for Web - Supported Commands](https://wiki.genexus.com/commwiki/wiki?40281) |

---
