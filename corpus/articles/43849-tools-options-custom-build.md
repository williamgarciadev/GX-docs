---
title: "Tools - Options - Custom Build"
source_id: 43849
source_url: https://wiki.genexus.com/commwiki/wiki?43849
genexus_version: "18"
---

# Tools - Options - Custom Build

In this node (GeneXus Menu > Tools > Options > Build > Custom Build), you can create custom Build commands.

A custom build command does only the steps you configure. By avoiding steps that are not necessary in certain circumstances, you optimize build times and get faster prototyping cycles.

Each custom build command has three fields

* Name - The name of the command
* Scope - Each command works under a certain scope. A scope defines basic (not avoidable) steps, what those steps do, and defines also under what menu option the custom command will appear.
  + One of the following scopes can be set: Build All, Rebuild All, Build, Rebuild, Build With These Only, Run, Run With This Only
* Enabled steps- A list of steps that the custom build command will do.

Once defined, a custom build command appears in the contextual menu of the object > Custom Build, or on the main GeneXus menu > Build > Custom Build.

## [Useful Samples](#Useful+Samples)

These samples are custom build commands that different users have defined, and found useful under certain circumstances.

1) Update Configuration file

After changing a Datastore property (password, user, etc) the only step GeneXus requires to do is to update the configuration file (eg web.config, client.cfg, etc); but any of the available standard commands do too many steps.  
So you can create a new custom action

* Name = Update Config
* Scope = Build With These Only
* Enabled steps = Generate, Compile

  2) Build SDTs (only valid for .NET)

In some particular case, some SDT hasn't been rebuilt properly and that produces compilation errors on objects that use that SDT. A rebuild all may take too long because it does unnecessary steps  
So you can create a new custom action

* Name = Rebuild all SDTs
* Scope = Rebuild All
* Enabled steps = Specify SDTs, Generate SDTs, Compile

3) Separate Generate from Compile and Transfer (RPG/400)

If you need to change something before compiling and transferring to the iSeries, you can create two custom build commands  
a)

* Name = Generate RPG
* Scope = Build All
* Enabled steps = all the first ones including 'Generate'

b)

* Name = Compile & Trf RGP
* Scope = Build All
* Enabled steps = All commands after 'Generate'

## [Sample screenshots](#Sample+screenshots)

`[imagen omitida: wiki id 44187]`

`[imagen omitida: wiki id 44188]`

### [Notes](#Notes)

* The list of steps is loaded dynamically, based on the steps done in previous builds. So Rebuild All at least one time in your installation, so that all steps are available to select or deselect.
* There is an MSBuild task related to [Custom Build](https://wiki.genexus.com/commwiki/wiki?3908).


|  |
| --- |
| **Backlinks** |
| [Category:IDE Configuration Options](https://wiki.genexus.com/commwiki/wiki?6772) |
| [MSBuild Tasks](https://wiki.genexus.com/commwiki/wiki?3908) | [MSBuild Tasks (GeneXus 18 Upgrade 1 or prior)](https://wiki.genexus.com/commwiki/wiki?53867) | [MSBuild Tasks (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54112) |

---
