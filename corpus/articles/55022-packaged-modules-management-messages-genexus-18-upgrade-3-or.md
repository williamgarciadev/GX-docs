---
title: "Packaged Modules Management messages (GeneXus 18 Upgrade 3 or prior)"
source_id: 55022
source_url: https://wiki.genexus.com/commwiki/wiki?55022
genexus_version: "18"
---

# Packaged Modules Management messages (GeneXus 18 Upgrade 3 or prior)

The following list shows the **pmm** messages that can appear when actions related to [Modules](https://wiki.genexus.com/commwiki/wiki?22414) are done.

| Code | Message |
| --- | --- |
|  | |
| **pmm0001** | **Updating 'GeneXus' module version to required %1** |
|  | The GeneXus module is the standard classes API, a component that is enhanced with each upgrade of GeneXus and is part of the generated application. This message appears when the GeneXus module is not found in the KB. During the Build process, it is installed in the KB. |
|  | |
| **pmm0002** | **Updating 'GeneXus' module version from 1.9.1.119656 to required 3.0.4.144757** |
|  | It indicates that the module 'GeneXus' (or the one mentioned in the message) is being updated automatically by GeneXus to the version that is required by it. |
|  | |
| **pmm0003** | **Built-in '%1' module must be updated to version %2** |
|  | Updating module %1 to version %2 is recommended; module %1 is installed in the KB with a version other than %2 and, in addition, it is one of the modules distributed by GeneXus. It is recommended to have it updated to the distributed version. The GeneXus developer is responsible for performing the update and for solving possible interface update issues as a result of this operation. |
|  | |
| **pmm0004** | **GeneXus Module installation failed** |
|  | During the Build process, it is determined that the GeneXus module definition needs to be updated; the update step that is done through the Import of the module definition fails.    **1)** Verify that the module has been properly installed. Check the GeneXus installation. The 'Modules' directory contains the list of modules distributed with GeneXus. Take note of the version information in the file GeneXus{version}.opc  * Check if this directory exists: %userprofile%\.gxmodules\.cache\GeneXus\_4f454e73-7d8f-4a0f-908a-1a355f3634a5\{version}.   + If it doesn't exist, you need to execute the command “genexus /install”. * Check if this file exists: %userprofile%\.gxmodules\.cache\GeneXus\_4f454e73-7d8f-4a0f-908a-1a355f3634a5\{version}\ModuleDefinition.xml   + If it doesn't exist, there was an error while decompressing the OPC: delete the directory %userprofile%\.gxmodules\.cache\GeneXus\_4f454e73-7d8f-4a0f-908a-1a355f3634a5\{version} and run the command “genexus /install”.  **2)** Check if there is any information left in the Windows EventViewer that shows an error during an Import in the KB.    **3)** This GeneXus module update can be run manually through the Module Manage Reference and by selecting Update of the GeneXus Module. |
|  | |
| **pmm0005** | **Cannot find the specified module '%1'** |
|  | The specified module to install is not found, given the module name %1. This error is expected when the InstallModule Task is configured in an assembly pipeline. |
|  | |
| **pmm0006** | **Cannot find the specified version %1 for module '%2'** |
|  | The specified module or module version to install is not found. The name %1 and a specific version of it, %2, are specified. This error is expected when the InstallModule Task is configured in an assembly pipeline. |
|  |  |
| **pmm0007** | **Cannot install module '%1', it is already defined in the Knowledge Base** |
|  | It is not possible to install a packaged module in the KB that defines the module. For example: when trying to install the “GeneXus” module through the Module Manage Reference in the KB that generates this module, this error will occur. This validation is performed using the internal GUID of the object so that if it was renamed in the KB, it cannot be overwritten with its packaged version. This error is expected when the InstallModule Task is configured in an assembly pipeline. |
|  |  |
| **pmm0008** | **Cannot update module '%1', it is already defined in the Knowledge Base and it is not a packaged one** |
|  | It is not possible to update a module defined in the KB. This error is expected when the UpdateModule Task is configured in an assembly pipeline. |
|  |  |
| **pmm0012** | **% module has no public objects, it cannot be packed.** |
|  | It indicates that certain module cannot be packed because it does not contain public objects. |
|  |  |
| **pmm0015** | **Circular Dependency with module** **'%1'** |
|  | It indicates that certain module contains a circular dependency.  **Sample**  Consider the Module7.Procedure13() which calls Module6.Procedure11() which calls Module7.Procedure12().   When trying to package Module 7, this error advertises the corresponding circular dependency. |
|  |  |
| **pmm0037** | **Maven installation not found. Please, add Maven installation 'bin' path to environment variable 'PATH'.'** |
|  | It indicates that GeneXus could not execute a command related to Maven. You may need to follow the instruction of the message, or even more: Install Maven, as required: [GeneXus 18 hardware and software requirements](https://wiki.genexus.com/commwiki/wiki?30900). |
| **pmm0046** | **'%1' module has a main object, it cannot be packed** |
|  | It indicates that there is a main object. Packaging main objects is not supported. If you need to package the business logic, you should separate the main object from the business logic. |

## [See also](#See+also)

* [Specification Error Codes and Messages](https://wiki.genexus.com/commwiki/wiki?5933)
* [Information Error Codes and messages](https://wiki.genexus.com/commwiki/wiki?45847)
* [When and how is the GeneXus module updated in a KB?](https://wiki.genexus.com/commwiki/wiki?47842)
