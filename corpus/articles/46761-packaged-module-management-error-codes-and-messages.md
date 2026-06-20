---
title: "Packaged Module Management Error Codes and messages"
source_id: 46761
source_url: https://wiki.genexus.com/commwiki/wiki?46761
genexus_version: "18"
---

# Packaged Module Management Error Codes and messages

The following list shows the **pmm** messages that can appear when actions related to [Modules](https://wiki.genexus.com/commwiki/wiki?22414) are performed.

| Code | Message |
| --- | --- |
|  | |
| **pmm0001** | **Updating 'GeneXus' module version to required '%1'** |
|  | The GeneXus module is the standard classes API, a component that is enhanced with each upgrade of GeneXus and is part of the generated application. This message appears when the GeneXus module is not found in the KB. During the Build process, it is installed in the KB. |
|  | |
| **pmm0002** | **Updating 'GeneXus' module version from 1.9.1.119656 to required 3.0.4.144757** |
|  | It indicates that the module 'GeneXus' (or the one mentioned in the message) is being updated automatically by GeneXus to the version that is required by it. |
|  | |
| **pmm0003** | **Built-in '%1' module should must be updated to version '%2'** |
|  | Updating module %1 to version %2 is recommended; module %1 is installed in the KB with a version other than %2 and, in addition, it is one of the modules distributed by GeneXus. It is recommended to have it updated to the distributed version. The GeneXus developer is responsible for performing the update and for solving possible interface update issues as a result of this operation. |
|  | |
| **pmm0004** | **GeneXus Module installation failed** |
|  | During the Build process, it is determined that the GeneXus module definition needs to be updated; the update step that is done through the Import of the module definition fails.    **1)** Verify that the module has been properly installed. Check the GeneXus installation. The 'Modules' directory contains the list of modules distributed with GeneXus. Take note of the version information in the file GeneXus{version}.opc  * Check if this directory exists: %userprofile%\.gxmodules\.cache\GeneXus\_4f454e73-7d8f-4a0f-908a-1a355f3634a5\{version}.   + If it doesn't exist, you need to execute the command “genexus /install”. * Check if this file exists: %userprofile%\.gxmodules\.cache\GeneXus\_4f454e73-7d8f-4a0f-908a-1a355f3634a5\{version}\ModuleDefinition.xml   + If it doesn't exist, there was an error while decompressing the OPC: delete the directory %userprofile%\.gxmodules\.cache\GeneXus\_4f454e73-7d8f-4a0f-908a-1a355f3634a5\{version} and run the command “genexus /install”.  **2)** Check if there is any information left in the Windows EventViewer that shows an error during an Import in the KB.    **3)** This GeneXus module update can be run manually through the Module Manage Reference and by selecting Update of the GeneXus Module. |
|  | |
| **pmm0005** | **Cannot find the specified module '%1'** |
|  | The specified module to install is not found, given the module name %1. This error is expected when the InstallModule or UpdatelModule Tasks are configured in an assembly pipeline. |
|  | |
| **pmm0006** | **Cannot find the specified version '%1' for module '%2'** |
|  | The specified module or module version to install is not found. The name %1 and a specific version of it, %2, are specified. This error is expected when the InstallModule or UpdatelModule Tasks are configured in an assembly pipeline. |
|  |  |
| **pmm0007** | **Cannot install module '%1', it is already defined in the Knowledge Base** |
|  | It is not possible to install a packaged module in the KB that defines the module. For example: when trying to install the “GeneXus” module through the Module Manage Reference in the KB that generates this module, this error will occur. This validation is performed using the internal GUID of the object so that if it was renamed in the KB, it cannot be overwritten with its packaged version. This error is expected when the InstallModule Task is configured in an assembly pipeline. |
|  |  |
| **pmm0008** | **Cannot update module '%1', it is already defined in the Knowledge Base and it is not a packaged one** |
|  | It is not possible to update a module defined in the KB. This error is expected when the UpdateModule Task is configured in an assembly pipeline. |
|  |  |
| **pmm0010** | **'%1' is a referenced module, it cannot be packed.** |
|  | It occurs when you try to package a referenced module. That is, a module that is already packaged by another KB and installed in the current KB. |
|  |  |
| **pmm0012** | **'%1' module has no public objects, it cannot be packed** |
|  | A module is packable when objects are defined in its interface. In order to be able to execute such action, the module must have available any object that is packable and that is public. This message indicates that a certain module cannot be packed because it does not contain any public object. |
|  |  |
| **pmm0015** | **Circular Dependency with module** **'%1'** |
|  | It indicates that a certain module contains a circular dependency.  **Sample**  Consider the Module7.Procedure13() which calls Module6.Procedure11() which calls Module7.Procedure12().   When trying to package Module 7, this error informs about the corresponding circular dependency. |
|  |  |
| **pmm0017** | **Module can’t be exported since it references the following objects from the Root module** |
|  | Some packable object has a dependency with an object in the Root Module (it is a reference to any generable object, such as a Procedure, SDT, Domain, or Image). You cannot have this type of dependency since it is not possible to resolve it later when installing the module in another KB. |
| **pmm0018** | **Module can’t be exported since it references the following transactions from other modules: '%1'** |
|  | Some packable object references some [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s included in other modules. You cannot have this type of dependency since it is not possible to resolve it later when installing the module in another KB. |
|  |  |
| **pmm0020** | **Cannot find the implementation of built-in module: '%1' v%2; execute “genexus.exe /install” command to restore it** |
|  | The implementation of the indicated built-in module is not found ('%1' is the module name and v%2 is the version).  You have to execute genexus.exe /install. |
|  |  |
| **pmm0022** | **Cannot find implementation of module '%1' (version '%2'). You need to restore or update it to an available version** |
|  | When trying to install a module, it is always done from the cache. If the module is not found in the cache, an attempt is made to download it (along with all its dependencies) from one of the available repositories.   If it is not possible to perform this download action, this error is displayed. |
|  |  |
| **pmm0030** | **Module '%1' was not found, version '%2' is required.** |
|  | When a module is requested to be installed, it is in the cache and the import process starts. Then the dependent modules are checked and an attempt is made to import it. If these dependencies are not available in the cache, this error is displayed. |
|  |  |
| **pmm0036** | **Packaged module '%1' does not exist.** |
|  | It occurs when trying to publish a module that does not exist among the packaged modules (ready to publish). |
|  |  |
| **pmm0037** | **Maven installation not found. Please, add Maven installation 'bin' path to environment variable 'PATH'.'** |
|  | It indicates that GeneXus could not execute a command related to Maven. You may need to follow the instructions of the message, or even more: Install Maven, as required: [GeneXus 18 hardware and software requirements](https://wiki.genexus.com/commwiki/wiki?30900). |
|  |  |
| **pmm0039** | **Cannot restore module '%1', only packaged modules defined in the Knowledge Base can be restored.** |
|  | It occurs when you try to restore a module for which you have the implementation in your KB. It is only possible to restore referenced modules. |
|  |  |
| **pmm0042** | **Unable to find Module '%1' '%2'. Reference needed by: '%3'** |
|  | When performing a Build this warning is displayed if module(s) on which other module(s) depend(s) are not found. |
|  |  |
| **pmm0044** | **Major version difference detected for '%1'; version %2 is currently installed but several module(s) were generated against a different one** |
|  | This message warns that there is a difference in the major version (the first number (X) of X.Y.Z) in one of the dependencies of the installed modules.  **Sample**  pmm0044: Major version difference detected for 'ModuleA'; version 4.4 is currently installed but several module(s) reference a different one.          - 'ModuleB' -> 'ModuleA' v3.0  In this case, module 'ModuleA' 4.4 is installed and module 'ModuleB' was packaged with a minimum dependency of 3.0. |
|  |  |
| **pmm0045** | **Version conflict detected for '%1'; Version %2 is currently installed but several module(s) were generated against a different one.** |
|  | This message informs that there is a version conflict because some modules reference a newer or older version of the module version displayed.  This depends on the module developer. When packaging a module the developer can indicate compatibility ranges indicating minimum and maximum versions.  **Sample**  pmm0045: Version conflict detected for 'ModuleB'; Version 2.1 is currently installed but several module(s) were generated against a different one.  This means that the 'ModuleB' version is 2.1 and other modules reference a newer or older version of it. |
|  |  |
| **pmm0046** | **'%1' module has a main object, it cannot be packed** |
|  | It indicates that there is a main object. Packaging main objects is not supported. If you need to package the business logic, you should separate the main object from the business logic. |
|  |  |
| **pmm0047** | **NuGet installation not found. Please, add NuGet installation path to environment variable 'PATH'.** |
|  | To install modules you need NuGet. This message indicates that you haven't got it.  When you work with an Internet connection, and you run genexus /install or when you run the GeneXus setup, nuget.exe is downloaded from the Internet and located in C:\Users\<user>\.gxmodules\.tools.  To avoid this message, download [nuget.exe](https://dist.nuget.org/win-x86-commandline/latest/nuget.exe) from the Internet and copy it to   %USERPROFILE%\.gxmodules\.tools (c:\users\<user>\.gxmodules\.tools) or add the location of the nuget.exe to the  environment variable 'PATH'. |
|  |  |
| **pmm0049** | **'%1' is not supported to be exported in the interface** |
|  | Indicates that the object '%1' is not part of the packaged module; that type of object may be defined as part of the module in the current KB (as a way to organize that knowledge base), but it is excluded in the packaging process. The list of supported types can be reviewed at [Modules Distribution in GeneXus](https://wiki.genexus.com/commwiki/wiki?31376). |
|  |  |
| **pmm0050** | **The module '%1' was not found in the Knowledge Base. Update operation cannot be performed.** |
|  | This message is displayed when you try to update a module that is not installed in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) using the [UpdateModule task](https://wiki.genexus.com/commwiki/wiki?46830). |

## [See also](#See+also)

* [Specification Error Codes and Messages](https://wiki.genexus.com/commwiki/wiki?5933)
* [Information Error Codes and messages](https://wiki.genexus.com/commwiki/wiki?45847)
* [When and how is the GeneXus module updated in a KB?](https://wiki.genexus.com/commwiki/wiki?47842)


|  |
| --- |
| **Backlinks** |
| [Toc:Coded Messages](https://wiki.genexus.com/commwiki/wiki?47288) | [Packaged Modules Management messages (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55022) |

---
