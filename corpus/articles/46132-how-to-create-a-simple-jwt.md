---
title: "How to create a simple JWT"
source_id: 46132
source_url: https://wiki.genexus.com/commwiki/wiki?46132
genexus_version: "18"
---

# How to create a simple JWT

This document describes how to create a very simple JWT with a common symmetric algorithm using GeneXusJWT module.

```
//******HEADER******//
//{
//  "alg": "HS256",
//  "typ": "JWT"
//}
//******PAYLOAD******//
//{
//  "jti": "0696bb20-6223-4a1c-9ebf-e15c74387b9c",
//  "iss": "example.com",
//    "exp" : 1909649720,
//  "company": "Example",
//}

//Obtaining an hexadecimal key for a symmetric encryption algorithm since it is what we are using (HS256)
&symmetricKey = &SymmetricKeyGenerator.DoGenerateKey(SymmetricKeyType.GENERICRANDOM, 256)

//Adding iss claim, it is a registered claim
//Registered claims are not mandatory therefore are added on JWTOptions SDT
//Documentation: https://wiki.genexus.com/commwiki/servlet/wiki?43983,JWT+Optional+Data
//For more information about JWT claim types https://wiki.genexus.com/commwiki/servlet/wiki?43981,JSON+Web+Token+Standard+%28JWT%29
&JWTOptions.AddRegisteredClaim(RegisteredClaim.iss, "example.com")

//Adding exp claim, it is a registered claim that validates time.
//Therefore AddCustomTimeValidationClaim is the method to use with a time with "yyyy/MM/dd HH:mm:ss" picture
&JWTOptions.AddCustomTimeValidationClaim(RegisteredClaim.exp, "2030/07/07 10:15:20", "0")
&JWTOptions.AddRegisteredClaim(RegisteredClaim.jti, "0696bb20-6223-4a1c-9ebf-e15c74387b9c")
//Adding the key to use for the signature
&JWTOptions.SetSecret(&symmetricKey)

&PrivateClaims.SetClaim("company","Example")

//Use DoCreate to sign and encode the token
//Documentation: https://wiki.genexus.com/commwiki/servlet/wiki?43989,JWT+Creator
&token = &JWTCreator.DoCreate(JWTAlgorithm.HS256, &PrivateClaims, &JWTOptions)

if &JWTCreator.HasError()
    msg("Error on creation: Code: " + &JWTCreator.GetErrorCode() + " Description: " + &JWTCreator.GetErrorDescription(), status)
else
    msg("Correctly generated", status)

    msg("Base 64 token: " + &token, status)

    //The JWTCeator object also has functions to obtain the header and  the payload from the encoded token in plain text

    &header = &JWTCreator.GetHeader(&token)

    msg("Token header: " + &header, status)

    &payload = &JWTCreator.GetPayload(&token)

    msg("Token payload: " + &payload, status)

    &verification = &JWTCreator.DoVerify(&token, JWTAlgorithm.HS256, &PrivateClaims, &JWTOptions)
    //This verification method verifies the recieved token agains the key and claims provided, not just the signature
    //If the token was changed in any mean it will fail
    //When the above specification fails it will return false as for any other type of error
    if &JWTCreator.HasError()
        msg("Error on creation: Code: " + &JWTCreator.GetErrorCode() + " Description: " + &JWTCreator.GetErrorDescription(), status)
    else
        msg("Correctly verified. Result: " + &verification.ToString(), status)
    endif

endif
```


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
