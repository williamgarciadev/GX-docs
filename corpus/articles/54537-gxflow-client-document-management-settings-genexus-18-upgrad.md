---
title: "GXflow Client Document Management Settings (GeneXus 18 Upgrade 2)"
source_id: 54537
source_url: https://wiki.genexus.com/commwiki/wiki?54537
genexus_version: "18"
---

# GXflow Client Document Management Settings (GeneXus 18 Upgrade 2)

This menu allows you to set the document management.

`[imagen omitida: wiki id 52405]`

**Enable**: It allows setting whether document management is enabled in the workflow processes or not.  
  
**Upload Path**: Path of a directory accessible by the system that will be used as temporary storage of the documents entered into the system. It must be an absolute path and the web server user must have write rights over that folder.  
  
**Enable Full-Text Search**: It allows searching for words inside the documents. Once this property is enabled, the Content filter will be viewed in the document filters. This filter is for specifying the content by which to filter the documents.  
  
**Index Directory**: It's the directory where the document index will be stored. This index, which will be used to do full-text searches in the document content, is updated every time a document is checked in. The directory must be accessible by the application.  
  
**Enable Digital Signature**: It allows digitally signing documents.  
  
**Certificates Directory**: Directory containing certificates of trusted root and intermediate certification authorities as well as revocation lists. It must be an on-disk directory accessible to the application, and it must have three subdirectories:

* inter\_ca\_certs: certificate directory of trusted intermediate certification authorities
* root\_ca\_certs: certificate directory of trusted root certification authorities
* crls: directory of revocation lists (CRLs)

Certificates and revocation lists stored in these directories must be in DER format. This preference is only used in Java.  
  
**Automatic User Certificate Insertion**: When a user signs a document, by default it is checked whether the certificate is trustworthy; if it doesn't belong to the certificate set of the user, it is automatically added.  
To manually manage user certificates, only an administrator user will be able to add or take certificates of application users.
