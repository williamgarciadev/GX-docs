---
title: "Find Formula"
source_id: 6547
source_url: https://wiki.genexus.com/commwiki/wiki?6547
genexus_version: "18"
---

# Find Formula

Find is an [Aggregate Formula](https://wiki.genexus.com/commwiki/wiki?5868).

## [Syntax](#Syntax)

**Find (** <a*ggregateExpression>*, <a*ggregateCondition>*, <*defaultValue>*) [ **if** <*triggeringCondition>*];

Where:

*<aggregateExpression>*:

Is the expression whose resultant value will be returned according to the first record found that matches the <a*ggregateCondition>*. It may contain attributes (even formula attributes), constants and variables (user variables are allowed only in [inline formulas](https://wiki.genexus.com/commwiki/wiki?6441)).

*<aggregateCondition>*:

Is a combination of a search condition with a [Data Selector](https://wiki.genexus.com/commwiki/wiki?5271) invocation. Both parts are optional:

[*<SearchCondition>*] [**USING** *<DataSelector>* '**(**' *<Parameter>1***,** *<Parameter>2***,** *<Parameter>n* '**)**']

*<SearchCondition>*

Is the condition that records must verify to be considered in the aggregation. It may contain attributes, constants and variables (user variables are allowed only in [inline formulas](https://wiki.genexus.com/commwiki/wiki?6441), GeneXus standard variables in [global formulas](https://wiki.genexus.com/commwiki/wiki?6440) and inline formulas).

*<defaultValue>*

Is the returned value when no records match the *<aggregateCondition>*. It is optional and only constant values are accepted (if the formula is being used with Date attributes, see [this article](http://wiki.gxtechnical.com/commwiki/servlet/hwiki?Date+Constants,) too).

*<triggeringCondition>*

Is the condition that determines if the formula must be triggered or not. It is optional. The only attributes allowed are those belonging to the contextual table (that the formula attribute would belong to if it were stored) and its extended.

### [Example](#Example)

```
Flight
{
    FlightId*
    FlightDescription
    Price
    {
        FlightDate*
        FlightPrice
    }
}

FlightInstance
{
    FlightInstanceNumber*
    FlightId
    FlightDescription
    FlightInstanceDate
    FlightInstancePrice
    FlightInstanceCurrencyValue = Find(CurrencyValue, CurrencyId = "Dollar" and CurrencyDate = FlightInstanceDate, 0) if FlightId=1;
}

Currency
{
    CurrencyId*
    Value
    {
         CurrencyDate*
         CurrencyValue
    }
}
```

The above example shows a defined Find [global formula](https://wiki.genexus.com/commwiki/wiki?6440).

The following image shows the FlightInstance transaction being edited (using the GeneXus transaction editor) and the FlightInstanceCurrencyValue global formula attribute being edited (using the GeneXus formula editor):

`[imagen omitida: wiki id 5877]`

FLIGHTINSTANCE is the contextual table of the *FlightInstanceCurrencyValue* global formula attribute.

CURRENCYVALUE is the table navigated by the Find formula in order to make the calculation.

The find calculation only triggers for the FlightId = 1.

The [tables involved in the formula definition](https://wiki.genexus.com/commwiki/wiki?6490) don't store common attributes, so GeneXus will not automatically apply any additional filter (only the defined *<aggregateCondition>* will be considered to find the searched record). Thus, the first record found in the CURRENCYVALUE table that fulfills the *<aggregateCondition>* will be selected, and the corresponding defined expression will be returned (in this example: a *CurrencyValue* is returned by the formula).

Note that in this example the defined *<aggregateCondition>* contains a filter by the primary key of the navigated table, so the navigated table may have a unique record that fulfills the *<aggregateCondition>*. This is the most common use of **Find** formulas, meaning that we usually define Find formulas **to search for a certain value**, filtering by the primary key of the navigated table (so that a unique record will fulfill the *<aggregateCondition>*). When filtering by secondary attributes or foreign key attributes, since many records may fulfill the *<aggregateCondition>*, the first record found that fulfills the *<aggregateCondition>* will be selected.


|  |
| --- |
| **Backlinks** |
| [Aggregate Formulas](https://wiki.genexus.com/commwiki/wiki?5868) | [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) |

---
