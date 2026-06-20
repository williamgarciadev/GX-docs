---
title: "My first BPM Native Mobile application"
source_id: 50516
source_url: https://wiki.genexus.com/commwiki/wiki?50516
genexus_version: "18"
---

# My first BPM Native Mobile application

This article describes how to create a [Business Process Diagram object](https://wiki.genexus.com/commwiki/wiki?16486) assigning [objects for Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?20087) to the user [Tasks](https://wiki.genexus.com/commwiki/wiki?17495).

If this is your first time creating a [Business Process Diagram object](https://wiki.genexus.com/commwiki/wiki?16486), it is recommended to read [My first BPM Application](https://wiki.genexus.com/commwiki/wiki?11218). If this is your first time using [Objects for Native Mobile applications development](https://wiki.genexus.com/commwiki/wiki?20087) it is recommended to read [My first Android application](https://wiki.genexus.com/commwiki/wiki?14555) or [My first iOS application](https://wiki.genexus.com/commwiki/wiki?14738).

The best way of explaining is by using examples. This document is based on [My first BPM Application](https://wiki.genexus.com/commwiki/wiki?11218), and so will be based on booking flight tickets.  
This simple and practical example illustrates the steps needed to complete it:

* Creating the process objects
* Creating the activity diagram that models the process
* Associating **Mobile** objects to the diagram
* Running the process

This is a simple example that shows how to use GXflow within the [IDE](https://wiki.genexus.com/commwiki/wiki?5272) to create a workflow for the [GXflow client for Native Mobile](https://wiki.genexus.com/commwiki/wiki?29037). As explained before, it represents a simplified process for booking airline tickets, which consists of entering the reservation details into the system, with the operator registering any customer that is not registered. If the customer is already registered, the control will go straight to checking availability. If the reservation is available, the process ends, and if it's not available, the flow will return to where the reservation was entered to update the data.

### [Step 1: Creating the objects that will be part of the process](#Step+1%3A+Creating+the+objects+that+will+be+part+of+the+process)

Two Transactions will be needed: Reservation and Customer.

#### [Reservation Transaction](#Reservation+Transaction)

`[imagen omitida: wiki id 5503]`

**Note**: The CustomerId attribute is defined to allow nulls, which is necessary for the example to work properly.

##### [*Rules*](#Rules)

CustomerId.SetNull() If CustomerId.IsEmpty();

#### [Customer Transaction](#Customer+Transaction)

`[imagen omitida: wiki id 5504]`

#### [ReservationMapRelevantData](#ReservationMapRelevantData)

Once the reservation is entered, it assigns the ReservationId and CustomerId [Relevant Data](https://wiki.genexus.com/commwiki/wiki?11759).

##### [*Rules*](#Rules)

Parm(ReservationId,CustomerId);

**Note**: ReservationId and CustomerId as attributes

##### [*Variables*](#Variables)

`[imagen omitida: wiki id 25424]`

##### [*Code*](#Code)

```
&WorkflowApplicationData = &Workflowcontext.ProcessInstance.GetApplicationDataByName("ReservationId")
&WorkflowApplicationData.NumericValue = ReservationId

&WorkflowApplicationData2 = &Workflowcontext.ProcessInstance.GetApplicationDataByName("CustomerId")
if not CustomerId.IsNull()
    &WorkflowApplicationData2.NumericValue = CustomerId
EndIf

Commit
```

#### [ProcCondAssignedCustomerId](#ProcCondAssignedCustomerId)

This Procedure checks if the Customer has been entered, returning 1 if so and 2 if not.

##### [*Rules*](#Rules)

Parm(in: &WorkflowProcessDefinition, in: &WorkflowProcessInstance, in: &WorkflowWorkitem, out: &ConditionalCode);

##### [*Variables*](#Variables)

`[imagen omitida: wiki id 25427]`

##### [*Code*](#Code)

```
&CustomerIdAppData = &WorkflowProcessInstance.GetApplicationDataByName('CustomerId')
&CustomerId = &CustomerIdAppData.NumericValue

if &CustomerIdmerId = 0
    &ConditionalCode = 2
Else
    &ConditionalCode = 1
EndIf
```

#### [CustomerMapRelevantData](#CustomerMapRelevantData)

Once the Customer is entered, it assigns the CustomerId [Relevant Data](https://wiki.genexus.com/commwiki/wiki?11759).

##### [*Variables*](#Variables)

`[imagen omitida: wiki id 25425]`

##### [*Code*](#Code)

```
&WorkflowApplicationData = &Workflowcontext.ProcessInstance.GetApplicationDataByName("CustomerId")
&WorkflowApplicationData.NumericValue = CustomerId

Commit
```

#### [AssignToCustomer Procedure](#AssignToCustomer+Procedure)

Once the reservation and user are entered, it assigns that reservation to that user.

##### [*Rules*](#Rules)

Parm(in:&ReservationId, in:&CustomerId);

##### [*Variables*](#Variables)

`[imagen omitida: wiki id 25428]`

##### [*Code*](#Code)

```
For each
     Where ReservationId = &ReservationId
             CustomerId = &CustomerId
Endfor
```

#### [ProcCondReservationAvailable](#ProcCondReservationAvailable)

This Procedure checks if the Reservation is available, returning 1 if so and 2 if not.

##### [*Rules*](#Rules)

Parm(in: &WorkflowProcessDefinition, in: &WorkflowProcessInstance, in: &WorkflowWorkitem, out: &ConditionalCode);

##### [*Variables*](#Variables)

`[imagen omitida: wiki id 25426]`

##### [*Code*](#Code)

```
&ReservationId = &WorkflowProcessInstance.GetApplicationDataByName('ReservationId')

For each
    Where ReservationId = &ReservationId.NumericValue
    if ReservationAvailable = False
        &ConditionalCode = 2
    Else
        &ConditionalCode = 1
    EndIf
EndFor
```

### [Step 2: Creating the activity diagram that models the process](#Step+2%3A+Creating+the+activity+diagram+that+models+the+process)

To add an activity diagram, all you have to do is add the [Business Process Diagram object](https://wiki.genexus.com/commwiki/wiki?16486), like with any other object.

`[imagen omitida: wiki id 25790]`

### [Step 3: Applying Work With Pattern for Smart Devices](#Step+3%3A+Applying+Work+With+Pattern+for+Smart+Devices)

Apply the Work With Pattern for Smart Devices to the Customer and Reservation Transactions, see [Applying Work With Pattern](https://wiki.genexus.com/commwiki/wiki?15975) for further details.

### [Step 4: Associating the objects to the diagram](#Step+4%3A+Associating+the+objects+to+the+diagram)

To mark the beginning of the process, drag a [None Start Event](https://wiki.genexus.com/commwiki/wiki?17347) symbol into the "TicketReservation" [Business Process Diagram object](https://wiki.genexus.com/commwiki/wiki?16486).

The first associated object will be the WorkWithDevicesReservation. To associate it, drag it from the [KB Explorer](https://wiki.genexus.com/commwiki/wiki?3210) to the line that connects the Start and End connectors in the diagram.

Or, drag a [User Task](https://wiki.genexus.com/commwiki/wiki?17495) from the [Toolbox](https://wiki.genexus.com/commwiki/wiki?16487) to the properties windows and press the button in the [Object property (BPD Task)](https://wiki.genexus.com/commwiki/wiki?25199). You can change its name by pressing the F2 button to "Reservation":

`[imagen omitida: wiki id 11219]`

You need to create Relevant Data with the same name and data type as the Transaction's primary key. This data, just like the rest of the relevant information, will be known throughout the flow.

Once the Relevant Data is created, open the [Object property (BPD Task)](https://wiki.genexus.com/commwiki/wiki?25199), and edit the Application to "WorkWithDevicesReservation.Reservation.**Detail**" and select the Relevant Data created before in the "Relevant Data" column. The purpose of this change is to call the WorkWithDevicesReservation in insert mode.  
The properties must be configured as shown below:

`[imagen omitida: wiki id 25430]`

Then open WorkWithDevicesReservation and edit the source of the 'Save' event as follows:

```
Event 'Save'
    Composite
        SDActions.Save()
        ReservationMapRelevantData.Call(ReservationId,CustomerId)
        return
    EndComposite
EndEvent
```

This is an important step. Relevant Data is not mapped automatically when using Smart Devices Objects, so the call to the Procedure *ReservationMapRelevantData* must be added.

The second step consists in adding the conditional that defines whether or not the customer is registered and associated with the reservation Transaction. To do so, add the exclusive gateway symbol from the diagram toolbar (by default it is located on the right-hand side of the screen), as shown in the figure below.

`[imagen omitida: wiki id 11220]`

Once the gateway has been inserted, you have to define the [Condition procedure property](https://wiki.genexus.com/commwiki/wiki?17510,,) to the Procedure *ProcCondAssignedCustomerId.* This Gateway will make the flow follow the usual course or follow the alternative course to register a customer.

Next, you need to add the WorkWithDevicesCustomer to the diagram and connect it with the conditional's alternative route, as follows:

`[imagen omitida: wiki id 11221]`

Change its name to "Customer" by pressing the F2 button.

**Note**: To connect the gateway with the 'Customer' task, click the right-hand side of the conditional and drag the arrow to the left-hand side of the task. Its type is defined in the route properties.

Now add the call to the Procedure CustomerMapRelevantData in order to update the RelevantData — just like with the WorkWithDevicesreservation, open the WorkWithDevicesCustomer and edit the source of the 'Save' event as follows:

```
Event 'Save'
    Composite
        SDActions.Save()
        CustomerMapRelevantData.Call(CustomerId)
        return
    EndComposite
EndEvent
```

To complete the conditional, you have to define the condition that will make the flow follow one route or the other. To this end, the IDE offers a condition editor that allows you to express the condition returned by the [Condition Procedure](https://wiki.genexus.com/commwiki/wiki?13266). Select the connector to the WorkWithDevicesCustomer and edit the Conditional Code to the value "2".

By defining this condition, non-registered customers—CustomerId.IsEmpty() = True—are registered.

Next, following the usual flow, the WorkWithDevicesReservation is added again. This task evaluates whether the reservation is available to be issued or not; change its name to "Reservation Availability" by pressing F2 button.

`[imagen omitida: wiki id 11222]`

Once the reservation availability has been determined, another gateway must be defined as follows to evaluate the condition:

`[imagen omitida: wiki id 25434]`

If the reservation is available, the process is finished. If it is not available, the flow goes back to the initial task in order to change the reservation details.

Once the gateway has been inserted, you have to define the [Condition procedure property](https://wiki.genexus.com/commwiki/wiki?17510,,) to the object *ProcCondReservationAvailable**.* So, after registering the customer, you have to assign him or her to the reservation and check availability.

Edit the connector to the [End Event](https://wiki.genexus.com/commwiki/wiki?17271) and set the Conditional Code to the value "1" and the Conditional Code of the connector to Reservation to the value "2".  
If the reservation is available, the process is finished. If it's not available, the flow goes back to the initial task in order to change the reservation details.

To complete the flow, define the alternative course to be followed when the customer is not registered. So, after registering the customer, you have to assign him or her to the reservation and check availability. To do so, add the Procedure AssignToCustomer and the connection routes as follows:

`[imagen omitida: wiki id 25435]`

Once the Procedure is added to the diagram, the parameter rule (parm) is automatically evaluated. If attributes or variables with the same name and type as the relevant data are found, they will be instantiated with their values. In this case, the **&ReservationId** and **&CustomerId** variables will be associated with the values of the corresponding relevant data.

### [Step 5: Importing and configuring the GXflow Client for Native Mobile](#Step+5%3A+Importing+and+configuring+the+GXflow+Client+for+Native+Mobile)

In order to run the newly created Business Process Diagram, it is required the [HowTo: Configuring GXflow Client For Smart Devices from xpz](https://wiki.genexus.com/commwiki/wiki?25443,,) to be configured. Follow the steps from [HowTo: Configure GXflow for Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?25444) in order to do so —skip the step of creating a Business Process Diagram.

Once the xpz has been imported you must add a call to each of the [Objects for Native Mobile applications development](https://wiki.genexus.com/commwiki/wiki?20087), that are used in your [Business Process Diagram object](https://wiki.genexus.com/commwiki/wiki?16486)s, to the "WorkflowMobileCalled" [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) in order to be included in the Native Mobile application.  
Therefore add the following code to "WorkflowMobileCalled":

```
Event 'DummyCalls'
        WorkWithDevicesReservation.Reservation.Detail(1)
        WorkWithDevicesReservation.Reservation.List()
        WorkWithDevicesCustomer.Customer.Detail(1)
        WorkWithDevicesCustomer.Customer.List()
EndEvent
```

**Note**: It’s required to include a “Dummy” event that calls the “WorkflowMobileCalled” Panel in the [Startup Object](https://wiki.genexus.com/commwiki/wiki?5393).

### [Step 6: Running the process](#Step+6%3A+Running+the+process)

Before running the process for the first time, do a [Build All](https://wiki.genexus.com/commwiki/wiki?5691), and lastly, run the application by pressing F5.

Next, GeneXus performs the necessary actions to run this diagram and show the changes made. The steps that follow are:

* Update workflow objects
* Specify objects
* Generate objects
* Compile workflow objects
* Impact the diagram on the database

Whether or not all these steps are performed will depend on the changes made; that is to say, a change in the diagram will cause all its objects to be specified, generated and compiled, impacting the diagram.

When generating for Android, the emulator will run automatically with the application, and the user will be requested to log in, as shown in the figure below:

`[imagen omitida: wiki id 50513]`

### [Example: When the user needs to be registered](#Example%3A+When+the+user+needs+to+be+registered)

Create a new Task, once created tap on it, in order to open the preview:

`[imagen omitida: wiki id 50530]` `[imagen omitida: wiki id 50531]` `[imagen omitida: wiki id 50532]` `[imagen omitida: wiki id 50533]`

Next press the execute button in order to take the task:

`[imagen omitida: wiki id 50534]`

Then add the reservation details, but left the CustomerId field blank because the customer is not registered yet:

`[imagen omitida: wiki id 50535]`

Now you have to register a new customer for the reservation.

`[imagen omitida: wiki id 50536]` `[imagen omitida: wiki id 50537]`

Once the Reservation and Customer are registered, the Procedure that assigns the customer to the reservation is automatically executed.

Finally, to end the process, you have to define whether the reservation is available or not. Notice that the customer has been associated with the reservation.

`[imagen omitida: wiki id 50538]`

### [See Also](#See+Also)

[Structure Editor](https://wiki.genexus.com/commwiki/wiki?3913)  
[Object property (BPD Task)](https://wiki.genexus.com/commwiki/wiki?25199)  
[Consult Object property](https://wiki.genexus.com/commwiki/wiki?25469)  
[Preview Object property](https://wiki.genexus.com/commwiki/wiki?25470)


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus BPM Suite](https://wiki.genexus.com/commwiki/wiki?43435) | [HowTo: Configure GXflow for Native Mobile applications](https://wiki.genexus.com/commwiki/wiki?25444) |

---
