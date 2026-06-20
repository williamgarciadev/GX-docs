---
title: "HowTo: Hide the GXflow Header"
source_id: 11950
source_url: https://wiki.genexus.com/commwiki/wiki?11950
genexus_version: "18"
---

# HowTo: Hide the GXflow Header

This document explains how to hide the GXflow header and provides a brief overview about it.

Add this code at the end of the gxui-all.js file.

```
gxui.afterShow(function(){
Ext.getCmp('gxui--wfmain-Layout-North').hide().collapse();
}, window);
```

You can find this file in:

* [**.NET**](https://wiki.genexus.com/commwiki/wiki?38604) **applications**: *<KB>\CSharpModel\Web\gxui*

* [**Java**](https://wiki.genexus.com/commwiki/wiki?12258) **applications**: *...\Apache Software Foundation\Tomcat XX\webapps\<genexus\_application\_directory>\static\gxui* (remember the web server reload).

The GXflow client will look like this:

`[imagen omitida: wiki id 11951]`

**Note**: This tip can be useful when you want to use the GXflow client embebed in a web site frame.
