---
title: "Blame in GeneXus Server"
source_id: 31190
source_url: https://wiki.genexus.com/commwiki/wiki?31190
genexus_version: "18"
---

# Blame in GeneXus Server

Blame it's a Team Development option which allows knowing when any aspect of an object was modified and who made those modifications by adding information about the author who committed a line, the revision the line was last changed and the date.

This option increases the control of all the objects of a Knowledge Base by unifying the objects content with the data related to each modification of that object showing in which [Commit](https://wiki.genexus.com/commwiki/wiki?10626) the changes were committed to GeneXus Server. The option can be applied to the current or another object version present on GeneXus Server.

The option attempts to solve those problems like wondering when, why or who had modified a part of an object when working in Teams and it shows since in which [Commit](https://wiki.genexus.com/commwiki/wiki?10626) each line or a Procedure was modified to when a tree node transaction structure changed.

It can be accessed from the [GeneXus IDE](https://wiki.genexus.com/commwiki/wiki?5272) at the Team Development History Tab

`[imagen omitida: wiki id 31215]`

Or from the Folder View by right-clicking the object and selecting the Team Development option

`[imagen omitida: wiki id 31222]`

### [Availability](#Availability)

The option can be applied to every local Knowledge Base object **but only if the object is Inserted.**

`[imagen omitida: wiki id 31214]`

### [Usage example](#Usage+example)

Let´s imagine a TravelAgency reality and two developers working together.

The first developer defines a new procedure which changes the name of a given Attraction:

`[imagen omitida: wiki id 31218]`

After the first developer commits the procedure to GeneXus Server and using the Blame option on that procedure, a Blame Tab will open, and the following information will be shown:

`[imagen omitida: wiki id 31219]`

Then, the second developer makes a change in the same procedure and Commit it to GeneXus Server:

`[imagen omitida: wiki id 31217]`

Using the Blame option on that procedure again, a Blame Tab will open, and the following image will be displayed showing which developer had modified each part of the procedure:

`[imagen omitida: wiki id 31220]`

### [Customization](#Customization)

The colors used by the Blame option can be configured using the Options dialog (Tools->Options) under the Team Development node (Team Development->Blame).

`[imagen omitida: wiki id 35737]`
