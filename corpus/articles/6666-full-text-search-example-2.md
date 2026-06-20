---
title: "Full Text Search example 2"
source_id: 6666
source_url: https://wiki.genexus.com/commwiki/wiki?6666
genexus_version: "18"
---

# Full Text Search example 2

In this example we will introduce paging in the results of the query, and a way to show a preview of the search results highlighting the specific words in the search query.

### [How to do it...](#How+to+do+it...)

Consider a [BC](https://wiki.genexus.com/commwiki/wiki?2416) transaction named "Customer" in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836), which is searchable  (its [Searchable property](https://wiki.genexus.com/commwiki/wiki?9018) is set to TRUE).

In addition, we have another type of information which will be searchable, as "Accounting Entries" are stored in the database or files.

In order to program the "search" [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916), define the following variables:

* &SearchResult is of SearchResult Datatype
* &SearchResultItem is of SearchResultItem DataType
* &Title, &Type, &Score, &TimeStamp are character variables used to load the results of the search.

The form at design time is as follows:

`[imagen omitida: wiki id 6669]`

This is the code that implements the search:

```
Sub 'Paging' 
    &SearchResult =  TextSearch.Find(&searchpattern,&items,&pageNumber)            
    for &SearchResultItem  in &SearchResult.Items()
        &title = &searchResultItem.Title
        &title.Link = &searchResultItem.Viewer
        &type = &searchResultItem.Type
        &score = &SearchResultItem.Score
        &TimeStamp = &SearchResultItem.TimeStamp
        if &type = 'Customer'
           &customer.Load(&SearchResultItem)
           &preview = TextSearch.HTMLPreview(&customer,&searchpattern,'HTML','<span STYLE="background: yellow"> ','</span>',200,1)
        endif
        grid1.Load()
    endfor 
EndSub
```

Note that based on the &Type (&searchResultItem.Type) value, we call the TextSearch.HTMLPreview function.  
  
This is the runtime image of the sample:

`[imagen omitida: wiki id 6667]`

### [Note](#Note)

Take into account that the text which is built and indexed has the following format: Attribute<1> Title + " " + Attribute<1> Value + .... Attribute<n> Title + " "+ Attribute<n> Value.

As a consequence, in our example "Customer Name" and "Customer Address" will be present in the index followed by the corresponding values, as they are the "Titles" of CustomerName, CustomerAddress attributes, etc.

`[imagen omitida: wiki id 6672]`

In addition, at runtime the user will see the "Contextual Title" as labels of each attribute.

`[imagen omitida: wiki id 6673]`

So, if the user wants to find customers named Sarah, the search query could be "Customer name Sarah". That's because Customer is the name of the transaction, and "Name" is the contextual title the user is interested in searching for.

`[imagen omitida: wiki id 6674]`

You can download the sample from [here](http://www.gxopen.com/gxopen/servlet/projectversioninformation?707,3).

### [See also](#See+also)

[Full-Text Search in Applications](https://wiki.genexus.com/commwiki/wiki?5278)  
[Full Text Search Examples - Indexing](https://wiki.genexus.com/commwiki/wiki?6036)  
[Full Text Search Data Types](https://wiki.genexus.com/commwiki/wiki?5292)


|  |
| --- |
| **Backlinks** |
| [Full Text Search example 3](https://wiki.genexus.com/commwiki/wiki?6682) | [Full Text Search Examples](https://wiki.genexus.com/commwiki/wiki?6701) |

---
