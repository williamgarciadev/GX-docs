---
title: "GeneXus for SAP Systems - Working with Attributes and Domains"
source_id: 34180
source_url: https://wiki.genexus.com/commwiki/wiki?34180
genexus_version: "18"
---

# GeneXus for SAP Systems - Working with Attributes and Domains

[Attributes](https://wiki.genexus.com/commwiki/wiki?7240) and [Domains](https://wiki.genexus.com/commwiki/wiki?7221) are key for modeling.

Create a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) called “Attraction”.

For each tourist attraction, the following information is requested:

* Its name
* The country where it is located
* A photo
* and a category that describes if it is a monument, a museum, a show, and so on.

`[imagen omitida: wiki id 34189]`

The key attribute of this Transaction will be called “AttractionId”. Remember to always type a dot, so that GeneXus suggests a prefix to avoid typing mistakes.

Complete the key attribute name and set its type as numeric of 4 digits, just like you did with the Customer identifier (CustomerId).

It would be a good idea to create a common data type for all identifiers, as you will probably need to create more of them. For instance, a type called "Id" and is a numeric value of 4 digits.

This data type created is called [Domain](https://wiki.genexus.com/commwiki/wiki?7221).

`[imagen omitida: wiki id 34191]`

For example, once the Id domain is created, several attributes can be set to Id type, and they will all be 4-digit numeric values.

One advantage it provides is that, if later on, you need identifiers to be “Numeric” of length 6 instead of “Numeric” of 4, changing the “Domain” definition will be enough to update all the attributes based on that “Domain” in a single step.

To create it, press the Tab key and in the Type, column write: Id=N (it is autocompleted with Numeric):

`[imagen omitida: wiki id 34192]`

As of now, leave the 4-digit value suggested by default.

After pressing Enter, you will see that the AttractionId attribute has now been set as Id type.

`[imagen omitida: wiki id 53070]`

Take a look at the properties of the AttractionId attribute.

If you are positioned on the AttractionId attribute and press F4, this window will display several settings made for this attribute and will allow you to change them.

`[imagen omitida: wiki id 53071]`

You can see that it is "Based on" the Id domain and for this reason, it is a 4-digit numeric value.

Note that properties can be sorted alphabetically

`[imagen omitida: wiki id 53072]`

Here, the [Autonumber property](https://wiki.genexus.com/commwiki/wiki?6798) can be seen. This property is set to False by default and if you change it to True, all the new attractions entered will be automatically numbered in sequence.

That is to say, every time that a new attraction is added, the AttractionId attribute will be automatically assigned a new number that's bigger than the last existing number.

So, you're setting the [Autonumber property](https://wiki.genexus.com/commwiki/wiki?6798) specifically for this AttractionId identifier attribute.

`[imagen omitida: wiki id 53073]`

Another option could be to set the same property for the Id domain that you've created,

`[imagen omitida: wiki id 53074]`

so that when you create more Transaction identifier attributes, the Id domain can be assigned. In this way, they would inherit all the domain definitions (such as the data type and all the properties configured).

To see the domains created, edit the Domains window: View > Domains

Here you can create and edit domains, in a similar way to how attributes are created.

`[imagen omitida: wiki id 53076]`

Click on the Id domain and the properties window is refreshed to show this domain’s properties.

Here you can see again the Properties categorized view instead of the alphabetical view:

`[imagen omitida: wiki id 53077]`

Find the Autonumber property and set it to True, this will cause all Id type attributes to be automatically autonumbered in sequence.

Go back to the structure window of the Attraction Transaction and start to create its second attribute. Add the AttractionName attribute. Also, create the Name domain of Character type, length 50.

Set the Name type for the AttractionName attribute.

`[imagen omitida: wiki id 53078]`

Now you need an attribute to record the country of the tourist attraction.

An attribute called AttractionCountry of Character(50) data type could be created and enter the country name when adding details.

`[imagen omitida: wiki id 53079]`

What happens if you want to enter two tourist attractions from the same country?

You should enter the same country name twice, and be careful to type it exactly the same! Later on, you might need to search for all the attractions in a certain country, and to get them, the country must have been typed the same every time.

Take a look at this case:

`[imagen omitida: wiki id 34204]`

Suppose that you’ve entered several attractions with their corresponding countries.

For example, you have an attraction with identifier 1, called Louvre, located in France, an attraction with identifier 2, called the Great Wall and located in China…and another attraction with Id=3, the Eiffel Tower, which is also in France.

You know that the Louvre is located in France and that the Eiffel Tower is also in France, but due to a typing or spelling mistake, the country name is typed differently.

`[imagen omitida: wiki id 34205]`

Here, France is typed with two Ns. So, for the system, this country is not the same as this other one.

`[imagen omitida: wiki id 34206]`

For this reason, this solution can't be used.

`[imagen omitida: wiki id 34207]`

It seems more reasonable to enter the country only once, in a single location, and then make reference to the corresponding country for each attraction.

That is to say, you should define something like this:

`[imagen omitida: wiki id 34208]`

One location where countries are stored, and in attractions you make reference to the corresponding country identifiers.

`[imagen omitida: wiki id 34209]`

The Louvre is in France: Country 2.

The Great Wall is in China: 3.

And the Eiffel Tower is in France, also 2.

To do this in GeneXus, create a Transaction object to record the countries, and then you will see how to assign a country to each Transaction.

Meanwhile, save the Attraction structure that hasn't been completed.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus for SAP Systems](https://wiki.genexus.com/commwiki/wiki?33616) | [GeneXus for SAP Systems - Data Model changes](https://wiki.genexus.com/commwiki/wiki?34336) | [GeneXus for SAP Systems Data Model changes (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54688) |

---
