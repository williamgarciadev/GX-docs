---
title: "LoadKmlLayer method"
source_id: 51341
source_url: https://wiki.genexus.com/commwiki/wiki?51341
genexus_version: "18"
---

# LoadKmlLayer method

Draws geometries given by a KML file in a [Panel](https://wiki.genexus.com/commwiki/wiki?24829) Grid whose [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) is set to Maps.

### [Syntax](#Syntax)

GridControlName**.LoadKmlLayer(***LayerId*, ***&**VarLayerData*, *AllowSelection***)**

**Where:**

*GridControlName*  
   Grid control name whose Control Type property is set to [Maps](https://wiki.genexus.com/commwiki/wiki?15309).

*LayerId*  
   Is the logical name of the KML file (Character data type).

***&**VarLayerData*  
   Is a variable with the KML file content (Longvarchar data type).

*AllowSelection*Is a boolean value.

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Controls:** | [Grid](https://wiki.genexus.com/commwiki/wiki?24817) (Control Type: [Maps](https://wiki.genexus.com/commwiki/wiki?15309)) |
| **Generators:** | [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453) |

### [Samples](#Samples)

```
&kmlString = '<kml>'
&kmlString += '<Document>'
&kmlString += '    <Style id="MyLine">'
&kmlString += '      <LineStyle>'
&kmlString += '       <color>802080ff</color>'
&kmlString += '       <width>6</width>'
&kmlString += '      </LineStyle>'
&kmlString += '    </Style>'
&kmlString += '     <Placemark>'
&kmlString += '        <LineString>'
&kmlString += '           <coordinates>-88.076680,43.945580 -88.077480,43.945930  -88.082470,43.942310 </coordinates>'
&kmlString += '        </LineString>'
&kmlString += '       <styleUrl>#MyLine</styleUrl>'
&kmlString += '     </Placemark>'
&kmlString += '</Document>'
&kmlString += '</kml>'

MapGrid.LoadKmlLayer("MyKml",&kmlString,false)
MapGrid.SetLayerVisible("MyKml",true)
```

### [Considerations](#Considerations)

This method only applies to events on the client, such as user events.

To draw geometries on the server, use the [Location Attribute property](https://wiki.genexus.com/commwiki/wiki?42209).

The Refresh event keeps the geometries drawn by this method.

To clear these geometries, use the Clear method or the SetLayerVisible method.

### [Availability](#Availability)

This method is available since [GeneXus 17](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46066,,).

### [Compatibility](#Compatibility)

Since [GeneXus 17 Upgrade 11](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49972,,), the Refresh method keeps the geometries drawn by LoadKmlLayer. Previous versions delete these geometries. In order to maintain the previous behavior, use the Grid.Clear method in the Refresh event.

```
Event Grid.Refresh()
      GridMaps.Clear()
EndEvent
```

This 'LoadKmlLayer' method is the same as the one named 'LoadKml' in previous versions (since [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?20247,,)).

### [See Also](#See+Also)

[DrawGeography method](https://wiki.genexus.com/commwiki/wiki?47024)


|  |
| --- |
| **Backlinks** |
| [HowTo: Group and Visualize Geographic Data Logically](https://wiki.genexus.com/commwiki/wiki?48253) | [KML Geographic data format](https://wiki.genexus.com/commwiki/wiki?59400) | [Maps Control Type Methods](https://wiki.genexus.com/commwiki/wiki?54095) |

---
