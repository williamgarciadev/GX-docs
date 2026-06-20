---
title: "Format property"
source_id: 46309
source_url: https://wiki.genexus.com/commwiki/wiki?46309
genexus_version: "18"
---

# Format property

Indicates whether the contents of the control must be interpreted as text or as HTML code.

### [Values](#Values)

|  |  |
| --- | --- |
| **HTML** | The content of the control will be interpreted as HTML code. |
| **Text** | The content of the control will be interpreted as text. This is the default value. |

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Controls:** [Text Block](https://wiki.genexus.com/commwiki/wiki?5948)

### [Description](#Description)

When the Format property is set to **HTML**, the control interprets the content of the Text Block as HTML code.

This property is intended to add style to the text, not to display a complete web page. In other words, it allows you to change the text style, colors, etc. To display a complete web page, it is recommended to use a variable based on the [Component](https://wiki.genexus.com/commwiki/wiki?16186) domain.

**Supported tags**

|  |  |
| --- | --- |
| **Tag** | **Description** |
| ``` <b> ``` | Bold text. |
| ``` <i> ``` | Italic text. |
| ``` <u> ``` | Underline text. |
| ``` <font color=""> ``` | Text color. |
| ``` <br> ``` | Line Break. |

**Not Supported tags:** <div>, <p>, <span>, <ul>, <ol>, <table>, and other layout or structural tags.

**Note:** To display rich or structured HTML content, use a WebView control or variable based on the Component domain.

When the Format property is set to **Text**, the control interprets the content as plain text.  
To insert a line break, use the [NewLine() function](https://wiki.genexus.com/commwiki/wiki?8469).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

**Correct use:**

```
TextBlock.Format = HTML
TextBlock.Value = "<b>Promotion:</b> 2x1 on Fridays!"
```

**Incorrect use:**

```
TextBlock.Format = HTML
TextBlock.Value = "<div><p>Promotion 2x1</p></div>"
```

**Note:** The HTML format for a TextBlock is intended only for styling text, not for rendering a complete HTML page or structured content.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770).

### [See Also](#See+Also)

[Format property (for Web)](https://wiki.genexus.com/commwiki/wiki?31666)


|  |
| --- |
| **Backlinks** |
| [Format property (for Web)](https://wiki.genexus.com/commwiki/wiki?31666) | [HowTo: Format plain text programmatically](https://wiki.genexus.com/commwiki/wiki?31657) |

---
