---
title: "GXtest UI Commands - Custom Commands"
source_id: 47402
source_url: https://wiki.genexus.com/commwiki/wiki?47402
genexus_version: "18"
---

# GXtest UI Commands - Custom Commands

GXtest provides a wide set of commands to simulate user interaction on a web page. However, there are more interactions that can not be achieved with these commands and, on this page, we provide some examples of custom commands that you can execute using the command [ScriptEval](https://wiki.genexus.com/commwiki/wiki?41616). You should be able to run any javascript code using this command taking into account that some browsers don't support the same functions.

## [Scroll](#Scroll)

Scrolling is automatically handled by GXtest, but some pages load the objects after a scrolling action is performed. If you need to simulate this action you can use some javascript functions like scrollTo or scrollBy:

```
&driver.ScriptEval("window.scrollTo(0, document.body.scrollHeight)") // scroll to the end of the page

&driver.ScriptEval("window.scrollBy(0,1000)") // scroll 1000 pixels down
```


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) |

---
