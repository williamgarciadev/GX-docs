---
title: "Import style rule"
source_id: 49346
source_url: https://wiki.genexus.com/commwiki/wiki?49346
genexus_version: "18"
---

# Import style rule

Imports and uses definitions made in any of the following entities: Design System Object, Design System Tokens, Design System Styles and External CSS.

It is written at the beginning of the set of DSO Style definitions.

### [Syntax](#Syntax)

```
{@import {{ <DSO_name> | <DSO_name>.tokens | <DSO_name>.styles }...
          |
          { <CSS_path_file> }...
          |
          {gx-file'('<CSS_KB_file>')'}... 
          }';'  
}...
```

View [Design System Syntax conventions](https://wiki.genexus.com/commwiki/wiki?49363)

**Where:**

*DSO\_name*[Qualified Name](https://wiki.genexus.com/commwiki/wiki?22477) of a DSO in the [KB](https://wiki.genexus.com/commwiki/wiki?2428).

*CSS\_path\_file*Relative or absolute path of the external CSS file to be imported.

*CSS\_KB\_file*Name of a [File object](https://wiki.genexus.com/commwiki/wiki?5852) of the KB with CSS format.

**gx-file**  
     Function that can be used in Styles to indicate the file object of the KB to be accessed.

### [Restrictions](#Restrictions)

●   Only .css files can be imported.  
●    It is not possible to combine the import of files with that of the DSO in the same line.  
●    This rule can only be written at the beginning of the definition of a Styles set.

### [Considerations](#Considerations)

●    In the Styles of a design system, there is always an implicit import of the Tokens of that same DSO. This implicit import takes precedence over all other imports performed and cannot be removed.  
●    Due to the above and because there is a direct dependency between the Styles part and the Tokens part of the same DSO, importing styles from an external DSO is equivalent to importing the complete DSO with its Tokens.  
●    The precedence of imports follows these rules:  
                       ○    All [classes](https://wiki.genexus.com/commwiki/wiki?49309) and Tokens of the DSO itself take precedence over classes and tokens imported from others.  
                       ○    If you have more than one import rule, the second written rule takes precedence over the previous ones.

### [Samples](#Samples)

```
styles MyStyles
{
    @import DesignSystem1 DesignSystem2.tokens DesignSystem3.styles;
    @import "../my_file1.css" "../my_file2.css";
    @import gx-file(CSSFile.css);
    
    .class1
    {
        //Properties...
    }
}
```

### [Availability](#Availability)

Since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?48684,,).

### [See Also](#See+Also)

See the general topic [Design System Style Rules](https://wiki.genexus.com/commwiki/wiki?47472).  
[Syntax conventions](https://wiki.genexus.com/commwiki/wiki?6626)


|  |
| --- |
| **Backlinks** |
| [Base CSS property in Design System Object](https://wiki.genexus.com/commwiki/wiki?49256) | [Design System Style Rules](https://wiki.genexus.com/commwiki/wiki?47472) | [Design System Styles](https://wiki.genexus.com/commwiki/wiki?47379) |
| [Design System Tokens](https://wiki.genexus.com/commwiki/wiki?47378) | [Toc:Design Systems](https://wiki.genexus.com/commwiki/wiki?40108) |

---
