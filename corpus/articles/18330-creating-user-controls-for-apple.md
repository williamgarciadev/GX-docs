---
title: "Creating User Controls for Apple"
source_id: 18330
source_url: https://wiki.genexus.com/commwiki/wiki?18330
genexus_version: "18"
---

# Creating User Controls for Apple

To create a [User Control object](https://wiki.genexus.com/commwiki/wiki?39356) for Apple you will have to take care of several things.

Take into account that the User Control should be compatible with XCFramework.

### [Implement the control in the Target Platform](#Implement+the+control+in+the+Target+Platform)

* Create a *Dynamic Library* using the [framework template](https://wiki.genexus.com/commwiki/wiki?32508).

#### [Item User Controls](#Item+User+Controls)

* Deploy your Base Class which will subclass the *GXControlEditableWithLabelSingleEditorViewBase* class.
* Create new properties and synthesize them.
* Implement the *-newEditorViewWithFrame:* method to render your desired User Control layout.
* Implement the *GXControlEditableWithLabelSingleEditorViewBase* abstract methods.
* Override the necessary *GXControlWithLabelBase* methods.

#### [List User Controls](#List+User+Controls)

* Deploy your Base Class which will subclass the *GXControlGridBase* class.
* Implement the *-newGridViewWithFrame:* method, which will be called by the base class when loading the view; you will have to render your desired User Control layout.
* Create a public method to return your view:

```
- (UIMyView *)myView {
    return (UIMyView *)[self gridView];
}
```

* Access the control properties defined by implementing resolvers for each defined property. You can use helper methods such as the following:

```
- (NSString *)attributeName {
    return [ [self properties] getPropertyValueString:@"@MyUserControlNameAttributeName"];   
}
```

* Implement the *-reloadData:* method to load the User Control data from the GeneXus provider.
* Define the default action and other actions the user control should respond to.

#### [Packaging](#Packaging)

List and Item User Controls for Smar Devices implementations must be packaged as a Framework.

### [Control Definition in GeneXus](#Control+Definition+in+GeneXus)

Follow the steps detailed in: [Creating a User Control Definition for Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?18338).

Execute GeneXus with the /install option and make sure it is available in an object for Native Mobile application.

### [Deployment](#Deployment)

* Copy the User Control folder and paste it on other GeneXus installations.

**Note**: There is a living code sample of a basic User Control implementation that can be found on GitHub. Take a look at [Native Mobile Extensions Repository Sample](https://wiki.genexus.com/commwiki/wiki?38277).

### [Samples](#Samples)

Follow these links:

* [Creating Item User Controls for iOS](https://wiki.genexus.com/commwiki/wiki?15828)
* [Creating List User Controls for iOS](https://wiki.genexus.com/commwiki/wiki?15827)

Or check:

* Objective-C sample code on the [Assembla site](http://svn.assembla.com/svn/gxusercontrols/SmartDevices/iOS/).
* Swift code sample on the article [BlurredImage: sample User Control for iOS](https://wiki.genexus.com/commwiki/wiki?32558).

### [See also](#See+also)

* [iOS Flexible Client Deprecations](https://wiki.genexus.com/commwiki/wiki?48112,,)


|  |
| --- |
| **Backlinks** |
| [Background Modes property](https://wiki.genexus.com/commwiki/wiki?35408) | [Framework template for iOS User Controls or External Objects](https://wiki.genexus.com/commwiki/wiki?32508) |
| [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Category:User Controls for Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?15301) |

---
