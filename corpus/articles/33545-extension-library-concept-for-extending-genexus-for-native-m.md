---
title: "Extension Library concept for Extending GeneXus for Native Mobile"
source_id: 33545
source_url: https://wiki.genexus.com/commwiki/wiki?33545
genexus_version: "18"
---

# Extension Library concept for Extending GeneXus for Native Mobile

The Extension Library concept is introduced in [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?28265,,) to simplify the development of extensions for Native Mobile.

### [Library concept](#Library+concept)

A Library is a way to group implementation details for some extension points such as [User Controls](https://wiki.genexus.com/commwiki/wiki?15301), [External Objects](https://wiki.genexus.com/commwiki/wiki?17880), and External Providers for Smart Devices. It consists of two main components:

* An XML-like file with extension *\*.**library* where the developer must list the extensibility components for each platform and their implementations.
* The binaries and any other dependent file needed for the implementation.

The *\*.**library* file defines tags with a special semantic:

* <ExtensionLibrary>...</ExtensionLibrary>  
  Root tag indicates the begin-end of the library file.
  + <*DependsOn*>...</*DependsOn*>

Declare the dependencies that are needed for the .library. Initially, only a node of <ExtensionLibrary>*ExtensionLibraryName*</ExtensionLibrary> type is allowed (where *ExtensionLibraryName* is a string with the name of the dependant extension library). For example, FirebaseAnalytics extension libraries could depend on a Firebase extension library, in which case the initialization code of Firebase is added.

* <Implements>...</Implements>  
  Lists whose components are implemented in the library.  
  The tags for its items must match the GeneXus object name. A few examples below:
  + <ExternalObject name="my\_external\_object" />  
    Refers to an External Object implementation.
    - <Method>MethodName</Method>  
      It is used to add a library extension when using a particular method of an external object. Available since [GeneXus 18 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?54242).
  + <UserControl name="my\_user\_control" />  
    Refers to a User Control implementation.
  + <NotificationProvider name="my\_notification\_provider" />  
    Refers to a [notification provider](https://wiki.genexus.com/commwiki/wiki?33670) implementation.
  + <CacheProvider name="my\_cache\_provider" />  
    Refers to a [cache provider](https://wiki.genexus.com/commwiki/wiki?31147) implementation.
  + <StorageProvider name="my\_storage\_provider" />  
    Refers to a [storage provider](https://wiki.genexus.com/commwiki/wiki?31121) implementation.
  + <Procedure name="my\_procedure\_name" />  
    Refers to a full-qualified name Procedure object implementation. Available since [GeneXus 16 Upgrade 11](https://wiki.genexus.com/commwiki/wiki?45901,,).

* <Android>...</Android>  
  Indicates the implementation of dependencies for the Android generator.  
  Also, it defines special tags.
  + <ModuleClass>...</ModuleClass>  
    Class instantiated at runtime responsible for mapping the extension to the components that use it. Optional\*.
  + <GroupId>...</GroupId>  
    Package group identifier for Maven repository where there are [AAR files](https://developer.android.com/studio/projects/android-library.html) that implement the library (with its transitive dependencies). Optional\*.
  + <Name>...</Name>  
    Name of the library in the Maven repository. Optional\*.
  + <Version>...</Version>  
    Version code of the library in the Maven repository. Optional\*.
  + <GradleExtensionFile>...<GradleExtensionFile>  
    Optional. A *\*.gradle* file for a library building. Use this option if you want to include external libraries' references.

**Note**: *Extension Libraries authors no longer have to add standard Maven repositories to their library definitions for Android because they're now included.* Therefore, since GeneXus 16 U5, it is no longer necessary to include this extension.

\* As of [GeneXus 17 upgrade 4](https://wiki.genexus.com/commwiki/wiki?47936,,) it's no longer necessary to add these values; now it is possible to create extension libraries without build.gradle dependencies.

<iOS>...</iOS>  
Indicates the implementation dependencies for the iOS generator.

**Attributes:** Platforms

Optional. It allows indicating the Apple platforms for which this extension is planned, separated by commas.

**Values:** iOS, tvOS, watchOS.

* <ModuleClass>...</ModuleClass>  
  Optional. Class instantiated at runtime responsible for mapping the extension to the components that use it. It is optional if the only component using the extension is a User Control.
* <PodFile>...</PodFile>  
  Optional. A [*\*.pod*](https://guides.cocoapods.org/using/the-podfile.html) complete filename for indicating the library dependencies.
* <XCProjExtensionFile>...</XCProjExtensionFile>  
  Optional. An XML filename for extending the generated XCode project.
* <CopyListFile>...</CopyListFile>  
  Optional. An XML filename which lists a set of files or directories to be copied to the generated project.
* ```
  <DisableBitcode>true</DisableBitcode>
  ```

  Optional. Use it to disable the Bitcode property if the project contains extensions that do not support it.
* Also, it defines special tags (details on [this](https://wiki.genexus.com/commwiki/wiki?36340) site).

## [Example](#Example)

For example, take the *\*.library* file defined as follows:

```
<ExtensionLibrary>
    <Implements>
       <UserControl name="MyUserControl"/> 
       <UserControl name="MyUserControlVariant"/>
       <ExternalObject name="MyExternalObject"/>
    </Implements>
    <Android>
        <GroupId>com.example</GroupId>
        <Name>MyExtension</Name>
        <Version>1.0</Version>
        <ModuleClass>com.example.MyExtensionLibraryClassName</ModuleClass>
        <GradleExtensionFile>mylibraryextension.gradle</GradleExtensionFile>
    </Android>
    <iOS>
        <PodFile>MyExtension.Template.pod</Library>
        <ModuleClass>MyExtensionLibraryClassName</ModuleClass>
        <XCProjExtensionFile>MyExtension.XCExtensionTemplate.xml</XCProjExtensionFile>
        <CopyListFile>MyExtension.CopyListTemplate.xml</CopyListFile>
    </iOS>
</ExtensionLibrary>
```

As we mentioned before, the <ModuleClass> tag references a class where each component is initialized.

The *mylibraryextension.gradle* file could add the following to reference the public repository; add whatever is needed:

```
repositories {
    jcenter()
}
```

### [Android initialization code sample](#Android+initialization+code+sample)

```
class com.mypackage.MyExtensionLibraryClassName {

    @Override
    public void initialize(Context context) {

         UserControlDefinition ucDefinition = new UserControlDefinition("MyUserControl", MyUserControl.class);
         UcFactory.addControl(ucDefinition);

         UserControlDefinition ucDefinition = new UserControlDefinition("MyUserControlVariant", MyUserControlVariant.class);
         UcFactory.addControl(ucDefinition);

         ExternalApiDefinition apiDefinition = new ExternalApiDefinition("Module.Example.MyExternalObject", MyExternalObject.class);
         ExternalApiFactory.addApi(apiDefinition);

         // Other components initialization.
    }
}
```

The Library itself details which component is implemented. The External Object does not need to fill the platform-specific parameters.

### [iOS initialization code sample](#iOS+initialization+code+sample)

```
@objc(MyExtensionLibraryClassName)
public class MyExtensionLibraryClassName: NSObject, GXExtensionLibraryProtocol {

    public func initializeExtensionLibrary(withContext context: GXExtensionLibraryContext) {

        GXActionExternalObjectHandler.register(MyGXActionExternalObjectHandlerSubclass.self, forExternalObjectName: "Module.Example.MyExternalObject")

        // Other components initialization, except for User Controls because GeneXus automatically generates the mapping by using the UC definition.

    }

}
```

Note that the implementation uses Swift language. In this case, the @objc(MyExtensionLibraryClassName)notation must be used in order to instantiate this class at runtime via reflection.

### [Availability](#Availability)

Android support as of [GeneXus 15 Upgrade 3](https://wiki.genexus.com/commwiki/wiki?33278,,).  
iOS support as of [GeneXus 15 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?35908,,).

### [See Also](#See+Also)

[User Controls for Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?15301)  
[External Objects for Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?17880)


|  |
| --- |
| **Backlinks** |
| [Alipay API](https://wiki.genexus.com/commwiki/wiki?37152) | [Creating an Extension Library for Android](https://wiki.genexus.com/commwiki/wiki?33546) | [Creating an Extension Library for iOS](https://wiki.genexus.com/commwiki/wiki?36340) |
| [External Objects and User Controls for Smart Devices Compatibility in GeneXus 15](https://wiki.genexus.com/commwiki/wiki?33547) | [External Objects for Android](https://wiki.genexus.com/commwiki/wiki?17878) | [Framework template for iOS User Controls or External Objects](https://wiki.genexus.com/commwiki/wiki?32508) |
| [GeneXusAI Module Overview](https://wiki.genexus.com/commwiki/wiki?40315) | [HowTo: Pay using Alipay in GeneXus applications](https://wiki.genexus.com/commwiki/wiki?37146) | [HowTo: Pay using WeChat Pay in GeneXus applications](https://wiki.genexus.com/commwiki/wiki?37321) |
| [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) | [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) | [WeChat Pay API](https://wiki.genexus.com/commwiki/wiki?37322) |

---
