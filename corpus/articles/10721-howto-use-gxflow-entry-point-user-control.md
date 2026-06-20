---
title: "HowTo: Use GXflow Entry Point User Control"
source_id: 10721
source_url: https://wiki.genexus.com/commwiki/wiki?10721
genexus_version: "18"
---

# HowTo: Use GXflow Entry Point User Control

This document explains how to use GXflow Entry Point User Control and provides a brief overview about it.

This [user control](https://wiki.genexus.com/commwiki/wiki?5273) is used to embed any of the [GXflow](https://wiki.genexus.com/commwiki/wiki?7896,,) components in the generated applications.

### [How to Install It](#How+to+Install+It)

Unzip the GXflowEntryPoint.zip file in the UserControls folder. Execute GeneXus with /install and open GeneXus.

**Note**: You can find the zip here: <GeneXusX>\Packages\GXPM\Extra, where <GeneXusX> is the GeneXus installation folder. The UserControls folder is in the GeneXus installation folder.

### [Using the control](#Using+the+control)

To use the *GXflow Entry Point control*, drag the control from the toolbox to a [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) and you will get the following:

`[imagen omitida: wiki id 53523]`

To use the control, change at least the following properties:

`[imagen omitida: wiki id 53524]`

* Set the *EntryPoint* property to the desired [GXflow](https://wiki.genexus.com/commwiki/wiki?17836) component.
* Set the *Connection* group with a valid username and password, or set a Workflow session with a valid username or password, as shown below:

```
&Session.Set('WorkflowUser','<Workflow_User>')
&Session.Set('WorkflowPassword','<Workflow_User_Password>')
&Session has webSession type.
```

Then, when executing your [WebPage](https://wiki.genexus.com/commwiki/wiki?6916) using the control, you should get the [GXflow](https://wiki.genexus.com/commwiki/wiki?4179,,) component within your application:

`[imagen omitida: wiki id 52627]`

### [Control Properties](#Control+Properties)

* *Width*: object width in pixels or % (default 100%).
* *Height*: object height in pixels (default: 700 pixels)
* *EntryPoint*: the GXflow component to show; available values are as follows:
  + [Inbox](https://wiki.genexus.com/commwiki/wiki?7465)
  + [Outbox](https://wiki.genexus.com/commwiki/wiki?10052)
  + [My Processes](https://wiki.genexus.com/commwiki/wiki?10133)
  + [GXflow My Documents](https://wiki.genexus.com/commwiki/wiki?10135)
  + [Processes](https://wiki.genexus.com/commwiki/wiki?32180)
  + [Tasks](https://wiki.genexus.com/commwiki/wiki?10145)
  + [GXflow Business Events](https://wiki.genexus.com/commwiki/wiki?11934)
  + [Process Definitions](https://wiki.genexus.com/commwiki/wiki?10153)
  + [Participants](https://wiki.genexus.com/commwiki/wiki?10161)
  + [Events](https://wiki.genexus.com/commwiki/wiki?9339)
  + [Documents](https://wiki.genexus.com/commwiki/wiki?9337)
  + [Users](https://wiki.genexus.com/commwiki/wiki?10193)
  + [Roles](https://wiki.genexus.com/commwiki/wiki?10194,,)
  + [Organizational Units Definitions](https://wiki.genexus.com/commwiki/wiki?10195)
  + [Organizational Units](https://wiki.genexus.com/commwiki/wiki?10196)
  + [History](https://wiki.genexus.com/commwiki/wiki?7469,,)
  + [GXflow Process Performance](https://wiki.genexus.com/commwiki/wiki?18412)
  + [GXflow Process Analysis](https://wiki.genexus.com/commwiki/wiki?18410)
  + [GXflow Task Performance](https://wiki.genexus.com/commwiki/wiki?18413)
  + [GXflow Task Analysis](https://wiki.genexus.com/commwiki/wiki?18411)
  + [GXflow Team Performance](https://wiki.genexus.com/commwiki/wiki?18414)
  + My Performance
* *Border*: details if a border is shown.
* *Scrolling*: displays the scroll bar with the available values:
  + *Auto*: as default value.
  + *Yes*.
  + *No*.
* *User*: [GXflow](https://wiki.genexus.com/commwiki/wiki?10193) valid user. Use only for prototyping.
* *Password*:  [GXflow](https://wiki.genexus.com/commwiki/wiki?10193) valid password. Use only for prototyping.

#### [**Notes:**](#Notes%3A)

* This [User Control](https://wiki.genexus.com/commwiki/wiki?5273) is included in the [GXflow U3 Preview #1](http://www2.gxtechnical.com/portal/hgxpp001.aspx?15,8,8,O,S,0,,3049e) or higher version. Check the [SAC # 26110](http://www2.gxtechnical.com/portal/hgxpp001.aspx?15,4,61,O,S,0,,26110) for more information.
* Remember that "GXflowEntryPointUC.ProcessInstanceId  = <value>" only applies to "History" entry point.

### [Troubleshooting](#Troubleshooting)

If loading an XPZ fails with "error: User control 'GXflowEntryPoint' is used by some object(s) but is not installed in this GeneXus instance. Please install it and retry." install this User Control. (keyword: gxflowentrypoint )


|  |
| --- |
| **Backlinks** |
| [Category:Common Controls](https://wiki.genexus.com/commwiki/wiki?5928) | [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) |
| [GXflow Entry Point User Control](https://wiki.genexus.com/commwiki/wiki?24184) |

---
