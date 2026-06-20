---
title: "Obfuscate Application property"
source_id: 33477
source_url: https://wiki.genexus.com/commwiki/wiki?33477
genexus_version: "18"
---

# Obfuscate Application property

If True, the application will be shrunk as part of the compilation process, removing unused code and obfuscating remaining methods and classes using short names.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Description](#Description)

Obfuscation is the practice of making something difficult to understand. Programming code is often obfuscated to protect intellectual property and prevent an attacker from reverse engineering a proprietary software program.

You can obfuscate code to provide security against reverse engineering, making this process difficult and economically unfeasible. Other advantages may include helping to protect licensing mechanisms, prevent unauthorized access, and shrink the size of an executable.

When the **Obfuscate Application property**is set to True, the .abb file is obfuscated during compilation.

Enabling this property causes the application to be obfuscated at compile time using the [ProGuard](https://www.guardsquare.com/en/proguard) tool, which detects and removes unused classes, fields, methods, and attributes. In addition, it optimizes bytecode, removes unused instructions, and renames the remaining classes, fields, and methods using short, meaningless names.

#### [**Notes**](#Notes)

* GeneXus generates mapping files under the *<model>/<environment>/mobile/Android/<main>/build/outputs/mapping/\** directory. It is highly recommended that developers keep these files when distributing the app to deobfuscate it (they can even be uploaded to Google Play Store, for example, for viewing the stack trace if a crash error occurs).
* For the **Obfuscate Application property** to take effect, the [Compilation Mode property](https://wiki.genexus.com/commwiki/wiki?35447) (available at generator level) must be set to 'Distribution'.
* Make sure to recompile your Android [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770) after changing this property value.

The property is available since [GeneXus 15 Upgrade 3](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?33278,,).

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#com.gxwiki.wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770).


|  |
| --- |
| **Backlinks** |
| [Compilation Mode property](https://wiki.genexus.com/commwiki/wiki?35447) |
| [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817) |

---
