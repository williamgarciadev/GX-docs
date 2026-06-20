---
title: "External Objects and User Controls for Smart Devices Compatibility in GeneXus 15"
source_id: 33547
source_url: https://wiki.genexus.com/commwiki/wiki?33547
genexus_version: "18"
---

# External Objects and User Controls for Smart Devices Compatibility in GeneXus 15

GeneXus #15 introduces the concept of a [Library](https://wiki.genexus.com/commwiki/wiki?33545) when developing External Objects or User Controls for Smart Devices.

The following are important comments to port your code to the new version.

## [Android](#Android)

The environment to develop native controls for Android is updated from Eclipse/Ant to Android Studio/Gradle.

The *FlexibleClient* component is not distributed as source file now it is compiled in a Module. To develop native controls you need to package your code in an Android Library and add it to GeneXus as third parties repository.

For more information check [Extension Library concept for Extending GeneXus for Native Mobile](https://wiki.genexus.com/commwiki/wiki?33545)

### [External Objects](#External+Objects)

There are two important changes to the implementation of External Objects.

The first is that the *execute()* method now returns an ***ExternalApiResult*** instead of a plain object. This class allows indicating both the actual returned value of the method (if any) and whether it succeeded or not. As a third option, it can also indicate that the call is *incomplete* (by returning *ExternalApiResult.SUCCESS\_WAIT*) -- this is necessary when the operation needs to wait for another activity (or user input) for completion, and therefore cannot simply block execution in order to do so.

The *catchOnActivityResult()* method was removed as a consequence of this change -- basically any EO that returned true for *catchActivityResult()* can simply return *SUCCESS\_WAIT* now.

The second difference is that since GeneXus 15 targets API level >= 23 (Android 6.0 Marshmallow) any External Objects that use system calls protected by permissions (such as reading contacts, accesssing the user's location, sending SMS, &c)  are responsible for requesting those permissions in runtime as well. You can either use the native Android calls (such as *ActivityCompat.requestPermissions()*) or via the *ExternalApi.executeRequestingPermissions()* method, which will take of the actual asking of the permission/checking its result for you.

Check the following samples on how to return values

```
// Correct execution
return new ExternalApiResult(ActionResult.SUCCESS_CONTINUE);
// Return a String
String data; // load it with the desired return value
return new ExternalApiResult(ActionResult.SUCCESS_CONTINUE, data);
```

### [External Object Helper methods](#External+Object+Helper+methods)

While not a breaking change per se, we've included a number of methods in the ExternalApi class to help reduce the amount of boilerplate in EO implementations. These are:

* *addMethodHandler*: registers an *IMethodInvoker* to handle a method with a particular name and number of parameters. The implementation for *IMethodInvoler.invoke()* must return an *ExternalApiResult* as described in the previous section.
* *addSimpleMethodHandler*: registers and *ISimpleMethodInvoker*. Unlike the previous option, *ISimpleMethodInvoker.invoke()* simply returns the actual output of the method. This is a simpler option when implementing methods that cannot actually fail or need to wait, so the *ExternalApiResult* mechanism is not really needed.
* *addMethodHandlerRequestingPermissions*: registers an *IMethodInvoker* that will be only executed if the specified permissions can be obtained when the EO method is called (or if the app already had them at that point). If this is not possible, the method call will fail, returning *ExternalApiResult.FAILURE*, and thus aborting the execution of the current Composite block.
