---
title: "GXtest UI Commands - Get / Set Attribute"
source_id: 43904
source_url: https://wiki.genexus.com/commwiki/wiki?43904
genexus_version: "18"
---

# GXtest UI Commands - Get / Set Attribute

These commands are useful to modify and retrieve specific element attributes such as class, style, or any other. It requires the element selector and the name of the attribute to get or set its value.

## [SetAttributeByID](#SetAttributeByID)

`[imagen omitida: wiki id 47699]`

Sets a new value for an attribute of an element by its ID attribute value. If the attribute is not present, it is created.

Parameters:

* ID: element ID
* Attribute: name of the attribute to set
* Value: value to set

Example:

Suppose the gx-button element:  
`[imagen omitida: wiki id 47693]`

```
&driver.SetAttributeByID("BTN_FIRST", "class", "new-class")
```

## [SetAttributeByName](#SetAttributeByName)

`[imagen omitida: wiki id 47700]`

Sets a new value for an attribute of an element by its name attribute value. If the attribute is not present, it is created.

Parameters:

* Name: element's name attribute value
* Attribute: name of the attribute to set
* Value: value to set

Example:

```
&driver.SetAttributeByName("elemName", "attrName", "newValue")
```

## [SetAttributeByCSS](#SetAttributeByCSS)

`[imagen omitida: wiki id 47701]`

Sets a new value for an attribute of an element by CSS selector. If the attribute is not present, it is created.

Parameters:

* CSS: element CSS selector
* Attribute: name of the attribute to set
* Value: value to set

Example:

```
&driver.SetAttributeByCSS("cssSelector", "attrName", "newValue")
```

## [SetAttributeByXPath](#SetAttributeByXPath)

`[imagen omitida: wiki id 47702]`

Sets a new value for an attribute of an element by an XPath selector. If the attribute is not present, it is created.

Parameters:

* XPath: element XPath selector
* Attribute: name of the attribute to set
* Value: value to set

Example:

```
&driver.SetAttributeByXPath("xpathSelector", "attrName", "newValue")
```

## [SetAttributeByLinkText](#SetAttributeByLinkText)

`[imagen omitida: wiki id 47703]`

Sets a new value for an attribute of an element by its link text. If the attribute is not present, it is created.

Parameters:

* LinkText: element link text
* Attribute: name of the attribute to set
* Value: value to set

Example:

```
&driver.SetAttributeByLinkText("link text", "attrName", "newValue")
```

## [GetAttributeByID](#GetAttributeByID)

`[imagen omitida: wiki id 47694]`

Gets the value of the attribute of an element by its ID.

Parameters:

* ID: element ID
* Attribute: name of the attribute to get its value

Returns:

* Attribute's value

Example:

```
&onclickEvent = &driver.GetAttributeById("buttonX", "onclick")
```

## [GetAttributeByName](#GetAttributeByName)

`[imagen omitida: wiki id 47695]`

Gets the value of the attribute of an element by its ID

Parameters:

* Name: element name
* Attribute: name of the attribute to get its value

 Returns:

* Attribute's value

Example:

```
&onclickEvent = &driver.GetAttributeByName("buttonX", "onclick")
```

## [GetAttributeByCSS](#GetAttributeByCSS)

`[imagen omitida: wiki id 47696]`

Gets the value of the attribute of an element by a CSS selector

Parameters:

* CSS: element CSS selector
* Attribute: name of the attribute to get its value

 Returns:

* Attribute's value

Example:

```
&onclickEvent = &driver.GetAttributeByCSS("buttonCSSSelector", "onclick")
```

## [GetAttributeByXPath](#GetAttributeByXPath)

`[imagen omitida: wiki id 47697]`

Gets the value of the attribute of an element by XPath

Parameters:

* XPath: element XPath selector
* Attribute: name of the attribute to get its value

 Returns:

* Attribute's value

Example:

```
&onclickEvent = &driver.GetAttributeByXPath("buttonXPath", "onclick")
```

## [GetAttributeByLinkText](#GetAttributeByLinkText)

`[imagen omitida: wiki id 47698]`

Gets the value of the attribute of an element by its link text

Parameters:

* LinkText: element's link text
* Attribute: name of the attribute to get its value

 Returns:

* Attribute's value

Example:

```
&link = &driver.GetAttributeByLinkText("Click here", "src")
```


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) |

---
