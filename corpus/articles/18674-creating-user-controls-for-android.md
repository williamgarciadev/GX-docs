---
title: "Creating User Controls for Android"
source_id: 18674
source_url: https://wiki.genexus.com/commwiki/wiki?18674
genexus_version: "18"
---

# Creating User Controls for Android

In a few steps, to create User controls for the [Android platform](https://wiki.genexus.com/commwiki/wiki?14453) you will have take care of the following issues.

1. Create the Control Definition in GeneXus so it will be available on the toolbox.
2. Implement the control in the Target platform; you need to create an Android Studio project.
3. Create a [library](https://wiki.genexus.com/commwiki/wiki?33546) definition to match the GeneXus control definition to the target implementation.

Follow the steps bellow

### [1. Control Definition in GeneXus](#1.+Control+Definition+in+GeneXus)

Follow the steps detailed in [Creating a User Control Definition for Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?18338) article to create a User Control definition for Smart Devices.

Execute GeneXus with the [/install](https://wiki.genexus.com/commwiki/wiki?6740) option and make sure it is available in the *Extension Manager* dialog.

Create a Smart Device object and bind an attribute or variable to the new User Control definition, generate the model.

The application will be deployed to the Android emulator, now you have to implement the User Control in the Androidplatform.

### [2. Implement the control in the Target Platform](#2.+Implement+the+control+in+the+Target+Platform)

To get your hands dirty and get an introduction to the Android framework you can check some of the Tutorials, for example:

* Go through the [tutorials](http://developer.android.com/resources/index.html)
* [Notepad Tutorial](http://developer.android.com/resources/tutorials/notepad/index.html)
* Check out an [open source app](http://code.google.com/p/apps-for-android/)

To get started from an existing sample check this [repository](https://github.com/genexuslabs/AndroidExtensionsSample).

There are two types of user control for smart devices: *Item* and *List*.

#### [Item User Controls](#Item+User+Controls)

* Deploy your Base Class which will subclass any *android.widget.\** class.
* The class must implement the *IGxEdit* interface from the *com.artech.controls* package. This means overiding the following methods:
  + *String getGx\_Value()*: Returns the value associated to this control in string format.
  + *void setGx\_Value(String value)*: Set the value associated to the control.
  + *String getGx\_Tag()*: return the *Tag* property as String, in general *return (String)this.getTag();*
  + *void setGx\_Tag(String tag)*: Set the Tag property as String, in general *this.setTag(stringData);*
  + *void setValueFromIntent(Intent data)*: if the user control implements a picker control, implement this method.
  + *void setEnabled(boolean enabled)*: Set the enabled state of the control.
  + *IGxEdit getListControl()*: Return the control reference; default implementation should return this.
  + *IGxEdit getViewControl()*: Return the control view reference; default implementation should return this.
  + *IGxEdit getEditControl()*: Return the control to use when editing; default implementation should return this.

For learning purposes check the following classes in the FlexibleClient  *com.artech.controls* and *com.artech.extendedcontrols* packages; all GeneXus standard controls are created internally as User Controls:

* GxButton
* RadioGroupControl
* GxCheckBox
* GxDateTimePicker
* GxEditText
* GxImage
* GxTextView
* SpinnerControl
* DynamicSpinnerControl
* SeekBarControl
* ScannerControl
* RatingControl
* GxWheelControl
* GxMeasuresControl
* GxSDGeoLocation

#### [List User Controls](#List+User+Controls)

* Deploy your Base Class which will subclass any android.widget.\* class.
* The class will have to implement the *IGridView* interface from the *com.artech.controls* package.
* This means overriding the following methods and implementing the *GridEventsListener* interface (Event handlers for requesting data, default action and buttons):
  + *void addListener(GridEventsListener listener)*: define the User Control listeners used to react to specific events.
  + *void update(ViewData data)*: populate the User Control with the data provided.
  + *public void requestMoreData()*: used to request more data, for example when scrolling.
  + *public boolean runAction(UIContext context, ActionDefinition action, Entity entity)*: execute an action associated to a grid item.
  + *public boolean runDefaultAction(UIContext context, Entity entity)*: execute the default action for the Grid.
* You can use the *GridHelper* class from the *com.artech.controls.grids* package, it contains common functionality for grid controls.
* When the User Control Constructor is executed with the following arguments *(Context context, LayoutItemDefinition def)* make sure to inflate your layout, for example:

```
LayoutInflater inflater = LayoutInflater.from(context);
     if (inflater != null)
        inflater.inflate(com.artech.R.layout.myusercontrol_layout, this, true);
```

* the *myusercontrol\_layout.xml* file will contain the layout to hold the list (XML markup).
* To access the control properties defined,  you can use helper methods from the *ControlInfo* class (*com.artech.base.metadata.layout* package):

```
ControlInfo info = layoutItemDefinition.getControlInfo();
controlItemValues = info.optStringProperty("@ControlItemValues"); //$NON-NLS-1$
controlItemDescription = info.optStringProperty("@ControlItemDescription"); //$NON-NLS-1$
addEmptyItem = info.optBooleanProperty("@AddEmptyItem");   //$NON-NLS-1$
emptyItemText = info.getTranslatedProperty("@EmptyItemText"); //$NON-NLS-1$
```

* Depending on your control, you may need to specialize the *BaseAdapter* class to populate your *View*. An Adapter object acts as a bridge between an AdapterView and the underlying data for that view. The Adapter provides access to the data items. The Adapter is also responsible for making a View for each item in the data set.  
  To define how each row should be inflated, getView is implemented in the custom adapter which inherits from [BaseAdapter](http://developer.android.com/reference/android/widget/BaseAdapter.html). A baseadapter is required if you don’t want to use anything that is provided by default in Android like *simple\_list\_item\_1*, *simple\_list\_item\_2*. You have to define how to iterate over the list by implementing following methods:
  + *public int getCount()*
  + *public Object getItem(int position)*
  + *public long getItemId(int position)*
* Define the method *getView*, where you will describe how to inflate the custom view, basically bind the data from the data structure (*UserControlName* class) to the view (*UserControlNameView* class).
  + *public View getView(final int position, View convertView, ViewGroup parent)*

For learning purposes check the following classes in the FlexibleClient  *com.artech.controls*, *com.artech.controls.grid* and *com.extensions.controls* packages:

* ImageGallery
* GxMapView
* GxMagazineViewer
* GxViewPager

Once you are done, make sure to execute *gradlew publishDebugPublicationToLocalRepository* to upload your implementation to a local repository used by GeneXus.  it is ready you need to execute

### [3. Create a Library](#3.+Create+a+Library)

Create a [library](https://wiki.genexus.com/commwiki/wiki?33546) definition to match the GeneXus control definition to the target implementation.

### [Samples](#Samples)

* [AndroidExtensionsSample](https://github.com/genexuslabs/AndroidExtensionsSample)

How To's

* [Creating Item User Controls for Android](https://wiki.genexus.com/commwiki/wiki?18712,,)
* [Creating List User Controls for Android](https://wiki.genexus.com/commwiki/wiki?18714,,)
* `[imagen omitida: wiki id 20668]`  [Develando los secretos para el desarrollo de estupendas extensiones Android para GeneXus 15](https://www5.genexus.com/meeting2016/gx26.search.aspx?Diana#es/Develando-los-secretos-para-el-desarrollo-de-estupendas-extensiones-Android-para-GeneXus)

### [See also](#See+also)

* [Android Flexible Client Deprecations](https://wiki.genexus.com/commwiki/wiki?48117,,)


|  |
| --- |
| **Backlinks** |
| [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Category:User Controls for Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?15301) |

---
