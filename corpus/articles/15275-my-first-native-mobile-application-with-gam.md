---
title: "My first Native Mobile application with GAM"
source_id: 15275
source_url: https://wiki.genexus.com/commwiki/wiki?15275
genexus_version: "18"
---

# My first Native Mobile application with GAM

In this article, you can learn how to have a login automatically in your Native Mobile application. Below, you have an easy guide for your first application using GAM, and the default credentials to enter the application for prototyping.

### [Step 0. Scope](#Step+0.+Scope)

This tutorial shows how it works in SQL Server and Android. It is recommended to read this paper before this one: [My first Android application](https://wiki.genexus.com/commwiki/wiki?14555).

### [Step 1. Set the Enable Integrated Security property](#Step+1.+Set+the+Enable+Integrated+Security+property)

* Create a new KB.
* Then set the [Enable Integrated Security Property](https://wiki.genexus.com/commwiki/wiki?14706) = True.

### [Step 2. Create your basic device application](#Step+2.+Create+your+basic+device+application)

* Create a Transaction called Transaction1 and apply the [Work With Pattern](https://wiki.genexus.com/commwiki/wiki?15974).
* Now create a Menu and add the workwithdevicestransaction1 as an item to it.

### [Step 3. Run it!](#Step+3.+Run+it%21)

Just press F5.

### [Step 4. Set your database connection properties](#Step+4.+Set+your+database+connection+properties)

`[imagen omitida: wiki id 51745]`

#### [Ready! Here is your login.](#Ready%21+Here+is+your+login.)

After running the application, you will see the login screen.

Use the following default credentials:  
Username: admin  
Password: admin123

### [How to Change an Administrator's Password](#How+to+Change+an+Administrator%27s+Password)

There are two methods to change an administrator's password in GAM:

#### [**1: Change Your Own Password**](#1%3A+Change+Your+Own+Password)

This method allows the logged-in user to change their own password. To do this, follow these steps:

* Run the web application and access the Developer Menu.
* Log in with the default credentials mentioned before.
* Go to the "Administrator User" menu and click on "Change password":

`[imagen omitida: wiki id 51746]`

**Note:** This method requires the user to know their current password.

#### [**2: Change Any User's Password**](#2%3A+Change+Any+User%27s+Password)

This method allows an administrator to change the password of any user without needing to know the user's current password.

To do this, follow these steps:

* Access the "Users" section in the GAM Backoffice.
* Find the user "admin" (or any other user).
* Click "Edit."
* Select "More Options."
* Click "Change Password."

**Note:** This method requires administrator privileges.


|  |
| --- |
| **Backlinks** |
| [Administrator User Password property](https://wiki.genexus.com/commwiki/wiki?15216) | [GAM - Getting Started](https://wiki.genexus.com/commwiki/wiki?19946) | [GAM - Native Mobile Authentication](https://wiki.genexus.com/commwiki/wiki?15222) |
| [Table of contents:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) | [HowTo: Configure GXflow Client for Native Mobile from xpz](https://wiki.genexus.com/commwiki/wiki?50551) | [Repository ID Environment property](https://wiki.genexus.com/commwiki/wiki?15802) |

---
