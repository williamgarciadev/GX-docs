---
title: "HowTo: Format plain text programmatically"
source_id: 31657
source_url: https://wiki.genexus.com/commwiki/wiki?31657
genexus_version: "18"
---

# HowTo: Format plain text programmatically

GeneXus is able to detect the presence of HTML tags written programmatically in [Client-side Events](https://wiki.genexus.com/commwiki/wiki?24332). This approach behaves as the [Format property](https://wiki.genexus.com/commwiki/wiki?46309) when used to format plain text at design time for certain string properties. However, in this case, GeneXus guesses at runtime which written strings are formatted with HTML tags.

### [HTML tags](#HTML+tags)

The table below shows the equivalence between HTML tags and Format effect names commonly found in text editors.

| Tags | Format | Examples | |
| --- | --- | --- | --- |
| *Input* | *Output* |
| **b, strong** | Bold | <b>example</b> text | **example**text |
| **i, em, cite, dfn** | Italics | <em>example</em> text | *example*text |
| **u** | Underline | <u>example</u> text | example text |
| **sub** | Subtext | <sub>example</sub> text | exampletext |
| **sup** | Supertext | <sup>example</sup> text | exampletext |
| **big** | Big | <big>example</big> text | example text |
| **small** | Small | <small>example</small> text | example text |
| **h1 … h6** | Headlines | - | - |
| **font** | Font face and color | <font color="red" size="3">example</font> text | example text |
| **blockquote** | For longer quotes | <blockquote>example</blockquote> | example |
| **a** | Link | <a href="genexus.com">example</a> | [example](genexus.com) |
| **div, p** | Paragraph | <p>example</p> | example |
| **br** | Linefeed | ex<br />ample | ex  ample |

### [Character entity reference](#Character+entity+reference)

In addition, a character entity reference to the string can be added. All characters have the following format:   
  
        **&***<name>***;**   
  
**Where:**

*<name>*  
      Is the name of the character.

Common character names are listed below with their results.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Name** | **Character** |  | **Name** | **Character** |
| quot | " |  | alpha | α |
| amp | & |  | beta | β |
| apos | ' |  | gamma | γ |
| lt | < |  | delta | δ |
| gt | > |  | epsilon | ε |
| le | ≤ |  | zeta | ζ |
| ge | ≥ |  | eta | η |
| ne | ≠ |  | theta | θ |
| pount | £ |  | iota | ι |
| current | ¤ |  | kappa | κ |
| yen | ¥ |  | lambda | λ |
| copy | © |  | mu | μ |
| reg | ® |  | nu | ν |
| trade | ™ |  | xi | ξ |
| plusmn | ± |  | omicron | ο |
| sup1 | ¹ |  | pi | π |
| sup2 | ² |  | rho | ρ |
| sup3 | ³ |  | sigma | σ |
| isin | ∈ |  | tau | τ |
| notin | ∉ |  | phi | φ |
| exist | ∃ |  | chi | χ |
| forall | ∀ |  | psi | ψ |
| part | ∂ |  | omega | ω |
| sum | ∑ |  | larr | ← |
| prod | ∏ |  | rarr | → |
| int | ∫ |  | uarr | ↑ |
| radic | √ |  | darr | ↓ |
| inf | ∞ |  | harr | ↔ |
| sub | ⊂ |  | carr | ↵ |
| sup | ⊃ |  | lArr | ⇐ |
| nsub | ⊄ |  | uArr | ⇑ |
| sube | ⊆ |  | rArr | ⇒ |
| supe | ⊇ |  | dArr | ⇓ |
| empty | ∅ |  | hArr | ⇔ |
| and | ∧ |  |  |  |
| or | ∨ |  |  |  |

Note that names are *case-sensitive*. A complete list can be found [here](https://en.wikipedia.org/wiki/List_of_XML_and_HTML_character_entity_references#Character_entity_references_in_HTML).

### [Samples](#Samples)

Suppose that you want to alert the user about a certain action. This can be done using a single invocation of [Confirm function](https://wiki.genexus.com/commwiki/wiki?31634) before the action section code.

```
Event 'AddToCart'
    Composite
        Confirm("<font color='#e68a00' size='3'>WARNING</font><br>Are you sure? It can <b>not</b> be <u>undone</u>")
        Do 'SubAddToCart'
    EndComposite
Endevent
```

The result of invoking this action is as follows:

`[imagen omitida: wiki id 31681]`

Also, you are able to format the Form (e.g. promoting some benefit for end users). In this case, this is achieved with a single line of code:

```
Event ClientStart
     Form.Caption = iif(ProductPrice < 100, "This product has <b>Free <i>shipping</i>!</b>", "Detail")
Endevent
```

`[imagen omitida: wiki id 31682]`

**Note**: If you use **[NewLine function](https://wiki.genexus.com/commwiki/wiki?8469)** and **<br />** HTML tag in the same text, the first one will be ignored.

### Scope

**Controls**: [Attribute](https://wiki.genexus.com/commwiki/wiki?7240)/[Variable](https://wiki.genexus.com/commwiki/wiki?7375), [Button](https://wiki.genexus.com/commwiki/wiki?6011), [Text Block](https://wiki.genexus.com/commwiki/wiki?5948)  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917),[.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Availability](#Availability)

This property is available since [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?28265,,).


|  |
| --- |
| **Backlinks** |
| [Control Properties - Font](https://wiki.genexus.com/commwiki/wiki?8889) | [Empty Grid Text property](https://wiki.genexus.com/commwiki/wiki?20224) | [FontUnderline property](https://wiki.genexus.com/commwiki/wiki?8780) |
| [Msg function](https://wiki.genexus.com/commwiki/wiki?31635) | [Tab control for Panels](https://wiki.genexus.com/commwiki/wiki?29986) | [Underline Property](https://wiki.genexus.com/commwiki/wiki?6956) |

---
