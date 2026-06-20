---
title: "Mini App Center - Updates Log"
source_id: 58035
source_url: https://wiki.genexus.com/commwiki/wiki?58035
genexus_version: "18"
---

# Mini App Center - Updates Log

This log shows the most important fixes or features being added to the system.

## [August 07, 2025](#August+07%2C+2025)

**IMPORTANT**  
The images have been migrated to a different ECR. The new URIs are:

* 908027417700.dkr.ecr.us-east-1.amazonaws.com/glo-gx/miniappcenter/qa/api
* 908027417700.dkr.ecr.us-east-1.amazonaws.com/glo-gx/miniappcenter/qa/console

## [June 10, 2025 - Version: prod.184](#June+10%2C+2025+-+Version%3A+prod.184)

**Features:**

* Can view in Mini App Version History screen the hour of the change.
* Added platform filtering in Mini Apps versions.
* Send a comment and/or activate or disable the previous version of a Mini App when it changes status through the API.
* Indicates the channel (API o console) that change the status.
* Return status and compatibilities on API of Mini App Version (GET, GET List, Bundle).
* Added a new API to disable a Mini App Version.
* Added a new API to list the Mini Apps with optional filter.
* Added a new API to list the Mini App Versions with optional filter.
* New Design of User Information Screen.
* Added Platform Icon.
* Added controls over the uploaded metadata file for a Mini App version.

**Fixes:**

* GetFilter By Highlighted is not correct with NotEqual condition.
* GetFilter By Text did not work.
* Do not view the back option on the Organization screen when you are not an Administrator.
* If you enter a very long Main Name, the data will be overwritten by the URL.
* The Service URL returns empty and the Main Type returns a GUID, instead of description, after adding a Bundle of Mini App Version.
* When there is no Highlighted Mini Apps Active, it does not allow viewing the history.
* The Super App of a Mini App was allowed to be modified.
* Services return wrong URL of external web images.
* It does not allow modifying the Client secret of an GAM Application.
* Cannot delete a future highlighted Mini App.

**Note**: This version requires running a database update script.

## [June 06, 2024 - Version: prod.124](#June+06%2C+2024+-+Version%3A+prod.124)

**Features:**

* New screen to change language.
* New format for ID of Mini App. The string should be in reverse DNS format using only the Roman alphabet in upper and lower case (A-Z, a-z), numbers (0-9), dots ("."), and hyphens ("-").
* New design and rename of the featured screen for highlight.

**Fixes:**

* Allows to make a Mini App ready without having configured Super App compatibility.
* Plus icon appears on the backgound of the Mini App images.

## [May 15, 2024 - Version: prod.116](#May+15%2C+2024+-+Version%3A+prod.116)

**Features:**

* Display the Super App name on the Mini App screen.
* Added language support for Spanish and Japanese.
* Improved user experience on the Mini App version screen by grouping actions into a "More Actions" button when exceeding two buttons.

**Fixes:**

* Error when additional attributes or their values contain characters such as ",", ";" or double and/or single quotes.
* It doesn't appear the plus icon when a metadata is deleted, to indicate that by clicking you can select the new one.

## [April 15, 2024 - Version: prod.115](#April+15%2C+2024+-+Version%3A+prod.115)

**Features:**

* Renamed the additional attributes service in a Super App to "attributes".
* Added enforcement controls and authentication for downloading the public certificate of a Super App version.
* Included additional attributes in the API response for managing a Mini App.
* Optimized the Mini Apps search service with developer-defined filters.
* Added a filter by Mini App ID in the developer-defined filter service.
* Added a service in the API to get the list of locations of a Mini App.

## [April 03, 2024 - Version: prod.114](#April+03%2C+2024+-+Version%3A+prod.114)

**Features:**

* New design of the organization screens.
* Made the organization ID optional in services for managing Mini Apps and Super Apps if the user is not a "Provisioning Administrator".

**Fixes:**

* Fixed filtering issue in the Mini Apps search service with developer-defined filters for the specified Super App.
* Allowed creation of a Mini App with an ID starting with a space.
* Fixed link error for returning from an organization.

## [March 04, 2024 - Version: prod.113](#March+04%2C+2024+-+Version%3A+prod.113)

**Features:**

* New environment variable to define the S3 location.

**Fixes:**

* Fixed issues with numeric values for additional attributes of a Mini App.
* Error, additional attributes were not saved in Super App and values were not saved in a Mini App.
* Allows to create additional attributes with the same name as the standard ones.
* The service for searching Mini Apps with developer-defined filters does not return any Mini App if called without filters.

## [February 23, 2024 - Version: prod.109](#February+23%2C+2024+-+Version%3A+prod.109)

**Fixes:**

* Error in the service for uploading a Mini App and a version via a bundle file when storing multimedia files in S3.
* Error in the API services for modifying and deleting a Mini App.
* Permissions error for users with "Organization Administrator" role accessing the API key screen.
* Error in the API for creating organizations.
* Google Key error for loading Mini Apps locations.

## [February 02, 2024 - Version: prod.61](#February+02%2C+2024+-+Version%3A+prod.61)

**Features:**

* New services were added to the API: Upload a Mini App and a version through a bundle file.

**Fixes:**

* Permissions error for users with "Mini App Developer" role creating Mini Apps.
* Super App filter in Mini Apps screen was empty for organizations with only permission to create Mini Apps.

## [January 22, 2024 - Version: prod.51](#January+22%2C+2024+-+Version%3A+prod.51)

**Features:**

* The authentication of the services has been changed to API Keys. It must be created by member of the organization or by users for "Provisioning administrator".

**Note**: This version requires running a database update script.

## [December 27, 2023 - Version: prod.44](#December+27%2C+2023+-+Version%3A+prod.44)

**Features:**

* Added functionality to indicate the security of the Super App and Mini Apps.
* Expanded the API with services for managing additional Super App attributes and assigning values for Mini Apps.
* Added a screen to assign values to the additional attributes of Mini Apps based on Super App requirements.
* New service for searching Mini Apps with developer-defined filters.

**Fixes:**

* Error in displaying the change history of a Mini App version.

## [December 04, 2023 - Version: prod.1](#December+04%2C+2023+-+Version%3A+prod.1)

**Features:**

* New design of the Mini Apps and Super Apps screens.
* Added a screen to manage online Mini Apps.
* Allowed disabling previous versions of a Mini App when a new "Ready" version is available.
* Allowed enabling a previous version of a Mini App by disabling the latest "Ready" version.
* New API to facilitate interaction with the data from Mini Apps, Super Apps, Organizations, or any other information provided by the Mini App Center.
* Added email notifications for status changes in the Mini App.
* Added ability to delete/disable a Super App.
* New service to obtain the information of a Mini App through its ID.

**Fixes:**

* Allowed the same name for two Mini Apps within the same Super App.
* Pagination issues in the services for searching Mini Apps.


|  |
| --- |
| **Backlinks** |
| [GeneXus Super App News and Roadmap](https://wiki.genexus.com/commwiki/wiki?53536) | [Table of contents:Mini App Center](https://wiki.genexus.com/commwiki/wiki?51290) |

---
