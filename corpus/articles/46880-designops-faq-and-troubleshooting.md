---
title: "DesignOps - FAQ and Troubleshooting"
source_id: 46880
source_url: https://wiki.genexus.com/commwiki/wiki?46880
genexus_version: "18"
---

# DesignOps - FAQ and Troubleshooting

Below you can find some frequently asked questions (FAQ) and Troubleshooting about [DesignOps](https://wiki.genexus.com/commwiki/wiki?47020).

### [FAQ (Frequently Asked Questions)](#FAQ+%28Frequently+Asked+Questions%29)

#### [**1. How can you report an incident?**](#1.+How+can+you+report+an+incident%3F)

You can open a thread in our [Technical Forum](https://www.genexus.com/en/developers/forums) and our team will be pleased to help you. Describe how we can reproduce your problem as detailed as possible, including the error detail. When the error is displayed in the import dialog, the complete error trace can be obtained by clicking on the "show error" icon (`[imagen omitida: wiki id 47225]`). It will also be very helpful if you provide a minimal [design file](https://wiki.genexus.com/commwiki/wiki?46875) (preferably a .gxsketch or an URL) ready to reproduce (including every required asset).  
Also, feel free to contact our [support team](https://www.genexus.com/en/developers/issue-tracking).

#### [**2. How can you import a design that includes fonts in .ttc or .otc formats?**](#2.+How+can+you+import+a+design+that+includes+fonts+in+.ttc+or+.otc+formats%3F)

Modern browsers do not support neither **.ttc** ([TrueType Collection](https://en.wikipedia.org/wiki/TrueType#TrueType_Collection)) nor **.otc** ([OpenType Colelction](https://en.wikipedia.org/wiki/OpenType#OpenType_Collections)) file formats. So, it is highly recommended your designer avoids using these file formats in your design files. In the first place, these file formats (as their names suggest) packs a set of **.ttf** ([TypeTrue Format](https://en.wikipedia.org/wiki/TrueType)) or **.otf** ([OpenType Format](https://en.wikipedia.org/wiki/OpenType)) font files into a single file but, like most software, they are under a term of use (known as End User Licence Agreement or EULA), and you have to be allowed to use them. In case you have a .ttc or .otc font file and you are allowed to use it, you must unpack their individual .ttf or .otf files (online services like [transfonter](https://transfonter.org/ttc-unpack) makes the job). Then, in order to import them to GeneXus, you have two alternatives:

1. Replace every occurrence of the original .ttc or .otc file in your design files by their respective .ttf or .otf files **[RECOMMENDED]**
2. Or, you can create a folder in the same location of your design file with the exact name of the design file suffixed by "Fonts" and put every .ttf or .otf into it.  
   e.g. if your design file is called "My Design.gxsketch", you will create a folder named "My DesignFonts" (note that spaces are significant) and then you will put the .ttf or .otf into it before importing the design file.  
   ㅤ

#### [**3. Can you export a design from other tools and then import the converted design to GeneXus?**](#3.+Can+you+export+a+design+from+other+tools+and+then+import+the+converted+design+to+GeneXus%3F)

You can export/convert a design from other tools (e.g. Figma, Adobe XD or Lunacy to Sketch format), but you have to be careful. A conversion process might contain inconsistencies or flaws that have a direct impact on the final result. In that sense, it is highly recommended that you open the exported/converted design in the proper tool (e.g. if you are converting from .xd to .sketch, open that .sketch in Sketch) and check everything is drawn and structured as it is expected (symbols, styles, color variables, anchors, etc). Also, remember that the file itself might not contain all the required resources when importing into GeneXus (e.g. fonts or exported images), so it is recommended that you read [Export design](https://wiki.genexus.com/commwiki/wiki?46875) article carefully first.

Contact [Unanimo.Design](https://unanimo.design/) if you need help converting your design into a GeneXus' supported format.

#### [**4. Can you import a design by indicating an URL instead of a local file path?**](#4.+Can+you+import+a+design+by+indicating+an+URL+instead+of+a+local+file+path%3F)

Since [GeneXus 17 upgrade 7](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49301,,) you can, but your URL must be accessible and must force the download of the file. In other words, the URL of your design will only work in GeneXus Design Inspector if you paste your URL in your browser and the download will automatically start (without redirects, authentications, etc). Take some examples for TravelAgencySample.sketch:

* **Custom hosting**: <https://files.genexus.com/pub/TravelAgencySample.gxsketch>  
  The design file is hosted in a public directory (/pub) that can be directly accessed by the browser for downloading. This URL will work in GeneXus Design Inspector without any problem.
* **Dropbox hosting**: <https://www.dropbox.com/s/uzvma6iku9kyn9t/TravelAgencySample.gxsketch?dl=1>  
  The design file is hosted at Dropbox and the file will be forced to download due to "dl=1" parameter ([learn more](https://help.dropbox.com/en-us/files-folders/share/force-download)). You can paste this URL in your browser and you will notice that the file will start downloading, so this URL can be used in GeneXus Design Inspector without any problem.
* **Google Drive hosting**: <https://drive.google.com/u/0/uc?id=1iX-rBOW8PP70Fx9JJdOre2yKyHwtHf5G&export=download>  
  The design file is hosted at Google Drive and it adds the "export=download" parameter in order to force de download but Google has a redirect for a virus scan bypass (this is added by Google when the file is relatively large). So, in this case, the URL will not work in GeneXus because the file cannot be directly downloaded (you can check the virus scan bypass redirect by copying the URL in your browser).

#### [**5. Are there any consideration when integrating the Import Design result with GeneXus Patterns (Work With Plus, K2B Tools, etc.) or existing components in the Knowledge Base?**](#5.+Are+there+any+consideration+when+integrating+the+Import+Design+result+with+GeneXus+Patterns+%28Work+With+Plus%2C+K2B+Tools%2C+etc.%29+or+existing+components+in+the+Knowledge+Base%3F)

The Import Design tool is designed to generate **standard GeneXus objects**, including one DesignSystem object, a series of Panel or WebPanel objects (based on the Main Frames from the design), Image objects (bitmaps or layers exported as images), File objects (associated with fonts), and Structured Data Types & Data Providers objects (when there are Frames defined by following the Grid convention).

Integrating the objects generated by the Import Design tool with any GeneXus Pattern or existing components within the Knowledge Base largely depends on the user's preference and experience. It is important to note that the Import Design tool was not specifically designed to interact with third-party extensions in the Knowledge Base. However, since the Import Design tool generates a set of standard GeneXus objects, users can manage or modify them according to their needs, either by applying patterns over the generated objects or extend them using predefined custom components. In this context, any integration would be the responsibility of the developer. For example, developers can extend the generated DesignSystem object to incorporate it with the GeneXus Pattern of their choice, maintain separate modules for predefined object and those generated by the Import Design tool, or explore other integration methods based on their experience and best practices in GeneXus.

In summary, while the Import Design tool provides a solid foundation with standard GeneXus objects, integrating these with GeneXus Patterns or existing components is flexible and can be tailored to meet specific needs and preferences.

Recommended readings

* `[imagen omitida: wiki id 4527]`

### [Troubleshooting](#Troubleshooting)

#### [**The app's appearance differs significantly from its intended design when it is run.**](#The+app%27s+appearance+differs+significantly+from+its+intended+design+when+it+is+run.)

|  |  |
| --- | --- |
| **Cause** | Remember that the [Design Import option](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46882,,) tries to approximate the design to GeneXus *as close as possible* and depends on how tidy your design file is. However, some scenarios can leak and should be analyzed one by one. |
| **Solution** | First, check if the design file follows the [designer guidelines](https://wiki.genexus.com/commwiki/wiki?46871) to achieve a good result. If that is not enough, think if that design can be modeled with GeneXus. If not, the developer must implement a custom solution (e.g. a User Control) and integrate it with what is imported from the design file. if you think that you can model the scenario with GeneXus but it was not generated during the import, add it manually in order to achieve the expected result. Feel free to contact support with your scenario and we will try to automate GeneXus' object generation in a future release.  |  |  |  | | --- | --- | --- | | **Missing feature** |  | **Support status** | | Blend mode |  | - | | Color Variables (Sketch) & Color Styles (Figma) |  | Available since [GeneXus 17 upgrade 1](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46852,,) | | External libraries |  | - | | Fix position when scrolling |  | Available since [GeneXus 17 Upgrade 9](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49956,,) | | Flipping |  | Available since [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066) | | Font collection (ttc/otc formats) |  | Won't implement.  Please check: [FAQ: How can you import a design that includes fonts in .ttc or .otc formats?](https://wiki.genexus.com/commwiki/wiki?46880) | | Font variables (woff2 format) |  | - | | Format text range |  | - | | Gradient coloring |  | Available since [GeneXus 17 upgrade 7](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49301,,) (for web apps) | | Hotspots links |  | - | | Letter spacing |  | Available since [GeneXus 17 upgrade 7](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49301,,) (for web apps) | | Line spacing |  | Available since [GeneXus 17 upgrade 7](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49301,,) (for web apps) | | Navigation Styles for mobile apps |  | Available since [GeneXus 17](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46066,,) (for Sketch designs, for Figma check [f/14993](https://forum.figma.com/t/get-directionaltransition-information-via-rest-api/14993)) | | Paragraph spacing |  | - | | Partial masking on images |  | - | | Rotation |  | Available since [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066) | | SVG images |  | Available since [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066) (for web and angular apps) | | Text on paths |  | - | | Text underline |  | - | | Tints |  | - | | Underline text (for mobile apps) |  | - | | Variations |  | Available since [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066) | | WebP images |  | - | |  |  |  | | **Figma** |  |  | | Variables (Number, String, Boolean, and Color) and Variables Collection definition |  | Won't implement it until Figma's official release. Variables are currently in open Beta and subject to breaking changes (more information at [Figma Developers: Variables](https://www.figma.com/developers/api#variables)). | | Wrap on Auto-Layouts |  | Modeling Flex Grids available since [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239).  Modeling Flex Tables is planned for upcoming releases. | | Min/Max Width/Height |  | - | | Canvas Stacking Order |  | Available since [GeneXus 18 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?54239). | | Triggers, Directional transition and Back transition in Prototypes |  | Unable to implement due to missing metadata.  Support us on this [Figma's forum post](https://forum.figma.com/t/get-directionaltransition-information-via-rest-api/14993).  **Notes:** |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | 1) | The [GeneXus Design Prototyper for Figma](https://wiki.genexus.com/commwiki/wiki?56683) plugin is capable of including such missing metadata in the design file, enabling the interpretation of: |  |  | | --- | --- | | - | Back action as a Return command. | | - | Open Link action as Link function or Open method (from the Interops external object), depending if the importation was made for Web Panels or Panels respectively. | | - | Push animations as Enter/Exit Effects in the Form's class. | | | 2) | Any trigger other than None will be defined with a Call method in GeneXus, behaving as an On Click event in Figma. | | | Expressions, Actions and Conditionals in Prototypes using variables |  | Unable to implement due to missing metadata.  Support us on this [Figma's forum post](https://forum.figma.com/t/get-variables-expressions-actions-and-conditions-via-rest-api/48107). | |  |  |  | |

#### [**Complex controls present in the design file are not generated during the import process.**](#Complex+controls+present+in+the+design+file+are+not+generated+during+the+import+process.)

|  |  |
| --- | --- |
| **Cause** | Complex controls require complex treatment. GeneXus' limitations are limitations when designing. |
| **Solution** | Keep your design simple. If there is a reason that you have to include a complex control in your design, let it know to the developer in order to manually implement it. Complex controls like Steppers, Calendars, Charts, or Maps should be marked as "Exportable" in order to display them as images that can be easily replaced by the developer in the application. |

#### [**Importing a design file overrides any previous changes made to the app.**](#Importing+a+design+file+overrides+any+previous+changes+made+to+the+app.)

|  |  |
| --- | --- |
| **Cause** | The [Design Import option](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46882,,) does not merge changes, and always overrides the objects. |
| **Solution** | Merge must be done manually. Before import, it's highly recommended to package your objects into a module in order to not override what you have created. Then, check for differences and merge them. |

#### [**Some controls in objects are not generated as expected.**](#Some+controls+in+objects+are+not+generated+as+expected.)

|  |  |
| --- | --- |
| **Cause** | The design may not follow the guidelines to achieve a good import. |
| **Solution** | First, check with your designer the guides and conventions to achieve a good import. Remember that the designer must group everything that has to be together in order to generate the appropriate tables containers. If the problem persists, feel free to contact support. |

#### [**Images appear as black squares when the app is running.**](#Images+appear+as+black+squares+when+the+app+is+running.)

|  |  |
| --- | --- |
| **Cause** | Black images are placeholders when your design file does not include the appropriate image for displaying it. |
| **Solution** | Check if the image is included with your design file. If it is included, check if that image includes every density variant needed (at least 1x for PNG, and SVG is recommended), and, in case some of them are missing, tell your designer to export it with missing densities. Also, check with the designer if complex shapes (e.g. custom icons, logos) were marked as 'Exportables'. If the problem persists, feel free to contact support. |

#### [**Controls do not display properly when switching between devices or changing from portrait to landscape mode.**](#Controls+do+not+display+properly+when+switching+between+devices+or+changing+from+portrait+to+landscape+mode.)

|  |  |
| --- | --- |
| **Cause** | The design file does not contain information for making your app responsive. |
| **Solution** | Check with your designer if controls are anchored or if they have fixed sizes when they required it. Both of you can test if the result Panel will be responsive by resizing the problematic artboard before importing it. |

#### [**Importing a design file results in the generation of numerous style classes without reusing them.**](#Importing+a+design+file+results+in+the+generation+of+numerous+style+classes+without+reusing+them.)

|  |  |
| --- | --- |
| **Cause** | The import process generates a style-class per control drawn by the designer, unless your designer uses Styles when designing the application. |
| **Solution** | In order to reuse style-classes, your designer must use Styles. Currently, GeneXus supports fill, border, and text styles. |

#### [**Design elements have inconsistencies when viewed across different platforms.**](#Design+elements+have+inconsistencies+when+viewed+across+different+platforms.)

|  |  |
| --- | --- |
| **Cause** | GeneXus always tries to follow the standard design guidelines for each platform (e.g. Material Design for Android, or HIG —Human Interface Guidelines— for Apple). That fact may produce differences between the design and the final result, and even between the platforms themselves. |
| **Solution** | It is a good practice to follow the design guidelines for a specific platform. If it is required not to follow the guidelines, it is up to you to develop a custom solution and then integrate it into the object that was imported from the design file. |

#### [**Some fonts are not displayed in the app.**](#Some+fonts+are+not+displayed+in+the+app.)

|  |  |
| --- | --- |
| **Cause** | The font was not included during the import, the font source is not supported (e.g. .variable fonts *.woff2* or font collections *.ttc*) or there could be a naming mismatch. |
| **Solution** | Check if your font has been created as a File object in your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836). If so, check if there is a @font-face rule in the Design System object using the gx-file function referencing the File object with your font.  (\*). Finally, check if the @font-face is referenced by font-family value in the target style class. If you are working on a mobile environment, check [Using Custom Fonts](https://wiki.genexus.com/commwiki/wiki?22781) article for further troubleshooting. If the problem persists, please send us your design and font files so we can reproduce the issue.    (\*) Alternatively, if you generated a Theme object, check if a Font node in the Theme object references the File object with your font. Finally, check if the target Theme Class has referenced the Font node. |

#### [**The design file specifies a color palette that is not included as Tokens in the Design System or the Color Palette object.**](#The+design+file+specifies+a+color+palette+that+is+not+included+as+Tokens+in+the+Design+System+or+the+Color+Palette+object.)

|  |  |
| --- | --- |
| **Cause** | Color Variables defined in a design file are supported since GeneXus 17 Upgrade 1. |
| **Solution** | Include these colors manually and update the style-class references to them, or upgrade to GeneXus 17 Upgrade 1. |

#### [**An error message 'Error validating formula expression: Upper(...' appears when importing a design file.**](#An+error+message+%27Error+validating+formula+expression%3A+Upper%28...%27+appears+when+importing+a+design+file.)

|  |  |
| --- | --- |
| **Cause** | Known issue. The designer combines upper-case and break-lines in a text element that produce the error when it tries to set the Initial Value of a variable. |
| **Solution** | As a workaround, your designer must write the text uppercased or delete the break-lines. This issue will be fixed in a future release. |

#### [**A warning message 'Using a placeholder as an image because...' appears when importing a design file.**](#A+warning+message+%27Using+a+placeholder+as+an+image+because...%27+appears+when+importing+a+design+file.)

|  |  |
| --- | --- |
| **Cause** | The target images cannot be found. Usually, this problem suggests that the designer forgot to mark a layer as "Exportable" (e.g. icons, logos, etc.). |
| **Solution** | Tell your designer to mark the layer indicated in the message as exportable. |

#### [**An error message 'Error: cp: %1: No such file or directory' appears when exporting a design file using the Sketch plugin**](#An+error+message+%27Error%3A+cp%3A+%251%3A+No+such+file+or+directory%27+appears+when+exporting+a+design+file+using+the+Sketch+plugin)

|  |  |
| --- | --- |
| **Cause** | Probably, the file path indicated in "%1" may not exist or contains blank-spaces. Try to execute that command through the Mac terminal. Sometimes, when you copy a file path it translates some folders into another language that is not English. |
| **Solution** | Ensure the file path indicated in "%1" exists, it is fully in English and has no blank spaces. |

#### [**Importing both Mobile and Web design files into the same Knowledge Base may cause inconsistencies in the class hierarchy if the style is a Theme object**](#Importing+both+Mobile+and+Web+design+files+into+the+same+Knowledge+Base+may+cause+inconsistencies+in+the+class+hierarchy+if+the+style+is+a+Theme+object)

|  |  |
| --- | --- |
| **Cause** | After importing a design file, each theme class created will inherit from a specific parent class depending on its type (e.g., ExternalDesignAttribute, ExternalDesignTable, ExternalDesignTextBlock, etc.). However, if you import both mobile and web design files into the same Knowledge Base, it may lead to inconsistencies in the class hierarchy. For instance, some classes may unintentionally inherit from web classes instead of mobile classes, and vice versa. |
| **Solution** | After your first import, rename every generated root theme class (e.g. 'ExternalDesignAttribute' by 'ExternalDesignAttributeMobile') and then import your second design file. |

#### [**A text-layer is imported with a single color when multiple colors were defined in the design.**](#A+text-layer+is+imported+with+a+single+color+when+multiple+colors+were+defined+in+the+design.)

|  |  |
| --- | --- |
| **Cause** | GeneXus does not support colored substring in a text, either by an Attribute or a TextBlock style-class. |
| **Solution** | You must split your text-layer in your design in order to generate two or more Attribute/TextBlocks when each of them has a theme-class with the appropriate color. Alternatively, after you import your design into GeneXus, you can set Format property to 'HTML' and reformat your text by adding a <span style="color:{your\_hex\_color};"></span> in the substring. |

#### [**The box-shadows are not correctly displayed when importing for mobile.**](#The+box-shadows+are+not+correctly+displayed+when+importing+for+mobile.)

|  |  |
| --- | --- |
| **Cause** | When you design a mobile app, GeneXus will try to infer a material-design elevation from your box-shadow definition. This mapping is an approximation, so it can fail if you do not define it correctly. |
| **Solution** | You can define the exact shadow for each elevation value:  |  |  | | --- | --- | | **Elevation** | **Shadow** | | 0 | N/A | | 1 | Color = #00000024, X = 0, Y = 1, Blur = 1, Spread =  0  Color = #0000001F, X = 0, Y = 2, Blur = 1, Spread = -1  Color = #00000033, X = 0, Y = 1, Blur = 3, Spread = 0 | | 2 | Color = #00000024, X = 0, Y = 2, Blur = 2, Spread = 0  Color = #0000001F, X = 0, Y = 3, Blur = 1, Spread = -2  Color = #00000033, X = 0, Y = 1, Blur = 5, Spread = 0 | | 3 | Color = #00000024, X = 0, Y = 3, Blur = 4, Spread = 0  Color = #0000001F, X = 0, Y = 3, Blur = 3, Spread = -2  Color = #00000033, X = 0, Y = 1, Blur = 8, Spread = 0 | | 4 | Color = #00000024, X = 0, Y = 4, Blur = 5, Spread =  0  Color = #0000001F, X = 0, Y = 1, Blur = 10, Spread = 0  Color = #00000033, X = 0, Y = 2, Blur = 4, Spread = -1 | | 6 | Color = #00000024, X = 0, Y = 6, Blur = 10, Spread = 0  Color = #0000001F, X = 0, Y = 1, Blur = 18, Spread = 0  Color = #00000033, X = 0, Y = 3, Blur = 5, Spread = -1 | | 8 | Color = #00000024, X = 0, Y = 8, Blur = 10, Spread = 1  Color = #0000001F, X = 0, Y = 3, Blur = 14, Spread = 2  Color = #00000033, X = 0, Y = 5, Blur = 5, Spread = -3 | | 9 | Color = #00000024, X = 0, Y = 9, Blur = 12, Spread = 1  Color = #0000001F, X = 0, Y = 3, Blur = 16, Spread = 2  Color = #00000033, X = 0, Y = 5, Blur = 6, Spread = -3 | | 12 | Color = #00000024, X = 0, Y = 12, Blur = 17, Spread = 2  Color = #0000001F, X = 0, Y = 5, Blur = 22, Spread = 4  Color = #00000033, X = 0, Y = 7, Blur = 8, Spread = -4 | | 16 | Color = #00000024, X = 0, Y = 16, Blur = 24, Spread = 2  Color = #0000001F, X = 0, Y = 6, Blur = 30, Spread = 5  Color = #00000033, X = 0, Y = 8, Blur = 10, Spread = -5 | | 24 | Color = #00000024, X = 0, Y = 24, Blur = 38, Spread = 3  Color = #0000001F, X = 0, Y = 9, Blur = 46, Spread = 8  Color = #00000033, X = 0, Y = 11, Blur = 15, Spread = -7 | |

#### [**The gradients defined in the design are ignored when importing for mobile.**](#The+gradients+defined+in+the+design+are+ignored+when+importing+for+mobile.)

|  |  |
| --- | --- |
| **Cause** | The mobile generators (Android and iOS) do not support the definition of gradients in the Design System object using [linear-gradient()](developer.mozilla.org/en-US/docs/Web/CSS/gradient/linear-gradient), [radial-gradient()](https://developer.mozilla.org/en-US/docs/Web/CSS/gradient/radial-gradient), or [conic-gradient()](https://developer.mozilla.org/en-US/docs/Web/CSS/gradient/conic-gradient) functions as the Web and Angular generators do through CSS. |
| **Solution** | Currently, there is no solution for defining gradients when using the mobile generators, even when working with the Angular generator because the [Import as Web Panels option](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?46882,,) consider both Angular and mobile generators when it is unchecked. As a workaround, you can create the gradient layer (e.g., a background) as a separate rectangle and [export it as an image](https://wiki.genexus.com/commwiki/wiki?46871). This way, GeneXus replaces the gradient definition with an image. However, be aware that this approach has limitations if the gradient color needs to change over time, as you will need to re-import the images representing the gradient layers to reflect any changes in color. |

#### [**Styles changes are not being applied to the grid's items.**](#Styles+changes+are+not+being+applied+to+the+grid%27s+items.)

|  |  |
| --- | --- |
| **Cause** | Currently, GeneXus does not support changing grid item styles specified in the design. |
| **Solution** | You must manually create those styles in the Theme or [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) and associate them in the grid Load event for each cell. |

#### [**The import process creates a Design System object and there is no possibility for creating a Theme object instead.**](#The+import+process+creates+a+Design+System+object+and+there+is+no+possibility+for+creating+a+Theme+object+instead.)

|  |  |
| --- | --- |
| **Cause** | Since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?48684,,), the Import Design tool generates a [Design System Object](https://wiki.genexus.com/commwiki/wiki?47375) by default. |
| **Solution** | If you really need to generate a Theme object, you have to create a file *ImportDesignStyleOption.flag* under your GeneXus installation. Then, when you re-open GeneXus, the Import Design dialog will display an "Import as Design System" option (checked by default) and you need to clear it before importing your design. Take into account that the Theme object generation from the Import Design tool will no longer be maintained nor receive support. |

#### [**An error message 'Error reading %1: Sketch file is missing' appears when attempting to load a design file.**](#An+error+message+%27Error+reading+%251%3A+Sketch+file+is+missing%27+appears+when+attempting+to+load+a+design+file.)

|  |  |
| --- | --- |
| **Cause** | GeneXus cannot find the sketch file indicated in the "File path" field of the Import dialog. |
| **Solution** | This error may occur on several occasions:  ● The file path indicated does not exist in your filesystem  ● The file path is a *.gxsketch*, generated with a *.sketchcloud* file (supported since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?48684,,)) |

#### [**An error message 'Design file "%1" could not be found' appears when opening the Import Design dialog.**](#An+error+message+%27Design+file+%22%251%22+could+not+be+found%27+appears+when+opening+the+Import+Design+dialog.)

|  |  |
| --- | --- |
| **Cause** | The import dialog stores the last five file paths you imported and it tries to load it for the last one, but that file is not in the filesystem anymore. |
| **Solution** | Recreate the file in the indicated path before starting the Import Dialog. This error is fixed since [GeneXus 17 upgrade 7](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49301,,). |

#### [**Certain images appear with a blue tint when running an Apple app.**](#Certain+images+appear+with+a+blue+tint+when+running+an+Apple+app.)

|  |  |
| --- | --- |
| **Cause** | GeneXus import all your images as Image objects, but they have set Rendering Mode property with 'Automatic' value. |
| **Solution** | Open the Image object and change the [Rendering Mode property in Images](https://wiki.genexus.com/commwiki/wiki?23135) with 'Original' value for every image variation. |

#### [**Some images do not display properly on the Web at runtime, despite having the correct gx-content-mode (or Scale Type) property set.**](#Some+images+do+not+display+properly+on+the+Web+at+runtime%2C+despite+having+the+correct+gx-content-mode+%28or+Scale+Type%29+property+set.)

|  |  |  |
| --- | --- | --- |
| **Cause** | Both properties [gx-content-mode](https://wiki.genexus.com/commwiki/wiki?23857) (from Design System objects) and Scale Type (for Theme objects) apply for Images controls, not for Image variables. Even if the import generates the correct value for the mentioned properties, it will not generate Image controls, It will generate Image variables. |  |
| **Solution** | Use the [CCS object-fit property](https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit) and map the values of gx-content-mode (or Scale Type) as follows:  |  |  |  | | --- | --- | --- | | fill-keeping-aspect | → | cover | | fill | → | fill | | fit | → | contain | | tile | → | not supported by object-fit |  Since [GeneXus 17 upgrade 7](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49301,,) you don't have to worry about this anymore. GeneXus will generate the appropriate object-fit when you import your design as [Web Panels](https://wiki.genexus.com/commwiki/wiki?6916). |  |

#### [**An error message '%1 is not a valid event' appears while importing a design.**](#An+error+message+%27%251+is+not+a+valid+event%27+appears+while+importing+a+design.)

|  |  |
| --- | --- |
| **Cause** | Your design defines a [Link/Interaction](https://wiki.genexus.com/commwiki/wiki?46871) that is unsupported in your GeneXus upgrade. |
| **Solution** | Consider upgrading your GeneXus installation and retrying to import your design. In case you have updated GeneXus and the problem persists, please [contact our support team](https://wiki.genexus.com/commwiki/wiki?46880).  Eighterway, you can inspect the .gxml and .code.gxml files generated by the Import Design tool (located at *{KB\_DIR}/DATA001/DesignToGxml*) in order to figure out which link is unsupported and then delete it from your design file (with help of your designer). Finally, you can implement the interaction after successfully importing your design. |

#### [**A warning message 'Could not get font {font-name}' appears when importing from Figma.**](#A+warning+message+%27Could+not+get+font+%7Bfont-name%7D%27+appears+when+importing+from+Figma.)

|  |  |
| --- | --- |
| **Cause** | The design uses a font provided by Figma that is not found in Google's repository, or it is a custom font. |
| **Solution** | You have to get the font file and install it for all users in the development machine before importing the design. In Windows, this can be done by right-clicking the font file and selecting "Install for all users" option. |

#### [**Certain layers are not visible after importing the design file.**](#Certain+layers+are+not+visible+after+importing+the+design+file.)

|  |  |
| --- | --- |
| **Cause** | You are probably using unsupported features that GeneXus does not understand, e.g. custom shapes or drawings, or external files or libraries. |
| **Solution** | In case you are using custom shapes or drawings, you have to group them semantically and make the group exportable as an image. On the other hand, if you are using external files or libraries, you have to detach every component from the external resource and replicated them in your design. |

#### [**An error message 'Cannot unmarshal type {0}: {1}' appears when importing from Figma.**](#An+error+message+%27Cannot+unmarshal+type+%7B0%7D%3A+%7B1%7D%27+appears+when+importing+from+Figma.)

|  |  |
| --- | --- |
| **Cause** | The design import tool does not recognize the value {1} for the property {0} because it is not documented by Figma and the import tool does not know how to handle it. |
| **Solution** | These kinds of errors will be fixed on demand. You must contact our support team indicating the error messages and a minimal example for reproducing the problem.  As of [GeneXus 18 Upgrade 1](https://wiki.genexus.com/commwiki/wiki?51081) these errors are treated as warnings and the complete layer is ignored. |

#### [**Navigation links defined in an instance layer are not generated when importing from Figma.**](#Navigation+links+defined+in+an+instance+layer+are+not+generated+when+importing+from+Figma.)

|  |  |
| --- | --- |
| **Cause** | Up to [GeneXus 17 Upgrade 11](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?49972,,), navigation links can only be defined in layers that are not part of a component's instance. |
| **Solution** | You should upgrade to [GeneXus 18](https://wiki.genexus.com/commwiki/wiki?51066), as navigation links defined from layers in an Instance are supported. For older releases, you should define the same link but from its Component (not from the Instance) and you should define the Component on the same page where your linked Main Frame is (remember that [prototypes in Figma are currently limited to single pages](https://www.figma.com/best-practices/five-ways-to-improve-your-prototyping-workflow/#_4-a-table-of-contents)). |

#### [**Texts overflow the cell container when importing for Web.**](#Texts+overflow+the+cell+container+when+importing+for+Web.)

|  |  |
| --- | --- |
| **Cause** | This is a known issue up to GeneXus 18 Upgrade 3. |
| **Solution** | Manually create a text cell class with the 'overflow: auto' property, or upgrade to GeneXus 18 Upgrade 4. |

#### **Texts are either clipped to the cell or displayed with line breaks.**

|  |  |
| --- | --- |
| **Cause** | The designer might have defined the text box without sufficient vertical or horizontal space to ensure uninterrupted text display and prevent clipping or line breaks (especially due to ascender or descender lines). Additionally, the font-size and line-height should not exceed the height of the text box, and it is essential to check the [touch-target values](https://wiki.genexus.com/commwiki/wiki?46874) when designing for mobile apps. |
| **Solution** | Ensure adequate space and font sizing and respect touch-target values for mobile design. |

#### **Instances of symbol/components marked as Exportable do not apply the defined overrides**

|  |  |
| --- | --- |
| **Cause** | When you define a symbol/component as Exportable, GeneXus treats it as an image. The Import Design tool will ignore any overrides applied to those instances, as well as any definitions in the nested layers of the component. |
| **Solution** | If you need a symbol/component to be marked as Exportable and also require applying some overrides on their instances, consider defining variants of that symbol/component, marking each variant as Exportable, and then instantiating them appropriately in your design. |


|  |
| --- |
| **Backlinks** |
| [Design Import option (GeneXus 18 latest upgrade or prior)](https://wiki.genexus.com/commwiki/wiki?59501) | [Design Import option (GeneXus 18 Upgrade 4 or prior)](https://wiki.genexus.com/commwiki/wiki?55439) |
| [DesignOps - FAQ and Troubleshooting](https://wiki.genexus.com/commwiki/wiki?46880) | [DesignOps - Guide for designers](https://wiki.genexus.com/commwiki/wiki?46871) | [DesignOps - Guide for developers](https://wiki.genexus.com/commwiki/wiki?46877) | [Table of contents:DesignOps and GeneXus](https://wiki.genexus.com/commwiki/wiki?46870) |

---
