---
title: "Design System Tokens Options"
source_id: 49381
source_url: https://wiki.genexus.com/commwiki/wiki?49381
genexus_version: "18"
---

# Design System Tokens Options

The set of [Tokens](https://wiki.genexus.com/commwiki/wiki?47378) of a [Design System](https://wiki.genexus.com/commwiki/wiki?40108) can be parameterized so that the value of some or all the tokens can be varied according to the options being used for the parameters at runtime.

A clear example is when you want to have a Light and a Dark mode for the application. This variation usually affects only the colors; therefore, it would be enough to add a parameter to the TokensSetName representing the mode, specify that its possible values will be Light and Dark, and set the values of the color Tokens for Light mode and of the color Tokens for Dark mode —for those that change according to the mode.

`[imagen omitida: wiki id 49379]`

Depending on the value of the color-scheme option selected at runtime, the classes that use the OnSurface, Surface and Highlight color Tokens will vary the associated values and therefore will be displayed differently at runtime (the generation of the DSO takes them into account and sets the corresponding selectors for each token depending on the parameters chosen):

`[imagen omitida: wiki id 49394]`

In [Design System Tokens](https://wiki.genexus.com/commwiki/wiki?47378), the general syntax was presented showing parameters and conditions as optional:

```
tokens TokensSetName [(option1,...,optionN)]
'{'
       [tokensDeclarations1]
        ...
       [tokensDeclarationsN]
'}'
```

[View Syntax conventions](https://wiki.genexus.com/commwiki/wiki?49363).

**Where:**

*TokensSetName*

      Name given to the set of token declarations. Currently, only one set of token declarations can be defined in a DSO, but more may be available in the future.

*option1,...,optionN*  
      Each option has the following format:

*option\_name***:** **'****['***value1***']****'** **'|'** *value2* ...'**|'** *valueN*

* *option\_name*: Name by which the definition of some or all tokens can be varied. It can be a name such as color-scheme, mode, platform, etc.
* *value1*: Value that can take the *option\_name*. The bold square brackets are used to define that this option is the default one.
* *value2,...,valueN*: Value that can take the *option\_name*.

**Notes:**

* The list of values must be separated by "**|**".
* Values are not enclosed in quotation marks.

*tokensDeclarations*  
     Each tokenDeclaration corresponds to an option declared, and has the following format:

```
[option_condition]
'{'
       [#token_group1]
      '{'
               [token_name1: value[unit];|valuewithData;] 
                ...
               [token_nameN: value[unit];|valuewithData;]
      '}'] 
      ...
     [#token_groupN]|[tokensDeclarations1]...[tokensDeclarationsN] 
'}'
```

         Each option*\_*condition has the following format:

**@***option\_name1* **=** *value1i ...*[**and** **@***option\_nameN* **=** *valueNk*]

* *option\_name1*: One of the parameters of *TokensSetName*.
* *value1i*: One of the values listed for the *option\_name*1.

### [Sample](#Sample)

```
tokens MyTokensSet (color-scheme: [Light]|Dark, platform: [Native]|Web Angular| Web)
{
       @color-scheme =  Light
       {
              #colors
              {
                      primary: black;
              }
       }

       @color-scheme = Light and @platform = Native
       {
              #colors
              {
                      primary: grey;
              }
              // more
       }
       // more
}
```

**Note**: In this case, the default options of color-scheme and platform are Light and Native respectively.

Nesting is also valid, and behaves like AND:

```
tokens MyTokensSet (color-scheme: [Light]|Dark, platform: [Native]|Web Angular|Web)
{
       @color-scheme =  Light
       {
              #colors
              {
                      primary: black;
              }
              @platform = Native
              {
                    #colors
                    {
                             primary: grey;
                    }
                    // more
              }
        }
        // more
}
```

### [Set the value of an option at runtime](#Set+the+value+of+an+option+at+runtime)

In order to assign and change the value of the parameters by code, the [Design System external object](https://wiki.genexus.com/commwiki/wiki?49367), inside the GeneXus module, provides the SetOption method.

`[imagen omitida: wiki id 49398]`

If an option has no value at runtime, only the tokens not conditioned according to the option will have a value. The others are left without a value.

The dark / light example is provided for illustrative purposes only. With these parameters, you can have any custom option that the developer wants to define. Therefore, there is no reason to vary only the color tokens. Conditions can be set for all token groups.

### [Image variation](#Image+variation)

It is also possible to vary an image at runtime according to the options. See [Image variation by Tokens options](https://wiki.genexus.com/commwiki/wiki?49372).

`[imagen omitida: wiki id 49375]`

### [Imported tokens](#Imported+tokens)

If a DSO A or only its token set is being imported into a DSO B (always from the Styles tab) and it has defined options not needed in DSO B because its tokens will not be varied by those options, the tokens from DSO A can be used in the classes of DSO B without having to declare the parameters again.

Example:

```
Tokens DSOA_Tokens (option1: a|b)
{
       @option1 = a
       {
              #colors           
              {
                      primary: red;
       }
              }
       @option1 = b
       {
             #colors
             {
                      primary: blue;
             }
       }
}

Tokens DSOB_Tokens
{
       #colors
       {
               secondary: black;
       }
}

Styles DSOB_Styles
{
       @Import DSOA.tokens;
       .class1
       {
              color: $colors.primary;
              background-color: $colors.secondary;
       }
}
```

Suppose that an object has DSOB as its associated Style, and contains a TextBlock with class class1. At runtime, the TextBlock font will look red or blue, depending on the option set for option1. In addition, it will always be displayed with a black background color.

To set the option at runtime you can use the SetOption method seamlessly even if the option doesn't come from the DSO itself, but from an imported one.

In the example, you could set the option as follows:

```
DesignSystem.SetOption(option1, a)
```

The code must be set on a UI Object (any Panel) otherwise the following error may appear:

```
spc0200 External Object GeneXus\Common\UI\DesignSystem does not implement method 'setoption(' for X environment.
```

### [Availability](#Availability)

Since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?48684,,).


|  |
| --- |
| **Backlinks** |
| [Design System external object](https://wiki.genexus.com/commwiki/wiki?49367) | [Design System Tokens](https://wiki.genexus.com/commwiki/wiki?47378) | [Toc:Design Systems](https://wiki.genexus.com/commwiki/wiki?40108) |
| [GetInternalURI method](https://wiki.genexus.com/commwiki/wiki?52480) | [Image variation by Tokens options](https://wiki.genexus.com/commwiki/wiki?49372) |

---
