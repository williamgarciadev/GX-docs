---
title: "Description annotation"
source_id: 56430
source_url: https://wiki.genexus.com/commwiki/wiki?56430
genexus_version: "18"
---

# Description annotation

Adds a documentation text to each API Object method.

### [Syntax](#Syntax)

```
 '['Description("<text>")']'
```

View [Syntax conventions](https://wiki.genexus.com/commwiki/wiki?6626)

**Where:**

*text*  
Method and parameter descriptions.

### [Description](#Description)

The Description annotation is introduced to enrich the documentation of each method within the API object, which may contain several methods performing different tasks or actions.

The purpose of this annotation is to provide brief descriptions that contextualize the function of each method, explaining its purpose and how it should be implemented.

This documentation is useful for OpenAPI generation by providing applications that import or parse this file with a deeper understanding of each method. Consequently, it facilitates a more accurate use of API calls, improving integration and efficiency in application development.

### [Sample](#Sample)

For the examples taken from [sample](https://wiki.genexus.com/commwiki/wiki?50879), the Description annotation is used to provide a concise and enlightening description of the functionality of each method in the APIAccount API object.

#### [Sample #1](#Sample+%231)

```
APIAccount {
         [Description("Provides access to account information, allowing querying of account status and owner.")]
         AccountInfo(in:&AccountId, in:&AccountPassword, out:&AccountStatus, out:&AccountOwner)
         => QueryAccount(&AccountId, &AccountPassword, &AccountOwner, &AccountStatus);
         }
```

#### [Sample #2](#Sample+%232)

```
APIAccount{
         [Description("Retrieves the account status based on the provided account number and password.")]
         AccountInfo(in:&AccountId, in:&AccountPassword, out:&AccountStatus)
         => QueryAccount(&AccountId, &AccountPassword, &AccountOwner, &AccountStatus);
         }
```

#### [Sample #3](#Sample+%233)

```
APIAccount{
         [Description("Retrieves the account status with a predefined account owner.")]
         AccountInfo(in:&AccountId, in:&AccountPassword, out:&AccountStatus)
         => QueryAccount(&AccountId, &AccountPassword, "Tomas Huck", &AccountStatus);
        }
```

### [Availability](#Availability)

This annotation is available since [GeneXus 18 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?54241).


|  |
| --- |
| **Backlinks** |
| [Table of contents:First Steps with API objects](https://wiki.genexus.com/commwiki/wiki?49754) | [GeneXus 18 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?54241) |

---
