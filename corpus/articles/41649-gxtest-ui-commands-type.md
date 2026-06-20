---
title: "GXtest UI Commands - Type"
source_id: 41649
source_url: https://wiki.genexus.com/commwiki/wiki?41649
genexus_version: "18"
---

# GXtest UI Commands - Type

These commands are used to type text inside text box controls. Can be used to type words, numbers, dates, etc..

## [Type](#Type)

`[imagen omitida: wiki id 46789]`

Types text in an input field

**Parameters**

* ControlName: name of the control to input text
* Text: the text to type in the field

**Example**

```
&driver.Type("clientname", "A Name")
```

## [Type](#Type)

`[imagen omitida: wiki id 47309]`

Types text in an input field inside a grid

**Parameters**

* ControlName: name of the control to input text
* Row: control's row number inside the grid
* Text: the text to type in the field

**Example**

```
&driver.Type("clientname", 4, "A Name")
```

## [TypeByID](#TypeByID)

`[imagen omitida: wiki id 41663]`  
Types text on an HTML element using the control's ID.

**Parameters**:

* ID: the HTML element ID to use.
* Text: text string to be typed

**Example of use**:

```
&driver.TypeByID("vVAR1","hello world")
```

## [TypeByName](#TypeByName)

`[imagen omitida: wiki id 41664]`

Types text on an HTML element using its 'name' attribute.

**Parameters**:

* Name: the NAME attribute of the control to type on.
* Text: text string to be typed

**Example of use**:

```
&driver.TypeByName("vVAR1", "bye bye")
```

## [TypeByCSS](#TypeByCSS)

`[imagen omitida: wiki id 41665]`

Types text on an HTML element using a CSS selector.

**Parameters**:

* CSS: the CSS selector to the element that you want to type on.
* Text: text string to be typed

**Example of use**:

```
&driver.TypeByCSS("#vVAR1","byebye")
```

## [TypeByXPath](#TypeByXPath)

`[imagen omitida: wiki id 41666]`

Types text on a certain HTML element using an XPath selector.

**Parameters**:

* XPath: the XPath selector to the element that wants to be typed on.
* Text: text string to be typed

**Example of use**:

```
&driver.TypeByXPath("//textarea","Here I want to use a large large string...")
```


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) | [GXtest UI commands - Edit Content](https://wiki.genexus.com/commwiki/wiki?41652) |
| [GXtest UI Commands - Keystroke](https://wiki.genexus.com/commwiki/wiki?41651) | [GXtest UI Test for Web - Supported Commands](https://wiki.genexus.com/commwiki/wiki?40281) |

---
