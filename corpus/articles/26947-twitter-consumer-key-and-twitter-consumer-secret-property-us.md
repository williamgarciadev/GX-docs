---
title: "Twitter Consumer Key and Twitter Consumer Secret property using GAM"
source_id: 26947
source_url: https://wiki.genexus.com/commwiki/wiki?26947
genexus_version: "18"
---

# Twitter Consumer Key and Twitter Consumer Secret property using GAM

In IOS platform the [Twitter Authentication Type](https://wiki.genexus.com/commwiki/wiki?17208) is performed using the credentials of the user in the device. That is, the login is done using the Twitter account of the user in the device.

These properties are available for each main SD object, under "Main object properties".

### [Values](#Values)

The Twitter Consumer Key and Twitter Consumer Secret values have to be taken from the configuration of the Twitter Application in Twitter developers site. See [Twitter Authentication Type](https://wiki.genexus.com/commwiki/wiki?17208) for details.

The values for these properties specified in the main SD object have to be the same of those configured in the GAM Authentication type.

### [Example](#Example)

Firstly you need to get the Consumer Key and Consumer Secret values in the Twitter developers site, and configure the GAM Authentication type:

`[imagen omitida: wiki id 26949]`

Secondly, configure the main SD object with the same values for Twitter Consumer Key and Twitter Consumer Secret properties:

`[imagen omitida: wiki id 26950]`

Afterwards, for IOS platforms, the Twitter login will be done using the local Twitter account.

If the Twitter account exists, the user will be asked for permissions to access this account.

`[imagen omitida: wiki id 26951]`

On the other hand, if the account does not exist, he will be prompted to define an account in the device. The message is **"No accounts. Please configure a twitter account in settings.app"**.

### [Note](#Note)

If you do not configure any of these properties (Consumer Key and Consumer Secret), you'll get the following error message: **CRASH: You must enter your consumer key**.

### [Availability](#Availability)

As of GeneXus Evolution 3, it is available for IOS using Net and Ruby generator. In other cases, the Twitter login is done in the Twitter web site.

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Objects:** | [Dashboard](https://wiki.genexus.com/commwiki/wiki?16321), [Smart Devices Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With pattern and Work With object](https://wiki.genexus.com/commwiki/wiki?15974) |
| **Generators:** | [Apple](https://wiki.genexus.com/commwiki/wiki?14917) |


|  |
| --- |
| **Backlinks** |
| [GAM - Twitter Authentication Type](https://wiki.genexus.com/commwiki/wiki?17208) |

---
