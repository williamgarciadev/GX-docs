---
title: "External Objects for Android"
source_id: 17878
source_url: https://wiki.genexus.com/commwiki/wiki?17878
genexus_version: "18"
---

# External Objects for Android

Suppose you want to mimic the GeneXus msg method which shows a notification which automatically fades in and out.

You can create a [Native Object](https://wiki.genexus.com/commwiki/wiki?6148) within GeneXus; publish the desired method and properties to be called and do the implementation to integrate to the Android platform.

Below there is a walkthrough you can follow to create an External object for the [Android platform](https://wiki.genexus.com/commwiki/wiki?14453).

You will use [Toast Notifications](http://developer.android.com/guide/topics/ui/notifiers/toasts.html) for the Android platform which enables sending short and long toasts.

What steps should be followed to add this feature in GeneXus?

* Create an External object: this is the definition in GeneXus and your objects will call the properties, methods and events defined.
* Create an [Extension Library](https://wiki.genexus.com/commwiki/wiki?33545) implementing the neccesary code for the desired platform, in this case Android.

**Info**: There is a living code sample for the External Object in this document that can be found on GitHub. Take a look at [Native Mobile Extensions Repository Sample](https://wiki.genexus.com/commwiki/wiki?38277) .

### [Create an External Object](#Create+an+External+Object)

Create a **New Native Object** called **MyApi**; make sure to set the following property values:

|  |  |
| --- | --- |
| Android External name | MyApi |
| External Package Name | com.example.samplemodule1 |

1 - This value may change depending on the name used for your library; for this case you will add the component to [this](https://wiki.genexus.com/commwiki/wiki?38277) existing sample.

Add a new **method** called **ShortToast** with the following values:

|  |  |
| --- | --- |
| Is Static | True |
| External Member Type | Instance |

... and a character **parameter** using:

|  |  |
| --- | --- |
| Access Type | In |
| Type | VarChar, Length: 128 |

Add a second **method** called **LongToast** with the same parameters, the following figure details the desired result:

`[imagen omitida: wiki id 33541]`

Done! This is the declaration needed from the GeneXus perspective.

#### [Usage in GeneXus](#Usage+in+GeneXus)

Once you save the External Object, you can use it with the following syntax:

```
MyApi.ShortToast("Hello Toast!")
MyApi.LongToast(&myMessage)
```

Now, you have to do some implementation to get this External Object working.

### [Implementation](#Implementation)

The next step is to implement the **MyApi** class in a [Extension Library](https://wiki.genexus.com/commwiki/wiki?33545). If you want to get started from scratch check [Creating an Extension Library for Android](https://wiki.genexus.com/commwiki/wiki?33546).

#### [MyApi.Java](#MyApi.Java)

Create a new class **MyApi.java** on the package **com.example.samplemodule**:

```
package com.example.samplemodule;

import android.support.annotation.NonNull;
import android.widget.Toast;
import com.artech.base.services.Services;
import com.artech.externalapi.ExternalApi;
import com.artech.externalapi.ExternalApiResult;

import java.util.List;

public class MyApi extends ExternalApi
{
    // GeneXus API Object Name
    final static String NAME = "MyApi";

    // API Method Names
    private static final String METHOD_SHORT_TOAST = "shortToast";
    private static final String METHOD_LONG_TOAST = "longToast";

    public MyApi(ApiAction action) {
        addMethodHandler(METHOD_SHORT_TOAST, 1, mShortToast);
        addMethodHandler(METHOD_LONG_TOAST, 1, mLongToast);
    }

    @SuppressWarnings("FieldCanBeLocal")
    private final IMethodInvoker mShortToast = new IMethodInvoker() {
        @Override
        public @NonNull ExternalApiResult invoke(List<Object> parameters) {
            final String parValue = (String) parameters.get(0);
            sendToast(parValue,Toast.LENGTH_SHORT);
            return ExternalApiResult.SUCCESS_CONTINUE;
        }
    };

    @SuppressWarnings("FieldCanBeLocal")
    private final IMethodInvoker mLongToast = new IMethodInvoker() {
        @Override
        public @NonNull ExternalApiResult invoke(List<Object> parameters) {
            final String parValue = (String) parameters.get(0);
            sendToast(parValue,Toast.LENGTH_LONG);
            return ExternalApiResult.SUCCESS_CONTINUE;
        }
    };

    private void sendToast(final String value, final int duration)
    {
        Services.Log.debug(NAME,"Toast:'"+value+"' duration:"+duration); //$NON-NLS-1$
        getActivity().runOnUiThread(new Runnable() {
            @Override
            public void run() {
                Toast.makeText(getContext(),value,duration).show();
            }
        });
    }
}
```

#### [External Object methods](#External+Object+methods)

Declare your method handlers on the class constructor; you can use the following methods:

* addSimpleMethodHandler
* addMethodHandler
* addMethodHandlerRequestingPermissions

for this sample the **addMethodHandler** is used:

```
addMethodHandler(METHOD_SHORT_TOAST, 1, mShortToast);
addMethodHandler(METHOD_LONG_TOAST, 1, mLongToast);
```

Define the invoke method and detail the implementation detail; for the case you will need it for the **mShortToast** and **mLongToast** handlers:

```
@SuppressWarnings("FieldCanBeLocal")
private final IMethodInvoker mShortToast = new IMethodInvoker() {
    @Override
    public @NonNull ExternalApiResult invoke(List<Object> parameters) {
        final String parValue = (String) parameters.get(0);
        sendToast(parValue,Toast.LENGTH_SHORT);
        return ExternalApiResult.SUCCESS_CONTINUE;
    }
};
```

For further detail check [this article](https://wiki.genexus.com/commwiki/wiki?33546).

The method arguments for the invoke method are the following:

* **parameters:** list of parameters defined in the GeneXus External Object.

You must get the list of parameters for the method; do the casting needed and delegate to the code that implements the feature. When using basic data type arguments, you can use the toString method to get a list of String parameters:

```
final String parValue = (String) parameters.get(0);
```

For those cases, when you are using an SDT or SDT collection object, you will need to cast it to Entity or EntityList (package com.artech.base.model).

In relation to the **Toast** sample, the External Object defines the **ShortToast** and **LongToast** methods using string arguments; when executing **MyApi.ShortToast("Hello Toast!")** the following code will actually be executed:

```
private void sendToast(final String value, final int duration)
{
    Services.Log.debug(NAME,"Toast:'"+value+"' duration:"+duration); //$NON-NLS-1$
    getActivity().runOnUiThread(new Runnable() {
        @Override
        public void run() {
            Toast.makeText(getContext(),value,duration).show();
        }
    });
}
```

The **value** variable gets the "Hello Toast!" value and the **duration** parameter the Toast type (short or long) to execute. The final result is:

`[imagen omitida: wiki id 33540]`

#### [Initialization](#Initialization)

You need to initialize the External object, locate the **initialize** method from Module class and add the following:

```
ExternalApiDefinition mAPI = new ExternalApiDefinition(
        MyApi.NAME,
        MyApi.class
);
```

In this case, the **SampleModule.java** is being used because the class from the **AndroidExtensionSample** is being reused, and it defines it in the \Android\ModuleClass tag defined in the .library file.

```
<ModuleClass>com.example.samplemodule.SampleModule</ModuleClass>
```

#### [Declaration](#Declaration)

Locate the **GENEXUS\_HOME\Libraries\SampleLibrary\SampleLibrary.library** file and add a new value for the External Object under the **Implements** tag

```
<Implements>
    ...
    <ExternalObject name="MyApi"/>
    ...
</Implements>
```

Great, you finished the implementation section.

### [Compilation](#Compilation)

Execute the following command from your Android module location:

```
gradlew uploadArchives
```

After the process finished the library gets compiled and is copied to the **GENEXUS\_HOME\Android\m2Repository** location so it will be included in the next Android compilation. A successful build should look like the following:

```
>gradlew uploadArchives
:library:androidSourcesJar
...
:library:compileReleaseJavaWithJavac
Incremental compilation of X classes completed in Y secs.
...
:library:bundleRelease
:library:publishDebugPublicationToLocalRepository
BUILD SUCCESSFUL
```

Done! You are ready to test your Android **MyApi** External Object.

### [Considerations](#Considerations)

When using extension points; the [Knowledge Base navigator](https://wiki.genexus.com/commwiki/wiki?14974) utility is no longer a valid option because it does not contain the platform-specific code added via the defined extensibility points. For those cases use the APK file instead.

When calling an EO from an offline Procedure, a few conditions have to be taken into consideration:

* The methods of the EO have to be static.
* The names of the methods have to be the same as the ones defined in the EO: [https://wiki.genexus.com/commwiki/servlet/wiki?17880,External+Objects+for+Smart+Devices](https://wiki.genexus.com/commwiki/wiki?17880),

### [Compatibility](#Compatibility)

The article is valid since GeneXus #15 upgrade #3 or higher versions.

### [Troubleshooting](#Troubleshooting)

You can add log messages in your extension point to do some basic troubleshooting. For example, you could add the following line in the execute method to log the External Object method called:

```
android.util.Log.v("GeneXusApplication", "MyApi::"+method);
```

or you can use the **Services.Log** GeneXus Helper class from the package com.artech.base.services.Services

```
Services.Log.debug("GeneXusApplication", "MyApi::"+method); //$NON-NLS-1$
```

Check the [Android logging system](http://developer.android.com/guide/developing/tools/logcat.html) for the result; something similar to the following should appear:

```
V/GeneXusApplication(ProcessID): MyApi::ShortToast
```

### [Installation checklist](#Installation+checklist)

To deploy the external object to a GeneXus installation:

* Make sure you have set the following Environment variables; otherwise the project will not compile:
  + GENEXUS\_HOME to your Genexus installation directory.
  + ANDROID\_HOME to your Android SDK directory.
* Run the command **gradlew uploadArchives** from the Androild extension library location; for this case SampleModule.
* Copy the .library file to the GENEXUS\_HOME\Libraries\LibraryName\ folder; it added the MyAPI External object information.
* Import an xpz with the External Object definition and use it.
* Rebuild the Smart Devices objects.

### [See Also](#See+Also)

[Extension Library](https://wiki.genexus.com/commwiki/wiki?33545)  
[Android Flexible Client Deprecations](https://wiki.genexus.com/commwiki/wiki?48117,,)


|  |
| --- |
| **Backlinks** |
| [External Objects for Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?17880) | [External Objects with Type property 'Native Object'](https://wiki.genexus.com/commwiki/wiki?6148) | [External Objects with Type property 'Native Object' (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?56447) |
| [HowTo: Compile Android's FlexibleClient](https://wiki.genexus.com/commwiki/wiki?29656) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) |

---
