---
title: "AWS Profile name property"
source_id: 43834
source_url: https://wiki.genexus.com/commwiki/wiki?43834
genexus_version: "18"
---

# AWS Profile name property

AWS Credential profile name. If specified, Access and Secret Key properties will not be used.

### [Description](#Description)

The AWS CLI supports using any of multiple named profiles that are stored in the config and credentials files. You can configure additional profiles by using aws configure with the --profile option, or by adding entries to the config and credentials files.

If profile name is specified, Access and Secret Key properties will not be used.

Refer to [AWS documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html) for more information.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [Availability](#Availability)

This property is available since [GeneXus 16 upgrade 4](https://wiki.genexus.com/commwiki/wiki?42755,,).

### [Scope](#Scope)

**Platforms:** Web(.Net, .Net Core, Java)  
**Level:** Deploy Target Options


|  |
| --- |
| **Backlinks** |
| [HowTo: Deploy to AWS Lambda Function](https://wiki.genexus.com/commwiki/wiki?51533) |

---
