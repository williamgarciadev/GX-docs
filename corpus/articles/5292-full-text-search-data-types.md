---
title: "Full Text Search Data Types"
source_id: 5292
source_url: https://wiki.genexus.com/commwiki/wiki?5292
genexus_version: "18"
---

# Full Text Search Data Types

In this paper we explain in detail the GeneXus data types provided for making your database and files full text searchable.

### [1. TextSearch.Find Function](#1.+TextSearch.Find+Function)

```
TextSearch.Find(Character Content, (optional) Numeric ItemsPerPage, (optional) Numeric PageNumber): SearchResult
```

#### [SearchResult Data Type](#SearchResult+Data+Type)

|  |  |
| --- | --- |
| **MaxItems** | **Total number of items returned by the search** |
| **ElapsedTime** | **Time elapsed by the search** |
| **Items** | **SearchResultItem Collection** |

#### [**SearchResultItem Data Type Properties**](#SearchResultItem+Data+Type+Properties)

|  |  |
| --- | --- |
| Title:character | Content title |
| Viewer:character | Url used to display a retrieval result |
| Id: character | document Id used to retrieve the object from the original source |
| Score:numeric | Relevance for the item, given a query. It is greater than 0 and less than or equal to 1, it indicates how closely the document matched the query. Search results are ordered by their score by default. |
| TimeStamp:DateTime | TimeStamp of the last document indexing |
| Type:character | Type identifier (the same value assigned to ContentInfo Type, see below) |

Note: SearchResultItem can be passed as parameter of the load method of a Business Component. So, if the result of the search is of *Type* any BC Transaction (e.g Customer), you can program: &Customer.load(&SearchResultItem)  
  
[Full Text Search Examples](https://wiki.genexus.com/commwiki/wiki?6701)

### [2. Index Function](#2.+Index+Function)

As you can search data stored in your database, in files, or in memory, you can index all of them. Data stored in memory (variables), as well as the other types of data, will be indexed in index files in order to make it searchable.  
  
Indexes have an optimized structure to search keywords.  
  
**Data stored in the database:**  
  
It indexes all attributes in the transaction structure (a searchable transaction). It indexes also inferred attributes and formulas if they are in the transaction structure.  
  
Indexing operations are performed automatically when working with the transaction in an asynchronous way, so application performance is not affected. It means that you won't see the new data immediately updated in your searches.  
  
*When does the indexing take place?*  
  
1. When inserting/deleting/updating data from the Business Component transaction form.  
2. When inserting/deleting/updating data using the Business Components methods.  
  
In the other cases (procedure updates for example), you should index the data by using the functions provided for this purpose. Their syntax and use will be explained later in this document.  
  
**Data stored in files or in memory:**  
  
In the case of files, the supported extensions are .Net: txt, html, pdf; Java: txt, doc, html, pdf

### [Index Functions](#Index+Functions)

|  |  |
| --- | --- |
| TextSearch.Add( Variable (BC | File | string) [, ContentInfo info]):Boolean | Inserts content on the index, it saves duplicated entries if the content already exists. |
| TextSearch.Update(Variable (BC | File | string) [, ContentInfo info]):Boolean | Deletes the content of the index if it already exists, and then inserts the content. |
| TextSearch.Delete(Variable (BC | File | string)):Boolean | Deletes the content from the index.  TextSearch.Delete(String) : The String must be the Id by which the information was indexed; check the *ContentInfo* Id property used with the *Add* and *Update* operations.  TexSearch.Delete(BC) : It´s calculated the Id (Transaction name plus transaction keys ) and the index information associated to that Id is deleted.  TextSearch.Delete(File) : It´s calculated the Id (Full file name) and the index information associated to that Id is deleted. |
| TextSearch.Reindexall():Numeric | Indexes all the content of tables defined in GeneXus as Searchable Business Components. |

**ContentInfo Properties**

|  |  |  |  |
| --- | --- | --- | --- |
|  |  | **Default Value** | |
| **Property** | **Definition** | **Business Components** | **Files** |
| Id:character | Document key used to retrieve the object from the original source | Transaction name plus transaction keys | Full file name |
| Viewer:character | Url used to display a retrieval result | Viewer property associated with the transaction (if it is none, the transaction in display mode is used). | File path |
| Type:character | Type identifier | Transaction name | "GxFile" |
| Title:character | Content title | Description attribute of the transaction for the Business Component | File name |

See examples of Indexing [here](https://wiki.genexus.com/commwiki/wiki?6036)

### [Browse the Index](#Browse+the+Index)

**Note: How can I peek into the index?**  
There is a Lucene index browser at [Luke](http://www.getopt.org/luke/) which can be used to navigate the index.

### [Other Full Text Search Functions](#Other+Full+Text+Search+Functions)

There are two functions related to the spell checking of search queries. The first one, BuildDictionary() should be called after indexing some data. BuildDictionary creates a dictionary from the index dictionary that can be used to check the spelling of a query. The more content the index has when calling BuildDictionary(), the better the spell check with CheckSpell function will be.

|  |  |
| --- | --- |
| TextSearch.BuildDictionary(): Boolean | Build a dictionary to check spelling using the indexed content |
| TextSearch.CheckSpell(Character query):Character | Suggest alternate spelling for words in the query. The suggested words are restricted to the words present in the dictionary built with BuildDictionary() function. |
| TextSearch.HTMLPreview(Variable (BC | string | File), Character Query, (optional) Character TextType, (optional) Character PreTag, (optional) Character PostTag, (optional) Numeric FragmentSize, (optional) Numeric MaxNumFragments); | Breaks the text into the best fragments highlighting the words in the query.  |  |  |  |  | | --- | --- | --- | --- | |  | Meaning | Possible Values | Default Value | | TextType(1) | The text is HTML or Text format? | Text, HTML | HTML | | PreTag | Tag used to highlight the Query text. This is the left tag of the text. | Any HTML Tag | <B> | | PostTag | Tag used to highlight the Query text. This is the right tag of the text. | Any HTML Tag | </B> | | FragmentSize | size in bytes of each fragment |  |  | | MaxNumFragments | maximum number of fragments |  |  | |

##### [Note (1):](#Note+%281%29%3A)

In order to use HTMLPreview function in .NET generator, the msvcp71.dll has to be copied to Windows\system32 of the server.  
That dll belongs to MS Visual C++ 7.1 Runtime Library (distributed by .NET 2003).  
This is necessary only when the TextType (third parameter of HTMLPreview function) is "HTML". You could install it from [here](https://support.microsoft.com/en-nz/help/2977003/the-latest-supported-visual-c-downloads).

### [FAQ](#FAQ)

Q. What is indexed?  
A. It indexes all attributes in the transaction (a searchable transaction) structure. The text which is built and indexed has the following format: Attribute<1> Title + " " + Attribute<1> Value + .... + Attribute<n> Value.

Q. What happens with the index information for the Invoice Transaction, if I change the customer name in the Customer Transaction?  
A. You have to run the Reindex process in order to update the Invoice Transaction index information.

### [See Also](#See+Also)

[Full-Text Search](https://wiki.genexus.com/commwiki/wiki?5277)  
[Full Text Search Examples](https://wiki.genexus.com/commwiki/wiki?6701)  
[Full Text Search Examples - Indexing](https://wiki.genexus.com/commwiki/wiki?6036)


|  |
| --- |
| **Backlinks** |
| [External utilities used by GeneXus generated web applications](https://wiki.genexus.com/commwiki/wiki?15671) | [External utilities used by GeneXus generated web applications (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54956) | [External utilities used by GeneXus generated web applications (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55934) |
| [Full Text Search example 1](https://wiki.genexus.com/commwiki/wiki?6024) | [Full Text Search example 2](https://wiki.genexus.com/commwiki/wiki?6666) | [Full Text Search example 3](https://wiki.genexus.com/commwiki/wiki?6682) | [Full Text Search example 4](https://wiki.genexus.com/commwiki/wiki?6709) |
| [Full Text Search Examples - Indexing](https://wiki.genexus.com/commwiki/wiki?6036) | [Category:Full Text Search in Knowledge Base](https://wiki.genexus.com/commwiki/wiki?5726) | [Category:Full-Text Search in Applications](https://wiki.genexus.com/commwiki/wiki?5278) | [HowTo: Configure Full Text Search in your application](https://wiki.genexus.com/commwiki/wiki?6468) |

---
