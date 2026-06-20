---
title: "Creating List User Controls for iOS"
source_id: 15827
source_url: https://wiki.genexus.com/commwiki/wiki?15827
genexus_version: "18"
---

# Creating List User Controls for iOS

The purpose of this document is to explain how to create a user control for Smart Devices, in this particular case, a user control for iOS.

What are e going to create?

We will create an image gallery from a given list of images. The image gallery will display a thumbnail image of the original image and when a certain image is selected, the original image will be displayed instead of the gallery along with a message showing a description.

After completing this step by step guide you will have a new user control named "ImageGallery" available in Work With for Smart Devices Pattern.

`[imagen omitida: wiki id 15831]` `[imagen omitida: wiki id 15832]` `[imagen omitida: wiki id 15833]`

## [Software Requirements](#Software+Requirements)

To develop user controls for iOS you'll need the following:

* Intel-based Mac running Mac OS X Snow Leopard or later
* XCode

## [Basic Steps](#Basic+Steps)

A list of steps to create the user control (with the basic functionality) is detailed below.

Create the [user control definition](https://wiki.genexus.com/commwiki/wiki?18338) and make sure it is available in GeneXus.

### [Project setup](#Project+setup)

In XCode, create a new *Cocoa Touch Static Library* project and there a new class named *UCImageGalleryList*.  
Make the new class a subclass of *GXControlGridBase*. This provides most of the functionality for a List User Control.

Get the [KTPhotoBrowser](https://github.com/kirbyt/KTPhotoBrowser) project from GitHub, and add the files to the project.  
The files needed are located under src/KTPhotoBrowser, plus the ones at src/Flickr+JSONSample/Flickr+JSONSample with names KTPhotoView+SDWebImage.\* and KTThumbView+SDWebImage.\*  
We'll need to make some small changes to this files in order to make the user control work.  
Rename the *SDWebImageManager* class to *SDWebImageManager2* not to clash with the GeneXus User Control internal implementation within the [SD ImageGallery control](https://wiki.genexus.com/commwiki/wiki?15308,,). Make sure the project compiles, you will have to change internal references (use a find/replace strategy).

Add the *GXFlexibleClient.framework* located on the /Users/MacUserName/Library/Artech/GeneXus to the project.

Add the following classes to the project:

* *UCImageGalleryList* class.
* *UCImageGalleryDataSource* protocol.
* UCImageGalleryDetail class

Check the complete source code [here](https://wiki.genexus.com/commwiki/wiki?18405,,).

Now, you have to make some changes to the *KTPhotoBrowser* files, *KTPhotoBrowserDataSource*, add the methods:

```
- (NSString *)titleForImageAtIndex:(NSInteger)index;
- (NSString *)captionForImageAtIndex:(NSInteger)index;
- (void) presentDetailViewForPhotoAtIndex:(NSUInteger) index;
```

the *KTPhotoScrollViewCntroller* class, add an iVar

```
UIBarStyle navbarPreviousStyle_
```

set it in *viewWillAppear* (see how it is done with *navbarWasTranslucent\_*, set the navigation bar style to black translucent there, and remember to set it back to what it was in *viewWillDisappear*.

add the method

```
- (void) presentDetailViewForPhotoAtIndex:(NSUInteger) index;
```

with the following implementation:

```
- (void) presentDetailViewForPhotoAtIndex:(NSUInteger)index {
    [self showChrome];
    [dataSource_ presentDetailViewForPhotoAtIndex:index];
}
```

Modify the *KTThumbsViewController* class, repeating the same with the iVar navbarPreviousStyle\_ from *KTPhotoScrollViewController* (see above)

create an iVar

```
UINavigationController *navController;
```

@synthesize it, and add the getter with the following code:

```
- (UINavigationController *) navController {
    if (self->navController) {
        return self->navController;
    }
    else {
        return [self navigationController];
    }
}
```

replace all the references to

```
[self navigationController]
```

with

```
[self navController]
```

Finally, make sure the project compiles.

Add a new target to generate a [library](https://wiki.genexus.com/commwiki/wiki?18088,,) and deploy your control as a *.a* file.

Once you have got the *.a* file associated to the User Control you are ready to copy it to the GeneXus User Control folder and start using it.


|  |
| --- |
| **Backlinks** |
| [Creating User Controls for Apple](https://wiki.genexus.com/commwiki/wiki?18330) | [Category:User Controls for Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?15301) |

---
