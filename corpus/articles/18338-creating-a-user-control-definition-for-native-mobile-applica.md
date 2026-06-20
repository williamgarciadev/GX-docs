---
title: "Creating a User Control Definition for Native Mobile applications"
source_id: 18338
source_url: https://wiki.genexus.com/commwiki/wiki?18338
genexus_version: "18"
---

# Creating a User Control Definition for Native Mobile applications

The definition of a User Control for Native Mobile applications is similar to the [User Control definition](https://wiki.genexus.com/commwiki/wiki?5273), with a few additional properties. Notice that the User Control editor is only available for [User Controls](https://wiki.genexus.com/commwiki/wiki?5273).

To create your own User Control for Native Mobile applications, copy and paste an already existing one and modify the following tags.

* Change the User Control *Name* and *Description*.
* Set the *Version* tag to an initial value.
* Set the user control properties in an XML file and reference it in the *PropertiesDefinition* tag

```
<PropertiesDefinition>UserControlNameProperties.xml</PropertiesDefinition>
```

* Set the *Platform* to "SmartDevices".

```
<Platforms>
  <Platform>SmartDevices</Platform>
</Platforms>
```

* If the control is a list one, make sure to set the *List* value on the *ControlType* tag:

```
<ControlType>List</ControlType>
```

### [Implementation of specific values](#Implementation+of+specific+values)

Then, you must fill in the platform specific values.

#### [For iOS](#For+iOS)

* You need to package your user control as a [library](https://wiki.genexus.com/commwiki/wiki?18088,,) and reference a bundle (resources) if needed using the *iOS\_SupportFiles* property.

```
<iOS_SupportFiles>
  <File>libmyUC.a</File>
  <Directory>myUC.bundle</Directory>
</iOS_SupportFiles>
```

* Declare the class in charge of the User Control for Native Mobile implementation using the *iOS\_ClassName* tag.

```
<iOS_ClassName>SampleUCMainClass</iOS_ClassName>
```

#### [For Android](#For+Android)

* Declare the class in charge of the User Control for Native Mobile implementation using the *Android\_ClassName* tag.

```
<Android_ClassName>com.mycompany.extendedcontrols.sampleuc.mainclass</Android_ClassName>
```

### [Adding platform default value](#Adding+platform+default+value)

Since [GeneXus 15 Upgrade 4](https://wiki.genexus.com/commwiki/wiki?33798,,) it is possible to specify the pd (platform default) value in dips associated with the user control by adding a tag to its definition (\*.control file).

For iOS

* Declare the value in dips using the *iOS\_PlatformDefault* tag.

```
<iOS_PlatformDefault>80</iOS_PlatformDefault>
```

For Android

* Declare the value in dips using the *Android\_PlatformDefault* tag.

```
<Android_PlatformDefault>80</Android_PlatformDefault>
```

For both

* Declare the value in dips using the *PlatformDefault* tag.

```
<PlatformDefault>80</PlatformDefault>
```

**Note**

Since Genexus 16 upgrade 2, when defining a user control of type List, you are able to hide the Row property, and you can also indicate a fixed value. Example: Inside the GeneXus installation directory (<Gx installation directory> UserControls \ SmartDevicesMapControl \ sdmapcontrol.control) you can find the user control SDMaps :

```
<Overrides>
   <Property>
   <Id>rows</Id>
   <Visible>false</Visible>
   <Value>&lt;unlimited&gt;</Value><!-- does not support paging, so it must be unlimited -->
                ....
</Overrides>
```

Note that in the example, the property Row is hidden, and the unlimited value has been set.

### [GeneXus activation](#GeneXus+activation)

Execute GeneXus with the */install* option and make sure it is available.


|  |
| --- |
| **Backlinks** |
| [Creating Item User Controls for iOS](https://wiki.genexus.com/commwiki/wiki?15828) | [Creating List User Controls for iOS](https://wiki.genexus.com/commwiki/wiki?15827) | [Creating User Controls for Android](https://wiki.genexus.com/commwiki/wiki?18674) |
| [Creating User Controls for Apple](https://wiki.genexus.com/commwiki/wiki?18330) | [HowTo: Compile Android's FlexibleClient](https://wiki.genexus.com/commwiki/wiki?29656) | [Category:User Controls for Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?15301) |

---
