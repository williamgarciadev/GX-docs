---
title: "Transaction levels"
source_id: 42569
source_url: https://wiki.genexus.com/commwiki/wiki?42569
genexus_version: "18"
---

# Transaction levels

Suppose an application must take into account that countries contain a set of cities.

GeneXus provides an easy way to represent a reality such as this of countries and cities.

It can be implemented by adding a second level to the Country Transaction.

Being in the Country Transaction, while positioned on the last attribute, right-click and select Insert Level.

`[imagen omitida: wiki id 42570]`

A sublevel is opened. You can call it: City.

Now, there are two possible ways to name the attributes on the 2nd level.

If you type a dot, you will see that GeneXus suggests “CountryCity” as a prefix, that is to say, the Transaction name + the 2nd level name. You would only have to complete it by adding Id at the end, and you would have the name CountryCityId.

If, on the other hand, you type inverted commas you will see that GeneXus suggests the prefix “City,” the 2nd level name. You would only have to complete it by adding Id at the end, and you would have the name CityId.

`[imagen omitida: wiki id 42572]`

This two-level Transaction indicates that each country has several cities and that each city belongs to only one country.

`[imagen omitida: wiki id 42573]`

When you save your Transaction structure, GeneXus defines (or change if it is necessary) the Web Form for this Transaction. As you can see, for each country now you can enter a group of cities.

`[imagen omitida: wiki id 42575]`

For every two-level Transaction, GeneXus determines that it has to create two physical tables:

* One table arises from the first level, in this case, to record the countries, with CountryId primary key.
* And another physical table, associated with the second level, in this case, to record the cities in each country.

`[imagen omitida: wiki id 42574]`

Note that GeneXus creates a table called Country and another table called CountryCity in the database. The second table name is taken from the Transaction name plus the name you gave to the second level.

Now, look at the primary key of the second table. It is composed of two attributes: CountryId and CityId. This means that the unique identifier of the cities is composed of both attributes.

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Transactions with more than one level](https://training.genexus.com/en/learning/courses/genexus/v18/core/content/transactions-with-more-than-one-level-6104683)


|  |
| --- |
| **Backlinks** |
| [Associated Table property (for Transaction's Levels)](https://wiki.genexus.com/commwiki/wiki?48109) | [Business Component GetByKey method](https://wiki.genexus.com/commwiki/wiki?31846) | [Business Component Load method](https://wiki.genexus.com/commwiki/wiki?23211) |
| [Business Component Mode method](https://wiki.genexus.com/commwiki/wiki?23790) | [Business Component Save method](https://wiki.genexus.com/commwiki/wiki?23229) | [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) | [Work With for Web pattern](https://wiki.genexus.com/commwiki/wiki?25475) |
| [Work With Pattern instance for Multi-level Transactions](https://wiki.genexus.com/commwiki/wiki?16004) |

---
