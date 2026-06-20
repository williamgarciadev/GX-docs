---
title: "Accessible Role property in Text Blocks"
source_id: 60913
source_url: https://wiki.genexus.com/commwiki/wiki?60913
genexus_version: "18"
---

# Accessible Role property in Text Blocks

Indicates the semantic role of the control (what it is used for).

### [Values](#Values)

|  |  |
| --- | --- |
| Paragraph | Defines the Text Block as a paragraph (<p>). This is the default value. |
| Heading 1 | Marks the Text Block as a main title (<h1>). |
| Heading 2 | Indicates the Text Block as a secondary title (<h2>). |
| Heading 3 | Defines the Text Block as a subtitle or lower-level title (<h3>). |
| Heading 4 | Marks the Text Block as a minor title (<h4>). |
| Heading 5 | Indicates the Text Block as a subheading of even lower hierarchy (<h5>). |
| Heading 6 | Defines the Text Block as the lowest-level heading (<h6>). |

### [Scope](#Scope)

**Generators:** [Angular](https://wiki.genexus.com/commwiki/wiki?42550)  
**Controls:** [Text Block](https://wiki.genexus.com/commwiki/wiki?5948)

### [Description](#Description)

When generating an Angular application, GeneXus adds accessibility-related tags to the resulting HTML code. These tags indicate the purpose of the elements displayed in the user interface.

For the Text Block control, the Accessible Role property specifies which semantic HTML element should be generated for it. This ensures that browsers and accessibility tools can correctly interpret the text as a paragraph, or heading.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 14](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?59631,,).

### [See Also](#See+Also)

[Accessible Role property](https://wiki.genexus.com/commwiki/wiki?55453)
