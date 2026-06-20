---
title: "Full Text Search example 1"
source_id: 6024
source_url: https://wiki.genexus.com/commwiki/wiki?6024
genexus_version: "18"
---

# Full Text Search example 1

This is a very simple example.

Suppose that in a university application you want to give the end user the possibility of searching for students using different wildcards in the search query.

`[imagen omitida: wiki id 5976]`

In this example, the "Students" [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) is a[Business Component](https://wiki.genexus.com/commwiki/wiki?5846), and its searchable property is set to TRUE. We have a "Search" web panel which displays a grid ("Students") that loads all the results returned by the search. Define the following variables in the "Search" [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916):

* &SearchResult of SearchResult DataType
* &SearchResultItem of SearchResultItem DataType

So the load event for the "Students" [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) will be the following:

```
Event Students.Load
    &SearchResult = TextSearch.Find(&filter)
    For &SearchResultItem in &SearchResult.Items()
        &title = &SearchResultItem.Title
        &title.Link = &SearchResultItem.Viewer
        Students.Load()
    Endfor
EndEvent
```

By selecting one of the items in the list of results returned by the search engine, you are linked to the object specified in the "Search Viewer" property of the Student Transaction.

`[imagen omitida: wiki id 6676]`  
  
If no value is specified in this property, the default values for the "Viewer" property of SearchResultItem data type are in this order:

1. The View of the Work With Pattern associated to this Transaction (if it has [Work With Patterns](https://wiki.genexus.com/commwiki/wiki?5636) applied).
2. The  Transaction called in Display mode.

The [Title property](https://wiki.genexus.com/commwiki/wiki?7234) of SearchResultItem data type is the description attribute of the Transaction (the name of the student in this case).

`[imagen omitida: wiki id 6677]`

### [See also](#See+also)

[Full-Text Search in Applications](https://wiki.genexus.com/commwiki/wiki?5278)  
[Full Text Search Examples - Indexing](https://wiki.genexus.com/commwiki/wiki?6036)  
[Full Text Search Data Types](https://wiki.genexus.com/commwiki/wiki?5292)


|  |
| --- |
| **Backlinks** |
| [Full Text Search Examples](https://wiki.genexus.com/commwiki/wiki?6701) | [Full Text Search Examples - Indexing](https://wiki.genexus.com/commwiki/wiki?6036) | [HowTo: Configure Full Text Search in your application](https://wiki.genexus.com/commwiki/wiki?6468) |

---
