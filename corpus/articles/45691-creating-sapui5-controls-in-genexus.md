---
title: "Creating SAPUI5 controls in GeneXus"
source_id: 45691
source_url: https://wiki.genexus.com/commwiki/wiki?45691
genexus_version: "18"
---

# Creating SAPUI5 controls in GeneXus

This document is intended for developers who already know the [User Control object](https://wiki.genexus.com/commwiki/wiki?39356) and its basic concepts.

It's possible to create User Control Objects using [SAPUI5](https://sapui5.hana.ondemand.com/)'s XML based language for views in the ["Screen Template"](https://wiki.genexus.com/commwiki/wiki?39356#User+control+object+sections') part of the object.  
The target can be specified using "target" attribute in the Definition tag, in the Properties part:

```
<Definition auto="false" target="SAPUI5" render-mode="first-time">
```

In addition, it is necessary to assign the Base Style of SAPUI5 to the User Control. It's possible using the [Base Style property](https://wiki.genexus.com/commwiki/wiki?40587):

`[imagen omitida: wiki id 45693]`

### [Property binding](#Property+binding)

A property can be bound to a SAPUI5 control using the double mustache syntax, as in [HTML UC objects](https://wiki.genexus.com/commwiki/wiki?39541). For example, here we are binding the SAPUI5 Button's text property to the UC object's Caption property.

*Screen template*

```
<mvc:View
  xmlns="sap.m"
  xmlns:mvc="sap.ui.core.mvc"
  xmlns:core="sap.ui.core">
    <Button type="Accept" text="{{Caption}}" />
</mvc:View>
```

### [Data bindings for control types](#Data+bindings+for+control+types)

For UC objects where "[Is Control Type](https://wiki.genexus.com/commwiki/wiki?40584)" property is true, the data binding between the screen element and the control's value can be expressed as in [HTML UC objects](https://wiki.genexus.com/commwiki/wiki?40652), using {{DataElement}} in the screen template. For example, this code shows how to bind the SAPUI5 Switch's control state property to the UC object's value:

*Screen template*

```
<mvc:View
  xmlns:mvc="sap.ui.core.mvc"
  xmlns="sap.m">
    <Switch
      customTextOn="{{TextOn}}"
      customTextOff="{{TextOff}}"
      {{DataElement:state}}>
    </Switch>
</mvc:View>
```

### [Event handlers](#Event+handlers)

SAPUI5 UC objects support defining event handlers, like their standard [HTML UC objects](https://wiki.genexus.com/commwiki/wiki?40687,,) counterparts. For example, this code shows how to declare an event called OnClick, which is called when the press event of the SAPUI5 Button control is fired:

*Screen Template*

```
<mvc:View
  xmlns="sap.m"
  xmlns:mvc="sap.ui.core.mvc"
  xmlns:core="sap.ui.core">
    <Button type="Accept" text="{{Caption}}" {{OnClick}} />
</mvc:View>
```

*Properties*

```
<Definition auto="false">
  <Event Name="OnClick" On="press" />
  <Property Name="Caption" Type="string" Default="" />
</Definition>
```

### [Slots](#Slots)

SAPUI5 UC objects support defining [slots](https://wiki.genexus.com/commwiki/wiki?40659), but with a slight difference to fully support SAPUI5 view's syntax. To define a slot, first, the XHTML namespace must be declared in the view definition, for example:

```
<mvc:View
      xmlns:l="sap.ui.layout"
      xmlns:core="sap.ui.core"
      xmlns:mvc="sap.ui.core.mvc"
==>   xmlns:html="[http://www.w3.org/1999/xhtml]"
      xmlns="sap.m">
```

Then, the slot can be placed like this:

```
<html:slot name="body" />
```

### [AfterSAPUI5Init scripts](#AfterSAPUI5Init+scripts)

A new moment was added for the scripts, called AfterSAPUI5Init. Scripts with "when='AfterSAPUI5Init'" will be executed once SAPUI5 is loaded and ready.

### [Render mode](#Render+mode)

As many of SAPUI5 controls are expensive to render, there is a property to specify if the User Control is completely re-rendered after a property change in an event or not. Up until now, User Controls always did a full re-render when a property was changed. The rendering mode can be specified using "render-mode" attribute in the Definition tag, in the Properties part. The accepted values are "first-time" and "always" (default). If render-mode="first-time", the control will be rendered only once, allowing the developer to update the control to reflect changes in an "AfterShow" script.


|  |
| --- |
| **Backlinks** |
| [GeneXus and SAP UI5](https://wiki.genexus.com/commwiki/wiki?44001) | [Toc:GeneXus for SAP Systems](https://wiki.genexus.com/commwiki/wiki?33616) |
|

---
