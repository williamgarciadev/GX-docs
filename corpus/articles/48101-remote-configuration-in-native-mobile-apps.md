---
title: "Remote Configuration in Native Mobile apps"
source_id: 48101
source_url: https://wiki.genexus.com/commwiki/wiki?48101
genexus_version: "18"
---

# Remote Configuration in Native Mobile apps

## [Introduction](#Introduction)

Being able to configure an application that has already been deployed, without modifying the code, is one important feature of GeneXus Native Mobile applications and that possibility has been around since the first version of the generator.

However easy it is to implement these remote configurations in GeneXus, it should be noted that there are tools (outside GeneXus) designed specifically for this task. One such tool is Firebase Remote Config.

One of these features is the one of Remote Config. What is it? As described by [the Firebase Remote Config’s documentation](https://firebase.google.com/docs/remote-config?hl=en):

> Firebase Remote Config is a cloud service that lets you change the behavior and appearance of your app without requiring users to download an app update. When using Remote Config, you create in-app default values that control the behavior and appearance of your app. Then, you can later use the Firebase console or the Remote Config backend APIs to override in-app default values for all app users or for segments of your user base. Your app controls when updates are applied, and it can frequently check for updates and apply them with a negligible impact on performance.

The key part of the Remote Config description, the one that is not easily solved with GeneXus, is this: “you can later use the Firebase console … to override in-app default values **for all app users or for segments of your user base**”. The user segmentation that Firebase can achieve is by far more complete than a custom solution a developer could manage to implement.

Note that you can still remotely configure any aspect of your app by coding the remote configuration directly in GeneXus. This is just another alternative to give the developer more power.

## [A/B testing](#A%2FB+testing)

Support of Remote Config is the sole requirement to also support A/B testing in your app with Firebase.

From [the Firebase page on A/B testing](https://firebase.google.com/docs/ab-testing?hl=en):

> A/B Testing helps you optimize your app experience by making it easy to run, analyze, and scale product and marketing experiments.

## [Common scenario](#Common+scenario)

The most common scenario for this feature is to have a set of application parameters that the developer will want to modify in runtime, and for some non-trivial user segmentation.

To achieve that, you'll have to provide a set of default valus, that is, values that will be used when they are not configured in the server or they have not been fetched yet.

The parameter fetching from the server will be performed mostly on application launch, but may also be performed at a given time interval. In some special cases.

Also applying the fetched parameters will be done at certain fixed moments. The most common case is at application launch so that the parameters don't change while the application is running. Another option is to apply them immediately after the parameters have been fetched from the server.

After the parameters have been fetched from the server and applyed locally, the application can read them by using getter functions.

### [Declarative vs. Imperative](#Declarative+vs.+Imperative)

Solving the most common scenario has been implemented in a declarative way so that no code is required to use this feature. That includes:

* defining the default values
* indicating when to fetch the values from the server
* indicating when the fetched values are applied
* providing a strongly-typed definition for the valid parameters

Besides providing the declarative solution, a custom, imperative solution is also provided to allow maximum flexibility.

## [Remote Configuration providers](#Remote+Configuration+providers)

A new property has been added to the Native Mobile Main objects, to indicate the desired remote configuration provider.

Note that the only provider implemented at this point is Firebase, but others may come in the future.

#### [[Remote Configuration Provider property](https://wiki.genexus.com/commwiki/wiki?48146)](#wiki%3F48146%2CRemote%2BConfiguration%2BProvider%2Bproperty+Remote+Configuration+Provider+property)

Provider to use for remotely configuring the mobile app, by using the RemoteConfig external object.

Values:

* None (default)
* Firebase

If the value **None** is selected, then this feature will be turned off.

### [Additional properties](#Additional+properties)

The following properties are available when the selected value for **Remote Configuration Provider** is different than **None**, in a section called "Remote Configuration Settings" inside the "Main object properties" section.

#### [[Default Values property](https://wiki.genexus.com/commwiki/wiki?48142)](#wiki%3F48142%2CDefault%2BValues%2Bproperty+Default+Values+property)

Provides the default values for the remote configuration parameters.

#### [[Fetching of Remote Values property](https://wiki.genexus.com/commwiki/wiki?48143)](#wiki%3F48143%2CFetching%2Bof%2BRemote%2BValues%2Bproperty+Fetching+of+Remote+Values+property)

Indicates how the values are fetched from the server.

Values:

* On Application Activation (default): the app will try to fetch the remote values every time it launches or returns from a background state, but only if the Minimum Fetch Interval (see below) has passed since the last successful fetch.
* After Elapsed Time: while the app is running, and after the Minimum Fetch Interval (see below) has passed since the last successful fetch, the app will try to fetch the values from the server.
* Manual: the app will not fetch the values automatically, it is up to the developer to add the corresponding code to perform the fetching.

#### [[Minimum Fetch Interval property](https://wiki.genexus.com/commwiki/wiki?48145)](#wiki%3F48145%2CMinimum%2BFetch%2BInterval%2Bproperty+Minimum+Fetch+Interval+property)

Indicates the minimum time that has to pass after a successful fetch, to perform a new automatic fetch (that is, when Fetching of Remote Values != Manual).

Value: An Integer value in minutes. Default value is 1.440 minutes (== 24 hours)

#### [[Application of Fetched Values property](https://wiki.genexus.com/commwiki/wiki?48144)](#wiki%3F48144%2CApplication%2Bof%2BFetched%2BValues%2Bproperty+Application+of+Fetched+Values+property)

Indicates when the fetched values should be applied.

Values:

* On Application Launch (default): the app will apply the fetched values, if any, when the application launches. If Fetching of Remote Values is set to On Application Activation, then the values are applied before fetching new values, meaning that the fetched values are applied on the next application launch.
* Immediately: the fetched values are applied immediately after the fetch finishes. The next read of these values will return the newly fetched value.
* Manual: values are not applied automatically, the developer is responsible for applying them.

## [[RemoteConfig external object](https://wiki.genexus.com/commwiki/wiki?48160)](#wiki%3F48160%2CRemoteConfig%2Bexternal%2Bobject+RemoteConfig+external+object)

This external object provides the functionality to be used by the application developer, to interact with the Remote Configuration Provider.

* Name: **RemoteConfig**
* Location: GeneXus.SD module.

This external object can be used in user events as well as in generated code (offline).

### [Properties](#Properties)

#### [LastSuccessfulFetch: DateTime](#LastSuccessfulFetch%3A+DateTime)

Indicates the timestamp of the last time the configuration was fetched successfully from the server.

Note: if the Remote Configuration Property is set to None, or if the values haven’t been fetched yet, it returns the empty DateTime. If the last fetch resulted in an error, the DateTime returned corresponds to the previous fetch.

Note: this property also takes into account fetch operations performed automátically.

#### [LastFetchStatus: Enum(FetchStatus) { None, Success, Failure }](#LastFetchStatus%3A+Enum%28FetchStatus%29+%7B+None%2C+Success%2C+Failure+%7D)

Returns the last fetch status.

Values:

* None: values have never been fetched from the server
* Success: the last fetch was successful
* Failure: the last fetch could not be completed.

Note: this property also takes into account fetch operations performed automátically.

### [Methods](#Methods)

#### [HasValue(key: String): Boolean](#HasValue%28key%3A+String%29%3A+Boolean)

Returns True if there is a value with the given key (being it a default value or a value fetched from the server), False otherwise.

#### [GetStringValue(key: String): String](#GetStringValue%28key%3A+String%29%3A+String)

Returns the configured value for the given key as a String.

Considerations:

* If the value has been fetched from the server, it returns that value. If not, the default value is returned. If there is no value from the server, nor a default value, the empty String is returned.
* If the Remote Configuration Provider is set to None, this method will return the empty string.

#### [GetIntegerValue(key: String): Numeric(9,0)](#GetIntegerValue%28key%3A+String%29%3A+Numeric%289%2C0%29)

Returns the configured value for the given key as a number without decimals.

Considerations: same consideration as from GetStringValue apply.

#### [GetDecimalValue(key: String): Numeric(12,4)](#GetDecimalValue%28key%3A+String%29%3A+Numeric%2812%2C4%29)

Returns the configured value for the given key as a number with decimals.

Considerations: same consideration as from GetStringValue apply.

#### [GetBooleanValue(key: String): Boolean](#GetBooleanValue%28key%3A+String%29%3A+Boolean)

Returns the configured value for the given key as boolean.

Considerations: same consideration as from GetStringValue apply.

#### [GetDateValue(key: String): Date](#GetDateValue%28key%3A+String%29%3A+Date)

Returns the configured value for the given key as a date.

Considerations: same consideration as from GetStringValue apply.

#### [GetDateTimeValue(key: String): DateTime](#GetDateTimeValue%28key%3A+String%29%3A+DateTime)

Returns the configured value for the given key as a date-time.

Considerations: same consideration as from GetStringValue apply.

#### [Fetch(): Boolean](#Fetch%28%29%3A+Boolean)

Tries to get the values synchronically from the server. Returns True if successful, False otherwise.

If the Remote Configuration Provider is set to None, this method returns False and finishes immediately.

#### [Apply(): Boolean](#Apply%28%29%3A+Boolean)

Tries to apply the values fetched by the last fetch operation (being it automatic or manual). Returns True if successful, False otherwise.

If the Remote Configuration Provider is set to None or if there are no fetched values, this method returns False and finishes immediately.

## [Examples](#Examples)

### [Before you start](#Before+you+start)

To use Firebase Remote Config, you'll have to first create a project in the [Firebase Console](https://console.firebase.google.com/), get the iOS and Android configuration files, and set them in your GeneXus KB.

Take a look at [Firebase Analytics Android File property](https://wiki.genexus.com/commwiki/wiki?41573) and [Firebase Analytics iOS File property](https://wiki.genexus.com/commwiki/wiki?41574,,) for more information.

### [Configuring values in the Firebase Console](#Configuring+values+in+the+Firebase+Console)

To add or change the properties' values in Firebase, go to the [Firebase Console](https://console.firebase.google.com/), select the appropriate project, and then search for Engage > Remote Config on the menu on the left.

There you can add or modify the values.

### [About the examples](#About+the+examples)

For this examples, suppose that you want to show some text inside a "box", and you want to be able to change the box's border and background color by applying certain Theme Classes. For that, you create three classes: RedBox, GreenBox and BlueBox with the appropriate colors, and also, define a remote-configuration property with name "box-class" that you can configure in the Firebase Console.

### [Fetch on app activation, Apply on app launch, change the class in the ClientStart event](#Fetch+on+app+activation%2C+Apply+on+app+launch%2C+change+the+class+in+the+ClientStart+event)

Leave the **Fetching of Remote Values** and **Application of Fetched Values** properties with their default values, add a default value in the **Default Values** property for "box-class".

Then, add the following code to the ClientStart event:

```
Event ClientStart
    composite
        &themeClassName = RemoteConfig.GetStringValue("box-class")
        ctlBox.class = &themeClassName
    endComposite
EndEvent
```

Note that:

* the first time the app launches, it will fetch the values from the server but it will not apply them
* the first time the ClientStart event is executed, the GetStringValue method will return the value defined in the **Default Values** property.
* the next time the app launches it will apply the fetched values and return the value configured in the Firebase Console (if any).

### [Fetch on app activation, Apply immediately, change the class in the ClientStart event](#Fetch+on+app+activation%2C+Apply+immediately%2C+change+the+class+in+the+ClientStart+event)

Leave the **Fetching of Remote Values** property with it's default value, set **Application of Fetched Values** to Immediately, add a default value in the **Default Values** property for "box-class".

Then, add the following code to the ClientStart event:

```
Event ClientStart
    composite
        &themeClassName = RemoteConfig.GetStringValue("box-class")
        ctlBox.class = &themeClassName
    endComposite
EndEvent
```

Note that:

* the first time the app launches, it will fetch the values from the server and it will apply them immediately
* the first time the ClientStart event is executed, the GetStringValue method will return the value fetched from the Firebase Console (if any), or it will fall back to the one defined in the **Default Values** property.

### [Manually Fetch and Apply values, change the class in the ClientStart event](#Manually+Fetch+and+Apply+values%2C+change+the+class+in+the+ClientStart+event)

Set **Fetching of Remote Values** property to Manual, set **Application of Fetched Values** to Manual, add a default value in the **Default Values** property for "box-class".

Then, add the following code to the ClientStart event:

```
Event ClientStart
    composite
        &themeClassName = RemoteConfig.GetStringValue("box-class")
        ctlBox.class = &themeClassName
    endComposite
EndEvent
```

Also add another event, somewhere in your app, like this:

```
Event 'FetchAndApply'
    composite
        &success = RemoteConfig.Fetch()
        if &success
            RemoteConfig.Apply()
        endif
    endComposite
EndEvent
```

Note that:

* no values will be fetched unless the 'FetchAndApply' event is executed.


|  |
| --- |
| **Backlinks** |
| [Application of Fetched Values property](https://wiki.genexus.com/commwiki/wiki?48144) | [Default Values property](https://wiki.genexus.com/commwiki/wiki?48142) | [Fetching of Remote Values property](https://wiki.genexus.com/commwiki/wiki?48143) |
| [Minimum Fetch Interval property](https://wiki.genexus.com/commwiki/wiki?48145) | [Remote Configuration Provider property](https://wiki.genexus.com/commwiki/wiki?48146) |
| [RemoteConfig external object](https://wiki.genexus.com/commwiki/wiki?48160) |

---
