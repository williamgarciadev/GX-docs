---
title: "Link function"
source_id: 8444
source_url: https://wiki.genexus.com/commwiki/wiki?8444
genexus_version: "18"
---

# Link function

Returns a character string with a URL format.

## [Syntax](#Syntax)

**Link(***Object* | *URL* [ *, Par**1 , ... Par**n* ] **)**  
  
**Where:**  
  
*Object* | *URL*  
    Is a [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,),
[Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916), [Web Component object](https://wiki.genexus.com/commwiki/wiki?1864),
[Panel object](https://wiki.genexus.com/commwiki/wiki?24829), [Work With object](https://wiki.genexus.com/commwiki/wiki?15974), [Image object](https://wiki.genexus.com/commwiki/wiki?23387), or URL to link.  
  
[ *par**1* ] *...* [ *par**n* ]  
    The set of parameters to pass to the object or URL.

**Type Returned:**  
Character

## [Scope](#Scope)

**Objects:**

[Transaction](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,),
[Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), 
[Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** 

[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[Java](https://wiki.genexus.com/commwiki/wiki?12258),
[Apple](https://wiki.genexus.com/commwiki/wiki?14917),
[Android](https://wiki.genexus.com/commwiki/wiki?14453),
[Angular](https://wiki.genexus.com/commwiki/wiki?42550)

## [Description](#Description)

This function returns a string to be used later in different scenarios (typically to add a link to a UI Control, or invoke an internal or external resource).

## [Samples](#Samples)

### [Linking Web Objects](#Linking+Web+Objects)

**Use case 1:** Add a link (known Web Object) to a UI Control

```
&MyLink = Link(MyObject,&Parm1, &Parm2)
Textblock1.Link = &MyLink
```

```
&MyObject = 'Module1.MyObject'
&MyLink = Link(&MyObject,&Parm1, &Parm2)
Textblock1.Link = &MyLink
```

MyObject can be a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916), [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,), [Web Component object](https://wiki.genexus.com/commwiki/wiki?1864) (with [URL access property](https://wiki.genexus.com/commwiki/wiki?7868) set to Yes), [Image object](https://wiki.genexus.com/commwiki/wiki?23387).

**Use case 2:** Instantiate a [Web Component control](https://wiki.genexus.com/commwiki/wiki?31172) with a [Web Component object](https://wiki.genexus.com/commwiki/wiki?1864)

```
&MyLink = Link(MyObject,&Parm1, &Parm2)
WebComponent.Object = CreateFromURL(&MyLink)
```

```
&MyObject = 'Module1.MyObject'
&MyLink = Link(&MyObject,&Parm1, &Parm2)
WebComponent.Object = CreateFromURL(&MyLink)
```

MyObject can be a [Web Component object](https://wiki.genexus.com/commwiki/wiki?1864).

**Use case 3:** Create a link from a Web Object and invoke it

```
&MyLink = Link(MyObject,&Parm1, &Parm2)
Link(&MyLink) //The link command is used to invoke the link, without returning any values.
```

```
&MyObject = 'Module1.MyObject'
&MyLink = Link(&MyObject,&Parm1, &Parm2)
Link(&MyLink) //The link command is used to invoke the link, without returning any values.
```

MyObject can be a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916), [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,), [Web Component object](https://wiki.genexus.com/commwiki/wiki?1864) (with [URL access property](https://wiki.genexus.com/commwiki/wiki?7868) set to Yes).

### [Linking Panels](#Linking+Panels)

**Use case 4:** Create a link from a known Object and invoke it

```
&MyLink = Link(MyObject,&Parm1, &Parm2)
call(&MyLink)

&MyObject = 'Module1.MyObject' 
&MyLink = Link(&MyObject,&Parm1, &Parm2) 
call(&MyLink)
```

MyObject can be a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829), [Work With pattern and Work With object](https://wiki.genexus.com/commwiki/wiki?15974).

**Note about use cases 1 to 4**: Recommended Coding style: Write 'MyObject.Link(Parm1,Parm2)' instead of Link(MyObject,Parm1, Parm2) when the linked object is known at design time.

### [Linking external resources](#Linking+external+resources)

**Use case 5:**Link resources of the same site  
  
You can use the link function to get a link to an external resource of the same site.

**5.1:** Document-relative

```
&MyLink = Link(!'mypath/document',&Parm1, &Parm2)
```

**Compatibility note specific to Java generator**: If the linked URL is a file (e.g. 'mypath/myspreadsheet.xlsx'), the resulting string is server-relative.

**5.2:** Server-relative

```
&MyLink = Link(!'/mypath/document',&Parm1, &Parm2)
```

**Use case 6:** Link resources of another site

**6.1:** Protocol-relative

```
&MyLink = Link(!'//example.com:80/mypath/folder1',&Parm1, &Parm2)
```

**6.2:** Absolute

```
&MyLink1 = Link(!'https://example.c:80/mypath/document',&Parm1, &Parm2) 
&MyLink2 = Link(!'http://user:pwd@example.com:80/mypath/document',&Parm1, &Parm2)
&MyLink3 = Link(!'myscheme://example.com:80/mypath/document',&Parm1, &Parm2)
```

### [Considerations](#Considerations)

* If the URL to be linked is stored in an attribute, you can write:

```
for each Company
   &MyLink = link(att:CompanyURL)
   //do something with &MyLink
endfor
```

* When the Backend generator is Java, and you are loading a Component via a relative URL in a server-side event in a Panel, the package name is added to the beginning of the path (<Base_URL>/package\_name.objectname). The Android generator checks whether the package name is already present and, if so, it does not add it again. If, for any reason, you need to have the package name duplicated in the URL, you must provide the absolute URL.
* **Rewrite rules:** When there are rewrite rules in the KB (i.e., at least one [URL Rewrite object](https://wiki.genexus.com/commwiki/wiki?46523)), all URLs are handled at runtime as server-relative URLs because it is required to avoid potential URL ambiguity. Therefore, in that case, the link function applied to a relative URL always returns a server-relative URL.
* **Parameter style**: The [Parameters Style property for Environments](https://wiki.genexus.com/commwiki/wiki?46404) determines how URLs are built when they have parameters. Thus, the link function result also takes into account this property.

### [See Also](#See+Also)

[Link command](https://wiki.genexus.com/commwiki/wiki?8446)  
[CreateFromURL function](https://wiki.genexus.com/commwiki/wiki?20509)  
[Call Variable](https://wiki.genexus.com/commwiki/wiki?17489)


|  |
| --- |
| **Backlinks** |
| [Call Variable](https://wiki.genexus.com/commwiki/wiki?17489) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) |
| [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [Link command](https://wiki.genexus.com/commwiki/wiki?8446) | [Link function (GeneXus 18 Upgrade 12 or prior)](https://wiki.genexus.com/commwiki/wiki?60052) | [Link property](https://wiki.genexus.com/commwiki/wiki?8811) |
| [Load balancing considerations](https://wiki.genexus.com/commwiki/wiki?45291) | [Category:URL Rewrite object](https://wiki.genexus.com/commwiki/wiki?46523) |

---
