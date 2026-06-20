---
title: "Google Intensity Map Control"
source_id: 10648
source_url: https://wiki.genexus.com/commwiki/wiki?10648
genexus_version: "18"
---

# Google Intensity Map Control

#### [Introduction](#Introduction)

This control shows a map that highlights regions or countries based on relative values.

#### [Example](#Example)

The user control is really simple, you just need to set one property in order to get the control working, the Series property.

#### [Show a simple chart to illustrate population and area of certain countries](#Show+a+simple+chart+to+illustrate+population+and+area+of+certain+countries)

* Drag and drop Intensity Map.
* Assign to Series property a variable based on CountryInfo data type (this SDT is automatically imported when dropping the control to the web form).
* Load the information that will be shown by the chart using the previous mentioned variable.

```
Sub 'LoadIntensityMap'
  &Countries.Info.Add("Population")
  &Countries.Info.Add("Area")

  &Country = new()
  &Country.CountryISO = "BR"
  // Population
  &Country.Values.Add(187)
  // Area
  &Country.Values.Add(8514877)
  &Countries.Countries.Add(&Country)

  &Country = new()
  &Country.CountryISO = "CN"
  // Population
  &Country.Values.Add(1324)
  // Area
  &Country.Values.Add(96400821)
  &Countries.Countries.Add(&Country)
EndSub
```

Note: &Country is based on CountryInfo.Country and &Countries is based on CountryInfo SDT.  
  
`[imagen omitida: wiki id 10649]`  
`[imagen omitida: wiki id 10650]`


|  |
| --- |
| **Backlinks** |
| [GXGoogle Visualization Library](https://wiki.genexus.com/commwiki/wiki?10447) |

---
