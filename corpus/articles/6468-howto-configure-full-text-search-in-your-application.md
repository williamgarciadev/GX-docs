---
title: "HowTo: Configure Full Text Search in your application"
source_id: 6468
source_url: https://wiki.genexus.com/commwiki/wiki?6468
genexus_version: "18"
---

# HowTo: Configure Full Text Search in your application

The purpose of this article is to explain the necessary steps to configure Full Text Search in your final application.

You have several properties to help you with this configuration:

### [Generator properties](#Generator+properties)

At generator level, you have these properties you can configure to get Full Text Search in your application.

#### [Searchable Property](#Searchable+Property)

If the [Searchable property](https://wiki.genexus.com/commwiki/wiki?9018) is set to TRUE, all the [Business Component](https://wiki.genexus.com/commwiki/wiki?5846) of the [KB](https://wiki.genexus.com/commwiki/wiki?2428) are made searchable. You can change this locally for certain Business Components (see Transaction defined as Business Component section below).

#### [Search Engine Property](#Search+Engine+Property)

It specifies the search Engine to be used. This property is only displayed if the Searchable property is set to True.

#### [Index Directory Property](#Index+Directory+Property)

It specifies the directory where the index files will be stored only if the Searchable property is set to True.

### [Transaction defined as Business Component](#Transaction+defined+as+Business+Component)

They are several properties available in a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) that was defined as a [Business Component](https://wiki.genexus.com/commwiki/wiki?5846) to configure Full Text Search.

#### [Searchable Property](#Searchable+Property)

If it is set to True, it means that this Transaction will be searchable.

#### [Search Viewer Property](#Search+Viewer+Property)

Sets a GeneXus object, which has to receive the key of the Transaction as a parameter. This property is only offered if the Searchable Transaction Property is set to True. See more information at: [Search viewer property](https://wiki.genexus.com/commwiki/wiki?36676).

**Note**: In order to use Full Text Search functions for files, you don't need to set any property, just use the functions explained in the See Also section.

### [See Also](#See+Also)

[Full Text Search Data Types](https://wiki.genexus.com/commwiki/wiki?5292)  
[Full Text Search Examples](https://wiki.genexus.com/commwiki/wiki?6024)  
[Full Text Search Examples - Indexing](https://wiki.genexus.com/commwiki/wiki?6036)


|  |
| --- |
| **Backlinks** |
| [Category:Full-Text Search in Applications](https://wiki.genexus.com/commwiki/wiki?5278) | [Searchable property](https://wiki.genexus.com/commwiki/wiki?9018) |

---
