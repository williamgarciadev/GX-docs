---
title: "Timezones Domain"
source_id: 21989
source_url: https://wiki.genexus.com/commwiki/wiki?21989
genexus_version: "18"
---

# Timezones Domain

The [TimeZone](https://wiki.genexus.com/commwiki/wiki?21997,,)s Domain was extracted from [the list of tz database timezones](http://en.wikipedia.org/wiki/List_of_tz_database_time_zones). The list is not extensive. Several values were removed for simplicity.

It is intended to be used when programming (i.e. TimeZones.Cairo instead of "Africa/Cairo"), for filling Combos/Lists controls, etc.

If the value you need is not in the domain and you need it for programming purposes, you may either:

* Add the value to the domain. If so, new GeneXus versions may overwrite your changes.
* Use the Convert method of [Enumerated Domains Methods and Properties](https://wiki.genexus.com/commwiki/wiki?9918). For example: &NewDateTime = TimeZones.Convert( "America/Puerto\_Rico").

TimeZones domain values

| Name | Description | Value |
| --- | --- | --- |
| Cairo | Africa/Cairo | Africa/Cairo |
| Johannesburg | Africa/Johannesburg | Africa/Johannesburg |
| Lagos | Africa/Lagos | Africa/Lagos |
| Anchorage | America/Anchorage | America/Anchorage |
| Buenos\_Aires | America/Argentina/Buenos\_Aires | America/Argentina/Buenos\_Aires |
| Asuncion | America/Asuncion | America/Asuncion |
| Bogota | America/Bogota | America/Bogota |
| Caracas | America/Caracas | America/Caracas |
| Chicago | America/Chicago | America/Chicago |
| Denver | America/Denver | America/Denver |
| Godthab | America/Godthab | America/Godthab |
| Guatemala | America/Guatemala | America/Guatemala |
| Halifax | America/Halifax | America/Halifax |
| Los\_Angeles | America/Los\_Angeles | America/Los\_Angeles |
| Mexico\_City | America/Mexico\_City | America/Mexico\_City |
| Montevideo | America/Montevideo | America/Montevideo |
| New\_York | America/New\_York | America/New\_York |
| Noronha | America/Noronha | America/Noronha |
| Phoenix | America/Phoenix | America/Phoenix |
| Santiago | America/Santiago | America/Santiago |
| Santo\_Domingo | America/Santo\_Domingo | America/Santo\_Domingo |
| Sao\_Paulo | America/Sao\_Paulo | America/Sao\_Paulo |
| St\_Johns | America/St\_Johns | America/St\_Johns |
| Baghdad | Asia/Baghdad | Asia/Baghdad |
| Beirut | Asia/Beirut | Asia/Beirut |
| Damascus | Asia/Damascus | Asia/Damascus |
| Dhaka | Asia/Dhaka | Asia/Dhaka |
| Dubai | Asia/Dubai | Asia/Dubai |
| Jerusalem | Asia/Jerusalem | Asia/Jerusalem |
| Kabul | Asia/Kabul | Asia/Kabul |
| Karachi | Asia/Karachi | Asia/Karachi |
| Katmandu | Asia/Katmandu | Asia/Katmandu |
| Kolkata | Asia/Kolkata | Asia/Kolkata |
| Rangoon | Asia/Rangoon | Asia/Rangoon |
| Shanghai | Asia/Shanghai | Asia/Shanghai |
| Tehran | Asia/Tehran | Asia/Tehran |
| Tokyo | Asia/Tokyo | Asia/Tokyo |
| Yerevan | Asia/Yerevan | Asia/Yerevan |
| Azores | Atlantic/Azores | Atlantic/Azores |
| Cape\_Verde | Atlantic/Cape\_Verde | Atlantic/Cape\_Verde |
| Adelaide | Australia/Adelaide | Australia/Adelaide |
| Brisbane | Australia/Brisbane | Australia/Brisbane |
| Darwin | Australia/Darwin | Australia/Darwin |
| Sydney | Australia/Sydney | Australia/Sydney |
| GMT\_12 | Etc/GMT\_12 | Etc/GMT\_12 |
| GMT\_2 | Etc/GMT\_2 | Etc/GMT\_2 |
| UTC | Etc/UTC | Etc/UTC |
| Berlin | Europe/Berlin | Europe/Berlin |
| Helsinki | Europe/Helsinki | Europe/Helsinki |
| Istanbul | Europe/Istanbul | Europe/Istanbul |
| London | Europe/London | Europe/London |
| Auckland | Pacific/Auckland | Pacific/Auckland |
| Honolulu | Pacific/Honolulu | Pacific/Honolulu |
| Noumea | Pacific/Noumea | Pacific/Noumea |
| Tongatapu | Pacific/Tongatapu | Pacific/Tongatapu |


|  |
| --- |
| **Backlinks** |
| [FromTimeZone method](https://wiki.genexus.com/commwiki/wiki?21916) | [GetTimeZone method](https://wiki.genexus.com/commwiki/wiki?21915) | [SetTimeZone method](https://wiki.genexus.com/commwiki/wiki?21893) |
| [Toc:TimeZone Support](https://wiki.genexus.com/commwiki/wiki?21988) | [View DateTime values in a selected time zone - TimeZone Scenario](https://wiki.genexus.com/commwiki/wiki?22140) |

---
