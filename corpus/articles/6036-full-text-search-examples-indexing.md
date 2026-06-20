---
title: "Full Text Search Examples - Indexing"
source_id: 6036
source_url: https://wiki.genexus.com/commwiki/wiki?6036
genexus_version: "18"
---

# Full Text Search Examples - Indexing

In this page we gather some examples of the use of Indexing functions for full text search purposes:

#### 1. Index all data stored in the database, related to Business Components Transactions

```
Event ReindexAll
    &error = TextSearch.ReindexAll()
EndEvent
```

Reindex all transactions with Searchable property True. All the information related to Searchable Business Components is deleted from the index, and indexed again. Note that only that information is deleted, not the other data that could have been indexed (as files and strings).

#### 2. Index all files of a specified directory

In this example, all files of a directory are indexed.

When the documents are retrieved by the search, they will link to what is specified in the &contentinfo.viewer property.

```
Event IndexFiles
    &directory.Source = &source
    For &file in &directory.GetFiles("*.*")
        &ContentInfo.Viewer = &URL + &file.GetName()
        &booleanvar = TextSearch.Add(&file,&ContentInfo)
        If &booleanvar= TRUE
           msg( format("Indexing %1", &file.GetName()))
        else
           msg(format("Error indexing %1",&file.GetName()))
        EndIf
    EndFor
EndEvent
```

Data types:

* &directoy is a  Directory Data Type
* &file is variable is a File Data Type
* &contentinfo is a ContentInfo Data Type.

#### 3. Update Index Content

```
Event UpdateContentFile
    &directory.Source = &source
    For &file in &directory.GetFiles("*.*")
        &ContentInfo.Viewer = &URL + &file.GetName()
        &booleanvar = TextSearch.Update(&file,&ContentInfo)
        If &booleanvar = TRUE
           msg( format("Re-Indexing %1", &file.GetName()))
        else
           msg(format("Error re-indexing %1",&file.GetName()))
        EndIf
    EndFor
EndEvent
```

#### 4. Delete File from Index

Delete a file from the index.

Notes:

* &sourcefile is the path to the file which will be deleted from the index.
* &file is of File Data Type.

```
Event Delete File Index
    &file.Source = &sourcefile
    &booleanvar = TextSearch.Delete(&file)
    if &booleanvar= TRUE
       msg( format("Index Entry %1 was deleted", &file.GetName()))
    else
       msg(format("Error deleting index entry %1",&file.GetName()))
    endif 
EndEvent
```

```
Event IndexString
      &ContentInfo.Id = &AccountingEntry.Id.ToString()
      &ContentInfo.Title = 'Accounting Entry # ' + &AccountingEntry.Id.ToString()
      &ContentInfo.Type = 'Accounting Entry'
      &ContentInfo.Viewer = AccountingEntrydata.Link(&AccountingEntry.Id,'DSP') //call the transaction in display mode
      &AccountingDetail = &AccountingEntry.ToXml() //convert all the accounting entry to a XML string
      &booleanvar = TextSearch.Add(&AccountingDetail,&ContentInfo)
      if &booleanvar= TRUE
         msg( format("Indexing %1", &ContentInfo.Id))
      else
          msg(format("Error indexing %1",&ContentInfo.Id))
     endif
EndEvent
```

In order to delete the entry from the index:

```
Event 'Delete Index'
    &AccountingEntryAux = &AccountingEntryDataId.ToString()
    &booleanvar = TextSearch.Delete(&AccountingEntryAux)
    if &booleanvar= TRUE
        msg( format("Deleting Index Content %1", &AccountingEntry.Id.ToString()))
    else
        msg(format("Error deleting index content %1",&AccountingEntryDataId.ToString()))
    endif
EndEvent
```

See also: [Full Text Search in Applications](https://wiki.genexus.com/commwiki/wiki?5278), [Full Text Search Examples](https://wiki.genexus.com/commwiki/wiki?6024), [Full Text Search Data Types](https://wiki.genexus.com/commwiki/wiki?5292).

#### 5. Index a string (value from memory)

Sometimes you may want to be able to search for information which isn't stored in a database or in a file, but that is the result or output of a process which gathers information from different sources.

For example, consider an accounting entry which is represented in GeneXus as a SDT, and you want to make the information of all the accounting entries searchable.

After the accounting entry is calculated, you would store the necessary information in a ContentInfo variable, and then, call the TextSearch.Add or TextSearch.Update function.

```
Event 'IndexString'
      &ContentInfo.Id = &AccountingEntry.Id.ToString()
      &ContentInfo.Title = format('Accounting Entry # %1', &AccountingEntry.Id)
      &ContentInfo.Type = 'Accounting Entry'
      &ContentInfo.Viewer = AccountingEntrydata.Link(&AccountingEntry.Id,'DSP') //call the transaction in display mode
      &AccountingDetail = &AccountingEntry.ToXml() //convert all the accounting entry to a XML string
      &booleanvar = TextSearch.Add(&AccountingDetail,&ContentInfo)
      if &booleanvar= TRUE
         msg( format("%1 was indexed", &ContentInfo.Id))
      else
         msg(format("Error indexing %1",&ContentInfo.Id))
      endif
EndEvent
```

### See also

[Full Text Search Data Types](https://wiki.genexus.com/commwiki/wiki?5292)  
[Full Text Search Examples](https://wiki.genexus.com/commwiki/wiki?6701)


|  |
| --- |
| **Backlinks** |
| [Full Text Search Data Types](https://wiki.genexus.com/commwiki/wiki?5292) | [Full Text Search example 1](https://wiki.genexus.com/commwiki/wiki?6024) | [Full Text Search example 2](https://wiki.genexus.com/commwiki/wiki?6666) |
| [Full Text Search example 3](https://wiki.genexus.com/commwiki/wiki?6682) | [Full Text Search example 4](https://wiki.genexus.com/commwiki/wiki?6709) | [Full Text Search Examples](https://wiki.genexus.com/commwiki/wiki?6701) | [Category:Full-Text Search in Applications](https://wiki.genexus.com/commwiki/wiki?5278) |
| [HowTo: Configure Full Text Search in your application](https://wiki.genexus.com/commwiki/wiki?6468) | [Searchable property](https://wiki.genexus.com/commwiki/wiki?9018) |

---
