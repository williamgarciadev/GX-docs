---
title: "BlurredImage: sample User Control for iOS"
source_id: 32558
source_url: https://wiki.genexus.com/commwiki/wiki?32558
genexus_version: "18"
---

# BlurredImage: sample User Control for iOS

## [Introduction](#Introduction)

This document shows with an example, how to create a (very simple) User Control for iOS.

This is not a complete guide on how to create a User Control. It is intended only as an example, to make it easier to get started.

## [Creating the control definition](#Creating+the+control+definition)

To create the User Control definition, it is highly recommended to use the [User Control Generator](https://wiki.genexus.com/commwiki/wiki?32550).

After you install the tool, you can go to [Atom](https://wiki.genexus.com/commwiki/wiki?32559,,) and create the project through *Packages > GeneXus > Create User Control*.  
For this sample, you must ensure that *Type* has value "Attribute & Variable" and *Supported Platforms* with "SmartDevices" (as shown below).

`[imagen omitida: wiki id 32958]`

There is not much to do after that because the control is pretty simple.  
In the *BlurredImage.control* file, the only thing you need to do is replace the empty tags for iOS\_SupportFiles, iOS\_ReferencedFiles and iOS\_ClassName with the following:

```
<iOS_SupportFiles>
       <File>iphoneos\BlurredImage.framework.gxzip</File>
       <File>iphonesimulator\BlurredImage.framework.gxzip</File>
</iOS_SupportFiles>
<iOS_ReferencedFiles>
        <File embed="true">./UserControls/$(PLATFORM_NAME)/BlurredImage.framework</File>
</iOS_ReferencedFiles>
<iOS_ClassName>GXUCBlurredImage</iOS_ClassName>
```

Then, in the properties file (*BlurredImageProperties.xml*), you need to tell the control that it is available for Image attributes, by setting the FlagDataTypeFilter to image.

## [User control implementation](#User+control+implementation)

To implement the User Control, you'll have to use the [Framework template](https://wiki.genexus.com/commwiki/wiki?32508).

When you reach the section ***Implement your User Control or External Object***, you'll have to provide the actual implementation.

To do that:

1. Create a new Swift file named GXUCBlurredImage.

2. Copy and paste the following code:

```
import Foundation
import GXCoreUI

@objc(GXUCBlurredImage)
public class GXUCBlurredImage: GXControlImage {
    public override func newEditorViewWithFrame(frame: CGRect) -> UIView {
        let editorView = super.newEditorViewWithFrame(frame)
        
        // the call to super.newEditorViewWithFrame(frame) creates the imageView
        if let imageView = self.imageView {
            let blurEffect = UIBlurEffect(style: .Dark)
            let blurEffectView = UIVisualEffectView(effect: blurEffect)
            blurEffectView.frame = editorView.bounds
            blurEffectView.autoresizingMask = [.FlexibleWidth, .FlexibleHeight]
            blurEffectView.userInteractionEnabled = false
            
            imageView.addSubview(blurEffectView)
            imageView.sendSubviewToBack(blurEffectView)
        }
        return editorView
    }
}
```

The code is pretty simple. A few things to note:

* We are subclassing GXControlImage, which in turn is a subclass of GXControlEditableWithLabelSingleEditorViewBase, which should be the base class of every Attribute User Control.
* We are overriding the implementation of the method newEditorViewWithFrame(frame:), calling the super version and returning it's result, but first we add the blur effect to the image view.
* The @objc() declaration is required, otherwise the implementation won't be found by the Flexible Client.

3. Continue with the [Framework template for iOS User Controls or External Objects](https://wiki.genexus.com/commwiki/wiki?32508) document to build the framework.

## [Deployment](#Deployment)

If you followed the steps in the [Framework template for iOS User Controls or External Objects](https://wiki.genexus.com/commwiki/wiki?32508) document, then you are all set.

Make sure you copied the .framewors to your User Control folder, build in debug or release mode in Atom, and test the User Control in GeneXus as you would normally do with any other User Control.


|  |
| --- |
| **Backlinks** |
| [Creating User Controls for Apple](https://wiki.genexus.com/commwiki/wiki?18330) |

---
