---
title: "Customize GeneXus Deployment capabilities"
source_id: 45672
source_url: https://wiki.genexus.com/commwiki/wiki?45672
genexus_version: "18"
---

# Customize GeneXus Deployment capabilities

The GeneXus [Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) is a powerful tool that allows you to deploy your GeneXus-generated applications to either on-premises servers or to a wide range of Cloud Providers.

Its sole purpose is to run through the so-called "references tree" to figure out what are all the necessary objects for your application to run properly on a production environment.

However, sometimes you may need something that's not in the Knowledge Base or, for some reason, you may need to remove something from the Knowledge Base—for security reasons, or when some objects have references to objects that you know are not used at runtime. Also, maybe you want to run a custom script before moving to production and before creating the WAR or ZIP file.

### [That's what the user.gxdproj file is for.](#That%27s+what+the+user.gxdproj+file+is+for.)

The generation of the WAR or ZIP file consists of two tasks. The first one (*CreateDeployProject*) will generate an MSBuild script file with the extension .gxdproj, which contains every GeneXus object form your Knowledge Base that is involved in the deployment of the selected Deployment unit or objects. The second task (*CreatePackage*), takes the previously generated gxdproj file and, based on its contents, tries to find every file generated for every declared object. More on these tasks here: [Application Deployment MSBuild tasks](https://wiki.genexus.com/commwiki/wiki?42073).

When the CreateDeployProject task is executed, it will look for a file called <Deployment Unit Name> \_user.gxdproj. If it does not exist, it will be created but never overwritten.

At first, the file looks like this:

```
<?xml version="1.0" encoding="utf-8"?>
<Project xmlns="http://schemas.microsoft.com/developer/msbuild/2003">

    <PropertyGroup>
        <!--AdditionalDirectory>some directory to copy</AdditionalDirectory-->
    </PropertyGroup>

    <!-- You can add a directory where every AdditionalFile will be copied (relative to the root) -->
    <PropertyGroup>
        <AdditionalFileDestination></AdditionalFileDestination>
    </PropertyGroup>

    <ItemGroup>
        <!--AdditionalFile Include="some File to copy"/-->

        <!--
        This file will be copied to $(DeployFullPath)\$(AdditionalFileDestination)
        <AdditionalFile Include="C:\myfiles\myfile.txt"/>
        This file will be copied to $(DeployFullPath)\TargetDir
        <AdditionalFile Include="C:\myfiles\my other file.txt">
            <RelativeTargetDir>TargetDir</RelativeTargetDir>
        </AdditionalFile>
        -->

    </ItemGroup>

    <Target Name="RemoveExtraFiles">
        <!-- Uncomment this section in case you want to delete files right before creating the package
        <ItemGroup>
            <UnneededFiles Include="$(DeployFullPath)\your\file\goes\here"/>
        </ItemGroup>

        <Message Text="RemovingUserExcludedFiles" Importance="high" />
        <Delete Files="@(UnneededFiles)"/>
        -->
    </Target>

    <Target Name="BeforePackaging" DependsOnTargets="RemoveExtraFiles">

    </Target>

</Project>
```

### [How to include complete folders](#How+to+include+complete+folders)

Note that there's an AdditionalDirectory tag, and you can add as many tags as you wish with all the directories you want to add. Keep in mind this will copy every file and directory in the destination, following the original structure.

There's also an IncludeDirectory tag to include the folder and its contents.

### [How to include files](#How+to+include+files)

There's also a tag called AdditionalFile which allows you to add as many files as you wish.

Where will these files be copied? You have two options for this. First, you can set a default destination folder with the tag AdditionalFileDestination; if you set a path there, every file will be copied to that destination. Alternatively, you can set an additional property to your files called RelativeTargetDir. This is a property that only applies to the file it belongs to and ensures that this file will be copied to that directory.

### [How to remove files](#How+to+remove+files)

There's a whole target for that called RemoveExtraFiles.

In the ItemGroup in that target, you need to add every file you want to delete. Keep in mind that you can use wild cards (\*) for either file names and/or directories.

The last task of the target deletes every file included in the UnneededFiles item group.

### [How to run a customized script](#How+to+run+a+customized+script)

The last target of the user.gxdproj file is called BeforePackaging and will be run exactly when you think, right before creating the package. So, at this point everything is in place –the extra files you added. Also, the ones you wanted to delete are gone. In this target, you can run your own scripts by calling the Exec task or adding the imports needed to call your own tasks.

Keep in mind that in this process there are a few variables you can use:

```
$(DeployFullPath): the absolute path where the deployed engine is copying files.
$(WebPath): this is the web directory from the source environment.
```

### [See also](#See+also)

[SAC 46921](https://www.genexus.com/en/developers/websac?data=46921)

### [Availability](#Availability)

This feature is available since [GeneXus 16 upgrade 10](https://wiki.genexus.com/commwiki/wiki?45624,,).


|  |
| --- |
| **Backlinks** |
| [Adding additional files to an application package](https://wiki.genexus.com/commwiki/wiki?35361) | [Toc:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Toc:Application Deployment tool (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54334) |
|

---
