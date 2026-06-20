---
title: "Delete Cascade"
source_id: 20901
source_url: https://wiki.genexus.com/commwiki/wiki?20901
genexus_version: "18"
---

# Delete Cascade

In a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) the delete option performs a delete cascade one level below the record being deleted.

Delete cascade automatically deletes only those table records included in the transaction structure you are executing.

If the subordinated level of the current one, has a subordinated table itself (included in that transaction or not), the delete cascade is not valid.

### Example 1

|  |  |  |  |
| --- | --- | --- | --- |
| **Order** | **Asociated Tables** | **Delivery** | **Asociated Tables** |
| PurchaseOrderNumber\*    PurchaseOrderDate        SupplierCode            SupplierName                 (ProductCode\*            ProductName             PurchaseOrderQuantity         PurchaseOrderPrice             ProductPrice)           PurchaseOrderTotal | PurchaseOrder  PurchaseOrderLevel | PurchaseDeliveryNumber\*  PurchaseOrderNumber\*        ProductCode\*  PurchaseDeliveryDate | PurchaseOrderLevel  PurchaseDelivery |

Let us explain in detail three possible delete cases:

**You are executing the transaction Order and you want to delete an Order**  
As the subordinated level of the current one has itself a subordinated table then the Delete Cascade is not valid. GeneXus will try to delete this record and if there is information in the subordinated table PurchaseOrderLevel an error message will be shown.

**You are executing the transaction Order and you want to delete an Order Line**   
As the Delete Cascade only works over tables involved in the structure of the current transaction. So the delete cascade will not be triggered for the above transaction nor is there automatic deletion. If there is no information in PurchaseDelivery for that line the normal delete could be done. Otherwise an error message will be shown.

**You are executing the Transaction Delivery and you intend to delete an Order Line**  
In this case the Delete Cascade is valid. So the records of table PurchaseDelivery related to that line will be automatically deleted.

### Example 2

|  |  |
| --- | --- |
| **Aircraft** | **Asociated Tables** |
| AircraftId  AircraftMake  AircraftModel  AircraftRegistrationCertificate        (AircraftMantenanceLevelDate              (AircraftPersonId               AircraftPersonName))        (AircraftCertNumberChangeDate         AircraftCertNumberChangeNewCertNumber) | Aircraft  AircraftMantenanceLevel  AircraftMantenanceLevelTechnicalPersonnelLevel  AircraftCertNumberChangesLevel |

**You are executing the transaction Aircraft and you want to delete an aircraft.**  
The Delete Cascade is not valid because the subordinated level of the current one has itself an other subordinated level.


|  |
| --- |
| **Backlinks** |
| [Mode variable](https://wiki.genexus.com/commwiki/wiki?31225) | [Transaction Web Layout](https://wiki.genexus.com/commwiki/wiki?8057) |

---
