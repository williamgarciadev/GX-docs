---
title: "User Control - Hello World Runtime Render File"
source_id: 4947
source_url: https://wiki.genexus.com/commwiki/wiki?4947
genexus_version: "18"
---

# User Control - Hello World Runtime Render File

**Warning**: Since GeneXus 16, it is strongly recommended to create a [User Control object](https://wiki.genexus.com/commwiki/wiki?39356) instead of creating a [Web User Control](https://wiki.genexus.com/commwiki/wiki?27212).

This document specifies how the User Control called [Hello World](https://wiki.genexus.com/commwiki/wiki?4880) must be displayed at runtime (js).

```
function HelloWorld()
{
 this.ContainerName;
 this.Width;
 this.Height;
 this.FontFace;
 this.FontColor;
 this.FontSize;

 this.show = function(data)
 {
  ///UserCodeRegionStart: show (do not remove this comment.)
  var buffer= '<font face="' + this.FontFace + '" color="' +  this.FontColor + '" size="' + this.FontSize + '">Hello World!!!</font>';   
  //document.getElementById(this.ContainerName).innerHTML = buffer.toString();   
  this.setHtml(buffer);   
  ///UserCodeRegionEnd: (do not remove this comment.)
 }
}
```


|  |
| --- |
| **Backlinks** |
| [Toc:Web User Controls](https://wiki.genexus.com/commwiki/wiki?27212) |

---
