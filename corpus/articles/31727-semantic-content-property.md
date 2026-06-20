---
title: "Semantic Content property"
source_id: 31727
source_url: https://wiki.genexus.com/commwiki/wiki?31727
genexus_version: "18"
---

# Semantic Content property

The Semantic content property allows determining the HTML attribute that will be generated for the control.

### [Values](#Values)

|  |  |
| --- | --- |
| **Address** | Address. |
| **Reference container** | Article. |
| **Related** | Aside. |
| **General** | Div (This is the default value). |
| **Footer** | Footer. |
| **Subtitle1** | H1 |
| **Subtitle2** | H2 |
| **Subtitle3** | H3 |
| **Subtitle4** | H4 |
| **Subtitle5** | H5 |
| **Subtitle6** | H6 |
| **Header** | Header. |
| **Main** | Main. |
| **Navigation menu** | Nav. |
| **Section** | Section. |

### [Scope](#Scope)

**Controls:** [Section](https://wiki.genexus.com/commwiki/wiki?6112)

### [Description](#Description)

Its purpose is to give semantics to the HTML and to comply with the recommendations related to [Accessibility for Web Applications](https://wiki.genexus.com/commwiki/wiki?30632).

It applies to the [Section Control](https://wiki.genexus.com/commwiki/wiki?6112).

### [Samples](#Samples)

Below are the properties for the section control whose ID is Section1. Note that the Semantic content property is set to "Related".

`[imagen omitida: wiki id 31728]`

So, the resulting HTML code is as follows:

```
<aside id="SECTION1" class="Section" style="">
<span class="TextBlock" id="TEXTBLOCK8">Test</span>
</aside>
```
