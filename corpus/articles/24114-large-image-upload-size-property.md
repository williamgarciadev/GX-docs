---
title: "Large Image Upload Size property"
source_id: 24114
source_url: https://wiki.genexus.com/commwiki/wiki?24114
genexus_version: "18"
---

# Large Image Upload Size property

This property indicates which is the size corresponding to the value Large of the [Maximum Upload Size property](https://wiki.genexus.com/commwiki/wiki?44940). It is specified at Knowledge Base Version level.

`[imagen omitida: wiki id 24119]`

|  |  |
| --- | --- |
| **<Size>** | Size expressed in Kbytes or resolution (WidthxHeight).  A numeric value will be considered as expressed in KBytes. To specify a resolution the following grammar should be followed:  <Width> 'x' <Height>  Both <Height> and <Width> as expressed in pixels.  Default value: 1024x1024 |

### [Description](#Description)

The [Maximum Upload Size property](https://wiki.genexus.com/commwiki/wiki?44940) values ​​are symbolic (Large, Medium, etc.). This property sets the corresponding actual dimensions of the symbolic value Large.

Specifying the value of this property on KBytes ensures a uniform size of images, with possible loss of quality.  
The actual size of the transferred images may exceed by 10% the specified value.  
Use this property in case that connectivity to the server is costly in time and/or money.

Specifying the value in resolution ensures uniform dimensions for the images but sizes in KBytes can vary significantly between images.

### [Examples](#Examples)

|  |  |
| --- | --- |
| 640x640 | Every image that exceeds the specified resolution scales, maintaining the aspect ratio. |
| 50 | Every image that exceeds the size of 50kb scales, maintaining the aspect ratio. |


|  |
| --- |
| **Backlinks** |
| [Maximum Upload Size property](https://wiki.genexus.com/commwiki/wiki?44940) |

---
