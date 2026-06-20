---
title: "HowTo: Prototye an iOS Application on a Mac"
source_id: 14761
source_url: https://wiki.genexus.com/commwiki/wiki?14761
genexus_version: "18"
---

# HowTo: Prototye an iOS Application on a Mac

The purpose of this article is to explain the necessary steps to prototype your iPhone or iPad application on your Mac.

### [Step 1: Install requirements](#Step+1%3A+Install+requirements)

Check Mac requirements on [Apple Requirements](https://wiki.genexus.com/commwiki/wiki?19478)

### [Step 2: Enable ssh](#Step+2%3A+Enable+ssh)

Go to System preferences.

`[imagen omitida: wiki id 14762]`

Then, go to the Sharing option.

`[imagen omitida: wiki id 14763]`

Check Remote Login.

`[imagen omitida: wiki id 14764]`

**Note**: You need to allow access to the user you will be using to connect from your Windows computer.

### [Step 3: Change the default shell to bash](#Step+3%3A+Change+the+default+shell+to+bash)

The latest versions of macOS use **zsh** as the default shell, but it is not supported by GeneXus. You must change it to **bash**.

To do that, open Terminal.app and execute the following command:

```
chsh -s /bin/bash
```

The next time you open *Terminal.app*, it will be using **bash**. It will also be used when you connect via SSH (as GeneXus does).

### [Step 4: Set GeneXus properties](#Step+4%3A+Set+GeneXus+properties)

Set Mac Host, Mac User and Mac Password properties on GeneXus.

`[imagen omitida: wiki id 37577]`

**Values**

* **Mac Host:**Your Mac computer name (computer name property on the "Remote Login" settings).
* **Mac User:**User to connect the Windows computer to the Mac computer (allowed previously on the "Remote Login" settings).
* **Mac Password:**Mac user password.

### [Step 5: Run the application](#Step+5%3A+Run+the+application)

You can use the Mac computer for prototyping the application with all the benefits provided by Apple.

`[imagen omitida: wiki id 37578]`

### [Notes](#Notes)

* You can get a paid or free version from Apple. A benefit of getting the paid one is that it allows you to test the application on the device, not just using the emulator.  
  Anyway, to test with the device the [GeneXus Project Navigator](https://wiki.genexus.com/commwiki/wiki?14974) option exists, and it's quick and simple.
* This error message could appear during the transfer from GeneXus when the Sharing option is not enabled: *"No connection could be made because the target machine actively refused it".*
* You have to use Bash as default shell, or you will have an error similar to this: *"Error 1 reading target directory. error: zsh:1: parse error near `}'"*

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Prototyping features and Deployment of applications](https://training.genexus.com/en/learning/courses/genexus-for-mobile/mobile-applications-with-genexus-course-v16/prototyping-features-and-deployment-of-applications-for-smart-devices?p=3694)


|  |
| --- |
| **Backlinks** |
| [Category:Apple platform](https://wiki.genexus.com/commwiki/wiki?14917) | [Apple Requirements](https://wiki.genexus.com/commwiki/wiki?19478) | [Distributing applications with pre-loaded cache](https://wiki.genexus.com/commwiki/wiki?19351) |
| [Execution Type property](https://wiki.genexus.com/commwiki/wiki?18658) | [Generate Apple property](https://wiki.genexus.com/commwiki/wiki?18656) | [HowTo: Prepare a Mac with an Intel processor for GeneXus](https://wiki.genexus.com/commwiki/wiki?51408) | [iOS Specific properties](https://wiki.genexus.com/commwiki/wiki?31827) |
| [Mac Host property](https://wiki.genexus.com/commwiki/wiki?36371) | [Mac User property](https://wiki.genexus.com/commwiki/wiki?36372) | [Toc:Native Mobile Applications Development](https://wiki.genexus.com/commwiki/wiki?24799) | [Prototyping in iOS with a compiled application](https://wiki.genexus.com/commwiki/wiki?17380) |

---
