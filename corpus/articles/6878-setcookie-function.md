---
title: "SetCookie function"
source_id: 6878
source_url: https://wiki.genexus.com/commwiki/wiki?6878
genexus_version: "18"
---

# SetCookie function

Saves a cookie, returning 0 if the result is correct or any other value otherwise.

### [Syntax](#Syntax)

**SetCookie(** *Name***,**  *Value* [**,** *Path*] [**,** *Exp-date*] [**,** *Domain-name*][**,** *Secure*]**)**

**Where**:  
  
*Name*  
     Is the cookie's name and it is of character type.

*Value*  
     Is the value to be stored and it is of character type. The value will be encoded before being sent to the browser

*Path*  
     Is the Path that indicates the web panels for which the cookie is valid, and it is also of character type. If it isn’t specified, the cookie is valid for the web panels that are in the same directory as the one it is stored in, or in subordinated directories. If “/” is indicated, the cookie will be valid for the entire domain.

*Exp-date*  
     Indicates the expiration date of the cookie. It is a date/datetime type. If it isn’t specified, it will expire when the session is closed in the browser.

*Domain-name*  
Is the domain where the cookie is valid. It is a character type. The default domain is the domain where it has been created.

*Secure*  
Is a numeric type. If it is 1, the cookie is transmitted only if the connection is secure (HTTPS). If it is 0, it is always transmitted.

**Note**: The parameters between brackets are optional and if any of the parameters are null, the default is assumed.

**Type Returned:**  
Numeric

### [Scope](#Scope)

**Objects:**[Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3)

### [Samples](#Samples)

These are some simple examples of how to store cookies.

**Example 1**

```
&Op = SetCookie('ID_USER', Str(UsrId), '/', CTOD('01/01/2010') )
```

Here, a cookie named ID\_USER is being stored. It is valid for the entire domain and its value corresponds to the UsrId attribute, which will expire January 1st, 2010.

**Example 2**

```
&OK = SetCookie('SESSION_ID_GX', &StrSession, '', Nullvalue(&Date) )
```

Here, a cookie named SESSION\_ID\_GX is being stored. It is valid for the application's web panels and its value corresponds to the &Strsession variable. This cookie will expire when the browser is closed.

**Example 3**

```
&Op = SetCookie('USR_CTRY', 'UY', '/', ADDYR(&Today, 1), 'otherdom.artech.com.uy', 1)
```

Here, a cookie named USR\_CTR is being stored. It is valid for the ‘otherdom’ domain and its value, UY, will expire exactly one year from today.

### [See Also](#See+Also)

[GetCookie function](https://wiki.genexus.com/commwiki/wiki?6879)


|  |
| --- |
| **Backlinks** |
| [Cookie data type](https://wiki.genexus.com/commwiki/wiki?21582) | [Cookies in GeneXus](https://wiki.genexus.com/commwiki/wiki?6322) | [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) |
| [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [GetCookie function](https://wiki.genexus.com/commwiki/wiki?6879) |
| [Security Scanner built-in tool](https://wiki.genexus.com/commwiki/wiki?46412) | [Security Scanner built-in tool (GeneXus 18 or prior)](https://wiki.genexus.com/commwiki/wiki?52570) |

---
