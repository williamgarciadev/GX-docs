---
title: "Window Data Type"
source_id: 7112
source_url: https://wiki.genexus.com/commwiki/wiki?7112
genexus_version: "18"
---

# Window Data Type

The Window Data Type allows opening an object or an external URL in a popup window. If the page called is in the same server as the caller screen, the popup will be opened in [modal](http://en.wikipedia.org/wiki/Modal_window) status, which means that it blocks the parent application until the user closes it in any way.

To open a popup window from any web object, a Window Data Type variable should be defined. Afterward, some information must be indicated, such as a ([Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916), [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908), HTTP Procedure) or a URL to be opened. The popup window will be opened in modal status (like GeneXus [Selection Lists](https://wiki.genexus.com/commwiki/wiki?23894)), except when the web page indicated to be opened is in a different server than the caller page. In such cases, a new window will be opened and both (caller and called) will be active. In addition, some properties are available to indicate the size and position of the popup window.

### [Properties](#Properties)

|  |
| --- |
| Autoresize |
| Height |
| Left |
| Object |
| Position |
| Top |
| URL |
| Width |

**Autoresize**

Indicates if the popup window will be resized to the web page content when opened. Possible values are True or False (Boolean).  
Default value: True.

**Height**

Indicates the height of the popup window to be opened. This property is considered only if Autoresize = False.

**Left**

Indicates the left position of the popup window to be opened. This property is considered only if Position = 1 (Absolute).

**Object**

Web Object to be opened in the popup window. The supported object types are as follows:

* Web Panels
* [Web Components](https://wiki.genexus.com/commwiki/wiki?2538) with URL Access = Yes
* Transactions (if Type = Component, URLAccess should be set to Yes in order to be supported)
* [Procedures](https://wiki.genexus.com/commwiki/wiki?6293) with Call Protocol = HTTP

The object is indicated using the Create command, i.e. using the following syntax:

* &Window.**Object** = *GeneXusWebObject*.**Create**(params)
* &Window.**Object** = **Create**(*GeneXusWebObject*, params)

If another object type is used to assign the Object property of a Window type variable, a specification error of the following types will be displayed.

* spc0008 Source : Call to program *<GeneXusWebObject>* that cannot be generated.
* spc0012 Source : Object *<GeneXusWebObject>* referenced in a create function must be a component.

**Position**

Indicates the position of the popup window to be opened. Possible values are 1 (Absolute) or 0 (Centered).  
Default value : 0 (Centered).

**Top**

Indicates the top position of the popup window to be opened. This property is considered only if Position = 1 (Absolute).

**URL**

Indicates a URL to be opened in the popup window. It admits any character value and assignment can be done using constants, attributes, variables or function results.

* &Window.**URL** = 'http://www.google.com'
* &Window.**URL** = CharAttribute
* &Window.**URL** = &CharVariable
* &Window.**URL** = link(*GeneXusWebObject*, params)

**Width**

Indicates the width of the popup window to be opened. This property is considered only if Autoresize = False.

### [**Methods**](#Methods)

**Open**

Opens the indicated web page in a popup window. The popup window will be opened in modal status, except when the web page indicated to be opened is in a different server than the caller page. In that case, a new window will be opened and both (caller and called) will be active.

**Considerations:**

* If there are two or more assignments of URL or Object properties in an event (i.e. two URL assignments, two Object assignments or one of each), only the last one will be considered.

### [Samples](#Samples)

The following code:

```
Event 'OpenInformation'
    &window.Object = AirlineList.Create()
    &window.Open()
EndEvent
```

Will have the following behavior:

`[imagen omitida: wiki id 6227]`

and the following code:

```
Event 'OpenGoogle'
    &window.URL = 'http://www.google.com'
    &window.Open()
EndEvent
```

The following behavior:

`[imagen omitida: wiki id 13677]`

As you can see, if the web page to be opened is in a different server from the caller page, the popup window is not opened in modal status (you can continue working on the caller page); in fact, a new browser instance is created.

### [Scope](#Scope)

**Objects:** [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Component](https://wiki.genexus.com/commwiki/wiki?1864), [Procedure](https://wiki.genexus.com/commwiki/wiki?6293)  
**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258), [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), Ruby (up to GeneXus X Evolution 3)


|  |
| --- |
| **Backlinks** |
| [Data types list](https://wiki.genexus.com/commwiki/wiki?6779) | [Open method](https://wiki.genexus.com/commwiki/wiki?6992) | [PopUp command](https://wiki.genexus.com/commwiki/wiki?6226) |
| [Web Events and Window Data Type](https://wiki.genexus.com/commwiki/wiki?8227) |

---
