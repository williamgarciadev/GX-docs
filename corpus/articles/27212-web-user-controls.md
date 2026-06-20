---
title: "Web User Controls"
source_id: 27212
source_url: https://wiki.genexus.com/commwiki/wiki?27212
genexus_version: "18"
---

# Web User Controls

**Warning**: Since GeneXus 16, it is strongly recommended to create a [User Control object](https://wiki.genexus.com/commwiki/wiki?39356) instead of creating a Web User Control. However, what it is explained in this Table of Content is still valid.

Web [User Controls](https://wiki.genexus.com/commwiki/wiki?5273) like the following can be included in GeneXus applications:

|  |  |  |  |
| --- | --- | --- | --- |
|  |  |  |  |

After a User Control is installed in GeneXus, it should be used as any other standard control. This means that:

* You will have User Controls available in the Toolbox.
* You will manipulate User Controls like any other standard control at design time.
* Some controls may be bound to variables or attributes. They may also be used in the attribute control information.
* Programming with User Controls is the same as programming with standard controls:
  + Setting Properties: control.PropertyName = value
  + Handling Server Events:  
        Event control.Click  
        EndEvent
  + So, when somebody develops a user control, GeneXus is extended!

To start working with User Controls, you can try with any of the User Controls which are available by default in the GeneXus toolbar, or download a new one from the [GeneXus marketplace](https://marketplace.genexus.com/home.aspx?,en)

The [User controls catalog](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?27213,,) is useful documentation to start with, as it shows some of the User Controls available and how to use each of them.


* Getting started
  + [User controls catalog](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?27213,,)
  + [HowTo: Install User Controls](https://wiki.genexus.com/commwiki/wiki?5920)
* Building a user control
  + [User control structure overview](https://wiki.genexus.com/commwiki/wiki?26973)
  + [How does a User Control work?](https://wiki.genexus.com/commwiki/wiki?26998)
  + [User Control Generator](https://wiki.genexus.com/commwiki/wiki?32550)
  + [User Control Editor](https://wiki.genexus.com/commwiki/wiki?26976)
  + [Useful Js functions in the gxgral.js](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?16689,,)
  + [User Controls based on jQuery](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?16044,,)
* Basic examples
  + [Creating a "Hello World" user control](https://wiki.genexus.com/commwiki/wiki?4880)
    - [Hello World Control Definition File](https://wiki.genexus.com/commwiki/wiki?4943)
    - [Hello World Control Properties File](https://wiki.genexus.com/commwiki/wiki?4946)
    - [Hello World Runtime Render File](https://wiki.genexus.com/commwiki/wiki?4947)
    - [Hello World Design Render File](https://wiki.genexus.com/commwiki/wiki?4949)
  + [Creating a Slider User Control](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?4804,,)
  + [Hello World Container User Control](https://wiki.genexus.com/commwiki/wiki?5387)
* Advanced examples
  + [Building a User Controls library based on Kendo UI](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?24529,,)
  + [Map User Control](https://wiki.genexus.com/commwiki/wiki?5029)
* Troubleshooting
  + [FAQ](https://wiki.genexus.com/commwiki/wiki?6771)
  + [Debugging a User Control](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?16685,,)

---
