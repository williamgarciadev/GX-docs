---
title: "RTL language reports"
source_id: 54481
source_url: https://wiki.genexus.com/commwiki/wiki?54481
genexus_version: "18"
---

# RTL language reports

In order to display Arabic texts in PDF reports, the fonts used need to be embedded in the documents using the PDFReport.ini file. An example of the lines needed in PDFReport.ini file are:

```
Embeed Fonts= true
[Embeed Fonts]
Arial Unicode MS= true
Microsoft Sans Serif= true

[Fonts Location (Sun)]
Arial Unicode MS= c:\windows\fonts\arialuni.ttf
Microsoft Sans Serif= c:\windows\fonts\micross.ttf
```

Notice that if you use variations such as Bold they need to be embedded too

```
Arial Unicode MS,Bold= true
...
Arial Unicode MS,Bold= c:\windows\fonts\arialuni.ttf
```


|  |
| --- |
| **Backlinks** |
| [Toc:Getting ready for Right-to-Left Development](https://wiki.genexus.com/commwiki/wiki?42322) |

---
