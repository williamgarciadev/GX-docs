---
title: "Selection List"
source_id: 23894
source_url: https://wiki.genexus.com/commwiki/wiki?23894
genexus_version: "18"
---

# Selection List

A **Selection List** (or [Prompt](https://wiki.genexus.com/commwiki/wiki?21635)) is a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) or [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) automatically created for each Transaction's primary key and foreign keys to provide end users with the possibility of querying the data existent in a specific database table and selecting certain record, returning its identifier.

For instance, suppose that an end user executes Company [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) to edit through its Layout a specific company. However, the end user does not remember the Company identifier. So, he/she will be able to select the Company through a Panel that shows all stored companies. Besides, if upon entering the company’s country (CountryId attribute, foreign key) the end user doesn't remember the possible countries, he/she will be able to activate another selection list that will allow querying all the countries stores in the COUNTRY table and selecting one.

## [Web applications](#Web+applications)

When generating for Web environment, for each *primary key* and *foreign key* present in a Transaction, a Selection List will be generated.

`[imagen omitida: wiki id 52970]`

In the Transaction Layout, to select a company´s country in runtime, the end user can click on the image to the right of the *CountryId* attribute.

`[imagen omitida: wiki id 52975]`

## [Native Mobile and Angular applications](#Native+Mobile+and+Angular+applications)

When generating for Native Mobile and Angular, selection lists will be created exclusively for the *foreign keys* present in the *Section (General)* of the corresponding Work With (since the location to interactively enter/modify the table’s information is not the Transaction but rather the Section(General) of WorkWith<Transaction>).

For example, to select a company's country, open the company detail in edit mode and select the prompt icon on the *CountryId* attribute.

`[imagen omitida: wiki id 56435]`

## [See also](#See+also)

* [When are selection lists created?](https://wiki.genexus.com/commwiki/wiki?23899)
* [Is it possible to modify Selection Lists?](https://wiki.genexus.com/commwiki/wiki?23900)
* [How are prompts invoked?](https://wiki.genexus.com/commwiki/wiki?23901)
* [How does GeneXus implement selection lists?](https://wiki.genexus.com/commwiki/wiki?23905)


|  |
| --- |
| **Backlinks** |
| [How does GeneXus implement selection lists?](https://wiki.genexus.com/commwiki/wiki?23905) | [Is it possible to modify Selection Lists?](https://wiki.genexus.com/commwiki/wiki?23900) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |
| [Prompt](https://wiki.genexus.com/commwiki/wiki?21635) | [When are selection lists created?](https://wiki.genexus.com/commwiki/wiki?23899) | [Window Data Type](https://wiki.genexus.com/commwiki/wiki?7112) |

---
