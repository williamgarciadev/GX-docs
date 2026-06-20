---
title: "GXtest UI Commands - Click"
source_id: 41647
source_url: https://wiki.genexus.com/commwiki/wiki?41647
genexus_version: "18"
---

# GXtest UI Commands - Click

These commands are used to perform click or double click actions over controls and elements.

## [Click](#Click)

`[imagen omitida: wiki id 46615]`

Clicks a control using its name.

**Parameters**

* ControlName (Character): name of the control to click

**Example**

```
&driver.Click("btn_enter")
```

## [Click](#Click)

`[imagen omitida: wiki id 47302]`

Clicks a control inside a grid using its name.

**Parameters**

* ControlName (Character): name of the control to click
* Row (Numeric): row number inside the grid of the element to click. To click the first row use number 1 and so on.

**Example**

```
&driver.Click("btn_edit", 2)
```

## [ClickByID](#ClickByID)

`[imagen omitida: wiki id 41654]`

Clicks an HTML element using the control's ID.

Parameters:

* ID: the HTML element ID to click.

Example of use:

```
&driver.ClickById("BTN1")
```

## [ClickByLinkText](#ClickByLinkText)

`[imagen omitida: wiki id 41655]`

Clicks a link using its text.

Parameters:

* LinkText: the link text to click.

Example of use:

```
&driver.ClickByLinkText("click here:")
```

## [ClickByName](#ClickByName)

`[imagen omitida: wiki id 41656]`

Clicks a certain HTML element using its 'name' attribute.

Parameters:

* Name: the NAME attribute of the control to click.

Example of use:

```
&driver.ClickByName("BTN2")
```

## [ClickByCSS](#ClickByCSS)

`[imagen omitida: wiki id 41657]`

Clicks an HTML element using a CSS selector.

Parameters:

* CSS: the CSS selector to the element that you want to click.

Example of use:

```
&driver.ClickByCSS("#button1")
```

## [ClickByXPath](#ClickByXPath)

`[imagen omitida: wiki id 41658]`

Clicks an HTML element using an XPath selector.

Parameters:

* XPath: the XPath selector to the element that wants to be clicked.

Example of use:

```
&driver.ClickByXPath("//span/input")
```

## [DoubleClick](#DoubleClick)

`[imagen omitida: wiki id 47303]`

Double clicks a control using its name.

Parameters:

* ControlName: the name of the control to double click.

Example of use:

```
&driver.DoubleClick("Image1")
```

## [DoubleClick](#DoubleClick)

`[imagen omitida: wiki id 47304]`

Double clicks a control inside a grid using its name.

Parameters:

* ControlName: the name of the control to double click.
* Row (Numeric): row number inside the grid of the element to click. To click the first row use number 1 and so on.

Example of use:

```
&driver.DoubleClick("Image1", 3)
```

## [DoubleClickByID](#DoubleClickByID)

`[imagen omitida: wiki id 41659]`

Double clicks an HTML element using the control's ID.

Parameters:

* ID: the HTML element ID to double click.

Example of use:

```
&driver.DoubleClickById("control2")
```

## [DoubleClickByName](#DoubleClickByName)

`[imagen omitida: wiki id 41660]`

Double clicks an HTML element using the 'name' attribute.

Parameters:

* Name: the NAME attribute of the control to double click.

Example of use:;

```
&driver.DoubleClickByName("vVAR1")
```

## [DoubleClickByCSS](#DoubleClickByCSS)

`[imagen omitida: wiki id 41661]`

Double clicks a certain HTML element using a CSS selector.

Parameters:

* CSS: the CSS selector to the element that you want to double click.

Example of use:

```
&driver.DoubleClickByCSS("#IMAGE1")
```

## [DoubleClickByXPath](#DoubleClickByXPath)

`[imagen omitida: wiki id 41662]`

Double clicks a certain HTML element using an XPath selector.

Parameters:

* XPath: the XPath selector to the element that wants to be double-clicked.

Example of use:

```
&driver.DoubleClickByXPath("//span/input")
```


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [FileUpload command examples](https://wiki.genexus.com/commwiki/wiki?47224) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) |
| [GXtest UI Commands - Mouse Move](https://wiki.genexus.com/commwiki/wiki?41653) | [GXtest UI Test for Web - Supported Commands](https://wiki.genexus.com/commwiki/wiki?40281) |

---
