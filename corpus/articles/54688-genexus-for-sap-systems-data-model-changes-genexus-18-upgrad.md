---
title: "GeneXus for SAP Systems Data Model changes (GeneXus 18 Upgrade 3 or prior)"
source_id: 54688
source_url: https://wiki.genexus.com/commwiki/wiki?54688
genexus_version: "18"
---

# GeneXus for SAP Systems Data Model changes (GeneXus 18 Upgrade 3 or prior)

Consider all the defined in [GeneXus for SAP Systems - Working with Attributes and Domains](https://wiki.genexus.com/commwiki/wiki?34180) and create a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) for countries. Click on **File > New > Object** in the GeneXus main menu and select "Transaction", call it "Country".

Create a country identifier attribute. As you can see, GeneXus assigned it the Id domain.

Create an attribute to store the name of the country, CountryName, which takes the Name domain.

`[imagen omitida: wiki id 53081]`

Save (Ctr + s).

Note that just as it did with Customer, GeneXus has automatically created the form in the [Web Layout](https://wiki.genexus.com/commwiki/wiki?8057) to add, edit and delete countries.  
   
Go back to the Attraction Transaction created in [GeneXus for SAP Systems - Working with Attributes and Domains](https://wiki.genexus.com/commwiki/wiki?34180), so as to assign a country to each attraction. Note that typing the letter C displays the list of attributes existing in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) that begin with this letter.

`[imagen omitida: wiki id 53083]`

Select CountryId, and its entire definition is displayed.

Also, include the CountryName attribute in this Transaction. It's useful to see the country´s name when this Transaction object is executed and a country identifier is selected.

Focus on these two attributes included in more than one Transaction, in order to find out what role they play in Attraction.

`[imagen omitida: wiki id 53084]`

Remember that CountryId is the **identifier** or **key** in the Country Transaction:

`[imagen omitida: wiki id 53085]`

To be more precise, CountryId is the [Primary Key](https://wiki.genexus.com/commwiki/wiki?1868) of the Country Transaction and when a Primary Key is included in another Transaction, it has the role of a foreign key.

`[imagen omitida: wiki id 53086]`

Including an attribute that is a Transaction's Primary Key in another Transaction relates them both. This means that when executing the Attraction Transaction, for this attribute you will have to enter a value that has been previously recorded through the Country Transaction.

`[imagen omitida: wiki id 53087]`

See it at runtime.

Remember to open the tunnel to connect the schema to the HANA database.

Press the Build All option.

GeneXus analyzes the impact caused by the new definitions made on the Knowledge Base

`[imagen omitida: wiki id 53088]`

and informs you that a new Table called Country will be created in the database with the CountryId and CountryName fields.

In addition, a new Table called Attraction will also be created with the fields AttractionId, AttractionName and CountryId.

`[imagen omitida: wiki id 53089]`

Note that in the Attraction physical Table that GeneXus will create, the CountryName attribute is not included, even though you had included it in the Attraction [Transaction Structure](https://wiki.genexus.com/commwiki/wiki?7661). This happens because the Transaction concept is not the same as the physical Table concept. Remember that Transaction is the GX object created in the Knowledge Base to represent an object or actor of reality. By examining it, GeneXus creates a Physical Table in the database, to store the data that will be entered when executing the Transaction.

`[imagen omitida: wiki id 34350]`

Not all the attributes included in a Transaction structure will later be stored in the physical Table created based on this Transaction.

`[imagen omitida: wiki id 34351]`

Storing the country´s name in several physical Tables would mean storing duplicate data.

`[imagen omitida: wiki id 34352]`

Instead, the country name can be retrieved from a single location where it is stored, in this case, from the country Table.

`[imagen omitida: wiki id 34353]`

Go back to the development environment and click on Reorganize. The term **Reorganize** means to reorganize the database. It refers to the task of making changes to it.

GeneXus creates the programs to change the database and executes them, making any necessary changes. Next, it generates all the programs corresponding to the application itself. For example, for each new Transaction that has been defined, programs in the selected programming language to enter, change and delete countries and tourist attractions were generated.

Go to View > Other Tool Windows > Launchpad

`[imagen omitida: wiki id 53090]`

Now, there are links to work not only with clients but also with attractions and countries.

Add data about some countries. Click on Country and this will open the browser.

`[imagen omitida: wiki id 53115]`

Since the CountryId attribute was previously defined as belonging to the Id domain and this domain has the [Autonumber property](https://wiki.genexus.com/commwiki/wiki?6798) set to True, there's no need to enter a value for the identifier because it will be numbered automatically. Add Brazil, France and China and execute the Attraction Transaction.

Add the tourist attraction “Louvre Museum”. You don’t have to enter a value for the identifier, so just type the name “Louvre Museum”. Indicate that the Louvre Museum is in France.

If you remember the identifier number of France, enter it.

`[imagen omitida: wiki id 53116]`

Note that the country´s name can´t be changed from here, because it is displayed only for reading purposes.

Remember that a selection arrow was automatically displayed next to CountryId, providing a list of available countries.

The arrow was displayed next to this attribute in particular because, as previously stated, CountryId is a foreign key here.

So, here the user will have to enter a value that has been previously registered as primary key value through the Country Transaction. Therefore, GeneXus collaborates by generating and offering a list of countries available.

Now, you will see at runtime how the Country and Attraction Transactions check that the values entered for the CountryId attribute are consistent.

Enter a new attraction, such as the “Pyramids of Egypt”. In the country field, enter the value "4", but an error message is displayed because country number 4 doesn’t exist.

`[imagen omitida: wiki id 53093]`

Check the registered countries and you will see that only countries 1, 2 and 3 have been entered, but not 4.

Likewise, if you want to change an attraction that has already been entered and try to replace its country with another one that doesn't exist —4 again— you will get the same error message:

`[imagen omitida: wiki id 53094]`

That is to say, when you enter or change data through Transactions, the associated data is automatically checked for consistency. Also, when trying to delete data through Transactions, the necessary controls are made to maintain the consistency of the stored data.

Now, for instance, when trying to delete the country France:

`[imagen omitida: wiki id 53117]`

A message will be displayed, informing that the deletion cannot be performed because related data exists in Attraction (remember the Louvre Museum, which belongs to France).

Something very important to take into consideration is that attributes must be named using exactly the same name when they are related to the same concept.

For example, suppose that you type "CountryIdentifier" instead of "CountryId" in the Attraction Transaction. They will be different attributes for GeneXus.

`[imagen omitida: wiki id 34368]`

Therefore, GeneXus won't check whether the value entered in the CountryIdentifier attribute of the Attraction Transaction exists in the Table Country.

Hence, it won't offer the country selection list in the Attraction Transaction.

Also, it won't be possible to retrieve the name of the corresponding country. Because CountryName is referenced in the Attraction Transaction due to the fact that CountryId plays the role of foreign key, retrieving its corresponding CountryName.However, CountryIdentifier is not a foreign key, as it isn’t the primary key of any Transaction, so it isn’t possible to retrieve data associated with this attribute.

Represent more features of the travel agency's reality. Another requirement is that every attraction has an associated category to indicate if it is a monument, museum, park, and so on.

`[imagen omitida: wiki id 34372]`  
   
Here, the same situation that was mentioned with countries arises. Create a "Categories" Transaction and assign the attractions’ categories.  
Create the Category Transaction with CategoryId and CategoryName.

`[imagen omitida: wiki id 34392]`

Now, add the CategoryId and the CategoryName attributes to the Attraction Transaction.

`[imagen omitida: wiki id 34373]`

Before trying this at runtime, allow the category not to be set, as you don't know its value at the time of entering the attraction.   
This is done by changing the value of the [Nullable property](https://wiki.genexus.com/commwiki/wiki?7642) of the CategoryId attribute. Set it to Yes:

`[imagen omitida: wiki id 34374]`

This only makes sense for foreign keys that reference values from another Table.

Implement another request of the travel agency: For each attraction, they want to enter its photo. So, in the Attraction Transaction, enter an attribute called AttractionPhoto.  
It will be of Image type because this type makes it possible to store images.

`[imagen omitida: wiki id 34375]`

Now, press F5 to apply the changes to the database and programs and run the application.  
Note that a new Table will be created in the database to store the categories.

`[imagen omitida: wiki id 53096]`

Click on Attraction:

`[imagen omitida: wiki id 53097]`

The Attraction Table has to be converted, which means that the CategoryId and AttractionPhoto attributes will be added.

This element is added to store the file and to give the option to only reference a URL to it.

`[imagen omitida: wiki id 34378]`

Press the REORGANIZE button.

Run the Category Transaction from the Launchpad:

`[imagen omitida: wiki id 53098]`

Add the categories Museum and Monument.

Execute the Attraction Transaction, note that it allows you to enter a category and a photo.

`[imagen omitida: wiki id 53099]`

Search for the Louvre Museum, assign the Museum category and a photo to it.

`[imagen omitida: wiki id 53100]`

Confirm.

A special feature of SAP HANA makes it possible to use Table row storage instead of column storage.

To do so, pay attention to when View > Tables is opened:

`[imagen omitida: wiki id 53101]`

Here, GeneXus shows all the Tables of the corresponding database.

`[imagen omitida: wiki id 53102]`

By clicking on one of the Tables, you will see that among its properties there's one that is related to the type of storage in a SAP Hana database.

`[imagen omitida: wiki id 34385]`

If you're trying to create a Table and the percentage of transactional operations (that is to say, INSERT, UPDATE and DELETE operations) is very high, using row storage is recommended, because it is the default value. Also, it is how traditional relational DBMSs work.

For SAP Hana, there is an option to use column storage, which is useful when the Table being designed has a very high percentage of reading operations (SELECT).   
If this is the case of ATTRACTION, change that value.
