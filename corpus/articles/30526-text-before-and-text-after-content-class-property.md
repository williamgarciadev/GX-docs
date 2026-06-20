---
title: "Text Before and Text After content class property"
source_id: 30526
source_url: https://wiki.genexus.com/commwiki/wiki?30526
genexus_version: "18"
---

# Text Before and Text After content class property

It displays a piece of text before or after the contents of a label. It applies to the Textblock class and its descendants.

It's very useful when indicating the required fields of a form.

### [Example](#Example)

Consider a web transaction where the ProductName field is going to be required.

The ProductName attribute Class property is assigned to the "AttributeRequired" class.

`[imagen omitida: wiki id 30527]`

The AttributeRequired class has the following characteristics:

* [Label Class property](https://wiki.genexus.com/commwiki/wiki?28631,,) = LabelRequired

`[imagen omitida: wiki id 30528]`

The LabelRequired class is a descendant of the Textblock class, and has the following settings:

* Forecolor = red
* Text After content = \*

`[imagen omitida: wiki id 30529]`

At runtime, the ProductName label is displayed as follows:

`[imagen omitida: wiki id 30530]`
