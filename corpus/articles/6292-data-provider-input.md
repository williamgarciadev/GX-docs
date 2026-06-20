---
title: "Data Provider: Input"
source_id: 6292
source_url: https://wiki.genexus.com/commwiki/wiki?6292
genexus_version: "18"
---

# Data Provider: Input

The Input of most GeneXus Objects is:

* taken from [parameters](#idParameters), and/or
* [embedded](#idEmbedded) into the code

#### [Parameters](#Parameters)

The [Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) supports receiving parameters, but all parameters are "IN" parameters. Remember the output is specified independently through the [Output property](https://wiki.genexus.com/commwiki/wiki?41037).

#### [Embedded](#Embedded)

Even though the input is usually taken from the Database, it is usually necessary to have other kinds of input data. Because a [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270) implements an output-driven programming (that is to say, declarative), the only way to obtain information to fill hierarchical structures is through assignations:

[&Element](https://wiki.genexus.com/commwiki/wiki?25096) = *Expression*  
[&var](https://wiki.genexus.com/commwiki/wiki?25413) = *Expression*

So, every 'thing' that could be considered as (part of) an *expression*, is a valid input. For instance: an [**udp**](https://wiki.genexus.com/commwiki/wiki?3964)(calling a [Procedure](https://wiki.genexus.com/commwiki/wiki?6293) as well as a Data Provider. For the latter, you can see a simple sample [here](https://wiki.genexus.com/commwiki/wiki?5309), or another one with [Recursive Data Providers](https://wiki.genexus.com/commwiki/wiki?4891)). Keep in mind that if the returned value is a collection, the [Input clause](https://wiki.genexus.com/commwiki/wiki?5309) is needed to iterate inside it.

GeneXus objects have other common Input sources: [web sessions](https://wiki.genexus.com/commwiki/wiki?6321) and [cookies](https://wiki.genexus.com/commwiki/wiki?6322).

How do we obtain a web session value corresponding to a key? By having a variable of the 'WebSession' GeneXus data type, through the '['Get'](https://wiki.genexus.com/commwiki/wiki?6321)' method:

```
value = &webSession.Get( key )
```

So, it could be a Data Provider's Input, as long as '&webSession.Get( Key )' returns a value. In other words, it could be assigned to an Element or variable of the Data Provider's source.

The same can be said about the '[GetCookie](https://wiki.genexus.com/commwiki/wiki?6322)' function, used to obtain a cookie's value:

```
value = GetCookie( CookieName )
```


|  |
| --- |
| **Backlinks** |
| [Category:Data Provider object](https://wiki.genexus.com/commwiki/wiki?5270) | [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) | [Input clause](https://wiki.genexus.com/commwiki/wiki?25406) |

---
