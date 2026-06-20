---
title: "Animations Layer property"
source_id: 43487
source_url: https://wiki.genexus.com/commwiki/wiki?43487
genexus_version: "18"
---

# Animations Layer property

Enables or disables the Animations Layer (that allows viewing map point animations) in a Grid whose Control Type is set to Maps.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Platforms:** Smart Devices(IOS)  
**Controls:** Grid (Control Type: [SD Maps](https://wiki.genexus.com/commwiki/wiki?15309))

### [Description](#Description)

This property allows viewing a map point animation. It can be used, for example, to show the route of a vehicle (taxi, Uber, delivery service).

`[imagen omitida: wiki id 44195]`

It applies only to [Grids](https://wiki.genexus.com/commwiki/wiki?24817) whose [Control Type property = Maps](https://wiki.genexus.com/commwiki/wiki?15309).

When you set the Animations Layer property to True, the following properties will be enabled to set related details:

* [Animation Key Attribute](https://wiki.genexus.com/commwiki/wiki?43488)
* [Animation Duration](https://wiki.genexus.com/commwiki/wiki?44580)
* [Animation Duration Attribute](https://wiki.genexus.com/commwiki/wiki?43490)
* [Animation End Behavior](https://wiki.genexus.com/commwiki/wiki?43492)
* [Animation End Behavior Attribute](https://wiki.genexus.com/commwiki/wiki?43493)

The [Location Attribute property](https://wiki.genexus.com/commwiki/wiki?42209) is another important property related to this kind of Grid whose Control Type property = Maps.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

Consider the following [Transaction object](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,)s:

```
Car
{
   CarId*
   .....
}

CarLocation
{
   CarId*
   CarLocationId*
   CarLocation (Data Type = GeoPoint)
}
```

Assume the existence of the following [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) in order to assign data to the physical tables associated with the previous Transactions:

```
new 
     CarId = 1
endnew
new
     CarId = 1
     CarLocationId = 1
     CarLocation = geopoint.FromString('POINT (-56.088973921240267 -34.883211936027749)')
     CarAnimationDuration = 2
endnew
new        
     CarId = 1
     CarLocationId = 2
     CarLocation = geopoint.FromString('POINT (-56.086742323339877 -34.883211936027749)')
     CarAnimationDuration = 1
endnew
new
     CarId = 1
     CarLocationId = 3
     CarLocation = geopoint.FromString('POINT (-56.083400226489289 -34.883156426543607)')
     CarAnimationDuration = 3
endnew
```

Next, a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) is created and a [Grid control](https://wiki.genexus.com/commwiki/wiki?24817) is included, with the following properties configured:

* Control Type = Maps
* Location Attribute = CarLocation
* Animation Layer = True
* Animation Key Attribute = CarId
* Animation Duration = 2

In the Grid conditions, the following is defined:

```
       CarLocationId = &CurrentAnimationStep;
```

In the events section of the Panel object, the following is defined:

```
Event Refresh
    Composite
        Grid1.Refresh()
        &currentAnimationStep += 1
    EndComposite
Endevent

Event ClientStart
      &currentAnimationStep = 1
Endevent
```

**Note:** To fully view the animation, defining a zoom based on a range that reaches the points to animate is recommended. The following Grid properties must be configured for this purpose:

* [Initial Zoom property](https://wiki.genexus.com/commwiki/wiki?42217) = Radius
* [Initial Zoom Radius Attribute property](https://wiki.genexus.com/commwiki/wiki?42218) = &Radio
* [Center property](https://wiki.genexus.com/commwiki/wiki?42220) = Default

Therefore, the ClientStart event has to be modified to start the &Radio variable:

```
Event ClientStart
     composite
         &currentAnimationStep = 1
         &Radio = 100
     endcomposite
EndEvent
```

**An alternative way to set the animation duration**

Suppose that attributes are added to the CarLocation Transaction in example 1 to store the duration and/or the final behavior of the animation:

```
CarLocation
{
   CarID*
   CarLocationId*
   CarLocation (Data Type = GeoPoint)
   CarAnimationDuration (Data Type = Numeric)
}
```

Since an attribute (CarAnimationDuration) contains the number of seconds that the animation lasts, for the Grid whose Control Type is set to Maps, you have to set the following property:

* Animation Duration Attribute = CarAnimationDuration

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build with this Only](https://wiki.genexus.com/commwiki/wiki?5693) of the object.

### [See Also](#See+Also)

[Maps Control Type](https://wiki.genexus.com/commwiki/wiki?15309)  
[Location Attribute property](https://wiki.genexus.com/commwiki/wiki?42209)


|  |
| --- |
| **Backlinks** |
| [Animation Duration Attribute property](https://wiki.genexus.com/commwiki/wiki?43490) | [Animation Duration Field Specifier property](https://wiki.genexus.com/commwiki/wiki?43491) | [Animation Duration property (for Grids with Control Type = SD Maps)](https://wiki.genexus.com/commwiki/wiki?44580) |
| [Animation End Behavior Attribute property](https://wiki.genexus.com/commwiki/wiki?43493) | [Animation End Behavior Field Specifier property](https://wiki.genexus.com/commwiki/wiki?43494) | [Animation End Behavior property](https://wiki.genexus.com/commwiki/wiki?43492) | [Animation Key Attribute property](https://wiki.genexus.com/commwiki/wiki?43488) |
| [Animation Key Field Specifier property](https://wiki.genexus.com/commwiki/wiki?43489) | [HowTo: Draw animations between locations on a Map](https://wiki.genexus.com/commwiki/wiki?59366) | [Maps Control Type Properties](https://wiki.genexus.com/commwiki/wiki?54092) |

---
