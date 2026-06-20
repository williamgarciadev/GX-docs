---
title: "Consuming SOAP web services in GeneXus"
source_id: 21003
source_url: https://wiki.genexus.com/commwiki/wiki?21003
genexus_version: "18"
---

# Consuming SOAP web services in GeneXus

Suppose that you need to consume the following SOAP web service in your GeneXus application:

```
http://www.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL
```

To do so in GeneXus:

**1. Open the [WSDL Import Wizard](https://wiki.genexus.com/commwiki/wiki?6181):**

`[imagen omitida: wiki id 21004]`

**2. Inspect the web service's WSDL and import it:**

Step 1

`[imagen omitida: wiki id 21005]`

Step 2

`[imagen omitida: wiki id 21006]`

Step 3

`[imagen omitida: wiki id 21007]`

**3. Use it in your GeneXus object:**

```
&CountryISOCode = &CountryInfoService.LanguageISOCode("Uruguay")
```

**Where:**

&CountryInfoService is a CountryInfoService variable based on the related [web service](https://wiki.genexus.com/commwiki/wiki?6154)

&CountryISOCode is a Character variable


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus for SAP Systems](https://wiki.genexus.com/commwiki/wiki?33616) | [GeneXus for SAP Systems - Application Integration](https://wiki.genexus.com/commwiki/wiki?34317) |

---
