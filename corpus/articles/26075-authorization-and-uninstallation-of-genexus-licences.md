---
title: "Authorization and uninstallation of GeneXus licences"
source_id: 26075
source_url: https://wiki.genexus.com/commwiki/wiki?26075
genexus_version: "18"
---

# Authorization and uninstallation of GeneXus licences

In this article, you can find information on how to authorize and uninstall GeneXus Licences.

### [Authorization of GeneXus products](#Authorization+of+GeneXus+products)

This process explains how to add licences and authorize GeneXus on a computer where GeneXus is installed for the first time and there are no active installations.   
Upon opening your version of GeneXus, if you do not have any active licenses, you will be asked to make the corresponding request.

`[imagen omitida: wiki id 53434]`

To do so, select “Request Authorization” and select the products you wish to authorize:

`[imagen omitida: wiki id 53435]`

### [Methods to request Licenses](#Methods+to+request+Licenses)

Select one of the two methods available to request licenses:

* **Authorize Online:** In this case, the request for licenses is done through the internet. To make the request, you must complete the data required on the web form that will be displayed.
* **Generate Authorization File:** This option is to be used only when you do not have an internet connection on your PC. This option generates a file that contains your licenses’ Site Codes. Follow the steps indicated in the Wizard, and then send the generated file to your distributor, indicating the company for which the request is being made, the GeneXus account to which they should be assigned (this user must be the company’s contact), and the desired options:
  + Activate the product that is not activated.
  + Add time to the installation.
  + Add a number of licenses.

If you select Authorize Online:

`[imagen omitida: wiki id 53438]`

 A screen will open up to select the products you wish to authorize.

`[imagen omitida: wiki id 53439]`

Once the products have been selected, click on Finish.

Another way to make the request is through the GeneXus License Manager, located in the GeneXus menu: **Help > License Manager.**

You could also execute **GxLMgr.exe** from the directory where GeneXus is installed, and once there, click on the Select Computer button and select either Local License or Remote License. If you select Remote License, a dialog will appear for you to enter the IP address of the remote server.

`[imagen omitida: wiki id 53437]`

**Note**: The Remote License option may only be selected when [**GeneXus Protection Server**](http://www.genexus.com/protectionserver) **was previously installed in the computer that will be acting as license server.**

Next, click on the Authorize button, select the Request Licenses option to select the components you want to authorize (what you have purchased), and click on Next.

### [Fill out request information](#Fill+out+request+information)

After selecting the products, you will be redirected to a web page to fill out your request’s data. But before that, you must log in, indicating your GeneXus account (username or Email) and password.

`[imagen omitida: wiki id 53441]`

Once you are logged in to the site, the next step is to indicate:

* The email address where you want the authorization key to be sent
* The company for which you are the contact.

`[imagen omitida: wiki id 53440]`

After entering the ID data, click on the Continue button.   
In the following screen, you will see data on the request, where you may introduce any necessary changes.   
If you do not have the permissions to request licenses, you may make the request but you will need your company’s Contact Administrator to authorize your request.

`[imagen omitida: wiki id 53469]`

In the event that you do have the permissions to make a request, the reply could either be immediate or it might depend on the approval of your distributor.

`[imagen omitida: wiki id 53470]`

The possible changes you may introduce in the request are as follows:

* Remove products you do not wish to activate from the request (with the checkbox located to the left of the product).
* The type of action you want to perform with the license:
  + Request a full authorization
  + Add users to the existing installation
  + Change the activation period of your licenses.

The activation period of a product (restriction) may be:

* Limited to a given number of days (you can change it with the "Change Restriction" option in the "Type" section)
* Unlimited, with the product active indefinitely, and no number of days defined.

As you introduce changes to the product, the system will indicate whether the request is accepted immediately or if it depends on the approval by an operator.

In case you encounter indications on certain products, you may:

1. Modify the request so that it matches the features of your product (for example: reduce the number of licenses or adjust the number of days, etc.)
2. Remove the product so that it will not be processed. This will enable you to continue processing the remaining products.
3. Maintain the request for the product, where you will have to clearly explain the reasons for requesting product(s) with errors.

After entering the request’s information and the comments necessary, press the “Finish” button.

`[imagen omitida: wiki id 53471]`

If the request is processed immediately, in the following screen you will be able to download the activation of the products you requested. The activation will also be sent to the email address you indicated in the identification step. The products that could not be processed immediately for administrative reasons will be sent to GeneXus for further processing.

`[imagen omitida: wiki id 53443]`

### [Activate product](#Activate+product)

When you download or receive by email the file with .gxa extension, copy it to disk and execute the GeneXus License Manager again.  
Click on the Authorize button and select the Enter Licenses option. Then, click on Next:

`[imagen omitida: wiki id 53444]`

Select the Authorize from file option and find the .gxa file you saved previously:

`[imagen omitida: wiki id 53466]`

`[imagen omitida: wiki id 53467]`

After selecting the .gxa file, click on Finish and the authorization result ("Product Successfully authorized") will be shown:

`[imagen omitida: wiki id 53468]`

### [Authorization of new versions of GeneXus products](#Authorization+of+new+versions+of+GeneXus+products)

To change the version, you must uninstall the authorized licenses (refer to “Uninstallation of GeneXus products”) and then go through the authorization process for the new version (refer to “Authorization of GeneXus products” in this document).

### [Uninstallation of GeneXus products](#Uninstallation+of+GeneXus+products)

The license uninstall process depends on the version of the product that you have installed. The two possible options are described here.

#### [Uninstalling by email](#Uninstalling+by+email)

Follow these steps to uninstall a GeneXus license by email:

1. Execute the GeneXus License Manager located in the GeneXus menu in **Help > License Manager**. You may also execute GxLMgr.exe from the directory where GeneXus is installed.
2. From the list of products displayed, select the product you want to uninstall and press the Uninstall button.​ `[imagen omitida: wiki id 53447]`
3. A new window is displayed to indicate, in the “Copies to Uninstall” field, the number of licenses to uninstall: `[imagen omitida: wiki id 53551]`

       4. Click on the "OK" button and the following message will be displayed: `[imagen omitida: wiki id 53449]`

**Note:** It will also redirect you to an Internet browser to uninstall online. Close that browser and continue with the steps to uninstall by email.

       5. Copy the .gxa file mentioned in the path code and send it by email to your distributor, also indicating your company’s name, the product, and the version being uninstalled.

       6. Press the “Close” button.

#### [Uninstalling through the Web](#Uninstalling+through+the+Web+)

The latest versions of GeneXus can be uninstalled through the web. In these cases, the process is as follows:

1. Execute the GeneXus License Manager located in the GeneXus menu in  **Help > License Manager**. You may also execute GxMgr.exe from the directory where GeneXus is installed.
2. From the list of products displayed, select the product to be uninstalled and press the Uninstall button. `[imagen omitida: wiki id 53447]`
3. In the new window displayed, indicate, in the “Copies to Uninstall” field, the number of licenses to be uninstalled, and press the OK button.
4. If you have an internet connection, you will immediately be redirected to a web page to fill out data on the uninstallation. Prior to this, you must log on, indicating your GeneXus account (user or Email and password). `[imagen omitida: wiki id 53456]`
5. After the login you will be able to view data about the uninstallation you made: `[imagen omitida: wiki id 53455]`
6. If you do not have an internet connection, or if you could not perform the process as indicated above, you should email your distributor with the most recent file named Key\_code.gxa, which is in the directory where GeneXus is installed. The file’s location will be indicated at the time of uninstallation:  
   `[imagen omitida: wiki id 53453]`

### [States shown in the GeneXus License Manager window for each product](#States+shown+in+the+GeneXus+License+Manager+window+for+each+product)

In the GeneXus License Manager window, the protection status is shown for each of the products. They can be as follows:

|  |  |
| --- | --- |
| Authorized | Correctly authorized. |
| Not authorized | Not authorized. |
| Uninstalled | Not installed. |
| Error | Protection failure. It can be shown when you go over the deadline (<1999 or> 2126). |
| Suspended, data changed | Protection suspended; a backward change has been made to the date of the machine. |
| Time Runout | The authorized period of days to run has expired. |
| Runs Runout | The number of authorized runs has ended. |
| Suspended, authorization data changed | Suspended; the license information could not be read correctly. |

### [See Also](#See+Also)

[HowTo: Work with GXflow license manager](https://wiki.genexus.com/commwiki/wiki?37207)
