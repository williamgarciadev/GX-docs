---
title: "MarkdownStyle property"
source_id: 60850
source_url: https://wiki.genexus.com/commwiki/wiki?60850
genexus_version: "18"
---

# MarkdownStyle property

Indicates the Design System object used to style the markdown content in a response of a Chat.

### [Scope](#Scope)

**Controls:** [Chat Control](https://wiki.genexus.com/commwiki/wiki?59254)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

This property allows you to customize the visual appearance of messages that include Markdown formatting.

By default, the value of this property is the Markdown [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375), but you can assign a different one if needed.

**Note:** For [.NET](https://wiki.genexus.com/commwiki/wiki?38604) and [Java](https://wiki.genexus.com/commwiki/wiki?12258) generators, this Design System Object cannot use the [Import style rule](https://wiki.genexus.com/commwiki/wiki?49346) or [Design System Tokens](https://wiki.genexus.com/commwiki/wiki?47378). For [Angular generator](https://wiki.genexus.com/commwiki/wiki?42550), both are supported.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Availability](#Availability)

Since [GeneXus 18 Upgrade 14](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?59631,,) and [GeneXus Next](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?57864,,).
