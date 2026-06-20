---
title: "GXtest UI Commands - Selectors"
source_id: 47719
source_url: https://wiki.genexus.com/commwiki/wiki?47719
genexus_version: "18"
---

# GXtest UI Commands - Selectors

In order to interact and get information from displayed elements on a web page, there are some locators to do so. They are presented below.

## [Control Name selector](#Control+Name+selector)

This is a GeneXus locator in the sense of it is HTML-independent. You can write your test without having to worry about dealing with the HTML selectors explained below.

You can recognize where this selector can be used because the parameter name is usually called ControlName or TableName and the command does not include HTML locators on its name such as ByID, ByXPath, etc.; you will just see Click(ControlName: character), Type(ControlName: Character, Text: character), etc.

In GeneXus, you can not define two elements with the same [control name](https://wiki.genexus.com/commwiki/wiki?40117), except when the control is replicated as a grid or table column or there are web components that include controls with the same name.

So, there are 4 flavors for this selector:

* Simple control: unique control in a web panel.
* Grid/Table control: control included on a grid or table, it can be in different rows, the Row parameter is needed to unequivocally locate a control.
* Simple control inside web component: if a simple control is inside a web component it can be located passing as control name the control name of the web component, a dot, and the control name.
* Grid/Table control inside web component: exactly as the previous flavor and adding the Row parameter due it is inside a table/grid control.

For example, for the following web panel:

`[imagen omitida: wiki id 47723]`

If you want to click the &Name variable at the third row in the grid you should write

```
&driver.Click("&Name", 3)
```

If the control would be inside a web component named Component1 you should write:

```
&driver.Click("Component1.&Name", 3)
```

If you want to click the variable outside the table, the simple control, you should write:

```
&driver.Click("&Name")
```

If the control would be inside a web component named MyWebComponent you should write:

```
&driver.Click("MyWebComponent.&Name")
```

Note 1: Variables require that the ampersand symbol (&) be included as a part of the control name selector.

Note 2: Error viewer controls don't have a control name property. Usually, you want to get their text, for those cases use GetMessages() command.

## [Id selector](#Id+selector)

This is the most recommended selector because the [id attribute must be unique](https://www.w3.org/TR/2011/WD-html5-20110525/elements.html#the-id-attribute) amongst all elements in a DOM. This attribute **is case-sensitive**.

Use it every time it is available; not all elements have it.

For example, for this button we have the following HTML element:

`[imagen omitida: wiki id 47720]`

So, for example, to click it write on your test:

```
&driver.ClickByID("BTN2")
```

## [Name selector](#Name+selector)

This selector is available for some common elements such as buttons, forms, inputs, selects, and others.

For example, for the same button shown in the previous image, to get its text you should write on your test:

```
&driver.GetValueByName("BTN2")
```

## [CSS selector](#CSS+selector)

CSS selector allows different ways of locating an element. For example, using Google Chrome, an easy way to obtain a CSS selector for an element is to inspect the element and right-click over it, then select the option Copy -> Copy Selector. It is very similar when using other browsers.

For example, for the following HTML element:

```
<div class="gx-warning-message">Button 2 pressed</div>
```

You can get its text executing the following command:

```
&driver.GetTextByCSS(".gx-warning-message") // It uses element class
```

## [XPath selector](#XPath+selector)

If the elements are not found by the previous locators like id, CSS, and name, then another option is using an XPath selector. This selector is from XML structure and it is powerful since it allows different search criteria such as by text, class name, tag name, attribute, etc.

For example, if you want to get the text of this element:

```
<div class="gx-warning-message">Button 2 pressed</div>
```

You can write the command:

```
&driver.GetTextByXPath('//div[@class="gx-warning-message"]')
```

## [LinkText selector](#LinkText+selector)

This selector can be used with link elements only. For example, for the following link:

`[imagen omitida: wiki id 47721]`

You can add the command:

```
&driver.ClickByLinkText("gxtest doc")
```

## [Locating elements inside shadow DOMs](#Locating+elements+inside+shadow+DOMs)

[Shadow DOMs](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_shadow_DOM) are documents inside other documents, and by default elements within them can't be accessed using only one selector. At least, you need to combine 2 selectors to interact with an element inside a shadow DOM: the first one to locate the element from which the nested document is the child, and the second one to locate the element itself.

For this reason, and to keep the selector as one parameter, you can combine as many selectors as you need using the following escape sequence >>> between selectors.

For example, if a page contains a div with id="element1" which is the parent of the dom document that contains the button with id="button1" you want to click, you should write the following command:

```
&driver.Click("id=element1>>>id=button1")
```

Note that you can use any other selection strategy replacing the id= part for any other valid option, such as name=, css=, control=, xpath=, and linktext=. The selector is not case-sensitive.


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Changelog GXtest](https://wiki.genexus.com/commwiki/wiki?43807) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) |

---
