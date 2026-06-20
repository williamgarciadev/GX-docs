---
title: "Import MSBuild Task"
source_id: 35599
source_url: https://wiki.genexus.com/commwiki/wiki?35599
genexus_version: "18"
---

# Import MSBuild Task

Imports an import file into the currently opened Knowledge Base.

## [Syntax](#Syntax)

```
<Import File="$(ImportFileName)" AutomaticBackup="$(AutomaticBackup)" ImportType="$(ImportType)"
LanguageTranslations="$(LanguageTranslations)" RedefineExternalPrograms="$(RedefineExternalPrograms)"
ImportKBInformation="$(ImportKBInformation)" IncludeItems="$(IncludeItems)" ExcludeItems="$(ExcludeItems)"
PreviewMode="$(PreviewMode)" UpdateFile="$(CompleteXpzPath)"  >
    <Output TaskParameter="ImportedItems" ItemName="ImportedItem" />
</Import>
```

### [Options](#Options)

*File*is the fully or partially qualified name of an Import File (.XPZ). **REQUIRED**

*AutomaticBackup*: defines whether an automatic backup is generated.

*ImportType*: Available options are: *AllObjects*, *DifferentObject* and *NewerObjects*.

*LanguageTranslations*: Available options are: *Update*, *Keep*, *ReplaceAll*.

*RedefineExternalPrograms*: check the [Redefine External Programs Property](https://wiki.genexus.com/commwiki/wiki?7615,,) property.

*ImportKBInformation (1):* defined wether KB/Version/Environment properties are imported. Possible values are "false" and "true", default value is true.

*IncludeItems:* List of objects to be imported from the xpz file.

*ExcludeItems:* List of objects to be excluded from the import process.

*PreviewMode :* Do not actually import objects; it is useful to get the list of possible imported items.

*UpdateFile :* Full path where the update file will be saved.

*TableIndexesImportBehavior: defined the behavior for tables*

* **"Overwrite"**: completely overwrites user defined Indexes with the provided values.
* **"IncrementalIntegration"**: merges existing Indexes with the provided values.
* **"ImportDefaultContent"**: Only import the system defined Indexes with the provided values.
* **"OverwriteEvenDefaultContent"**: completely overwrites both user and system defined Indexes with the provided values.

### [Output](#Output)

*ImportedItems (1):* Returns a collection with the list of imported objects.

### [Samples](#Samples)

Import file c:\MyExports\ImportTestFile.xpz into the currently opened Knowledge Base.

```
<Import File="c:\MyExports\ImportTestFile.xpz" />
```

### [Notes](#Notes)

#### [Object List](#Object+List)

The object list for the *IncludeItems*, *ExcludeItems* and *ImportedItems* parameters use the syntax detailed [here](https://wiki.genexus.com/commwiki/wiki?35636).

#### [Verbosity](#Verbosity)

If MSbuild.exe is executed with /verbosity:detailed each object imported will be shown:

```
Importing Attribute 'ClientAddress'...
Importing Attribute 'ClientBalance'...
Importing Transaction 'Client'...
Importing Procedure 'IsAuthorized'...
```

1 - The property is deprecated since GeneXus 15 Upgrade 7; use *IncludeItems* or *ExcludeItems* options.

### [See Also](#See+Also)

[GeneXus MSBuild Taks](https://wiki.genexus.com/commwiki/wiki?3908)


|  |
| --- |
| **Backlinks** |
| [MSBuild Tasks](https://wiki.genexus.com/commwiki/wiki?3908) | [MSBuild Tasks (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?53867) | [MSBuild Tasks (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54112) |

---
