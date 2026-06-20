---
title: "Like operator"
source_id: 9991
source_url: https://wiki.genexus.com/commwiki/wiki?9991
genexus_version: "18"
---

# Like operator

This operator allows the user to select data according to a matching text string.

### [Syntax](#Syntax)

*CExp1* **LIKE** *CExp2* [**when** *constraint*]

#### [Where:](#Where%3A)

*CExp1, CExp2*  
   Can be attributes, variables, or character strings between quotes.

[When](https://wiki.genexus.com/commwiki/wiki?8629)  
   Specifies when the where clause will apply.

Working with iSeries Environment: CExp2 will work just as the iSeries Search Pattern; also, it makes use of the '\*' and ‘\_’ wildcard characters. '\*' indicates that 0 or n characters can exist in the position where this character is placed, and '\_' indicates that one character can exist in the position where this character is placed. After searching in CExp1, it returns all instances that contain CExp2.

Working with Client/Server Environment: Programs generated for this environments implement the LIKE operator differently than how the other generators implement it:

* This change gives rise to a more potential search criteria since it makes use of statistics and as a consequence, it uses indices created by the system; its performance is much better than the comparison involving '>='.
* It is also possible to search for Wildcard characters (% and \_) apart from searching for sequential characters located in any position of a string (floating). It is possible to search for those which "start with ...", "have a letter in a certain position of the string", etc. It is not possible to search for "those which end with ....".
* Allows DBMSs to perform optimizations when searching.
* Compatible with SQL. All users who are familiar with this language will not require training. This implementation is similar to how the SQL's LIKE operator works. There are two characters that act as wildcards:
* '%' (percent sign). Used to indicate that the position where the symbol is placed can contain 0 or n numbers of any type of character.
* '\_' (underscore sign). Used to indicate that the position where the symbol is placed can contain 1 character of any type. Note: This operator is case sensitive.

### [Example](#Example)

Let us assume we have a system that handles information about clients. In the fixed-part of a Web Panel, we have included a &Search variable, where the user can enter a string. The scrolling part of the panel will contain a name that is "like" the character string mentioned. In other words, in the [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) we want to include only lines whose descriptions match or contain a given string.

The solution is very simple: We must include a line in the Web Panel Conditions (ClientName LIKE &Search), defining the corresponding Grid attribute that is to be "like" the variable used in the fixed-part of the panel.

In iSeries, these would be the results according to the entered search string:

|  |  |
| --- | --- |
| **Search string** | **Result** |
| JOHN | All names starting with the ‘JOHN’ string. |
| \*SMITH | All names containing the ‘SMITH’ string at any place within the name. |
| JOHN\*SMITH | All names starting with the ‘JOHN’ string followed by the ‘SMITH’ string, 0 or more characters may exist between the two strings. |
| ANDERS\_N | All names containing the ‘ANDERS’ string followed by another character and then an ‘N’. Useful to search for ANDERSON and ANDERSEN. |

In SQL environment:

|  |  |
| --- | --- |
| **Search string** | **Result** |
| JOHN | All names that start with the following character sequence, 'JOHN', are valid. |
| %SMITH | All names that contain ‘SMITH’ anywhere within the string are considered. |
| JOHN%SMITH | All names that start with 'JOHN' and are followed by 'SMITH' are considered. Zero or more characters can lie between these two sequences. |

### [Scope](#Scope)

**Objects**[Procedure object](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916), [Work Panel object](https://wiki.genexus.com/commwiki/wiki?7387,,)


|  |
| --- |
| **Backlinks** |
| [HowTo: In-app search in Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?31862) | [Category:Operators](https://wiki.genexus.com/commwiki/wiki?6882) | [When clause](https://wiki.genexus.com/commwiki/wiki?8629) |

---
