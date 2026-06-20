---
title: "Build Events"
source_id: 39474
source_url: https://wiki.genexus.com/commwiki/wiki?39474
genexus_version: "18"
---

# Build Events

Sometimes you need a simple task, like emptying a directory or moving a file from your network to your target folder before a build, or maybe copy some files to a different location once the build is complete. If that’s your case, you probably created a bat file which you run (when you remember) to do so.

### [Build Events to the rescue.](#Build+Events+to+the+rescue.)

'Build Events' is a feature that allows you to program simple tasks on the before and after build events.

You can access it from Toolbar and go to **Build > Build Events**. There you’ll see a simple interface with two edit boxes where you can type your commands.

To create those commands, you can use already provided macros. These macros allow you to access the path of your working model or GeneXus installation without the need of hard-coding these paths. The values of these macros are solved at runtime, right before they’re needed.

`[imagen omitida: wiki id 39475]`

Important: The above sample (that deletes the \*.ver files before building) works only in environments where the only build action that happens is a "Rebuild All".

**Note**: All these commands will be saved in your Environment, so if you commit your Environment properties they will travel back and forth to your Genexus Server. MSBuild tasks take them in account too. You will be able to see in Genexus’ output window when these commands are executed, and their output (in case they provide output).

### [Pre-build event command line:](#Pre-build+event+command+line%3A)

This is where you want to write the commands that need to run before a build. Keep in mind that if any of these commands fail, the build will be canceled.

### [Post-build event command line:](#Post-build+event+command+line%3A)

This is where you will write your commands that will run after a build is completed, depending on the selection of the “Run the post-build event” which can be either “Always” or “On successful build”, and the status of the build event. These will not modify the state of a build action.

### [Usage](#Usage)

You may use this feature for things like

* After a build, adding to the web.xml some url-rewrite rules
* After a build, save reorganizationscript.txt on a Git
* After a build, deploy binaries to another server

## [Availability](#Availability)

This feature is available as of [GeneXus 15 upgrade 12](https://wiki.genexus.com/commwiki/wiki?39737,,)
