---
title: "Use Huawei In App Billing property"
source_id: 47543
source_url: https://wiki.genexus.com/commwiki/wiki?47543
genexus_version: "18"
---

# Use Huawei In App Billing property

Specifies if the application uses In-App Billing when generating for the Huawei platform.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974)  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Description](#Description)

Defines if the generated application will use the Huawei-specific In-App Purchases platform called [HUAWEI In-App Purchases (IAP)](https://developer.huawei.com/consumer/en/doc/development/HMSCore-Guides/android-config-agc-0000001050163815) to monetize your app.

When this property is enabled, remember to follow [these steps](https://developer.huawei.com/consumer/en/doc/development/HMSCore-Guides/config-agc-0000001050033072) to correctly configure the account and enable the [Merchant Service](https://developer.huawei.com/consumer/en/doc/start/merchant-service-0000001053025967). Once the process is approved, you need to:

* Update the [Huawei Services File property](https://wiki.genexus.com/commwiki/wiki?47545) with the correct *agconnect-services.json* configuration file.
* Configure the [Huawei In App Public Key property](https://wiki.genexus.com/commwiki/wiki?47544) with the provided value.

For testing purposes, you can add different HuaweiID users to the application [Sandbox Testing](https://developer.huawei.com/consumer/en/doc/development/HMS-Guides/iap-sandbox-testing-v4) environment, so no charges will be made to your credit card when purchasing products. The following warning message will appear before starting with the purchase process:

```
Sandbox test
This is a test. The system will skip the payment process without deducting any fees.
[OK]
```

### [Troubleshooting](#Troubleshooting)

#### [Null pointer exception on com.genexus.inappbillinglib.util.SkuDetails.getSku()](#Null+pointer+exception+on+com.genexus.inappbillinglib.util.SkuDetails.getSku%28%29)

The following error occurs when using the StoreManager PurchaseProduct method:

```
java.lang.NullPointerException: Attempt to invoke virtual method 'java.lang.String com.genexus.inappbillinglib.util.SkuDetails.getSku()' on a null object reference
        at com.genexus.inappbillinglib.StoreManager$3.invoke(StoreManager.java:137)
        at com.artech.externalapi.ExternalApi.invokeMethod(ExternalApi.java:276)
        at com.artech.externalapi.ExternalApi.execute(ExternalApi.java:70)
        at com.artech.actions.ApiAction.runExternalObjectMethod(ApiAction.java:76)
        at com.artech.actions.ApiAction.Do(ApiAction.java:57)
        at com.artech.actions.CompositeAction.Do(CompositeAction.java:119)
        at com.artech.actions.ActionExecution$2.doInBackground(ActionExecution.java:363)
        at com.artech.actions.ActionExecution$2.doInBackground(ActionExecution.java:352)
        at com.artech.utils.TaskRunner.lambda$executeOnExecutor$2(TaskRunner.java:22)
        at com.artech.utils.-$$Lambda$TaskRunner$epLfyblLY1hXkfy5GrschUD8-W0.run(Unknown Source:2)
        at java.util.concurrent.ThreadPoolExecutor.processTask(ThreadPoolExecutor.java:1187)
        at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1152)
        at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:641)
        at java.lang.Thread.run(Thread.java:784)
```

If you are executing on a device with Google Services, the Huawei configuration is not taken into account; configure the [Google In-App Billing](https://wiki.genexus.com/commwiki/wiki?21330) instead.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770). |

### [Availability](#Availability)

This property is available since [GeneXus 17 upgrade 2](https://wiki.genexus.com/commwiki/wiki?47418,,).

### [See Also](#See+Also)

[Main Platform property](https://wiki.genexus.com/commwiki/wiki?18657)  
[Huawei In App Public Key property](https://wiki.genexus.com/commwiki/wiki?47544)  
[Huawei Services File property](https://wiki.genexus.com/commwiki/wiki?47545)  
[StoreManager external object](https://wiki.genexus.com/commwiki/wiki?31320)


|  |
| --- |
| **Backlinks** |
| [Generate Huawei property](https://wiki.genexus.com/commwiki/wiki?47485) | [GeneXus support for Huawei Mobile Services Platform](https://wiki.genexus.com/commwiki/wiki?47484) | [Huawei In App Public Key property](https://wiki.genexus.com/commwiki/wiki?47544) |

---
