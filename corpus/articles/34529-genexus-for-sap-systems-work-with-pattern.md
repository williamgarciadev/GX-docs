---
title: "GeneXus for SAP Systems - Work With Pattern"
source_id: 34529
source_url: https://wiki.genexus.com/commwiki/wiki?34529
genexus_version: "18"
---

# GeneXus for SAP Systems - Work With Pattern

You have been developing a web application for a travel agency. To do so, you have created [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908)s, applied the Fiori pattern that creates objects as [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Procedures](https://wiki.genexus.com/commwiki/wiki?6293), etc., and you will continue to work in this way, developing objects until completing the web development.

`[imagen omitida: wiki id 34531]`

In this case, you have prototyped in a local server that accessed a Hana database through SAP Business Technology Platform. See [How to use SAP HANA Database on SAP Business Technology Platform](https://wiki.genexus.com/commwiki/wiki?47848)

`[imagen omitida: wiki id 34532]`

However, when the application is deployed, the programs built by GeneXus in Java will be saved in a server that can be accessed from the web.

`[imagen omitida: wiki id 34533]`

Therefore, the end user, with a browser and the URL of some of the app's pages will be able to run the corresponding object (built by GeneXus in Java). If necessary, it will make requests to the database and return the data to the browser so as to build the page with the retrieved data and display it to the user on the device screen.

`[imagen omitida: wiki id 34534]`

How is an application similar to the web application but native for Android and/or Apple devices obtained?

`[imagen omitida: wiki id 34535]`

This will be done by developing some specific GeneXus objects for mobile that will be compiled from a main object. GeneXus will compile that main object in Java for Android if the application is built for that platform, and in Swift for Apple if necessary. What is more, for these native apps to be able to access the data stored in the centralized database, one part of the web app (Java) is exposed as Rest services.

`[imagen omitida: wiki id 34536]`

Therefore, when the Android or Apple app needs data from the database, it will have to consume the corresponding Rest services. You doesn't need to worry about this, because it is hidden inside the logic of the GeneXus objects for mobile.

See this with an example:

To review what has been done in the web application, there's the app's home object –the Launchpad, which is a sort of menu.

`[imagen omitida: wiki id 53189]`

From this object, various lists (the Fiori List Report of countries and attractions) are invoked. The invocation to a Transaction called Customer has also been explicitly added.  That's left aside here as something similar, but for mobile, is required.

To do so, first, the equivalent pattern to the Fiori List Report of the selected Transactions needs to be applied.

Open the Patterns section of the Country Transaction and then select the [Work With](https://wiki.genexus.com/commwiki/wiki?5636) tab.

`[imagen omitida: wiki id 53190]`

The two screens that will be generated are clearly seen: one for the countries List and another one with detailed information about a country, with their two tabs displayed as “sections”.

The great difference is that here, these nodes will correspond directly to the objects generated and will not be “declared” by you so as to have them implemented by GeneXus later. Instead, they will be directly implemented. So, if you click on the List node:

`[imagen omitida: wiki id 53191]`

Here is its Layout, which has been initialized and has a grid that will show the value of the CountryName attribute of each country to be loaded from the database.

In addition, sections such as Rules, Events, etc. are enabled to define rules, events and other aspects of this object. That is to say, the sections that allow for its implementation are displayed.

Moreover, if the Detail is opened:

`[imagen omitida: wiki id 53192]`

You can see that the screen object only contains a control called <All Sections Content>. All the sections contained in this Detail will be loaded in this control. Here, there are two of them: one that shows the country's general information:

`[imagen omitida: wiki id 53193]`

Here, the attributes CountryId and CountryName are shown.

And the other one shows the country's attractions in a grid:

`[imagen omitida: wiki id 53194]`

The attributes AttractionPhoto and AttractionName have been placed here.

It will be clearer when you run it.

Select the check box to apply this pattern; before saving, take a look at the generators (of programs) that you have defined. So far, only one: for Web Java.

`[imagen omitida: wiki id 53195]`

Now, save.

For the frontend Android and Apple has been automatically added.

`[imagen omitida: wiki id 53196]`

By default, it will generate for Android and Apple, but Android will be the main platform:

`[imagen omitida: wiki id 53197]`

Note that below the Country node, the object WorkWithDevicesCountry is now displayed:

`[imagen omitida: wiki id 53198]`  
  
Unlike the web example, in which FioriCountry was only a declaration file and the objects that effectively implement the pattern features were built separately (they are listed below), in this case, it is a GeneXus object that will contain sub-objects that can be invoked independently using the corresponding syntax.

Apply the pattern to the Attraction Transaction and to Category.

How can you test this quickly? One option is to use a device connected to the computer in which GeneXus is running.  Another option is to use the emulators provided by the platforms. For simplicity purposes, use this option (testing on an actual device will always be better because the emulators don't have all their features available).

It is missing a menu —in the web environment you had the Launchpad— to invoke the Lists you are interested in.  This menu is not automatically created by GeneXus. You need to create it.

File > New > Object, filter by the objects for User Interface, and select the Menu, which is an object to implement menus. Call it TravelAgency:

`[imagen omitida: wiki id 53199]`

This will be the main object of the application for mobile devices. It will be the object compiled by GeneXus for Android and/or Apple and that the end user will install on his/her device, once the development work has been completed.

Enter the items you want to include in the menu:

`[imagen omitida: wiki id 53200]`

The first one will correspond to the action of invoking the List of countries:

`[imagen omitida: wiki id 53201]`

A window is opened to select the object you want to invoke when the user selects this menu item. Filter by object type Work With:

`[imagen omitida: wiki id 53202]`

Select WorkWithCountry.

Now see this action, which by default receives the same name as the object invoked. This action —double-click— will be associated with an event that programs the invocation:

`[imagen omitida: wiki id 53203]`

There, the List of the WorkWithCountry object is being invoked (not the Detail).

Open the action's properties and change the item Description, which will be displayed in the menu at runtime:

`[imagen omitida: wiki id 53204]`

Bearing in mind that mobile apps tend to be much more iconographic than web apps due to the reduced screen size, choose an image for this option. The image must be imported into the Knowledge Base from an external file. Now, add an item to invoke the attractions List.

Before running it, replace the Android property, “Base Cholor Scheme”, with 'Light with Dark action bar' so that the screen background is white with a dark “Action Bar”:

`[imagen omitida: wiki id 53205]`

To run it, right-click on its tab and select Run:

`[imagen omitida: wiki id 53206]`

To prototype this mobile application in Android please check [Android Requirements](https://wiki.genexus.com/commwiki/wiki?14449).

If you have an emulator installed with the Android Studio, the compiled file will be automatically installed there and will be run.

Otherwise, the default emulator of Android's SDK will be opened and the same will happen.

So, here you can see the menu running with the two items defined with their images and descriptions:

`[imagen omitida: wiki id 53207]`

Tapping on “Countries” displays the List of countries, which shows each country's name in a grid:

`[imagen omitida: wiki id 53208]`

As it was implemented, if a country is tapped:

`[imagen omitida: wiki id 53209]`

its details are shown with two tabs: the general information in one (which is implemented here):

`[imagen omitida: wiki id 34570]`

and the country's attractions in the other one:

`[imagen omitida: wiki id 53210]`

The attractions' photo and name is seen, as implemented here:

`[imagen omitida: wiki id 53214]`

Note that you can change or delete the country's information from the General tab:

`[imagen omitida: wiki id 53211]`

Change the name:

`[imagen omitida: wiki id 53212]`

Confirm.

The object that updated the database was one of the Rest services mentioned at the beginning.

`[imagen omitida: wiki id 34576]`

If you run the web application again and refresh the page:

`[imagen omitida: wiki id 53213]`

Here it is!

The country's update and delete buttons are displayed here in the WorkWith, in the application bar area:

`[imagen omitida: wiki id 53215]`

But, while in the web pattern the Transaction was invoked when trying to update or delete:

`[imagen omitida: wiki id 53216]`

(For example, here it is invoked in UPDATE mode:

`[imagen omitida: wiki id 53218]`  
  
and what you're viewing is the Transaction form)

In native mobile applications the same Detail is opened but with another screen: the edit screen:

`[imagen omitida: wiki id 53219]`

It looks exactly the same when initialized, except for the Save and Cancel buttons in the Application bar:

`[imagen omitida: wiki id 53220]`

`[imagen omitida: wiki id 53221]`

When the user clicks on the Save button, the device app will invoke, sending the data from this screen, the Rest service in the web server containing the Transaction logic, and therefore will update the information on the database. All this is done in a transparent manner, you will not have to worry about these low-level details.

Just like for the web pattern, if you return to the List, you will see that it is possible to add a new country:

`[imagen omitida: wiki id 53222]`

Here, the same screen is invoked for the Detail and for the Update.

Add Mexico:

`[imagen omitida: wiki id 53223]`

This is what the pattern generates by default. It can be customized, though.

If you open the Attractions List:

`[imagen omitida: wiki id 53224]`

The attraction's image and name are displayed in the grid. You may also want to add the attraction's category.

To do so, open the toolbox, drag the Attribute/Variable control, and select the CategoryName attribute:

`[imagen omitida: wiki id 53225]`

Change the Label Caption property:

`[imagen omitida: wiki id 53226]`

It could be deleted with Label position None.

Select Run, over the main object.

`[imagen omitida: wiki id 53227]`

Note that by default the option to make searches by attraction name is offered:

`[imagen omitida: wiki id 53228]`

This is configured in the grid's properties, here:

`[imagen omitida: wiki id 53229]`

You could add CountryName, for example, to allow making searches by country name as well.

`[imagen omitida: wiki id 34594]`

`[imagen omitida: wiki id 34595]`

So, if you search “Fr”… France's attractions are displayed.

There are also advanced filters, by the attributes CountryId and CategoryId, which are the foreign keys of the Attraction Transaction. Change the description to Country and Category, respectively, and run the main menu again…

Open the attractions List and see that this option is available in the application bar:

`[imagen omitida: wiki id 53230]`

If you look at the list, it is ordered by AttractionName. This is specified in the properties of the grid's Data group:

`[imagen omitida: wiki id 53231]`

`[imagen omitida: wiki id 34603]`

You may want to allow the user to order by country:

`[imagen omitida: wiki id 34604]`

Choosing the same option used for filtering:

`[imagen omitida: wiki id 53232]`

It can be ordered by Country:

`[imagen omitida: wiki id 53233]`

The Great Wall of China and the two attractions entered for France are seen.

You can try the same application for Apple by only changing these properties.

This was just a small example of what can be done. Just like for a web application, there are more objects available to cover other features, such as [Panel](https://wiki.genexus.com/commwiki/wiki?24829)s.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus for SAP Systems](https://wiki.genexus.com/commwiki/wiki?33616) |

---
