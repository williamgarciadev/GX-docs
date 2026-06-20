---
title: "GeneXus SDK for SAP Leonardo: Using a pretrained ML service"
source_id: 41859
source_url: https://wiki.genexus.com/commwiki/wiki?41859
genexus_version: "18"
---

# GeneXus SDK for SAP Leonardo: Using a pretrained ML service

Calling SAP Leonardo ImageClassification Service from a GeneXus application.

In this first sample, we will work using the Pretrained SAP Services (SAP API Business Hub) with the security approach through APIKey.

For this reason, only for the service published here, GeneXus SDK for SAP Leonardo, has a Domain, called Settings, where the developer can storage two values:

Base URL for SAP Leonardo Machine Learning Services, initialized with ‘https://sandbox.api.sap.com/ml/’

APIKey, where the developer sets the value corresponding to the user, for test purposes.

`[imagen omitida: wiki id 42012]`

-Download and Import SDK Module

Start by including the SDK module in your Knowledge Base, to do so you can follow the steps in this [article](https://wiki.genexus.com/commwiki/wiki?41182)

-Creating a Transaction.

Create a GeneXus Transaction object by right-clicking on the Root Module and selecting New->Transaction

`[imagen omitida: wiki id 41798]`

Name the transaction object as 'ImageClassification' and click Create.

The Transaction will be displayed in the main panel.

`[imagen omitida: wiki id 41891]`

Since in this particular case you will store images to classify, you are going to describe three main attributes:

* Id – Unique key to identify a record, set as a numeric type. As default, the Numeric(4) type is assigned.
* Description- The description assigned to the image, set as a variable character field VarChar type.
* Image- The image itself. For this type of data, GeneXus has the Image type.

We can observe that GeneXus in most cases infers the data type according to the name of the attribute.

If the developer presses the dot character (.) while having the prompt in an attribute name line, GeneXus will add the name of the transaction. Therefore the developer will only need to enter the rest of the attribute name.

(Naming attributes in a unique way throughout the Knowledge Base is a **highly recommended** practice since GeneXus infers through the attribute name, valuable information that saves a lot of development time)

After describing the attributes, the transaction should look like this.

`[imagen omitida: wiki id 41892]`

The asterisk shows that the objects have unsaved changes. Once the transaction changes are saved, the asterisk character at the end will disappear.

Now save your work by clicking the diskette Icon or pressing Ctrl+S.

- Applying Fiori Pattern in a GeneXus Object

To apply the pattern, go to the 'Patterns' selector in the transaction object and click on Initialize Fiori.  
`[imagen omitida: wiki id 41893]`

Applying Fiori Pattern for the first time in the Knowledge Base involves the automatic generation the FioriBaseObjects Module.

`[imagen omitida: wiki id 41803]`

FioriBaseObjects Module is now included in our Knowledge Base. From this point on, you only have to choose which Fiori floorplan want to apply to your GeneXus Object.

`[imagen omitida: wiki id 41894]`

To select a floorplan for a GeneXus Object, go to 'Patterns' selector and click 'Select Floorplan'.

`[imagen omitida: wiki id 41895]`

A list of different floorplans is shown. Select List Report floorplan.

`[imagen omitida: wiki id 41928]`

Now save your work by clicking the diskette Icon or pressing Ctrl+S to apply the floorplan.

`[imagen omitida: wiki id 41897]`

-Create Classify button

User actions can be created in the ListReport as buttons.

Right click on 'Grid' element in the right panel and select New->User Action.  
`[imagen omitida: wiki id 41898]`

Now, set the Name property to "Classify" and the Caption property to "Classify" . Now you can see the button at the end of the List Report registry.

`[imagen omitida: wiki id 41899]`

-Creating Web Panel (with Image and Grid)

To create a new Web Panel right click on the Root Module and select New->Web Panel

`[imagen omitida: wiki id 41900]`

Name the Web Panel 'ViewClassificationSample’ and click Create.

`[imagen omitida: wiki id 41901]`

Now save your work by clicking the diskette Icon or pressing Ctrl+S. The web panel now will appear in your KB explorer.

There are four main elements that we want to show in this web form.

1. The image selected to process.
2. A Grid object to list the following elements (3 & 4).
3. The categories in which the service has classified the image.
4. The matching percentage for each category.

1- To add an Image drag the Attribute/Variable control from the toolbox to the Web Panel.

Upon dragging the control, you can observe a window panel showing all attributes and variables defined in our Knowledge Base.

In this case, you will need to create a new variable, so click New Variable.

`[imagen omitida: wiki id 41902]`

Now, name the Variable 'ProcessedImage'. GeneXus will automatically infer the variable type since the variable ends in Image. Click OK.

`[imagen omitida: wiki id 41903]`

The Web Panel will look like this.

`[imagen omitida: wiki id 41904]`

Make sure that the Label Position property is set to ‘None’.

Set the AutoResize property to ‘False’, so the image has a fixed size.

Set Width property to ‘450px’.

`[imagen omitida: wiki id 41905]`

2- Add a Grid control dragging the item from the toolbox to the bottom of Web Form.

`[imagen omitida: wiki id 41906]`

3-Click New Variable to create a variable to be displayed in the Grid.

`[imagen omitida: wiki id 41907]`

To specify the Category variable, name the variable as ‘Category’ and select ‘Varchar’ as Data Type, with Maximum length assigned to ‘100’. When completed click Ok.

`[imagen omitida: wiki id 41908]`

Once the variable is added the Web Panel will look like this

`[imagen omitida: wiki id 41839]`

4-Now add a second Variable to the Grid, dragging the Attribute/Variable control to the right side of the Grid control.

`[imagen omitida: wiki id 41909]`

Once the control is placed, click on ‘New Variable’ after the windows form appears.

`[imagen omitida: wiki id 41910]`

Name the variable ‘MatchPercentage’ and assign the Data Type property to ‘Numeric’ with Length property set to ’10’ and Decimals property set to ‘5’.

Click Ok.

`[imagen omitida: wiki id 41911]`

Now your Web Panel will look like this.

`[imagen omitida: wiki id 41912]`

Now save your work by clicking the diskette Icon or pressing Ctrl+S.

As this panel will work with the Image Id (ImageClassificationId), it is required to define the input parameters to call this object.

To do this, we have to select the ‘Rules’ tab next to the WebForm tab.

In this tab, we can specify rules to this particular object.

`[imagen omitida: wiki id 41913]`

To define the input in the rules editor, specify the following line.

```
parm(in:ImageClassificationId);
```

parm is the rule that defines the input and output parameters; they can be in for input, out for output or inout for input/output.

Save your web panel pressing Ctrl+S or clicking the diskette icon.

-Link Classify button to Web Panel.

To link the Classify button to the Web Panel, click on the transaction and select the User Action added. Click the GX Object property to bind the Web Panel.

`[imagen omitida: wiki id 41914]`

All GeneXus objects will be displayed; you may want to filter using Pattern textbox.

Once you have found the ViewClassificationSample WebPanel, select OK.

`[imagen omitida: wiki id 41915]`

As the web panel object to be called has the input parameter of ImageClassificationId, you have to assign it to the User Action.

First, you need to define that the User Action sends a set of parameters.

Right click on User Action->Add->Parameters.

`[imagen omitida: wiki id 41916]`

You just the defined that the user action control sends a set of parameters, but you need to specify which are those parameters.

Right Click on Parameters->Add->Parameter.

`[imagen omitida: wiki id 41917]`

After adding the parameter, you have to set the name of the parameter in the properties.

`[imagen omitida: wiki id 41918]`

Name it ‘ImageClassificationId’

After naming the parameter, save by clicking the diskette icon or press Ctrl+S.

`[imagen omitida: wiki id 41919]`

-Code Service call upon load event of the web panel

The final step is to program the SAP Leonardo Machine Learning service call to process the image and work with the results on the web panel.

In the 'ViewClassificationSample' web panel, select the 'Events' Tab and from the dropdown list, click on Load.

`[imagen omitida: wiki id 41920]`

Once selected the following code will appear denoting the beginning and the end of the Load Event block.

```
Event Load

Endevent
```

Inside of the event Load we will write this code.

```
     Event Load
     for each           
             &ProcessedImage = ImageClassificationImage
             &ImageClassificationBlob = ImageClassificationImage
       endfor

       &ImageClassificationFile.Source = &ImageClassificationBlob

      //Call SAP Leonardo API for Image Classification
      &IsResultOK = GeneXusSAPLeonardo.ImageClassification.POSTInferenceSync(&ImageClassificationFile,'','', &ResponseOkOUT, &ResponseErrorOUT, &ErrorOUT, &Message)

      if &IsResultOK
          for &ClassificationResults in &ResponseOkOUT.predictions
              for &Classification in &ClassificationResults.results
                  &Category = &Classification.label                         
                  &MatchPercentage = Round(&Classification.score * 100, 2 ) 
                  load
              endfor
          endfor
      endif
Endevent
```

What this code does, it will be reviewed line by line.

Before reviewing the code, define the variables and its types.

|  |  |
| --- | --- |
| **Variable Name** | **Data Type** |
| ImageClassificationBlob | Blob |
| ImageClassificationFile | File |
| IsResultOK | Boolean |
| ResponseOkOUT | ResponseOk, GeneXusSAPLeonardo.ImageClassification |
| ResponseErrorOUT | ResponseError, GeneXusSAPLeonardo.ImageClassification |
| ErrorOUT | Error, GeneXusSAPLeonardo.ImageClassification |
| Message | Messages.Message, GeneXus.Common |
| ClassificationResults | ClassificationResult, GeneXusSAPLeonardo.ImageClassification |
| Classification | Classification, GeneXusSAPLeonardo.ImageClassification |

It is important that the data type of a variable refers to the appropriate module, in this case as you are using the Image Classification service, the module is GeneXusSAPLeonardo.ImageClassification.

Take a look at what this code does.

```
 for each           
    &ProcessedImage = ImageClassificationImage
    &ImageClassificationBlob = ImageClassificationImage
 endfor
```

The [For Each command](https://wiki.genexus.com/commwiki/wiki?24744) performs a database query filtering registers where the registry id (defined in the Transaction object) is the same as the parameter provided id, once the Id matches, the register image data will be assigned to the image variable.

The registry image data will also be assigned to a blob type variable; this will be of use for the next line.

```
&ImageClassificationFile.Source = &ImageClassificationBlob
```

The image retrieved from the database is assigned as the source of the file to be processed by the Image Classification service.

Now you have all the required data to call the service.

```
&IsResultOK = GeneXusSAPLeonardo.ImageClassification.POSTInferenceSync(&ImageClassificationFile, '', '', &ResponseOkOUT, &ResponseErrorOUT, &ErrorOUT, &Message)
```

The service call returns a Boolean indicating whether the service executed successfully or not.

The POSTInferenceSync method is included in GXSAPLeonardo.ImageClassification module and has the following parameters.

|  |  |  |  |
| --- | --- | --- | --- |
| **Parameter** | **In/ Out** | **Data Type** | **Value passed** |
| &file | In | File | &ImageClassificationFile |
| &options | In | Varchar(256) | ‘ ’ |
| &Oauth2\_ClientCredentials | In | Character(20) | ‘ ‘ |
| &ResponseOkOUT | Out | ResponseOk, GeneXusSAPLeonardo.ImageClassification | &ResponseOkOUT |
| &ResponseErrorOUT | Out | ResponseError, GeneXusSAPLeonardo.ImageClassification | &ResponseErrorOUT |
| &ErrorOUT | Out | Error, GeneXusSAPLeonardo.ImageClassification | &ErrorOUT |
| &HttpMessage | Out | Messages.Message, GeneXus.Common | &Message |
| &IsSuccess | Out | Boolean | &ResultOK |

The service call will load the elements in the structure of the ImageClassification Service objects.

To display the results, we have to read the information loaded in those objects as a result of the service call.

```
if &IsResultOK
   for &ClassificationResults in &ResponseOkOUT.predictions
       for &Classification in &ClassificationResults.results
           &Category = &Classification.label                                      
           &MatchPercentage = Round(&Classification.score * 100, 2 )              
           load
        endfor
    endfor
endif
```

If the procedure executed without errors you iterate through every Classification results in the response (In this case, since you called the service for one image, there will be only one item, but the service can process more than one image in one call, this is due that the call allows .zip files as file parameters).

For each classification in the Classification Result, the name of the category in which the object was classified and its matching score to that category is loaded in the grid (using the load command).

Now you are ready to Build and Run your application. Press F5 or click Run `[imagen omitida: wiki id 41864]`

This is the main menu of the application. Click on the Image Classification Sample tile to access the Fiori List Report.

`[imagen omitida: wiki id 41921]`

The List Report shows no elements. Click Insert to add a new element.

`[imagen omitida: wiki id 41922]`

To add a new element enter a unique Id: '0'.

Choose a name for the image: 'Puppy'.

Select the image clicking the Change button.

`[imagen omitida: wiki id 41923]`

After browsing for the image select Confirm.

`[imagen omitida: wiki id 41868]`

Now that you have selected the image click on confirm to create the registry.

`[imagen omitida: wiki id 41924]`

Once the image is listed, click on 'Classify' to call SAP Image Classification service.

`[imagen omitida: wiki id 41925]`

This is the result.

The image displays the service call results, classifing it acording to default categories inclueded in the pretrained model of the Image Classification service available in SAP API Business Hub.

`[imagen omitida: wiki id 41871]`


|  |
| --- |
| **Backlinks** |
| [GeneXus SDK for SAP Leonardo: End User Documentation](https://wiki.genexus.com/commwiki/wiki?41183) |

---
