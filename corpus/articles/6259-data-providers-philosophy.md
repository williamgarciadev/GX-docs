---
title: "Data Providers philosophy"
source_id: 6259
source_url: https://wiki.genexus.com/commwiki/wiki?6259
genexus_version: "18"
---

# Data Providers philosophy

When designing an application, it is crucial to conceptualize what our business logic will be, regardless of the architecture we plan to develop. This business logic applied in knowledge-based development is represented naturally through rules.

Subsequently, with Transactions (and in particular, with [Business Component - Publication as an Enterprise Java Bean](https://wiki.genexus.com/commwiki/wiki?1993,,)) GeneXus provides a way of capturing these rules and effectively generating and maintaining them, so that they are complied with when required. Business Components, therefore, play a major role in the construction of the Business Logic.

However, these rule application and updating components are complemented by other, essential components: those that in a sense define our application’s information retrieval and presentation services, thus forming what we could refer to as the application’s Business Framework.

We’ll call these intelligent components –components capable of processing various types of inputs, filtering them, sorting them, and producing some form of desired output–  [Data Providers](https://wiki.genexus.com/commwiki/wiki?5270). Together with Business Components, they will play the leading roles in the construction of our applications’ future Business Frameworks.

### Declaring our Data Providers

Data Providers are a major step in GeneXus’ evolution, as they are objects that will enable the capturing of automatable knowledge in a declarative way.

The great innovation is in the way GeneXus users will be able to express them, so that we could say that for a great number of cases we will go from programming [Procedures](https://wiki.genexus.com/commwiki/wiki?6293) to declaring Data Providers.

Being declarative in whatever you want enables you to obtain a knowledge that opens the doors to innumerable variations in terms of generating the application’s definitive code. GeneXus will always tend to declare knowledge instead of programming the application, as the latter is simply an automatic step that comes after declaring.

If a Data Provider declares that it wants a set of data with certain filters, that same data can be obtained in several ways, from various sources, and with different technologies. If I have something that is declarative, I won’t have to worry about these parameters when declaring knowledge: this will simply be a decision that is adopted later, and possibly automatically.

### What is it that I declare?

In every process we can say that we have an input, a transformation, and an output. In Data Providers what is important and what is declared is the output.  
   
As we said, by declaring the output, GeneXus will be able to evolve in such a way as to obtain that output. When we say output, we’re not thinking solely of cases of outputs to a certain given format. These are, no doubt, common cases, but they vary with time.

There are a number of “outputs” that are more important than these, and they are outputs to, for example, internal components of my Business Framework.

A Data Provider that has an Invoice as input and a set of accounting entries as output is clearly more important for my Framework than the Data Provider that generates an [RSS](https://wiki.genexus.com/commwiki/wiki?2337,,) with the entries. The latter will surely change over time, as the RSS format may no longer exist, while the former is pure knowledge of how to convert an invoice into the corresponding entries. A specific example: [entering a sales invoice into accounting records](https://wiki.genexus.com/commwiki/wiki?6342).  
  
You will find many examples of Data Providers in the [documentation](https://wiki.genexus.com/commwiki/wiki?5270).


|  |
| --- |
| **Backlinks** |
| [Category:Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) |

---
