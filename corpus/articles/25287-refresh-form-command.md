---
title: "Refresh Form command"
source_id: 25287
source_url: https://wiki.genexus.com/commwiki/wiki?25287
genexus_version: "18"
---

# Refresh Form command

Executes a refresh on the whole web page, causing the Start, Refresh and Load Event to be executed.

### [Syntax](#Syntax)

Form**.Refresh()**

### [Description](#Description)

It is similar to the form's implicit refresh when [Web User Experience property](https://wiki.genexus.com/commwiki/wiki?22449) is set to Previous Versions Compatible.

In general, the Form.Refresh command is used when [Web User Experience property](https://wiki.genexus.com/commwiki/wiki?22449) = Smooth. So, you must obtain the behavior of a compatible model.

### [Samples](#Samples)

Consider a web page - WEB PANEL X - containing WEB COMPONENT A, and WEB COMPONENT B, as shown in the figure below:

`[imagen omitida: wiki id 25293]`

When a user event inside the web panel X executes the form.refresh command, the following will happen:

* UserEvent    WebPanel X
* Start    WebPanel X
* Refresh    WebPanel X
* Start    WebComponent A
* Start    WebComponent B
* Load    WebPanel X
* Refresh    WebComponent A
* Load    WebComponent A
* Refresh    WebComponent B
* Load    WebComponent B

**Note:**

There is a difference between the execution of the form.refresh command in  a Smooth model's web panel and the implicit refresh of a compatible model's web page. In the second one, if we use the example mentioned before, the execution will be as follows (Note that the start event of web panel X is executed before the web panel's User event):

* Start    WebPanel X
* UserEvent    WebPanel X
* Refresh    WebPanel X
* Start    WebComponent A
* Start    WebComponent B
* Load    WebPanel X
* Refresh    WebComponent A
* Load    WebComponent A
* Refresh    WebComponent B
* Load    WebComponent B

### [See Also](#See+Also)

[Refresh method for Grid controls](https://wiki.genexus.com/commwiki/wiki?22578)  
[Refresh Web Component command](https://wiki.genexus.com/commwiki/wiki?22579)  
[Refresh command in web](https://wiki.genexus.com/commwiki/wiki?25286)


|  |
| --- |
| **Backlinks** |
| [Component control](https://wiki.genexus.com/commwiki/wiki?29811) | [Event Execution comparison between Smooth and compatible models](https://wiki.genexus.com/commwiki/wiki?25296) |
| [Event Execution Scheme](https://wiki.genexus.com/commwiki/wiki?22472) | [Refresh command in web](https://wiki.genexus.com/commwiki/wiki?25286) |

---
