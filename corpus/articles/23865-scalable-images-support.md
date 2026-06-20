---
title: "Scalable Images Support"
source_id: 23865
source_url: https://wiki.genexus.com/commwiki/wiki?23865
genexus_version: "18"
---

# Scalable Images Support

Scalable images adapts its size to the content. This allows us to use only one image for many different sizes. The most common case of use is the one of an image used as a background for a rounded button.

The [Scalable Image Property](https://wiki.genexus.com/commwiki/wiki?23862,,) indicates if an image is or not scalable.

If the image is scalable, two extra properties groups will be shown for the image object: Scalable area and Fill area.

`[imagen omitida: wiki id 23867]`

The Scalable area is used to indicate the areas of the image that can be scaled to fill the required size. This area is indicated in the following properties:

* Image Scale area - Top
* Image Scale area - Left
* Image Scale area - Bottom
* Image Scale area - Right

These properties represent the distance between each border of the image and the center of it that should not be scaled. Their values are expressed on pixels and must be larger than 0.

`[imagen omitida: wiki id 23872]`

The Fill area is used to indicate the rectangle where the content (text, images, etc.). This area is indicated in the following properties:

* Image Fill area - Top

Its default value is taken from Image Scale area - Top

* Image Fill area - Left

Its default value is taken from Image Scale area - Left

* Image Fill area - Bottom

Its default value is taken from Image Scale area - Bottom

* Image Fill area - Right

Its default value is taken from Scale area - Right

These properties represent the distance between each border of the image and the center of it that should not be scaled. Their values are expressed on pixels and must be larger than 0.

**Note**: .9 Patch images with more than one scalable area are not supported.


|  |
| --- |
| **Backlinks** |
| [Fill Area property](https://wiki.genexus.com/commwiki/wiki?37308) | [Category:Image object](https://wiki.genexus.com/commwiki/wiki?23387) | [Scalable Area property](https://wiki.genexus.com/commwiki/wiki?37307) |

---
