---
title: "GeneXus GEMA for Figma"
source_id: 56951
source_url: https://wiki.genexus.com/commwiki/wiki?56951
genexus_version: "18"
---

# GeneXus GEMA for Figma

The GeneXus GEMA plugin automatically generates the [Figma design](https://www.figma.com/) (the front-end) of a [GeneXus Next](https://wiki.genexus.com/commwiki/wiki?55887,,) application, using Generative Artificial Intelligence (Generative AI).

## [Installation](#Installation)

Install the plugin from this website: [Figma Community | GeneXus GEMA](https://www.figma.com/community/plugin/1328744258781351944).

## [Usage](#Usage)

### [1. Create a new GeneXus Next application](#1.+Create+a+new+GeneXus+Next+application)

**Note**: If you are a designer lacking knowledge or interest in GeneXus Next, you may skip this step, but you should request the **Application Web URL** and **Application Access Key** from your developer.

Go to the [GeneXus Next website](https://next.genexus.ai) and log in (or sign up).

|  |
| --- |
|  |

Then, [create a new project on GeneXus Next](https://wiki.genexus.com/commwiki/wiki?55967,,), wait until the process is finished (you will be notified by email), and open your generated project through the Menu > My Projects option.

|  |
| --- |
|  |

Once you open your project, you will see a section like this:

|  |
| --- |
|  |

Finally, get the **Application Web URL** and the **Application Access Key** as follows:

1. Click on the Access Key tab.
2. Click on the Copy button for the Access Key section. This key will be your **Application Access Key**.
3. Click on the Copy button for the Backoffice URL section. This URL will be your **Application Web URL**.

### [2. Set up the GEMA plugin](#2.+Set+up+the+GEMA+plugin)

Go back to Figma, open the GeneXus GEMA plugin, and set up the parameters for generating a new application flow.

**Warning**: Do not close the plugin in any stage. You can use the resize icon in the upper right to minimize or maximize. If you close the plugin, the process will restart from the beginning.

|  |  |
| --- | --- |
|  | Options:  * **GeneXus Next Web Application URL**    The Web Application URL you obtained in [step 1](https://wiki.genexus.com/commwiki/wiki?56951). * **GeneXus Next Application Access Key**    The Application Access Key you obtained in [step 1](https://wiki.genexus.com/commwiki/wiki?56951). * **Platform**    The target platform for generating the design (mobile or web). * **Describe your project**    A brief description of the design to be generated. * **Generate Application Flow**    Starts the generation process for an initial application flow, and continues with the following step: Flow. |

### [3. Generate the Application Flow](#3.+Generate+the+Application+Flow)

After generating the initial application flow, it's important to review results to either accept or reject them (by regenerating a new one).

|  |  |
| --- | --- |
|  | Options:  * **Restore**    Allows you to restore a previously generated flow (only available after regenerating). * **Generate New Flow**    Creates a new application flow, considering that the previous flow was not good enough. * **Keep Flow**    Accepts the generated application flow, and continues with the following step: Wireframes. |

### [4. Generate the application Wireframes](#4.+Generate+the+application+Wireframes)

Configure how the initial set of wireframes is generated.

|  |  |
| --- | --- |
|  | Options:  * **Generate wireframes for the complete flow**    Generates a set of wireframes for the whole set of nodes in the application flow. * **Generate wireframes for an individual node**    Generates a single wireframe from an individual node in the application flow. * **Generate Wireframes**    Starts generating the wireframes. |

When the initial wireframes are generated, you have to review the results and either accept or reject them (by generating a new set of wireframes).

|  |  |
| --- | --- |
|  | Options:  * **Restore**    Allows you to restore a previously generated flow (only available after regenerating). * **Generate New Ones**    Creates a new set of wireframes, considering that the previous set was not good enough. * **Keep Wireframes**    Accepts the generated wireframes and continues with the following step: Look & Feel. |

### [5. Generate the application Look & Feel](#5.+Generate+the+application+Look+%26+Feel)

At this point, GEMA will recommend you a set of color styles (palette). Each color is followed by a brief description of its purpose.

|  |  |
| --- | --- |
|  | Options:  * **Try Again**    Regenerate a new set of color styles. * **Use this Color Styles**    Accepts the proposed color styles for the final application, and continues with the text styles selection. |

GEMA will then recommend a set of text styles. Each text style is followed by a set of properties (font-family, font-size, etc.) and a brief description of where to apply them.

|  |  |
| --- | --- |
|  | Options:  * **Try Again**    Regenerate a new set of text styles. * **Use the Text Styles**    Accepts the proposed text styles for the final application, and continues with the generation of the final application. |

### [6. Generate the final application](#6.+Generate+the+final+application)

After completing the wizard, GEMA will generate the final application drawing, applying the color and text styles to the wireframes. At this point, you can start all over again.

|  |  |
| --- | --- |
|  | Options:  * **Start New**    Restart the complete process from the beginning. * **Rate your experience**    Allows you to rate your experience and share it with us. |

Finally, the designer can make any adjustments deemed necessary.

## [See also](#See+also)

[Export from Figma](https://wiki.genexus.com/commwiki/wiki?50578)  
GeneXus Prototyper for Figma


|  |
| --- |
| **Backlinks** |
| [Toc:DesignOps and GeneXus](https://wiki.genexus.com/commwiki/wiki?46870) | [GeneXus GEMA for Figma](https://wiki.genexus.com/commwiki/wiki?56951) |

---
