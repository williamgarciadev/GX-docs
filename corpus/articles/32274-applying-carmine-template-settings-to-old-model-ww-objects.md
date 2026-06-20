---
title: "Applying Carmine Template settings to old-model WW objects"
source_id: 32274
source_url: https://wiki.genexus.com/commwiki/wiki?32274
genexus_version: "18"
---

# Applying Carmine Template settings to old-model WW objects

The Carmine Theme determines a design template for the [Work with for Web Pattern](https://wiki.genexus.com/commwiki/wiki?25475) objects since [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?28265,,) .

In particular, note in the image below the *Insert* form action, and the *Update* and *Delete* grid actions, which are represented as labels.

`[imagen omitida: wiki id 32277]`

For KBs which are converted from GeneXus X Evolution 3 (which use the Flat Theme) and are converted for using Carmine, the template used for the WW objects has some aspects which are inherited from the old (Flat) template.

This behavior is due to compatibility reasons.

The Insert action form is displayed like a button, and the Update and Delete grid actions are represented as images, as shown in the figure below:

`[imagen omitida: wiki id 32278]`

If you want to change this behavior, you have to edit the pattern settings...

`[imagen omitida: wiki id 32279]`

And make the following changes:

1. For the Update and Delete Standard Actions, remove the Image and Disabled Image, and change the value of the "In Grid Class" to "TextActionAttribute".

`[imagen omitida: wiki id 32275]`

So after the changes it will be as follows:

`[imagen omitida: wiki id 32280]`

2. For the Insert Standard Action, change the Button Class to "BtnAdd" value.

`[imagen omitida: wiki id 32276]`


|  |
| --- |
| **Backlinks** |
| [Work With for Web pattern](https://wiki.genexus.com/commwiki/wiki?25475) |

---
