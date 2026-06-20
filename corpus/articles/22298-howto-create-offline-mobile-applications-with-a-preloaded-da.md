---
title: "HowTo: Create offline mobile applications with a preloaded database"
source_id: 22298
source_url: https://wiki.genexus.com/commwiki/wiki?22298
genexus_version: "18"
---

# HowTo: Create offline mobile applications with a preloaded database

There are many scenarios where the Offline Mobile Apps will need to be installed with some data already loaded into the local database. Furthermore, the first synchronization may take a long time, or initial data may not vary in the future. So there are reasons to have a preloaded database mechanism in developing time.

This tutorial is a simple and quick guide for developers that want to create offline applications for Smart Devices with a preloaded database.

As an example, this document is based on the Offline branch from [EventDay](https://wiki.genexus.com/commwiki/wiki?22550,,) sample.

### [Before you begin...](#Before+you+begin...)

**Important**: To preload the application's database, you will be using a simulator or a device. **You cannot use the same simulator/device to synchronize again!**

See the section titled *Preloaded Hashes* below for further information.

### [[Apple](https://wiki.genexus.com/commwiki/wiki?14917) Applications](#wiki%3F14917%2CCategory%253AApple%2Bplatform+Apple+Applications)

#### [**Step 1: Creating the database**](#Step+1%3A+Creating+the+database)

The first step to have preloaded data is to create the database

**1.** Open the project in Xcode.  
**2.** Run the application in theiOS Simulator and let it execute the data synchronization process.  
**3.** Once the synchronization is complete, theXcode console shows us a message similar to this (Look at [this document](https://wiki.genexus.com/commwiki/wiki?22339,,) for further information about the debug on Xcode):

> ---------------------------------------  
> -- DATABASE SYNCHRONIZATION FINISHED --  
>   
> Database file: /Users/%USERNAME%/Library/Application Support/iPhone Simulator/%IOS\_TARGET%/Applications/%APP\_RANDOM\_ID%/Documents/EventDay.sqlite  
>   
> Hashes file: /Users/%USERNAME%/Library/Application Support/iPhone Simulator/%IOS\_TARGET%/Applications/%APP\_RANDOM\_ID%/Documents/EventDay\_hashes.json  
>   
> BLOB data zip file: /Users/%USERNAME%/Library/Application Support/iPhone Simulator/%IOS\_TARGET%/Applications/%APP\_RANDOM\_ID%/Documents/GXBlobData.zip  
> ---------------------------------------

**Where:**

*%USERNAME%*  
      Is your username

*%IOS\_TARGET%*  
      Is the target of the iPhone Simulator, for example "7.0.3".

**4.** Copy these three files to include them in the Xcode project. This filenames are *%**APP\_NAME**%.sqlite,* *%**APP\_NAME**%\_hashes.json* and GXBlobData.zip where *%**APP\_NAME**%* is the name of the application.

**Note**: If you have trouble finding this files, please check out the [HowTo: Look for offline database files](https://wiki.genexus.com/commwiki/wiki?23815) document.

#### [**Step 2: Add the preloaded database to the project**](#Step+2%3A+Add+the+preloaded+database+to+the+project)

**1.** In Xcode go to *Build Phases* and expand the section *Copy Bundle Resources.*

`[imagen omitida: wiki id 23756]`

**2.** Include the copied files to the project.

`[imagen omitida: wiki id 23758]`

**Important:**The file names must be respected because otherwise they will not be found by the application.

**3.** Build the project on Xcode. Now, when you run the application, the synchronizer process will not bring any data.

### [[Android](https://wiki.genexus.com/commwiki/wiki?14453) Applications](#wiki%3F14453%2CCategory%253AAndroid%2Bplatform+Android+Applications)

#### [**Step 1: Creating the database**](#Step+1%3A+Creating+the+database)

The first step to have preloaded data is to create the database

**1.** If you do not have a rooted phone, you have no access to the database unless you change the template to generate the database in sd card. To do that, follow the instructions mentioned in the [HowTo: Store Android offline database files in the device card](https://wiki.genexus.com/commwiki/wiki?23816) document.  
**2.** With the device connected to your PC and USB debugging enabled, open logcat and then run the application and let it execute the data synchronization process.  
**3.** Once the synchronization is complete, *logcat* will show a message similar to this one:

```
GeneXusApplication: DATABASE SYNCHRONIZATION FINISHED

GeneXusApplication: Database file: /mnt/sdcard0/Android/data/com.artech.eventdayoffline.eventday/EventDay.sqlite

GeneXusApplication: Hashes file: /mnt/sdcard0/Android/data/com.artech.eventdayoffline.eventday/EventDay_hashes.json
```

**4.** Copy both files to include them in the Android project. These filenames are *%APPNAME%.sqlite* and *%APPNAME%\_hashes.json* where *%APPNAME%* is the name of the application.  
If the application has blobs (images, videos) must also be copied the directory */mnt/sdcard0/Android/data/com.artech.eventdayoffline.eventday/files/blobs*

**Note**: If you have trouble finding these files, please check out the [HowTo: Look for offline database files](https://wiki.genexus.com/commwiki/wiki?23815) document.

#### [**Step 2: Add the preloaded database to the project**](#Step+2%3A+Add+the+preloaded+database+to+the+project)

**1.** Rename the copied file *EventDay.sqlite* to e*ventday\_sqlite*(change "." to "\_" and lowercase) and rename EventDay\_hashes.json to eventday\_hashes (remove the extension and lowercase). In addition, replace the dot "." present after the module name (if used) to an underscore "\_" (the names will be something like *modulename\_eventday\_sqlite* and *modulename\_eventday\_hashes*)  
**2.** Add the files *EventDay\_sqlite* and *EventDay\_hashes* in the directory *raw* of the project generated (*\mobile\Android\Main>\src\main\res\raw*) and the directory blobs in the directory assets (*\mobile\Android\<Main>\assets)*

**Important:** The file names must be respected because otherwise they will not be found by the application.

**3.** For security, revert the change made in Step 1.1.  
**4.** Build the app on Genexus. Now, when you run the application, all the data and images are going to be in the device without synchronizing them.

### [Advanced concepts](#Advanced+concepts)

#### [**Preloaded Hashes**](#Preloaded+Hashes)

The application's backend (server-side) keeps track of the synchronization hashes by {device, application}. When you preload a database, the DeviceId of the simulator or device used is stored with the hashes that correspond to the preloaded data.

If you synchronize again using the same simulator or device, then the original hashes will be removed from the server database, and no other device will be able to synchronize.

That's why you **must not** use the simulator or device used to generate the preloaded database to synchronize again.

#### [A possible workaround is to identify the preloaded hashes in the database, by changing the GXDeviceId in the GXDEVICERESULT table.](#A+possible+workaround+is+to+identify+the+preloaded+hashes+in+the+database%2C+by+changing+the+GXDeviceId+in+the+GXDEVICERESULT+table.)

To do that, after executing the first synchronization in the process described above, you may run the following SQL query:

```
UPDATE [GXDEVICERESULT] SET [GXDeviceId] = "Preloaded Data";
```

**Notes**:

* Device identifiers are UUIDs because that's what the devices send, but the GXDeviceId field is defined as Character(127).
* The update sentence updates **all** records in the GXDEVICERESULT table. If the database already has production data, you will want to filter by the GXDeviceId. To do that, you'll need to find the identifier used by the simulator or device, for example by looking at the headers in the synchronization HTTP request.


|  |
| --- |
| **Backlinks** |
| [Automatic Offline Data Synchronization](https://wiki.genexus.com/commwiki/wiki?22267) | [Data Synchronization](https://wiki.genexus.com/commwiki/wiki?22269) | [Events App scenario](https://wiki.genexus.com/commwiki/wiki?23775) |
| [Extract Zip property](https://wiki.genexus.com/commwiki/wiki?56753) | [HowTo: Convert online applications into offline applications](https://wiki.genexus.com/commwiki/wiki?24591) | [HowTo: Look for offline database files](https://wiki.genexus.com/commwiki/wiki?23815) | [HowTo: Store Android offline database files in the device card](https://wiki.genexus.com/commwiki/wiki?23816) |
| [Toc:Offline Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?22228) | [Synchronization API](https://wiki.genexus.com/commwiki/wiki?23602) | [Synchronization.ResetOfflineDatabase method](https://wiki.genexus.com/commwiki/wiki?29785) |

---
