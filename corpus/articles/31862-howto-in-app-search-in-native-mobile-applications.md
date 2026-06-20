---
title: "HowTo: In-app search in Native Mobile applications"
source_id: 31862
source_url: https://wiki.genexus.com/commwiki/wiki?31862
genexus_version: "18"
---

# HowTo: In-app search in Native Mobile applications

This document explains how to create an in-app search in Native Mobile applications and provides a brief overview about it.

The increasing amount of data managed by an application is a reality. Nowadays, it is vital for every system to display content to the end user as quickly as possible and in a friendly way.  
In order to achieve this aim, GeneXus provides two different, but closely related, components to enhance this essential element called Search Pattern.

### [SearchBox control](#SearchBox+control)

The SearchBox control is a feature designed to improve the search mechanism in an application. Its aim is to store the last keyword that the end user wants to search and give a friendly UI for them.

**Warning**: When you use a search-box control, the [Enter Event property for Attribute/Variable controls](https://wiki.genexus.com/commwiki/wiki?24520,,) **should not** be set because the keyboard enter action will always execute a search.

#### [**Adding the control**](#Adding+the+control)

**1.** Create a string variable in a [Panel](https://wiki.genexus.com/commwiki/wiki?24829) ([Character](https://wiki.genexus.com/commwiki/wiki?6777), [VarChar](https://wiki.genexus.com/commwiki/wiki?6778) or [LongVarChar](https://wiki.genexus.com/commwiki/wiki?7371)).  
**2.** Drag it from the toolbox and drop it in the abstract layout.  
**3.** Set the [Control Type](https://wiki.genexus.com/commwiki/wiki?9550) property in SearchBox.  
  
These steps are summarized in the following image:  
  
`[imagen omitida: wiki id 32271]`

#### [**Properties**](#Properties)

When the [Control Type](https://wiki.genexus.com/commwiki/wiki?9550) property is set with SearchBox value, new properties are displayed.

|  |  |  |
| --- | --- | --- |
| **Property** | **Values** | **Description** |
| **Type** | *Dynamic* (default) | The search-box will be displayed on the application bar once the end user focuses on it. |
| *Explicit* | The search-box is not going to be displayed on the application bar until the end user executes a search (i.e. the search button on the keyboard). |
|  |  |  |
| **Result Panel** | (none) | This property is the essential item in the Search Pattern. It must be set with a specially designed [Panel](https://wiki.genexus.com/commwiki/wiki?24829) in order to display the search result. The search box will be displayed on the application bar of this [Panel](https://wiki.genexus.com/commwiki/wiki?24829). See Tips section for a canonical example. |

#### [**Methods**](#Methods)

**DoSearch**

Calls the search *Result Panel* programmatically in a [client-side](https://wiki.genexus.com/commwiki/wiki?17042) event with the value set in It.  
For example, if *&SearchedText* is the variable defined with SearchBox control, then the following sentence can be written:

```
&SearchBox.DoSearch()
```

**Parameters:**None  
**Return:**None

### [Usage example](#Usage+example)

#### [**Designing the Result Panel**](#Designing+the+Result+Panel)

The first decision to make is to properly design the Result Panel which shows the result of the search.  
You might be interested in the rules that must be followed to design it properly.

**1. Adding a** ***parm*****rule**

The Result Panel is called implicitly by the main object which includes the associated SearchBox control. Remember that this control only applies to string variables (i.e. Character, VarChar, LongVarChar domains) that contain the searched word or a sequence of them. For that reason, the Result Panel must include a parm rule that receives this string in order to show the result.

```
parm(&SearchedText)
```

The variable received in this rule is declared without *in*/*out* directives, because it can be helpful to assign it or simply read it.

**2. Include a grid with a condition**

The Result Panel's aim is to show a set of records that match with the keyword. For that reason, It is necessary to include a Grid control and then set a [condition](https://wiki.genexus.com/commwiki/wiki?9763) over it to filter the content. Generally, this condition takes advantage of the [Like operator](https://wiki.genexus.com/commwiki/wiki?9991) and the '%' wildcard character, hence the condition can be written like:

```
MyStringAttribute LIKE '%'+&SearchedText;
```

**Where:**

*&SerchedText*   
      Is the string variable received in the *parm*rule

*MyStringAttribute*   
      Is the string attribute you want to match the text with.

Summarizing, the complete process to create the Result Panel is similar to that described in the image below.

`[imagen omitida: wiki id 32064]`

#### [**Adding features to the Result Panel**](#Adding+features+to+the+Result+Panel)

The [Search external object](https://wiki.genexus.com/commwiki/wiki?39378,,) purpose is to define events in the Result Panel in order to be triggered when the end user executes a certain condition. For example, it can be useful to refresh the Grid in the Result Panel when the text changes. Consequently, an event like this can be written:

```
Event Search.SearchTextChanged(&vText)
    &SearchedText = &vText
    refresh
EndEvent
```

Remember that *&SerchedText* is the string variable received in the *parm* rule.

### [Download](#Download)

You can download this example from [here](https://wiki.genexus.com/commwiki/wiki?33814,,).

**Note**: On
[Android](https://wiki.genexus.com/commwiki/wiki?14453) devices, the SearchBox control will be shown in place of the application bar. Then, it can be customizable by its respective theme class (e.g. Forecolor of the searched text).

### [Scope](#Scope)

**Objects:** [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974)   
**Data Types:**[Character](https://wiki.genexus.com/commwiki/wiki?6777), [VarChar](https://wiki.genexus.com/commwiki/wiki?6778), [LongVarChar](https://wiki.genexus.com/commwiki/wiki?7371)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604), 
[Java](https://wiki.genexus.com/commwiki/wiki?12258), 
[Apple](https://wiki.genexus.com/commwiki/wiki?14917), 
[Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Availability](#Availability)

This feature applies since [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?28265,,).


|  |
| --- |
| **Backlinks** |
| [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) | [Results Panel property](https://wiki.genexus.com/commwiki/wiki?42205) |

---
