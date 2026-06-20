---
title: "Full Text Search example 3"
source_id: 6682
source_url: https://wiki.genexus.com/commwiki/wiki?6682
genexus_version: "18"
---

# Full Text Search example 3

To our last example, [Full Text Search example 2](https://wiki.genexus.com/commwiki/wiki?6666), let's add the possibility of working with a dictionary in order to refine the search query.

If the user query is not available in the index, another word or expression will be suggested to the user in order to make the query. The function used for that purpose will be TextSearch.CheckSpell. The suggested word is looked up in the dictionary; that is, for each word in the search query, CheckSpell returns the most similar one found in the dictionary.

The dictionary can be built up from the index, using the function TextSearch.BuildDictionary:

```
Event 'ReindexAll'
    &er = TextSearch.ReindexAll()
    &BooleanVar = TextSearch.BuildDictionary()
EndEvent
```

So, the code in the "Search" [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) will be like the one below. Remember that:

* &SearchResult is of SearchResult DataType
* &SearchResultItem is of SearchResultItem DataType

```
&SearchResult = TextSearch.Find(&searchpattern,&items,&pagenumber)
&maxItems     = &SearchResult.MaxItems 
&elapsedTime  = &SearchResult.ElapsedTime
if &maxItems = 0 //There are no results
   &suggestword = TextSearch.CheckSpell(&searchpattern)
   if  &suggestword = ' '
       &tpage = 0
       msg(format("Your search - <b>%1</b> - did not match any documents.", &searchpattern))
   else
       msg('Did you mean .. ' + &suggestword + ' ?')
       &searchpattern = &suggestword
   endif
endif
```

### Note

If you have a dictionary (which you can download in HTML format), you can index it and call BuildDictionary afterwards.

### See also

[Full-Text Search in Applications](https://wiki.genexus.com/commwiki/wiki?5278)  
[Full Text Search Examples - Indexing](https://wiki.genexus.com/commwiki/wiki?6036)  
[Full Text Search Data Types](https://wiki.genexus.com/commwiki/wiki?5292)


|  |
| --- |
| **Backlinks** |
| [Full Text Search Examples](https://wiki.genexus.com/commwiki/wiki?6701) |

---
