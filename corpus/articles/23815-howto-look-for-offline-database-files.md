---
title: "HowTo: Look for offline database files"
source_id: 23815
source_url: https://wiki.genexus.com/commwiki/wiki?23815
genexus_version: "18"
---

# HowTo: Look for offline database files

Getting your devices offline database files will help you significantly on testing and debugging the synchronization processes of your application.  
In this document is explained how to take access to these files whether using [Apple](https://wiki.genexus.com/commwiki/wiki?14917) or [Android](https://wiki.genexus.com/commwiki/wiki?14453) platform, and even if you are using real devices or simulators.

### [Using iOS Simulator:](#Using+iOS+Simulator%3A)

**1.** Every time you run a new application in the iOS emulator, a new folder with a random name is going to be created in */Users/<your\_user>/Library/Application Support/iPhone Simulator/<iOS target version>/Applications/*  
**2.** Find the folder that contains the application you have recently run:

`[imagen omitida: wiki id 23820]`

**Tip:** It could be useful to order folders by Date Modified.  
**Tip:**Since Mac OSX Lion, the Library folder is hidden by default. Anyway, it is possible to access that folder by using the "Go to folder..." action in the "Go" menu of Finder application.

**3.** Once you have found that folder, you will find the *.sqlite* file you were looking for in the *Documents*folder. It is named as *<AppName>.sqlite*, where *<AppName>* is the name of the main object associated with the offline database. If needed, the *<AppName>\_hashes.json* file is in the same folder.

`[imagen omitida: wiki id 23821]`

### [Using iOS Devices:](#Using+iOS+Devices%3A)

**1.** If you are using your iOS device to test your application, once you have run the application in Xcode, open the Organizer by going to Window > Organizer (Or by pressing Command+Shift+O)

**2.** Find your application by selecting the Applications section under your device on the left panel.  
**3.** Once you have found the application, you can download its content as a Xcode Application Data Package file (.xcappdata)

`[imagen omitida: wiki id 23822]`

**4.** To open that package, just right-click on it and select *“Show package content”*.  
**5.** After that, a Finder folder will pop up, and finally if you go to the *Documents* folder you will find the *<AppName>.sqlite* file you are looking for:

`[imagen omitida: wiki id 23823]`

If needed, the *<AppName>\_hashes.json* file is in the same folder.

### [Using Android Virtual Devices:](#Using+Android+Virtual+Devices%3A)

As said in the [HowTo: Store Android offline database files in the device card](https://wiki.genexus.com/commwiki/wiki?23816) document, you can decide whether to choose local storage, or choose the external storage (sdcard) to place the offline database files.

If local storage is selected, then the offline database files will be stored in the AVD at the following directory: */data/data/<Android Package Name>/files/db/*  
Otherwise, it is going to be stored in the following directory:*<External Storage>/Android/data/<Android Package Name>/files/db/*  
Where the *<Android Package Name>* is the value of the Main object [Android Package Name property](https://wiki.genexus.com/commwiki/wiki?17814) and *<External Storage>* is the path to the device external storage disk (it may vary on different devices), for example: "*/storage/sdcard/", "*/mnt/shell/emulated/sdcard/", among others.

Finally, you need to know the name of the offline database files, which are named like: *<appName>.sqlite* where *<appName>* is the name **in lower case** of the Main offline object. If needed, the *<AppName>\_hashes.json* file is in the same folder.

#### [Summarizing:](#Summarizing%3A)

* If using local storage, the full path will be: */data/data/<Android Package Name>/files/db/<appName>.sqlite*
* Otherwise, the full path will be: <External Storage>*/Android/data/<Android Package Name>/files/db/<appName>.sqlite*

Now that you have the full path of the file, you can get that file using the *adb push* command.

Open the cmd console and navigate towards *<AndroidSDKDirectory>/platform-tools*  
After that, execute the following command:

```
adb pull <fullDatabaseFilePath> <localPath>
```

Where *<localPath>* is the destination where you want the *.sqlite* file to be placed in your computer.

For example:

```
adb pull /data/data/com.artech.abcoffline.abcoffinetest/files/db/abcoffinetest.sqlite C:/temp/MyOfflineDatabaseFiles
adb pull /data/data/com.artech.abcoffline.abcoffinetest/files/db/abcoffinetest_hashes.json C:/temp/MyOfflineDatabaseFiles
```

### [Using Android Devices:](#Using+Android+Devices%3A)

If offline database files are going to be stored in the SD card, as explained in the [HowTo: Store Android offline database files in the device card](https://wiki.genexus.com/commwiki/wiki?23816) document, once you plug your Android device as a storing device, go to the following path in the sdcard device: *<sdcard path>\Android\data\<Android Package Name>\files\db*

Where the *<Android Package Name>* is the value of the Main object [Android Package Name property](https://wiki.genexus.com/commwiki/wiki?17814).  
The *<appName>.sqlite* file will be placed in that folder.

For example:

```
Computer\GT-P5110\Tablet\Android\data\com.artech.abcoffline.abcoffinetest\files\db\abcoffinetest.sqlite
Computer\GT-P5110\Tablet\Android\data\com.artech.abcoffline.abcoffinetest\files\db\abcoffinetest_hashes.json
```

#### [**Android Considerations**](#Android+Considerations)

All images referenced by the offline database are visible even if the device is offline, and you can find those images in the *files\blobs* folders.

### [How to open the SQLite DB](#How+to+open+the+SQLite+DB)

Once you copy the SQLite file to your PC you can use any Application to open it like [SQLSpy](http://www.yunqa.de/delphi/doku.php/products/sqlitespy/index)

### [See Also](#See+Also)

[HowTo: Create offline mobile applications with a preloaded database](https://wiki.genexus.com/commwiki/wiki?22298)  
[HowTo: Store Android offline database files in the device card](https://wiki.genexus.com/commwiki/wiki?23816)  
[Offline Database object](https://wiki.genexus.com/commwiki/wiki?22509)


|  |
| --- |
| **Backlinks** |
| [HowTo: Create offline mobile applications with a preloaded database](https://wiki.genexus.com/commwiki/wiki?22298) | [HowTo: Store Android offline database files in the device card](https://wiki.genexus.com/commwiki/wiki?23816) |

---
