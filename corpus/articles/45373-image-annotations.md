---
title: "Image Annotations"
source_id: 45373
source_url: https://wiki.genexus.com/commwiki/wiki?45373
genexus_version: "18"
---

# Image Annotations

Draws traces on images.  
  
You can store only the trace made on an image, or store the image together with the annotations.  
  
This control cannot be placed inside Grids because they generate a Scroll, and when a trace is drawn on the scroll axis the event triggered will be the scroll and not the trace.

## [**Properties**](#Properties)

[Trace Color property](https://wiki.genexus.com/commwiki/wiki?45382)

[Trace Thickness property](https://wiki.genexus.com/commwiki/wiki?45381)

## [**Methods**](#Methods)

### [**GetAnnotatedImage**](#GetAnnotatedImage)

It stores the modified image along with the annotations.

```
&ResultImage = &AnnotationImage.GetAnnotadeImage()
```

### [**GetAnnotations**](#GetAnnotations)

It stores only the annotations made on an image.

```
&AnnotationsImage = &AnnotationImage.GetAnnotations()
```

### [**Undo**](#Undo)

It undoes the last trace made. The trace is taken from the moment you press on the device screen until you release it.

```
&AnnotationImage.Undo()
```

### [**Redo**](#Redo)

It redraws the last trace discarded by the previous Undo.

```
&AnnotationImage.Redo()
```

**Note:**

In both cases, when a new trace is made, the trace history changes.

## [**Sample**](#Sample)

A car rental company uses an application for the rental process. When the car is delivered, it is checked by both the supervisor and the client, so that both of them try to find any scratches or dents before the client takes the car out on the street. That way the supervisor will record anything that might be found.

This example will show the steps to follow to design a screen like the one shown below, using several of the methods provided by the control:

`[imagen omitida: wiki id 45376]`    `[imagen omitida: wiki id 45377]`

Step 1:   
  
Create a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829), and drag an [Attribute/Variable](https://wiki.genexus.com/commwiki/wiki?6911) based on the [Image data type](https://wiki.genexus.com/commwiki/wiki?15204) to the Main Table. Set the image [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) to "Image Annotations."

`[imagen omitida: wiki id 46429]`

Step 2:

Enter some images that will allow you to indicate the thickness of the trace, and to delete and recover the traces made. Schedule the following events for these images.

`[imagen omitida: wiki id 45388]`

```
Event Start
    &CarImage.FromImage("ExampleImageCar")
Endevent

// They configure the thickness (in dips) of the traces to be drawn on the background image.
Event ImageNarrowLine.Tap
    &CarImage.TraceThickness = 1
Endevent
Event ImageWideLine.Tap
    &CarImage.TraceThickness = 3
Endevent

// It undoes the last trace drawn by the user.
Event ImageUndo.Tap
    &CarImage.Undo()
Endevent

// It redraws the last trace discarded by the previous Undo.
Event ImageRedo.Tap
    &CarImage.Redo()
Endevent
```

Step 3:

Lastly, add some images with the colors available for the trace. Program the Tap events for each of the colors. This way you can change the color of the trace at runtime.

`[imagen omitida: wiki id 45389]`

```
// They configure the different colors for the traces.
Event ImageBlack.Tap
    &CarImage.TraceColor = rgb(0,0,0)
Endevent
Event ImageRed.Tap
    &CarImage.TraceColor = rgb(249,104,104)  
Endevent
Event ImageBlue.Tap
    &CarImage.TraceColor = rgb(94,169,231)  
Endevent
Event ImageGreen.Tap
    &CarImage.TraceColor = rgb(164,220,141) 
Endevent
Event ImageMustard.Tap
    &CarImage.TraceColor = rgb(255,217,87)  
Endevent
```

The application will then be programmed to meet the proposed scenario:

`[imagen omitida: wiki id 45395]`

Download Sample: [Sample SD Annotations](https://wiki.genexus.com/commwiki/wiki?47155,,)

## [**Scope**](#Scope)

**Generators:** iOS, Android.

## [**Availability**](#Availability)

This external is available only for iOS as of [GeneXus 16 upgrade 9](https://wiki.genexus.com/commwiki/wiki?45275,,).

This external is available for Android as of [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/wiki?45624,,).

## [**See also**](#See+also)

[Trace Thickness property](https://wiki.genexus.com/commwiki/wiki?45381)

[Trace Color property](https://wiki.genexus.com/commwiki/wiki?45382)


|  |
| --- |
| **Backlinks** |
|
| [Trace Color property](https://wiki.genexus.com/commwiki/wiki?45382) | [Trace Thickness property](https://wiki.genexus.com/commwiki/wiki?45381) |

---
