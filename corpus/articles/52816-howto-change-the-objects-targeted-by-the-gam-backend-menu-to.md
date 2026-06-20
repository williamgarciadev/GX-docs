---
title: "HowTo: Change the objects targeted by the GAM Backend menu to GAM Examples"
source_id: 52816
source_url: https://wiki.genexus.com/commwiki/wiki?52816
genexus_version: "18"
---

# HowTo: Change the objects targeted by the GAM Backend menu to GAM Examples

This article explains the necessary steps to change the objects loaded by the GAM Backend menu.

In particular, this is useful when you want to use [GAM - Examples](https://wiki.genexus.com/commwiki/wiki?21993) instead of compiled objects.  
Instead of using objects named “gam\_\*,” which belong to the compiled Backend, the objects named “gamexample\*” will be used. The latter belong to the examples that are distributed. (\* = objectname).  
  
Next, the “dashboard” menu item will be updated as an example, but all the menu items of each of them must be updated.

**Steps:**

1. Go to the GAM Backend application; there, click on the “More Options” button, and then on Menus.  
   `[imagen omitida: wiki id 52817]`
2. Select the Menu you want to change and click on the “Options” button. (This step must be repeated for each Menu shown in the image, **GAMBackendMainMenu, GAMBackendRepositoryMenu, GAMBackendSettingsMenu**).  
   `[imagen omitida: wiki id 52818]`
3. Click on “Edit” for the Menu Option you want to update. (This step must be repeated for each Menu Option shown in the image).  
   `[imagen omitida: wiki id 52819]`
4. Edit the value of the “Resource” field.  
   Original value:  
   `[imagen omitida: wiki id 52820]`  
     
   New value:  
   `[imagen omitida: wiki id 52821]`

**Note:**When using the Java generator, the Package property of the application must be taken into account, since it is part of the path to the objects.  
This property is located inside the application, below the “Environment Settings” tab:  `[imagen omitida: wiki id 52823]`

\*In general, the value of the package must be changed to “com.kbname.”


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |

---
