---
title: "AWS Access Key creation"
source_id: 32106
source_url: https://wiki.genexus.com/commwiki/wiki?32106
genexus_version: "18"
---

# AWS Access Key creation

Steps to create an AWS Access Key for managing AWS Resources remotelly from the Command Line.

1. Go to [AWS Console](https://console.aws.amazon.com/) and click "Identity & Access Management".
2. Go to Users and click "Create new User".
3. Fill with the name of the user and click create.
4. Save the Access Key ID and the Secret Access Key and click close.
5. Go to the list of Users and select the one created.
6. On the Permissions Tab click on "Attach policy".
7. Select the Policy "AdministratorAccess" **\*** and click Attach Policy.

Keep secure the Access Key and Secret Key.

**\***Never grant FullAdministrator Access to an AWS Production Account.  Use [IAM Policies instead](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html).


|  |
| --- |
| **Backlinks** |
| [HowTo: Deploy an Application to AWS Elastic Beanstalk](https://wiki.genexus.com/commwiki/wiki?32104) |

---
