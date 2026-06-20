---
title: "Does GeneXus Determine a Base Table in a Data Selector?"
source_id: 6053
source_url: https://wiki.genexus.com/commwiki/wiki?6053
genexus_version: "18"
---

# Does GeneXus Determine a Base Table in a Data Selector?

No, it doesn't. Because a Data Selector only stores the definition required to obtain a navigation, and it does not access any table in the database.

The purpose of Data Selectors is to reuse navigations. This means that in a Data Selector we can store a set of conditions, filters, orders, parameters and clauses to retrieve a specific set of data from the database. Through the Data Selector, we can reuse that definition without writing down all the conditions and filters every time we need the data.

Therefore, because the Data Selector itself does not navigate a table, GeneXus does not need to determine a Base Table.

The information stored in the Data Selector is like a "dead code" that comes to life only at specification time, when it is expanded and merged with the information of the object that uses the Data Selector. So the final navigation depends on the context where the Data Selector is used.

For further information see [Data Selectors](https://wiki.genexus.com/commwiki/wiki?5271)
