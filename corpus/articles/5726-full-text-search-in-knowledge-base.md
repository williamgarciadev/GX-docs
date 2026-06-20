---
title: "Full Text Search in Knowledge Base"
source_id: 5726
source_url: https://wiki.genexus.com/commwiki/wiki?5726
genexus_version: "18"
---

# Full Text Search in Knowledge Base

GeneXus provides a powerful search engine that allows you to quickly find anything in your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?2428). You can search for any given text or even for specific property values (anything having property X with value Y).

Based on complex algorithms, GeneXus' full-text search engine finds what you are looking for among what could be tons and tons of words contained in all objects making up the KB. Like most search engines, it allows you to use intuitive syntax to limit your searches.

All search starts by the Search window.

### [How to display the Search window](#How+to+display+the+Search+window)

You can display the Search window by:

* Option View \ Tool Windows \ Search
* Typing any word or phrase in the Search Text Box in the menubar

Look at the following images:

#### [Option View \ Tool Windows \ Search](#Option+View+%5C+Tool+Windows+%5C+Search)

`[imagen omitida: wiki id 5913]`

#### [Search Text Box in the menubar](#Search+Text+Box+in+the+menubar)

`[imagen omitida: wiki id 5914]`

As a result, in both cases, you will see the Search window:

`[imagen omitida: wiki id 5915]`

**Note:** When the indexer is working (creating the index) or when objects are outdated in the index (for example when the indexer is stopped and objects have been updated since the last index created), a warning image

(`[imagen omitida: wiki id 22928]`) will be displayed.

#### [Example 1](#Example+1)

The following image shows how a "To-Do Mary" search can be done.

`[imagen omitida: wiki id 5300]`

You can also query by specific property values by writing the query in the "Properties" text block which is inside the Search window Advanced area. You need to write a condition like "Object Type=Transaction".

**Note:** The only searchable properties are those whose values have been predefined (they are usually presented in a combo box in the properties windows). For example, the Theme Dependant property can be searched but the Name property cannot be searched.

#### [Example 2](#Example+2)

Search for Transaction objects. Steps:

* Display the Search window.
* Specify the search criteria (select a property in the Advanced area).

Look at the following images:

`[imagen omitida: wiki id 5921]`          `[imagen omitida: wiki id 5922]`

A query can be saved as a [Category](https://wiki.genexus.com/commwiki/wiki?5287,,) by clicking on Save as Category button. This allows you to see the results of predefined queries on the [Category View](https://wiki.genexus.com/commwiki/wiki?5287,,).

### [Additional Technical Information](#Additional+Technical+Information)

- This feature is implemented using Lucene indexer (also used in [gxsearch](https://wiki.genexus.com/commwiki/wiki?4778,,)).

- The indexing process runs in the background while GeneXus is active. If you see that Genexus.exe uses some CPU even when you're not doing anything, this process may be indexing the Knowledge Base.  
While importing or exporting or during a Build process, indexing is disabled and restarted when import or build has ended.

- The indexing process assigns different weight to the indexed words (depending on whether they appear in rules, properties, if the complete word is found, distance of words).

- Not all Lucene wildcards are supported. These are the supported ones:

* **fuzzy search:** search "geneus" and it finds "genexus" "genero", etc.
* **inclusion/exclusion:** search "msg -event" and it finds the **parts** where "msg" exists and where no "event" appears

- It is not supported to use leading wildcard characters. For example, you cannot search for \*objectname\*

- Control characters like "(" are not taken into account by the indexer (i.e. "parm(" will return no results)

- Underscore ("\_") is a word separator for Lucene, this should be considered especially when doing exact searches on the knowledge base.

Example:

there are two procedures A and B

procedure A, have the following comment:

```
/ / Comment
```

and  B:

```
/ / Comment_ario
```

Then if we search for the word "comment" in the KB, the results of this search are both procedures. For lucene there are two words in procedure B, comment and ario because underscore is used as a word separator.

### [Troubleshooting](#Troubleshooting)

To see if the indexing process is the one consuming your CPU, go to the <KB directory>\FTindex. Files in this directory should increase in size every 20 or 30 seconds in that case.

### [See also](#See+also)

[Full Text Search Data Types](https://wiki.genexus.com/commwiki/wiki?5292), [Full-Text Search in Applications](https://wiki.genexus.com/commwiki/wiki?5278)


|  |
| --- |
| **Pages** |
| [Indexer Monitor](https://wiki.genexus.com/commwiki/wiki?5461) |

---
