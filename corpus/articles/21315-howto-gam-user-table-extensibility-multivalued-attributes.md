---
title: "HowTo: GAM User table extensibility - multivalued attributes"
source_id: 21315
source_url: https://wiki.genexus.com/commwiki/wiki?21315
genexus_version: "18"
---

# HowTo: GAM User table extensibility - multivalued attributes

[GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) User entity can be extended using the methodology explained in [Extensibility of GAM entity properties](https://wiki.genexus.com/commwiki/wiki?19634), based on OAV pattern.

This article shows you the steps to add multivalued attributes to the GAM User table.

### [Add multivalued attributes to GAM User Table](#Add+multivalued+attributes+to+GAM+User+Table)

Suppose you need to store the telephone numbers of a user (home, job, mobile phone, etc). You need to define a variable based on GAMUserAttribute data type, where you should store the "Id" and "value" of the attribute you are defining. In the example, both Id and value could be "Telephone number".  
The "isMultivalue" property should be set to True.

##### Figure #1

The "Multivalues" property is of GAMUserAttributeMultivalues collection data type, and it stores a vector with the "Id" and "value", in the example it could be ("job number", "235555"), ("home number",97666), etc.

##### Figure #2

### [Sample code:](#Sample+code%3A)

```
    &GAMUser = new()
    &GAMUser.Name                   = !"Nickname"
    &GAMUser.EMail                  = !"example@mail.com"
    &GAMUser.FirstName              = !"Juan"
    &GAMUser.LastName               = !"Perez"
    &GAMUser.Password               = !"123"
    &GAMUser.Phone                  = "2601 20 82"
    &GAMUser.URLProfile             = !"https://wiki.genexus.com/commwiki/servlet/wiki?24746,Toc%3AGeneXus+Access+Manager+%28GAM%29"
    &GAMUser.DontReceiveInformation = False
    &GAMUser.CannotChangePassword   = False
    &GAMUser.MustChangePassword     = False
    &GAMUser.IsBlocked              = False
    &GAMUser.PasswordNeverExpires   = False
    
    //User Attributes (optional)
    &GAMUserAtt              = new()
    &GAMUserAtt.Id           = !"EmployeeID"
    &GAMUserAtt.IsMultiValue = False
    &GAMUserAtt.Value        = !"123456"
    &GAMUser.Attributes.Add(&GAMUserAtt)
    &GAMUserAtt              = new()
    &GAMUserAtt.Id           = !"Company"
    &GAMUserAtt.IsMultiValue = True
    &GAMUserAttMV            = new()
    &GAMUserAttMV.Id         = !"GX"
    &GAMUserAttMV.Value      = !"GeneXus"
    &GAMUserAtt.MultiValues.Add(&GAMUserAttMV)
    &GAMUserAttMV            = new()
    &GAMUserAttMV.Id         = !"GL"
    &GAMUserAttMV.Value      = !"Globant"
    &GAMUserAtt.MultiValues.Add(&GAMUserAttMV)
    &GAMUser.Attributes.Add(&GAMUserAtt)
    &GAMUser.Save()
    If &GAMUser.Success()
        Commit
    Else
        &GAMErrorCollection = &GAMUser.GetErrors()
        For &Error in &GAMErrorCollection
            Msg(Format(!"Save User %1 error: %2 (GAM%3)", &Name, &Error.Message, &Error.Code))
        EndFor
    Endif
```

### [GET, Update or delete multivalued attributes](#GET%2C+Update+or+delete+multivalued+attributes+)

These methods are available since [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,).

|  |  |
| --- | --- |
| **Method** | **Description** |
| &GAMUser.GetMultiValuedAttribute(in:&GAMPropertyId, in:&GAMPropertyId, out:&GAMError collection): GAMPropertyValue | Given the GAMUserAttribute.Id for a multivalued GAMUserAttribute, and the GAMUserAttribute.Multivalues.Id, it returns the Value corresponding to that pair (see figure #1 and figure #2) |
| &GAMUser.SetMultiValuedAttribute(in:&GAMPropertyId, in:&GAMPropertyId, in:&GAMPropertyValue, out:&GAMError collection):Boolean | Given the GAMUserAttribute.Id for a multivalued GAMUserAttribute, and the GAMUserAttribute.Multivalues.Id, it updates the Value of this object with the given GAMPropertyValue parameter (see figure #1 and figure #2 for a reference). |
| &User.DeleteMultiValuedAttribute(in:&GAMPropertyId, in:&GAMPropertyId, out:&GAMError collection): Boolean | Given the GAMUserAttribute.Id for a multivalued GAMUserAttribute, and the GAMUserAttribute.Multivalues.Id, it removes the record corresponding to that pair (see figure #1 and figure #2) |

### [Samples](#Samples)

Get the GAMProperty value of all of the multivalued GAMUserAttribute objects of a GAM user

```
&GAMUser.Load(&UserGUIDselected)
For &UserAttr In &GAMUser.Attributes //&UserAttr is GAMUserAttribute data type
  &UserAttributeId = &UserAttr.Id
  &AttrValue = &UserAttr.Value
  if &UserAttr.IsMultiValue

   &GAMUserAttrMultiValuesCollection = &UserAttr.MultiValues //&GAMUserAttrMultiValuesCollection is collection of GAMUserAttributesMultivalues data type
   for &GAMUserAttributeMultivalues in &GAMUserAttrMultiValuesCollection
    &GAMPropertyId = &GAMUserAttributeMultivalues.Id
    &GAMPropertyValue = &GAMUser.GetMultivaluedAttribute(&UserAttributeId,&GAMUserAttributeMultivalues.Id,&errors) //&errors is collection of GAMError
   endfor
  endif
EndFor
```

Delete a GAMUserAttributeMultivalues object

```
&GAMUser.Load(&GAMGUID)
&isok = &GAMUser.DeleteMultivaluedAttribute(&UserAttributeId,&GAMPropertyId,&errors)
if &isok
  commit
else
  For &Error In &errors
   msg(&Error.Message + !"(GAM" + &Error.Code.ToString().Trim() + !")")
  EndFor
endif
```

Update a GAMUserAttributeMultivalues object

```
&GAMUser.Load(&GAMGUID)
&isok = &GAMUser.SetMultivaluedAttribute(&UserAttributeId,&GAMPropertyId,&GAMPropertyValue,&errors)
if &isok
  commit
else
  For &Error In &errors
   msg(&Error.Message + !"(GAM" + &Error.Code.ToString().Trim() + !")")
  EndFor
endif
```

### [See Also](#See+Also)

[HowTo: Extend GAM entity properties](https://wiki.genexus.com/commwiki/wiki?19639,,)


|  |
| --- |
| **Backlinks** |
| [Extensibility of GAM entity properties](https://wiki.genexus.com/commwiki/wiki?19634) | [GAM - Users](https://wiki.genexus.com/commwiki/wiki?22082) | [Toc:GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746) |

---
