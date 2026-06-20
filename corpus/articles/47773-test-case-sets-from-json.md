---
title: "Test case sets from JSON"
source_id: 47773
source_url: https://wiki.genexus.com/commwiki/wiki?47773
genexus_version: "18"
---

# Test case sets from JSON

The test case set is a series of values that can be used as input values in a unit test or UI test workflow.

The values contained in the data pool will be the input, output, or expected values of the test. For example, the UI tests typically will be typed using the [type command](https://wiki.genexus.com/commwiki/wiki?41649). 

The test cases can be read from a JSON file. You must load the test cases in the JSON file, load in the KB, and read it from any test object.

Suppose that your application has a WebPanel with two input fields and a confirm button:   
**![](https://lh3.googleusercontent.com/46y2g0X-g96UT9JlVgUolKZ9EdNOBZdE_N4dY3icS9rAhfV5UypkXHFHm7DRyyYFvJ_oWgLreqlQGvzGeZJh9zXjbwrxaI0155WEb5coMz8WQ2mKvBBnnpexJwDf-bPXXBJF_DxH)**

The first step is to write the input values in a JSON file:

`[imagen omitida: wiki id 47775]`

The second step is to add the JSON [file](https://wiki.genexus.com/commwiki/wiki?5852) in Customization -> Files, in order for it to be used from a test and the [Extract property](https://wiki.genexus.com/commwiki/wiki?5852) of the respective environment must be set in True.

**![](https://lh5.googleusercontent.com/YD1gLhKdMNBl7RmInA4Sb9HfeZnNzds8QWmdtC6TmH2_z9lVseQdxfbE-ee6xu32_FgHflgck3H1p_Vfz7krRv1blVU4pQKGxx1T5YuGuATUlpOG-nvQRd-aM1-fGERflwtqhNgM)**

During the building process, the JSON file will be copied to the environment folder ([Extract property](https://wiki.genexus.com/commwiki/wiki?5852) must be set to True).

**![](https://lh4.googleusercontent.com/-Etf-bMEia32XfkjmWfuDLm6BstEO2WC5nyMnFCWy9plTqAJvFhx-eMQDq07MN0-24kMMSC3KoqJKpnoj57Ln20Wbx6TlhapCrmAzXPF3QJJTfzSErEMPPl9NyNctUUjxEmlZ3rm)**

Then, you have to update the test to read the test values from the JSON. The JSON values will be saved in an SDT data collection and the test will iterate over it.

```
&driver.Start()
&driver.Maximize()

&File.Source = "TestDataFile.json"
&TestCases.FromJsonFile(&File)

for &TestCase in &TestCases
   &driver.Go(WebPanel.Link())
   &driver.Type("&Field1",&TestCase.InputValue1)
   &driver.Type("&Field2",&TestCase.InputValue2)
   &driver.ClickByID("Confirm")
endfor

// End driver
&driver.End()
```

To define the below variables, an SDT structure should be created and the variables should be defined:

**![](https://lh4.googleusercontent.com/idS7tMxZzaMGUgv6dL3TwJ1LSf-Yz9ZavYy2SiL05Y-orfeIfunLD14bML6eFaAd4DQhnp6Ao_55WcuDh-76T7c3wxsR5wQaQlMdKhsVCffk3iTea5pWQkhuZOrD7J-llMdTbygk)**

**![](https://lh5.googleusercontent.com/modDea5l4SwsNrKWjNK8aNFYTEr_snrmJcoHyKell2NSdAJVR4X3YNwv_uEhmGSGgssiAM0s6so4hQMspPGpHVFEprTqTTVliuBptQnqB2vElfVhijBoIBCvPOx3mG9f7aKHLmM9)**

Note that you can use the test case sets for all test types.

Another possible solution to manage test case sets values is to implement a data provider, in which you write the different test cases, and the test iterates over this (like in the automatic generated unit tests).


|  |
| --- |
| **Backlinks** |
| [Toc:Automated Testing](https://wiki.genexus.com/commwiki/wiki?56229) | [Toc:GXtest](https://wiki.genexus.com/commwiki/wiki?38327) |

---
