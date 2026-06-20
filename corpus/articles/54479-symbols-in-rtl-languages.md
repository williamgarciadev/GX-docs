---
title: "Symbols in RTL languages"
source_id: 54479
source_url: https://wiki.genexus.com/commwiki/wiki?54479
genexus_version: "18"
---

# Symbols in RTL languages

When combining symbols that can be used in both RTL and LTR languages (such as periods, commas, or other punctuation marks), their displayed positions will depend on the direction of the text. This is because the data format starts from the beginning, but a browser is still processing an RTL word in the RTL direction and punctuation is converted towards the direction that has been specified.

Take the following image, the question mark symbol are correctly set but the Arabic text is not aligned to the right side.

`[imagen omitida: wiki id 42333]`

Changing the alignment to the right solves the problem but creates a new one related with the question mark symbol.

`[imagen omitida: wiki id 42334]`

To fix this problem, try converting RTL and LTR strings (or text fragments) into separate elements, for example, use different Textblocks. Then, specify their direction with either the [dir attribute](https://caniuse.com/?search=html%20dir%20attribute) or the CSS direction property, for that matter changing the associated Theme class.


|  |
| --- |
| **Backlinks** |
| [Toc:Getting ready for Right-to-Left Development](https://wiki.genexus.com/commwiki/wiki?42322) |

---
