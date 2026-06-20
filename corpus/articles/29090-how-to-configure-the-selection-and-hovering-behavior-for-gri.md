---
title: "How to configure the Selection and Hovering behavior for Grids in the Abstract Layout"
source_id: 29090
source_url: https://wiki.genexus.com/commwiki/wiki?29090
genexus_version: "18"
---

# How to configure the Selection and Hovering behavior for Grids in the Abstract Layout

In [Responsive Web Design (RWD)](https://wiki.genexus.com/commwiki/wiki?25161) the control properties are configured in general through Theme Classes.

In particular, if the [Allow Selection property](https://wiki.genexus.com/commwiki/wiki?8680) is configured for the grid, the selection color of the grid rows has to be configured as follows:

1. Configure the [Allow Selection property](https://wiki.genexus.com/commwiki/wiki?8680) of the grid.

`[imagen omitida: wiki id 29091]`

2. Check which is the Theme associated with the object, and the class associated with the grid.

`[imagen omitida: wiki id 29093]`

3. Edit the Theme, and configure the *Selected Row Class* property of the class associated with the grid (in the example, the "Grid" class).

`[imagen omitida: wiki id 29094]`

The Selected Row Class property has to be configured with the name of a class descendant of the GridRow class.

For the GridRow (or any of its descendants), configure the BackColor property, to set the grid row selection color.

`[imagen omitida: wiki id 29096]`

### [Notes](#Notes)

1. To configure the selection color at runtime, simply associate the grid with a class using the desired settings.
2. The criteria explained in this document applies to the Hovering color for grids, when AllowHovering property is set to TRUE using the [Abstract Layout](https://wiki.genexus.com/commwiki/wiki?25209). The *Hover Row Class* is a property of the Grid Class (and its descendants), to specify the class that will define the hovering settings of the grid rows.

### [Availability](#Availability)

As from [GeneXus X Evolution 3 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?28251,,).
