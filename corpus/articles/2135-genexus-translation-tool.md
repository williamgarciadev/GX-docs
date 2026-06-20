---
title: "GeneXus Translation Tool"
source_id: 2135
source_url: https://wiki.genexus.com/commwiki/wiki?2135
genexus_version: "18"
---

# GeneXus Translation Tool

[GeneXus](https://wiki.genexus.com/commwiki/wiki?1756) Translation Tool is part of the [GeneXus Application Localization](https://wiki.genexus.com/commwiki/wiki?6330) scenario. It is a free program intended for translators who have to translate an application but do not have a GeneXus license.

Support for this feature starts with GeneXus 9.0.

The latest version can be [downloaded here](https://www.genexus.com/en/developers/downloadcenter?data=4411).

## [Description](#Description)

Today's applications have to be able to run in different languages. Usually, developers do not have the skills to translate them into all the required languages and therefore translators are typically hired for this job. Developers send all translatable strings to the translator, who translates them using this tool and sends them back to the developer, who then integrates them into the application. The process can be repeated as many times as needed.

## [Export Translation](#Export+Translation)

The first step in the translation process, called Export Translation, is to prepare what has to be translated. It involves selecting a language (or more than one) and creating a file containing translatable strings (the translation file). To do so, select **Tools > Translation > Export Translation File** from the GeneXus main menu. The following screen will be displayed:

`[imagen omitida: wiki id 7792]`

**Export Translation File**: Is the name of the translation file. The default translation file name is LanguageExport.xml, and the default directory is the KB directory. You can change both according to your needs.  
  
**Objects**: Displays the language objects to be exported.  
  
**Add**: Allows you to add more language objects to the list of objects to be exported through the Select Object Dialog.  
  
**Add All**: Allows you to add all language objects.  
  
**Remove**: Deletes all selected objects from the column of objects to be exported.  
  
**Remove All**: Deletes all language objects.  
  
**Include messages cross reference in export file**: Allows you to include text cross references in the translations file (i.e. what objects in the KB reference what messages).  
  
**Advanced**  
By clicking on this button, you can see advanced options for the messages that you want to export.

`[imagen omitida: wiki id 7793]`

**Filter Options**  
  
**Messages that match pattern**: Allows you to specify a pattern (not a regular expression) to include messages matching that pattern.  
  
**Messages in range**: Allows you to specify a range (for example, from 'A' to 'C') to include messages matching that range.  
  
**Messages with translation**: Includes all messages for the Language, only those translated, only those that do not have a translation (default value), or both.  
  
**Messages of type**: Allows selecting User messages (default value), Internal (i.e. GeneXus) messages, or Both.  
  
**Messages used in objects**: Selecting a list of objects will include message references for any (or all) of the selected objects.

## [Using GeneXus Translation Tool](#Using+GeneXus+Translation+Tool)

To start translating, translators must first create a project and specify the name of the file created in the previous step (the translation file).

`[imagen omitida: wiki id 7795]`

Once imported, the translation file containing the Language object(s) will be displayed as follows:

`[imagen omitida: wiki id 7794]`

The left column shows all the project languages and the right side shows the contents of each one of them.

The options in the upper part of the Language object allow filtering the messages to translate. The options are as follows:

**Messages that match pattern:** Shows only the messages that match the pattern.

**Messages used in object:** Allows you to select the messages used in one object.

**Untranslated messages only:** Shows only the untranslated messages.

**User messages only:** Shows only the user messages.

In addition to the previous options, you can add a reference language if it's necessary to simplify the translation work. This option can be accessed by right-clicking on the language and selecting Load Reference Language.

`[imagen omitida: wiki id 26567]`

This language is used if the translator doesn't know the original language of the Knowledge Base. For example, suppose that the Knowledge Base is in Spanish and has to be translated into Simplified Chinese. To do so, it is translated from Spanish into English, and then from English into Simplified Chinese by using English as reference language.

Once the translation is done, it needs to be sent back to the developer via a translation file. To do so, select Tools/Export Translations.

`[imagen omitida: wiki id 7797]`

Next, send back this file to be imported into the Knowledge Base.  
  
Sometimes you will need to add more messages to the project to be translated, so you will have to Import the new messages by selecting Tools/Import Translations. You need to select whether you want to **Overwrite existing translations** or not.

`[imagen omitida: wiki id 7798]`

## [Import Translation](#Import+Translation)

Once the translation is done, it has to be imported from the translation file created by the translator. To import the translation file, select **Tools > Translation > Import Translation File**from the GeneXus main menu. Only translated messages from the translation file are imported.

**Note** for GeneXus 9.0 users: the import can be done in any model (Design, Prototype, etc.) as translations are Model-independent.

You will be prompted for:

`[imagen omitida: wiki id 7796]`

**Export File**: This is the name and directory of the translation file.  
  
**Add new messages**: Allows adding new messages to the Knowledge Base. If this option is not selected, only the translations of existing messages in the Knowledge Base will be imported.  
  
**Overwrite existing translations**: Imports translation file messages that have already been translated in your Knowledge Base.


|  |
| --- |
| **Backlinks** |
| [Category:Language object](https://wiki.genexus.com/commwiki/wiki?7258) | [Translation types](https://wiki.genexus.com/commwiki/wiki?54437) |

---
