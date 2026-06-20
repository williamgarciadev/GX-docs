---
title: "Applying Patterns"
source_id: 6551
source_url: https://wiki.genexus.com/commwiki/wiki?6551
genexus_version: "18"
---

# Applying Patterns

To apply [Patterns](https://wiki.genexus.com/commwiki/wiki?2814) in GeneXus, follow these steps:

* Open the [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) to which you want to apply the pattern
* In the Patterns selector, choose the pattern you want to apply. At this point, you can see the Transaction's default instance
* Customize the instance by making the modifications you need or configuring the necessary properties
* Check the option "Apply this pattern on save"
* Save the Transaction

`[imagen omitida: wiki id 6544]`

Messages are shown in the **Output Window**. If an error occurs, it is also shown in this window.

It is also possible to select a Transaction or a group of Transactions to apply the pattern. You can make multiple selections of Transactions by pressing the Ctrl or Shift key and the mouse button.

There are two ways to apply the pattern to a group of Transactions at the same time:

* Select all the Transactions in the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210), right-click on them, select the "Apply pattern" option and select the pattern.
* Go to **Work With Object** panel (View menu option), filter all the Transaction you want to apply the pattern (filtering by name or by type), select all the Transactions by pressing the Ctrl or Shift key and the mouse button and select the "Apply pattern" option and select the pattern

General configurations for all instances can be made in [Pattern settings](https://wiki.genexus.com/commwiki/wiki?6546).

### [Generated Objects and Pattern Instance](#Generated+Objects+and+Pattern+Instance)

When you apply the pattern, you can see that all objects are generated associated with the Transaction. The root of this object is the associated instance for the Transaction (in the example, WorkWithClient), and you also have all the associated objects for the selected Transaction (Work With, View, Export to Excel procedure, etc.) as children of the Transaction's instance.

`[imagen omitida: wiki id 6545]`

### [Refreshing Instances](#Refreshing+Instances)

When you make changes to your GeneXus objects in pattern instance or pattern settings and build the application, in the output window you can see the message below:

`[imagen omitida: wiki id 6552]`

The decision to refresh instances is taken if any of the following situations occur:

* It is the first build
* The instance has been modified from the last time it was opened
* Settings have been modified from the last time they were opened
* The definition files of the pattern or the templates have been modified from the last time they were opened

### [The instance is Up to Date](#The+instance+is+Up+to+Date)

When you build the application and none of the instances or GeneXus objects have been modified, the following message is displayed in the output window:

`[imagen omitida: wiki id 6553]`

### [Dynamic Pattern Update Property](#Dynamic+Pattern+Update+Property)

If you don't want the instances to be refreshed or updated ever and ever this property will help you and speed up your work [Dynamic Pattern Update Property](https://wiki.genexus.com/commwiki/wiki?11605).

**Note**: As from GeneXus X Evolution 2 version, when applying pattern besides the date in which pattern was applied for the last time, the version of the pattern is stored. More information at [SAC 30506](http://www2.gxtechnical.com/portal/hgxppredirect.aspx?15,26,0,,,30506).

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Using Patterns](https://training.genexus.com/en/learning/courses/genexus/genexus-16-course-analyst/using-patterns-v16?p=5352)


|  |
| --- |
| **Backlinks** |
| [Category:Patterns](https://wiki.genexus.com/commwiki/wiki?2814) |

---
