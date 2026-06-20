---
title: "GXtest UI Commands - Mouse Move"
source_id: 41653
source_url: https://wiki.genexus.com/commwiki/wiki?41653
genexus_version: "18"
---

# GXtest UI Commands - Mouse Move

You can simulate the mouse moving to a certain location, by providing the HTML element location. This will cause the mouse position to be set at the top-left corner of the specified element.

In case you want to select options or click elements, refer to:

* [Click and Double click](https://wiki.genexus.com/commwiki/wiki?41647)
* [Select](https://wiki.genexus.com/commwiki/wiki?41650)

## [MouseMoveByID](#MouseMoveByID)

Sets the mouse position at the top-left corner of the specified element using its ID.

Parameters:

* ID: the HTML element ID to locate.

Example of use:

```
&driver.MouseMoveById("BTN1")
```

## [MouseMoveByLinkText](#MouseMoveByLinkText)

Sets the mouse position at the top-left corner of the specified link using its text:

Parameters:

* LinkText: the link text to locate.

Example of use:

```
&driver.MouseMoveByLinkText("mouse-over here")
```

## [MouseMoveByName](#MouseMoveByName)

Sets the mouse position at the top-left corner of the specified element using its 'name' attribute.

Parameters:

* Name: the NAME attribute of the control to locate.

Example of use:

```
&driver.MouseMoveByName("BTN2")
```

## [MouseMoveByCSS](#MouseMoveByCSS)

Sets the mouse position at the top-left corner of the specified element using a CSS selector.

Parameters:

* CSS: the CSS selector to the element that you want to locate.

Example of use:

```
&driver.MouseMoveByCSS("#button1")
```

## [MouseMoveByXPath](#MouseMoveByXPath)

Sets the mouse position at the top-left corner of the specified element using an XPath selector.

Parameters:

* XPath: the XPath selector to the element that wants to be located.

Example of use:

```
&driver.MouseMoveByXPath("//span/input")
```


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) | [GXtest UI Test for Web - Supported Commands](https://wiki.genexus.com/commwiki/wiki?40281) |

---
