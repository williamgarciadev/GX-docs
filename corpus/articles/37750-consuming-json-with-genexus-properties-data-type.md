---
title: "Consuming JSON with GeneXus Properties Data Type"
source_id: 37750
source_url: https://wiki.genexus.com/commwiki/wiki?37750
genexus_version: "18"
---

# Consuming JSON with GeneXus Properties Data Type

Perhaps one of the simplest ways to consume JSON with GeneXus is to use [Structured Data Types](https://wiki.genexus.com/commwiki/wiki?10021) (SDTs).

What you have to do is to declare the structure of the JSON in an SDT and then use the SDT [FromJson method](https://wiki.genexus.com/commwiki/wiki?37809) to move content from the JSON string to the SDT.

For example:

```
&SDT.FromJson( jsonString )
```

A problem may occur when the properties of a certain object of a JSON are variable, and it may be worse if they are variable and with high cardinality.

For example, [CryptoCompare](https://www.cryptocompare.com/api/#-api-data-coinlist-) API exposes your coins as:

`[imagen omitida: wiki id 37753]`

Note that it is not feasible to declare all the elements of the "Data" property because there are thousands of coins, and you would have an SDT with thousands of elements. On top of that, when a new currency appears, it would not be declared in the SDT structure.  
  
In these cases, the [Properties Data Type](https://wiki.genexus.com/commwiki/wiki?31606) comes into action to solve the parsing of this structure.

The Properties data type conceptually maps a dictionary. And that is exactly what a JSON is.

A JSON Object, delimited by {}, is essentially a dictionary. Therefore, it can be represented perfectly by a Properties object.

In case of JSON Array, delimited by [], use Properties Data Type with the Collection property as True.

### [The solution](#The+solution)

To do the parsing of this JSON, the following is enough:

```
&Properties.FromJson(&jsonString) //Properties is of Properties Data Type
```

After this, you can check the value of any of its properties as follows:

```
&Properties.Get(!"Response") // Returns Success for the example shown above
```

Or, interestingly, you can ask for the "Data" property which will return a string with another JSON of the form:

```
{
       "LTC": {
            "Id": "3808",
            "Url": "/coins/ltc/overview",
            "ImageUrl": "/media/19782/ltc.png",
            "Name": "LTC",
            "CoinName": "Litecoin",
            "FullName": "Litecoin (LTC)",
            "Algorithm": "Scrypt",
            "ProofType": "PoW",
            "SortOrder": "2"
        },
        “BTC” : { … },
                          ...

},
```

Now, you can turn this value into a variable of type Properties again:

```
&CoinsProperties.FromJson(&dataString) //&CoinsProperties is of Properties data type
```

Going through the elements of that dictionary can be done as follows:

```
For &Coin in &CoinProperties //&Coin is of Property data type
    msg(&Coin.Key) // this prints LTC, BTC, ...
    msg(&Coin.Value) 
EndFor
```

Therefore, the final result of parsing that JSON using Properties Data Type would be as follows:

if &CoinsListProperties.Get(!"Response") = !"Success"  
        &CoinProperties.FromJson(&CoinsListProperties.Get(!"Data"))  
        for &Coin in &CoinProperties  
            &CoinDataStructure.FromJson(&Coin.Value)  
            &CoinDataStructureCollection.Add(&CoinDataStructure)  
            &CoinDataStructure = new()  
        endfor  
  else  
        msg(!"Failed to retrieve the information.")  
  endif

Note: The Coin data structure can be represented in an SDT as follows:

`[imagen omitida: wiki id 37755]`

Download the sample from [here](https://wiki.genexus.com/commwiki/wiki?37757,,).

### [How to execute the sample](#How+to+execute+the+sample)

Run the Web Panel SampleJsonConsumer and enter the following JSON:

```
{
    "Response": "Success",
    "Message": "Coin list succesfully returned!",
    "BaseImageUrl": "https://www.cryptocompare.com",
    "BaseLinkUrl": "https://www.cryptocompare.com",
    "Data": {
        "LTC": {
            "Id": "3808",
            "Url": "/coins/ltc/overview",
            "ImageUrl": "/media/19782/ltc.png",
            "Name": "LTC",
            "CoinName": "Litecoin",
            "FullName": "Litecoin (LTC)",
            "Algorithm": "Scrypt",
            "ProofType": "PoW",
            "SortOrder": "2"
        },
        "IN": {
            "Id": 0,
            "Url": "/coins/in/overview",
            "ImageUrl": "/media/1381987/in.png",
            "Name": "IN",
            "CoinName": "InCoin",
            "FullName": "InCoin (IN)",
            "Algorithm": "X11",
            "ProofType": "PoW/PoS",
            "SortOrder": 988
        },
        "AURS": {
            "Id": 0,
            "Url": "/coins/aurs/overview",
            "ImageUrl": "/media/12318345/aurs.png",
            "Name": "AURS",
            "CoinName": "Aureus",
            "FullName": "Aureus (AURS)",
            "Algorithm": "Scrypt",
            "ProofType": "N/A",
            "SortOrder": 1711
        }

    },
    "Type": 100
}
```

View the results.

`[imagen omitida: wiki id 37759]`

### [Examples with Array JSON](#Examples+with+Array+JSON)

Here are some canonical examples.

Suppose you have this JSON and you want to print all the Student's names:

```
{
  "Students": [
    {
      "Name": "Amit Goenka",
      "Major": "Physics"
    },
    {
      "Name": "Smita Pallod",
      "Major": "Chemistry"
    },
    {
      "Name": "Rajeev Sen",
      "Major": "Mathematics"
    }
  ]
}
```

The GeneXus code would be:

```
&Properties.FromJson(&json)
&StudentsProperties.FromJson(&Properties.Get(!"Students"))
For &StudentProperties in &StudentsProperties
    msg(&StudentProperties.Get(!"Name"))
Endfor
```

Where &StudentProperties and &StudentsProperties are defined as Properties Data Type, but the last one has the Collection property set to True.

Output:

```
Amit Goenka
Smita Pallod
Rajeev Sen
```

The following example is an Array JSON (it starts and ends with '[' and ']').

```
 [ { "Name": "Amit Goenka", "Major": "Physics" }, { "Name": "Smita Pallod", "Major": "Chemistry" }, { "Name": "Rajeev Sen", "Major": "Mathematics" } ]
```

The GeneXus code to print the student's names within the collection is:

```
&PropertiesCollection.FromJson(&json)
For &StudentProperties in &PropertiesCollection
    msg(&StudentProperties.Get(!"Name"))
endfor
```

Where &PropertiesCollection is defined as Properties Data Type with Collection property set to True. &StudentProperties is just defined as Properties Data Type.

Output:

```
Amit Goenka
Smita Pallod
Rajeev Sen
```


|  |
| --- |
| **Backlinks** |
| [Properties Data Type](https://wiki.genexus.com/commwiki/wiki?31606) |

---
