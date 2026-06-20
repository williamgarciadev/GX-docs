---
title: "Creating Item User Controls for iOS"
source_id: 15828
source_url: https://wiki.genexus.com/commwiki/wiki?15828
genexus_version: "18"
---

# Creating Item User Controls for iOS

In this document we'll explain how to create an *Item* User Control for iOS to display the contents of an attribute or variable.

To do this, we are going to create a Star Rating User Control, that displays a numeric field as a list of stars; very similar to the GeneXus [SD StarRating](https://wiki.genexus.com/commwiki/wiki?18350).

This is how it looks in execution:

`[imagen omitida: wiki id 15829]` `[imagen omitida: wiki id 15830]`

## [Software requirements](#Software+requirements)

To develop user controls for iOS you'll need the following:

* a Mac
* XCode

## [Steps to create the user control](#Steps+to+create+the+user+control)

The user control has two components: a definition and an implementation.

The definition is similar to the definition of the web user controls, with some minor differences.

For the implementation, you'll need to program in XCode, using the Objective-C language. This document asumes you are familiar with both.

### [Definition](#Definition)

For the definition of the control, you can start by copying an existing control definition

What you'll need to do is:

* Change the User Control name and description; for example *UCStarRating*.
* Set the Version tag to an initial value.
* Set the Platform to "SmartDevices".
* Add a File to the iOS\_SupportFiles, with the name of the library (for example: libUCStarRating.a); this is the library containing the implementation of your user control.

```
<iOS_SupportFiles>
<File>libUCStarRating.a</File>
  </iOS_SupportFiles>
```

* Add the name of the main class to the iOS\_ClassName tag (in this case, UCStarRating)

```
<iOS_ClassName>UCStarRating</iOS_ClassName>
```

Check the *Rating.control* file if you are in doubt.

### [Implementation](#Implementation)

* For this control, we will be using the *DLStarRatingControl* that can be found at <https://github.com/dlinsin/DLStarRating>, so go grab a copy of it.  
   - There are a few changes you need to do in order to make it work.  
  Rename the *DLStarRatingControl* class to *DLStarRatingControl2*, and *DLStarView* class to *DLStarView2* not to clash with the GeneXus User Control internal implementation. Make sure the project compiles, you will have to change internal references (use a find/replace strategy).  
  Then, In *DLStarRatingControl2.m*, go to the *-endTrackingWithTouch:withEvent:* method, add the following line:

```
[self sendActionsForControlEvents:UIControlEventValueChanged];
```

* Create a new XCode *Cocoa Touch Static Library* project called *UCStarRating* and  
   - import the *GXFlexibleClient.framework* located on the */Users/MacUserName/Library/Artech/GeneXus*  
   - import the *DLStarRating* project downloaded. Locate the xcodeproj associated project and drag it and drop it onto the root of your Xcode project's "Groups and Files" sidebar. A dialog will appear -- make sure "*Copy items*" is unchecked and "*Reference Type*" is "*Relative to Project*" before clicking "*Add*".
* Create a new class and name it *UCStarRating*. Make it subclass of *GXControlEditableWithLabelSingleEditorViewBase*  
   - you will need to import <GXFlexibleClient/GXFlexibleClient.h>  
   - add two properties: *maxValue* and *step* (both of type int)  
   - the *UCStarRating.h* header file should look like this:

```
#import <Foundation/Foundation.h>
#import <GXFlexibleClient/GXFlexibleClient.h>
@interface UCStarRating : GXControlEditableWithLabelSingleEditorViewBase {
    float _maxValue;
    float _step;
}
@property (nonatomic, readonly) float maxValue;
@property (nonatomic, readonly) float step;
@end
```

* Go to the implementation file, add a private property named *starRatingControl* of type *DLStarRatingControl2* (remember to import the h file)
* Synthesize the "delegate" property, that has been declaren in *GXControlEditableWithLabelSingleEditorViewBase*. This object will be used to notify the creator of the control of value changes.

```
@synthesize maxValue = _maxValue, step = _step;
```

* Implement the *GXControlEditableWithLabelSingleEditorViewBase* abstract methods

```
- (UIView *)newEditorViewWithFrame:(CGRect)frame {
    if ([self properties]) {
        _maxValue = [[self properties] getPropertyValueInteger:@"@UCStarRatingMaxValue"];
        _step =     [[self properties] getPropertyValueInteger:@"@UCStarRatingStep"];
    }
    else {
        _maxValue = 5;
        _step = 1;
    }
    
    int cantStars = CalculateNumberOfStars(_maxValue, _step);    
    DLStarRatingControl2 *control = [[DLStarRatingControl2 alloc] initWithFrame:frame andStars:cantStars isFractional:NO];
    control.rating = 3;
    [control setAutoresizingMask:UIViewAutoresizingFlexibleWidth|UIViewAutoresizingFlexibleHeight];
    [control setContentVerticalAlignment:UIControlContentVerticalAlignmentCenter];
    [control addTarget:self action:@selector(valueChangedForControl:) forControlEvents:UIControlEventValueChanged];
    [control setEnabled:self.enabled && !self.readOnly];
    return control;
}

- (void)valueChangedForControl:(id)sender {
    if ([sender isEqual:self.starRatingControl]) {
        int val = self.starRatingControl.rating * self.step;
        if (val > self.maxValue)
            val = self.maxValue;
        
        id<gxentitydata> entityData = [self entityData];
        
        if ([entityData conformsToProtocol:@protocol(GXMutableEntityData)]) {
            id fieldValue = [GXEntityHelper coreDataFieldValueFroFieldInfo:[[self fieldDescriptor] entityDataFieldInfo]
                                                                 fromValue:[NSNumber numberWithInt:val]
                             ];
            [(id<gxmutableentitydata>)entityData setValue:fieldValue forEntityDataField:[self fieldDescriptor]];
        }
    }
}

#pragma mark - GXControlEditableWithLabelBase overrides 

- (void)setReadOnly:(BOOL)readOnly {
    [super setReadOnly:readOnly];
    if ([self isEditorViewLoaded]) {
        [self.starRatingControl setEnabled:!readOnly && self.enabled];
    }
}

- (void)setEnabled:(BOOL)enabled {
	[super setEnabled:enabled];
	if ([self isEditorViewLoaded]) {
		[self.starRatingControl setEnabled:enabled && !self.readOnly];
	}
}

- (void)loadEntityDataFieldValue {
	int value = [self.entityDataFieldValue respondsToSelector:@selector(intValue)] ? MAX(0, [self.entityDataFieldValue intValue]) : 0;
	[self.starRatingControl setRating:CalculateNumberOfStars(value, self.step)];
}

+ (BOOL)isValidForDataType:(GXDataType)dataType {
    return (dataType == GXDataTypeNumeric);
}
</gxmutableentitydata></gxentitydata>
```

* Override the necessary GXControlWithLabelBase methods

```
- (DLStarRatingControl2 *)starRatingControl {
   return (DLStarRatingControl2 *)[self loadedEditorView];
}

+ (BOOL) isValidForDataType:(GXDataType)dataType {
    return (dataType == GXDataTypeNumeric);
}

- (DLStarRatingControl *) starRatingControl {
    return (DLStarRatingControl *) [super editorView];
}
```

* Define the *CalculateNumberOfStars* method:

```
static int CalculateNumberOfStars(int value, int step) {
    if (step == 0) return 0;
    return (value / step) + (value % step == 0 ? 0 : 1);
}
```

* create a bundle (DLImages.bundle) to locate the used images

`[imagen omitida: wiki id 27048]`

* Change the following lines in DLStarRatingControl2.m from:

```
star = [[UIImage imageNamed:@"star.png"] retain];    
highlightedStar = [[UIImage imageNamed:@"star_highlighted.png"] retain];
```

to:

```
star = [GXUtilities imageNamed:@"star.png" inBundle:@"DLImages"];
highlightedStar = [GXUtilities imageNamed:@"star_highlighted.png" inBundle:@"DLImages"];
```

* Make sure your library compiles.
* Copy the *libUCStarRating.a* file generated and bundles if needed and define the [GeneXus User Control](https://wiki.genexus.com/commwiki/wiki?18338).


|  |
| --- |
| **Backlinks** |
| [Creating User Controls for Apple](https://wiki.genexus.com/commwiki/wiki?18330) | [Category:User Controls for Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?15301) |

---
