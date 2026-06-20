---
title: "Full-Text Search in Applications"
source_id: 5278
source_url: https://wiki.genexus.com/commwiki/wiki?5278
genexus_version: "18"
---

# Full-Text Search in Applications

The purpose of this feature is to allow the end user to find specific information in different sources.

"Full-Text Search" gives you the ability to change the way end users navigate through the pages in your site.

There are two basic ways of navigating a website: one way is to go through the links (knowing the entire path of the place you want to reach); and the other is to make a full-text search in the whole site in order to go directly to the link that will bring you to the place you want.

So, you can automatically add search functions to your application with a full-text search engine. Having Full-Text Search in your application means that your end users will be able to search for non-structured data (Comment fields, Name fields, etc.). It's very useful when you need to look for information that cannot be matched exactly to a table field, like generic information which can be stored anywhere in the database or hard disk and you need to make a generic query based on what you can remember (for example: "loan\* or urgent and 199").

As all savvy Internet users know, in a full-text search the search engine examines all the words in every stored document as it tries to match search words supplied by the user.

For example, when the user only remembers something like "Missing accounting information", "won the prize", "InvoiceTotal:2500 or asked for loan", etc., searching the content of this Comments field cannot be easily programmed and that is when Full-Text Searching (FTS) comes to the rescue.

GeneXus automatically indexes transaction data as well as data from sources other than databases. For example, think of indexing files, html pages, MS word documents, text files, etc.

### [**So what's the scope of Full-Text Search?**](#So+what%27s+the+scope+of+Full-Text+Search%3F)

* It searches in all the fields in database tables (associated to Business Components transactions)
* It searches in hard disk files

### [**How can the user make the query?**](#How+can+the+user+make+the+query%3F)

* Searching by all the keywords entered, for example: loan AND debt (including blank spaces between words is equivalent to the AND operator)
* Searching by exact phrases like "repayment interest"
* Searching for at least one: creditor OR lend
* wildcards: credi\*
* fuzzy words: pay OR credit
* grouping words: (assets OR purchase) AND NOT finance
* searching by Title i.e: Customer Name Jhon
* and there are more options, depending on the search engine you use, see for example [here](https://lucene.apache.org/core/2_9_4/queryparsersyntax.html) (not all the options are available)

For more information: [HowTo: Configure Full Text Search in your application](https://wiki.genexus.com/commwiki/wiki?6468)

### [See also](#See+also)

[Full Text Search Data Types](https://wiki.genexus.com/commwiki/wiki?5292)  
[Full Text Search Examples](https://wiki.genexus.com/commwiki/wiki?6701)  
[Full Text Search Examples - Indexing](https://wiki.genexus.com/commwiki/wiki?6036)


|  |
| --- |
| **Pages** |
| [Full Text Search example 1](https://wiki.genexus.com/commwiki/wiki?6024) | [Full Text Search example 2](https://wiki.genexus.com/commwiki/wiki?6666) | [Full Text Search example 3](https://wiki.genexus.com/commwiki/wiki?6682) |
| [Full Text Search example 4](https://wiki.genexus.com/commwiki/wiki?6709) | [Full Text Search Examples](https://wiki.genexus.com/commwiki/wiki?6701) | [Full Text Search Examples - Indexing](https://wiki.genexus.com/commwiki/wiki?6036) |

---
