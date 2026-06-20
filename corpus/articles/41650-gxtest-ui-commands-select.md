---
title: "GXtest UI Commands - Select"
source_id: 41650
source_url: https://wiki.genexus.com/commwiki/wiki?41650
genexus_version: "18"
---

# GXtest UI Commands - Select

Select commands are used to choose an option from drop-down boxes (and radiobuttons if using controlName commands) using the visible **Text** of the elements.

## [Select](#Select)

`[imagen omitida: wiki id 46618]`

Selects an option using drop-down or radiobutton's control name.

**Parameters**

* ControlName: name of the control where the option is displayed
* Value: the option to select

**Example**

```
&driver.Select("clientPreferredContactTime", "Morning")
```

## [Select](#Select)

`[imagen omitida: wiki id 47307]`

Selects an option using the drop-down or radiobutton's control name inside a grid.

**Parameters**

* ControlName: name of the control where the option is displayed
* Row: row number inside the grid to locate the control
* Value: the option to select

**Example**

```
&driver.Select("clientPreferredContactTime", 1, "Morning")
```

## [SelectByID](#SelectByID)

`[imagen omitida: wiki id 46619]`

Selects an option using drop-down's ID attribute.

Parameters:

* ID: the HTML element ID of the drop-down control.
* Text: the visible text of the option to choose.

Example of use:

```
&driver.SelectById("Country", "England")
```

## [SelectByName](#SelectByName)

`[imagen omitida: wiki id 46620]`

Selects an option using drop-down's 'name' attribute.

Parameters:

* Name: the 'name' attribute of the drop-down control.
* Text: the visible text of the option to choose.

Example of use:

```
&driver.SelectByName("City", "London")
```

## [SelectByCSS](#SelectByCSS)

`[imagen omitida: wiki id 46621]`

Selects an option from a drop-down using a CSS selector.

Parameters:

* CSS: the CSS selector to the drop-down that you want to Select.
* Text:  the visible text of the option to choose.

Example of use:

```
&driver.SelectByCSS("#currency", "US Dollars")
```

## [SelectByXPath](#SelectByXPath)

`[imagen omitida: wiki id 46622]`

Selects an option from a drop-down using an XPath selector.

Parameters:

* XPath: the XPath selector to the drop-down item that you want to Select
* Text:  the visible text of the option to choose

Example of use:

```
&driver.SelectByXPath("//select[@id='groupSelect']", "First Option")
```


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) | [GXtest UI Commands - Mouse Move](https://wiki.genexus.com/commwiki/wiki?41653) |
| [GXtest UI Test for Web - Supported Commands](https://wiki.genexus.com/commwiki/wiki?40281) |

---
