---
title: "Required configuration for Amazon S3 bucket"
source_id: 54610
source_url: https://wiki.genexus.com/commwiki/wiki?54610
genexus_version: "18"
---

# Required configuration for Amazon S3 bucket

Below is the recommended [Amazon S3](https://aws.amazon.com/s3/?nc1=h_ls) configuration that you should consider when developing with GeneXus. Information is provided on the new defaults for buckets and how to properly configure access properties in Amazon S3 to ensure smooth integration with GeneXus.

### [Required configuration for Amazon S3 bucket for GeneXus](#Required+configuration+for+Amazon+S3+bucket+for+GeneXus)

Changes to the default security settings of S3 Buckets can affect the behavior of your GeneXus-developed applications. To ensure smooth integration between GeneXus and Amazon S3, it is important to configure your S3 bucket with the following settings:

#### [ACLs Enabled](#ACLs+Enabled)

`[imagen omitida: wiki id 54614]`

While Amazon has disabled Access Control Lists (ACLs) by default for new buckets, GeneXus requires ACLs to be enabled for proper functionality. Configure your bucket to have ACLs enabled.

To work with Privacy = PublicRead, disable the "Block all public access" setting for allowing public read access to the objects in the bucket. However, if the entire bucket's contents should be private, you can leave the "Block all public access" setting enabled.

#### [Disable "Block all public access"](#Disable+%22Block+all+public+access%22)

`[imagen omitida: wiki id 54612]`

It's important to note that these settings ensure compatibility between GeneXus and Amazon S3, allowing you to manage access permissions effectively and securely. However, it's recommended to review the detailed information for a better understanding of the changes and their impact on GeneXus applications. A brief summary of the changes is provided below.

### [Amazon S3 and Block Public Access](#Amazon+S3+and+Block+Public+Access)

As of April 2023, Amazon S3 automatically implemented S3 Block Public Access configuration and disabled ACLs for new S3 buckets. That is, buckets created by default in Amazon S3 have the following configurations:

Block Public Access: Enabled (Block Public Access = TRUE)  
ACL (Access Control Lists): Disabled (ACL = OFF)

The first configuration, S3 Block Public Access, is designed to prevent unwanted public access to S3 buckets and their objects. Enabling S3 Block Public Access ensures that new buckets have settings that block public access by default. This helps prevent security incidents and protects the data stored in S3 buckets.

The second configuration involves disabling S3 access control lists (ACLs). ACLs are an access control mechanism previously used in S3 to define specific permissions on buckets and objects. However, Amazon has decided to disable this functionality by default in the new buckets.

Instead, Amazon S3 now recommends using Identity and Access Management (IAM) policies to manage access permissions to S3 buckets and objects. IAM policies provide greater flexibility and control over permissions and are the recommended way to manage access to S3 resources.

### [See Also](#See+Also)

[Amazon S3 will automatically enable S3 Block Public Access](https://aws.amazon.com/about-aws/whats-new/2022/12/amazon-s3-automatically-enable-block-public-access-disable-access-control-lists-buckets-april-2023/?nc1=h_ls)


|  |
| --- |
| **Backlinks** |
| [DesignOps - Export design - Sketch](https://wiki.genexus.com/commwiki/wiki?46875) | [External Storage for Multimedia](https://wiki.genexus.com/commwiki/wiki?31120) | [Storage Provider property](https://wiki.genexus.com/commwiki/wiki?31121) |
| [Storage Provider property (GeneXus 18 Upgrade 8 or prior)](https://wiki.genexus.com/commwiki/wiki?57448) |

---
