---
title: "HowTo: Include animations in Native Mobile and Angular apps"
source_id: 37189
source_url: https://wiki.genexus.com/commwiki/wiki?37189
genexus_version: "18"
---

# HowTo: Include animations in Native Mobile and Angular apps

GeneXus allows integrating animations when developing applications, more specifically, Lottie animations.

[Lottie](https://airbnb.io/lottie/#/) is an animation library created by Airbnb. It is highly flexible, allows creating any kind of animations, uses small files, and provides a JSON API to integrate the animations into mobile applications. With these JSON files, you can include the animations in a GeneXus Knowledge Base. Many design software tools provide export capabilities to *Lottie JSON format* files. In addition, there are several animation repositories (like  [Lottie Files](https://lottiefiles.com/)) with many animations in JSON files that can be downloaded.

### [Steps to add animations to the KB](#Steps+to+add+animations+to+the+KB)

To include the animations in the Knowledge Base, you need to do two things:

#### [1. Add the Lottie JSON files as a File object in the Knowledge Base.](#1.+Add+the+Lottie+JSON+files+as+a+File+object+in+the+Knowledge+Base.)

To create a [File object](https://wiki.genexus.com/commwiki/wiki?5852), select in the main GeneXus Menu: File > New > Object and a [New object dialog](https://wiki.genexus.com/commwiki/wiki?9931) will be displayed. Select File object from the list.

#### [2. Create Animation classes with Design System Object.](#2.+Create+Animation+classes+with+Design+System+Object.)

In Design System objects, you can create a class to add your animations to an application.

For example: the class called “Animation” where you set the Animation type, in this case, Lottie Animation Type.

```
.Animation
{
    gx-animation-type: idLottie;
}

.LoadingAnimation
{
    @include Animation;
    gx-lottie-file: gx-file(LottieAnimationLoading);
}
```

And a “LoadingAnimation” class that contains the “Animation” class and declares the jsonFile you want to add to your application.

After the Design system classes are created, the animation is ready to be included in the application.

### [Including the animation in the application](#Including+the+animation+in+the+application)

Now that the animations are included in the KB, you can integrate them into the application. There are four ways to make this integration:

#### [1. Animation View User Control](#1.+Animation+View+User+Control)

With the [Animation View User Control](https://wiki.genexus.com/commwiki/wiki?37185), an animation can be included on any screen of an application. The control provides methods that allow setting the animation and managing its execution and progress.

`[imagen omitida: wiki id 55730]`

```
Event ClientStart
   Composite
      AnimationView1.SetAnimation("LoadingAnimation", true)
      AnimationView1.Play()
   EndComposite
Endevent

Event 'PauseAnimation'
   AnimationView1.Pause()
EndEvent

Event 'SetProgress'
   Composite
      &Progress = 0.5
      AnimationView1.SetProgress(&Progress)
   EndComposite
EndEvent
```

#### [2. Customizing the loading of forms and grids](#2.+Customizing+the+loading+of+forms+and+grids)

It is possible to use animations to customize the loading process of object forms and grids. That is, you can replace the usual loading circle with a more sophisticated Lottie animation.

To do this, there is a property that can be set in the Styles section of a Design System Object, named gx-loading-animation-class.

The definition is as follows:

```
.Form

{
      gx-enter-effect: gx_default;
      gx-close-effect: gx_default;
      gx-call-type: gx_default;
      gx-target-size: gx_default;
      gx-target-width: 100%;
      gx-target-height: 100%;
      gx-content-size-change: gx_default;
      gx-input-view-appearance: gx_default;
      gx-loading-animation-class: Animation;
      gx-loading-animation-behavior: platform_default;
}
```

`[imagen omitida: wiki id 55731]`

#### [3. Customizing Progress Indicator controls](#3.+Customizing+Progress+Indicator+controls)

An animation can be used to customize a [Progress Indicator User Control](https://wiki.genexus.com/commwiki/wiki?31275). To do this, a [Progress theme class](https://wiki.genexus.com/commwiki/wiki?37765) has to be created and an Animation-type class name set in the [Animation Class property](https://wiki.genexus.com/commwiki/wiki?37707) of this class. The indicated animation will be displayed when the [Progress Indicator User Control](https://wiki.genexus.com/commwiki/wiki?31275) is shown.

It is important to ensure that the class assignment is done before showing the progress indicator. The code should be configured as follows:

```
GeneXus.Common.UI.Progress.Class="Progress"
GeneXus.Common.UI.Progress.Show()
```

`[imagen omitida: wiki id 37767]`

#### [4. Customizing the Launch Screen](#4.+Customizing+the+Launch+Screen)

It is possible to use an animation as the Launch Screen of your application. This can be set in the Styles section of a Design System Object.

```
.Application

{
     gx-background-image-mode: stretch;
     gx-image-loading-indicator: False;
     gx-launch-screen-animation-class: Animation;
}
```

### [Integrating Animations in Grids](#Integrating+Animations+in+Grids)

This section will guide you to integrate Lottie animations in grids using the Animation View control.

First, add the Lottie JSON files to the Knowledge Base, as explained above.

Next, set up the Grid and Animation View control. To do so, drag a Grid to the Layout of a Panel object, and then drag an Animation View control to that Grid:

`[imagen omitida: wiki id 58870]`

#### [Configuring the Load Event](#Configuring+the+Load+Event+)

Define the following in the Load Event of the Grid:

```
Event GridAnimations.Load
    AnimationView.SetAnimation("Animation1", True)
    AnimationView.Play()
    Load
    AnimationView.SetAnimation("Animation6", True)
    animationView.Play()
    Load
    AnimationView.SetAnimation("Animation4", True)
    animationView.Play()
    Load
    AnimationView.SetAnimation("Animation2", True)
    animationView.Play()
    Load
EndEvent
```

#### [Defining grid properties for styling the Grid and its elements](#Defining+grid+properties+for+styling+the+Grid+and+its+elements)

You can make the Grid display part of the next animation in a way that encourages the user to swipe, as shown below:

`[imagen omitida: wiki id 58872]`

To do so, define the following grid properties:

**Control Type property**: Grid  
**Scroll Direction property:** Horizontal  
**Snap to Grid property:** True

#### [Creating and assigning custom classes](#Creating+and+assigning+custom+classes)

In the Style section of a Design System Object (DSO), create custom classes to enhance the appearance of the Grid and its elements.

#### [Creating Grid Class](#Creating+Grid+Class)

Define a class named .GridAnimationExample to add padding to the animations within the Grid.

```
.GridAnimationExample {
    @include Grid;
    padding-right: 30;
    padding-left: 30;
}
```

Next, assign this class to the Class property of the Grid to apply the style.

#### [Creating the Grid Table Class](#Creating+the+Grid+Table+Class)

Define a class named .GridAnimationTable in the Style section of the DSO to add margins to the tables within the Grid:

```
.GridAnimationTable {
    @include GridContainer;
    margin-left: 5;
    margin-right: 5;
}
```

Next, assign this class to the Class property of the table containing the Grid elements.

**Note:** The classes used in this example with the @include rule refer to predefined styles that are part of the Unanimo DSO library in GeneXus.


|  |
| --- |
| **Backlinks** |
| [Animation Class property](https://wiki.genexus.com/commwiki/wiki?37707) | [Animation View User Control](https://wiki.genexus.com/commwiki/wiki?37185) | [Form theme-class for Smart Devices](https://wiki.genexus.com/commwiki/wiki?37648) |
| [Grid Theme class](https://wiki.genexus.com/commwiki/wiki?37657) | [Launch Screen Animation Class property](https://wiki.genexus.com/commwiki/wiki?37705) |
| [Table of contents:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Theme object Animation Class](https://wiki.genexus.com/commwiki/wiki?37939) |

---
