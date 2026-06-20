---
title: "Parameter encryption on Dynamic calls"
source_id: 29842
source_url: https://wiki.genexus.com/commwiki/wiki?29842
genexus_version: "18"
---

# Parameter encryption on Dynamic calls

Applies to [GeneXus X Evolution 3 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?30520,,) and higher versions.

When invocating (using a [Call method](https://wiki.genexus.com/commwiki/wiki?16224) or link) a Web object ([Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Procedure](https://wiki.genexus.com/commwiki/wiki?6293) as HTTP) that receives parameters, their encryption depends on the [Encrypt URL Parameters property](https://wiki.genexus.com/commwiki/wiki?8068) value.

You can set this property at object or Environment level (this option is available to determine the default value for objects included in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836)).

If the called object has the [Encrypt URL Parameters property](https://wiki.genexus.com/commwiki/wiki?8068) set as **Session Key or Site Key**, the parameters will be encrypted. Otherwise, if the property is set to **No**, they won't.

### [What happens when you have Dynamics calls/links?](#What+happens+when+you+have+Dynamics+calls%2Flinks%3F)

At first, you don't know what object will be called, so you can't possibly infer the [Encrypt URL Parameters property](https://wiki.genexus.com/commwiki/wiki?8068) value.

Then, the default behavior is that dynamic calls are not encrypted.

However, that behavior can be changed using the config.gx file. Only one of the following entries can be added to the config.gx file, which means that the dynamic calls will be encrypted using Session or Site Key, respectively.

```
EncryptDynCalls=SESSION 
EncryptDynCalls=SITE
```

If none of these entries is included in the config.gx file, the behavior is the default (no encryption is done).

Tip: when using Call command and generating Java: remember to use fully qualified object name to be called. That is: to include package name before object name (e.g. "com.myapp.myobject").

#### [Compatibility Note](#Compatibility+Note)

From GeneXus X Evolution 3 Upgrade 4 until Upgrade 7, the [Encrypt URL Parameters property](https://wiki.genexus.com/commwiki/wiki?8068) value at Environment level used to be considered as a criterion to encrypt the dynamic calls. To keep the previous behavior use the config.gx file.

### [What about the [Expand Dynamic Calls Property](https://wiki.genexus.com/commwiki/wiki?8223,,)](#What+about+the+wiki%3F8223%2CExpand%2BDynamic%2BCalls%2BModel%2BProperty%2B%2528GeneXus%2B9.0%2529+Expand+Dynamic+Calls+Property+)

If the [Expand Dynamic Calls Property](https://wiki.genexus.com/commwiki/wiki?8223,,) value is **No**, the behavior is the same as mentioned before.

However, if the property value is **Yes**, the behavior is as described below.

When you have Dynamics calls/links, an attempt to establish a group of objects to invocate (based on parameters, types, etc. of the call and objects) is made.

Then, in the caller object, a code structure is generated calling every possible object from the group, making the parameter encryption based on the called object [Encrypt URL Parameters property](https://wiki.genexus.com/commwiki/wiki?8068) value. This behavior is the same as that of a Static call (a 'weak reference' is generated and can be seen from the [IDE](https://wiki.genexus.com/commwiki/wiki?5272) References).

*Note: The code structure is an If's structure that includes an Otherwise to resolve all the cases where the called object is not contemplated. For this case, the criterion is the same as when*Expand Dynamic Calls Property = No. *So, use the config.gx file if you need to encrypt the parameters of those calls that are going to be considered inside the Otherwise group.*

### [What if you invocate [External objects](https://wiki.genexus.com/commwiki/wiki?5669) dynamically](#What+if+you+invocate+wiki%3F5669%2CCategory%253AExternal%2Bobject+External+objects+dynamically+)

If you have [External objects](https://wiki.genexus.com/commwiki/wiki?5669) (as an object from other [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836)), the [Expand Dynamic Calls Property](https://wiki.genexus.com/commwiki/wiki?8223,,) value doesn't matter, this is because:

If the property value is **No**, the parameters won't be encrypted by default, unless the config.gx file is configured.

On the other hand, if the property value is **Yes**, it will be contemplated in the Otherwise case so the parameters won't be encrypted either (unless the config.gx file is configured as when the property value is No).
