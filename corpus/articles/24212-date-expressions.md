---
title: "Date expressions"
source_id: 24212
source_url: https://wiki.genexus.com/commwiki/wiki?24212
genexus_version: "18"
---

# Date expressions

There are a lot of expressions to work with dates in GXquery. Check the links below to know more about this expressions.

|  |  |  |
| --- | --- | --- |
| **Expression** | **Purpose** | **Example** |
| [AddMth](https://wiki.genexus.com/commwiki/wiki?8314) | To add a specific number of months to a given date. | AddMth(&Date,&Month) |
| [AddYr](https://wiki.genexus.com/commwiki/wiki?8317) | Adds a given number of years to a given date. | AddYr(&FromDate,1) |
| [EoM](https://wiki.genexus.com/commwiki/wiki?8392) | To return the last date of the month in the given date parameter. | EoM(&Today()) |
| [YMDHMStoT](https://wiki.genexus.com/commwiki/wiki?7626) | Returns a DateTime value representing the date and time received as parameters. | YMDHMStoT(&Year,&Month,&Day,&HH,&MM,&SS) |
| [YMDtoD](https://wiki.genexus.com/commwiki/wiki?7627) | To return a date from three given numbers: year, month and day. | YMDtoD(&YY, &MM, &DD) |
| [Age](https://wiki.genexus.com/commwiki/wiki?8330) | To calculate the difference, in years, between two date expressions. | Age(&Today) |
| [Day](https://wiki.genexus.com/commwiki/wiki?8376) | To extract the number that indicates the day in a given date. | Day(&Date) |
| [DoW](https://wiki.genexus.com/commwiki/wiki?8344) | To return the number (1...7) of the day of the week. This number is associated with a day of the week (Sunday = 1). | DoW(&Date) |
| [Hour](https://wiki.genexus.com/commwiki/wiki?8415) | To return a numeric value representing the time in 24-hour format. | Hour(&DateTime) |
| [Minute](https://wiki.genexus.com/commwiki/wiki?8416) | To return a numeric value representing the minutes of a datetime argument. | Minute(&DateTime) |
| [Month](https://wiki.genexus.com/commwiki/wiki?8379) | To return the numeric month identifier in a given date. | Month(&Date | &DateTime) |
| [Second](https://wiki.genexus.com/commwiki/wiki?8417) | To return a numeric value representing the seconds in a datetime argument. | Second(&DateTime) |
| [Year](https://wiki.genexus.com/commwiki/wiki?8380) | To return the year number in a given date. | Year(&Date | &DateTime) |
| [CMonth](https://wiki.genexus.com/commwiki/wiki?8343) | Returns the name of the month for the given date. | CMonth(&Date | &DateTime) |
| [CDoW](https://wiki.genexus.com/commwiki/wiki?8340) | Returns the weekday for a given date. | CDoW(&Date | &DateTime) |
