---
title: "GeneXus Installation Steps"
source_id: 25842
source_url: https://wiki.genexus.com/commwiki/wiki?25842
genexus_version: "18"
---

# GeneXus Installation Steps

This chapter describes the steps to install [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066). Note that you must have Administrator rights to execute the installation and make sure to install as a user with full control of the target installation folder.

Below are detailed instructions for the installation process.

1. Be sure to fulfill the [requirements](https://wiki.genexus.com/commwiki/wiki?30900)
2. Run the GeneXus 18 Setup [installer](http://www.genexus.com/v18-download), a wizard will start shortly  
   `[imagen omitida: wiki id 52718]`
3. A dialog like the following appears:  
   `[imagen omitida: wiki id 52719]`  
   By clicking on 'Install', you accept the License Terms, and the 'typical' installation process begins.
   * GeneXus 18 is installed in the displayed Product Install path
   * Default GAM Platforms are installed (i.e. SQL Server and MySQL)  
     (follow up reading in step 5)
4. By clicking on 'License Terms', these are displayed in 3 different languages:  
   `[imagen omitida: wiki id 52720]`  
   By clicking on 'Install', you accept the License Terms, and the 'typical' installation process begins.
   * GeneXus 18 is installed in the displayed Product Install path
   * Default GAM Platforms are installed (i.e. SQL Server and MySQL)  
     (follow up reading in step 5)
5. To change the GAM Platforms to be installed, you need to select 'Custom' in the dialog of step 3:  
   `[imagen omitida: wiki id 52721]`  
   By clicking on 'Next', you accept the License Terms, and you can select additional GAM Platforms to install.
6. `[imagen omitida: wiki id 52722]`  
   Click on 'Install' to install GeneXus 18 and the selected GAM Platforms.
7. Now you are installing GeneXus 18.  
   `[imagen omitida: wiki id 52723]`  
   If you click on 'Cancel' the installation process is canceled.
8. When installation finishes, the following dialog appears:  
   `[imagen omitida: wiki id 52724]`  
   Click on 'Close' to finish setup. Click on 'Run' to open GeneXus 18, or 'Restart' if requested to.

**Note:** At the end of the setup process a Genexus.exe /install operation is executed to register User Controls, Extensions, and Documentation. This process creates in the installation folder the files:

* userControls.ari
* \*.supportfiles
* \*.html

These files are needed for standard GeneXus usage.

### [FAQ](#FAQ)

#### [Q: Can I have more than one GeneXus 18 installation in the same PC?](#Q%3A+Can+I+have+more+than+one+GeneXus+18+installation+in+the+same+PC%3F)

A: Yes and No :) You can’t have more than one local installed version. But, every GeneXus 18 Upgrade is treated as an independent setup so you could have installed different upgrades of the version, let's say v18, v18 Upgrade #1 and so on.

if you still need several instances for the same Version and Upgrade; just duplicate the desired GeneXus root folder and rename it accordingly.

#### [Q: Can I have more than one GeneXus version installed on the same PC?](#Q%3A+Can+I+have+more+than+one+GeneXus+version+installed+on+the+same+PC%3F)

A: Yes, you can. The only constraint is that they must be installed in different folders.


|  |
| --- |
| **Backlinks** |
| [Category:GeneXus 18 Installation Manual](https://wiki.genexus.com/commwiki/wiki?31997) | [GeneXus Workstation Setup](https://wiki.genexus.com/commwiki/wiki?25844) | [HowTo: Prepare a Mac with an Intel processor for GeneXus](https://wiki.genexus.com/commwiki/wiki?51408) |
| [HowTo: Prepare a Mac with ARM architecture for GeneXus](https://wiki.genexus.com/commwiki/wiki?51149) |

---
