---
title: "CallOptions Target"
source_id: 25323
source_url: https://wiki.genexus.com/commwiki/wiki?25323
genexus_version: "18"
---

# CallOptions Target

[CallOptions](https://wiki.genexus.com/commwiki/wiki?23666) are used to specify at runtime the transitions, behavior, and position in a call to a particular [Panel object](https://wiki.genexus.com/commwiki/wiki?24829).

In some cases you may want the called Panel to appear in another frame and not where the caller is located. In order to do this, you must use the Target option.

This is possible when the [Navigation style](https://wiki.genexus.com/commwiki/wiki?16229) is Split or Slide, or when Dashboard has [control](https://wiki.genexus.com/commwiki/wiki?16098) Tab set.  
In abstract terms, the Panel adopts the following aspects:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Slide / Split** |  | **Tab** |  | *Note*: The difference between Slide and Split is  if "Left" region is displayed fixed or not. |
| |  |  | | --- | --- | | Left | Content | |  | |  |  |  | | --- | --- | --- | | Content | | | | Tab1 | ... | TabN | |  |

In these cases, the target (or region) will be indicated using its name in the property Target of the CallOptions.  
The syntax is:

```
<Object Name>.CallOptions.Target = TargetName
<Object Name>()
```

### [Domain values](#Domain+values)

The domain of values that the property Target support is given by the list of names of the components on the UI and the names of Navigation Style regions (as is shown above). These values can be defined in two ways:

* Using **bracket notation**: A generic way using "[" and "] ".
  + By its **target index**: Each index references a particular target (e.g. *Target[ i ]*is the i-th target).
  + By its **navigation index**: Each index reference a particular navigation target (e.g. *<N>[ i ]*is the ith target for navigation *N*).
* Using **alias**: It is a relevant navigation value (e.g. Left, Right, Detail, Content, and Center in Slide navigation).

For that reason, there are named equivalence (summarized in the following table)

|  |  |  |  |
| --- | --- | --- | --- |
| **Synonyms** | | | **Description** |
| **Navegation** | **Target** | **Alias** |
| Slide[1] | Target[1] | Left | It is shown in the left section. |
| Slide[2] | Target[2] | Center, Content, Detail | It is shown in the central section. |
| Tab[1] | Target[1] | N/A | It shows the first tab. |
| ... | ... | ... | ... |
| Tab[K](1) | Target[K] | N/A | It shows the K-th tab. |
| Split[1] | Target[1] | Left | It is shown on the left side. |
| Split[2] | Target[2] | Center, Content, Detail | It is shown on the center side. |
| All | N/A | Blank | It is shown as an independent Panel (as if it were a 'pop-up fullscreen') (2) |

**Notes**:  
    (1) K represents the tabs quantity.   
    (2) Usually, these Panels are not part of the ´content´ of the application (e.g. Settings, About, Help, Login, etc)

#### [Behavior](#Behavior)

* A Panel called from the left will be displayed on the content region - using [call type replace](https://wiki.genexus.com/commwiki/wiki?25322).
* A Panel called from the content region will be displayed in the same region -using [call type push](https://wiki.genexus.com/commwiki/wiki?25322).

#### [Other targets](#Other+targets)

|  |  |  |
| --- | --- | --- |
| Left | Content | Right |
| Bottom | | |

* When Slide navigation is enabled, a "*Right*" section is also available.
* For iOS devices is available a "*Bottom*" region, independently of the Navigation style used.

The only requirement is that these sections can only be displayed through explicit programming as is explained in the next section.

### [Triggering programmatically](#Triggering+programmatically)

The [Navigation external object](https://wiki.genexus.com/commwiki/wiki?32395) allows the developers to show (or hide) content dynamically in the drawer that they want to.

For example, if the application uses Navigation Style = Slide and the central Panel has a user event defined as shown below, not only load the Panel in the right drawer, It also will display the right drawer.

```
Event 'ShowRight'
   Composite
      SomePanel.CallOptions.Target = "Right" // Set in which drawer it will be display
      SomePanel()                            // Load the Panel in that target 
      Navigation.ShowTarget("Right")         // Display the target
   EndComposite
EndEvent 
```

### [Special behavior for Android App with Slide Navigation and GAM](#Special+behavior+for+Android+App+with+Slide+Navigation+and+GAM)

When de App main object uses authentication (Integrated security property was set as Authentication) and the App uses Slide Navigation, every called object displayed on the Slide section (default behavior) will also require authentication. Therefore, in case you call an object without integrated security, the Login Object will be shown instead.

For that reason, if you need to call the Register object from the Login Panel (which also has not integrated security), it must be called with Target ‘Blank’, to be shown in an independent Panel. This also applies if you need to call the Login Panel manually.

### [See Also](#See+Also)

[KB: EventDay](https://wiki.genexus.com/commwiki/wiki?22550,,)


|  |
| --- |
| **Backlinks** |
| [Back event](https://wiki.genexus.com/commwiki/wiki?24950) | [CallOptions](https://wiki.genexus.com/commwiki/wiki?23666) | [CallOptions Type](https://wiki.genexus.com/commwiki/wiki?25322) |
| [DynamicCall External Object](https://wiki.genexus.com/commwiki/wiki?47056) | [Features that are exclusive to Angular development](https://wiki.genexus.com/commwiki/wiki?46455) | [Features that are exclusive to Angular development (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?57003) |
| [Form theme-class for Smart Devices](https://wiki.genexus.com/commwiki/wiki?37648) | [Navigation external object](https://wiki.genexus.com/commwiki/wiki?32395) |

---
