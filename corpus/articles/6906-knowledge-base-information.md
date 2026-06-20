---
title: "Knowledge Base Information"
source_id: 6906
source_url: https://wiki.genexus.com/commwiki/wiki?6906
genexus_version: "18"
---

# Knowledge Base Information

Sometimes we may want to have an idea of what kind of objects are in our Knowledge Bases and how they are proportionally used. In other words, we may want statistics.

You can access this feature through the "View/Knowledge Base Information" command menu.

`[imagen omitida: wiki id 6907]`

In the top section of the window you have the folder location, the connection string to the DBMS, the current environment folder, and the current user.

The link under **Folder Location**, for example, allows you to explore the Knowledge Base directory. When this option is selected, a Windows Explorer window is opened in the directory corresponding to the model. The link under **Current Environment** has a similar use.

In the box on the left, labeled "Information", you will find a list of object-related information. When you position yourself on each type of information on the list, the corresponding content will be shown in the area to the right.

* **GeneXus Objects By Type.** With the help of a pie chart, you can view the proportion of use of every object in the KB (objects in the Model). The number of objects per type is shown on the far right.
* **Database Schema.** You can see the number of attributes, tables, and indexes in the model.
* **Not Referenced Objects.** This list contains all the objects that have not been referenced by other objects.
* **Last Referenced Objects.** This list contains all the objects that are referenced last.
* **Most Referenced Objects.** This list contains the objects with the highest number of references by other objects.

Note: The Refresh Information button restarts the statistics feature. When you press it, the focus will return to the first information shown (GeneXus Objects By Type).
