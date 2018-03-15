---
title: "Point Compression Algorithm | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 315dec80-3d91-46be-957a-c3519e7285bd
caps.latest.revision: 12
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Point Compression Algorithm
When the number of points (latitude and longitude pairs) becomes too large, the length of the URL request may exceed limits imposed by clients, proxies, or the server. To reduce the size of the request or when you cannot use the HTTP POST method, you can implement the compression algorithm described below to get a compressed string that you can use instead of the lengthy points list. The `points` parameter in the Elevation API URLs supports these compressed strings and automatically returns uncompressed elevation data. There is no need for a decompression algorithm.  
  
 This algorithm is best for 400 points or less. If you are requesting elevation data for more than 400 points, make an HTTP POST request.  
  
 The following example shows the difference in size between a list of points and the equivalent compressed string.  
  
 **Original Values**  
  
 points=35.894309002906084,-110.72522000409663,35.893930979073048,-110.72577999904752,35.893744984641671,-110.72606003843248,35.893366960808635,-110.72661500424147  
  
 **Equivalent Compressed Value**  
  
 points=vx1vilihnM6hR7mEl2Q  
  
 The following example shows how to use this encoded value as the points value when you request elevation values along a polyline path.  
  
```  
http://dev.virtualearth.net/REST/v1/Elevation/Polyline?points=vx1vilihnM6hR7mEl2Q&samples=20&heights=sealevel&key=BingMapsKey  
```  
  
## Algorithm Description  
 The following step-by-step instructions describe the point compression algorithm complete with an example. A test URL that you can use with a small number of points to test your algorithm implementation is described in [Testing Your Algorithm Implementation](../rest-services/point-compression-algorithm.md#TestingYourAlg), and a [JavaScript Implementation](../rest-services/point-compression-algorithm.md#javascriptalg) is provided.  
  
1.  Start with a set of latitude and longitude values.  
  
    ```  
    35.894309002906084, -110.72522000409663  
    35.893930979073048, -110.72577999904752  
    35.893744984641671, -110.72606003843248  
    35.893366960808635, -110.72661500424147  
  
    ```  
  
2.  Multiply each value by 100000 and round each result to the nearest integer.  
  
    ```  
    3589431, -11072522  
    3589393, -11072578  
    3589374, -11072606  
    3589337, -11072662  
  
    ```  
  
3.  Calculate the difference between every pair of values. If a longitude difference exceeds +18000000 or -18000000, add or subtract 36000000 from the value.  
  
     If your set of points spans a path that is greater than 180 degrees, divide the path into multiple segments so that no individual segment exceeds 180 degrees.  
  
    ```  
  
    3589431, -11072522  
        -38,       -56  
        -19,       -28  
        -37,       -56  
  
    ```  
  
4.  Multiply each value by 2.  
  
    ```  
    7178862, -22145044  
        -76,      -112  
        -38,       -56  
        -74,      -112  
  
    ```  
  
5.  If any value is negative, change it to be a positive value, and then subtract 1.  
  
    ```  
    7178862,  22145043  
         75,       111  
         37,        55  
         73,       111  
  
    ```  
  
6.  For each pair of latitude and longitude coordinates, compute the following value: ((latitude + longitude) * (latitude + longitude + 1) / 2)  + latitude. This can require up to 51 bits of precision. (Javascript performs exact arithmetic with up to 53 bits of precision).  
  
    ```  
    429945724065327  
              17466  
               4315  
              17093  
  
    ```  
  
7.  For each number, form a list of numbers by dividing the number by 32 repeatedly and recording each remainder. Stop when the quotient (not the remainder) reaches zero. If you start at zero, just record a zero.  
  
     For example, 17466 divided by 32 is 545 with a remainder of 26, so "26" is the first number.  Divide 545 by 32 to get 17 with a remainder of 1 making "1" the second number.   Divide 17 by 32 to get zero with a remainder of 17 making "17". the last and final number in the sequence.  
  
    ```  
    15, 17, 21, 15, 2, 5, 2, 1, 7, 12  
    26, 1, 17  
    27, 6, 4  
    5, 22, 16  
    ```  
  
8.  Add 32 to each number except for the last number in each list.  
  
    ```  
    47, 49, 53, 47, 34, 37, 34, 33, 39, 12  
    58, 33, 17  
    59, 38, 4  
    37, 54, 16  
    ```  
  
9. Form a string by converting each number to a character using the following lookup table.  
  
    ```  
    0  1  2  3  4  5  6  7  8  9  10  11  12  13  14  15    
    A  B  C  D  E  F  G  H  I  J  K   L   M   N   O   P     
  
    16  17  18  19  20  21  22  23  24  25  26  27  28    
    Q   R   S   T   U   V   W   X   Y   Z   a   b   c  
  
    29  30  31  32  33  34  35  36  37  38  39  40  41  
    d   e   f   g   h   i   j   k   l   m   n   o   p    
  
    42  43  44  45  46  47  48  49  50  51  52  53  54  
    q   r   s   t   u   v   w   x   y   z   0   1   2  
  
    55  56  57  58  59  60  61  62  63  
    3   4   5   6   7   8   9   _   -  
    ```  
  
    ```  
    vx1vilihnM  
    6hR  
    7mE  
    l2Q  
  
    ```  
  
10. Concatenate the strings and use this string as the encoded value for the points parameter.  
  
    ```  
    points=vx1vilihnM6hR7mEl2Q  
  
    ```  
  
<a name="javascriptalg"></a>   
## JavaScript Implementation  
 The following JavaScript code is an implementation of this algorithm.  
  
```javascript  
function encodePoints(points) {  
    var latitude = 0;  
    var longitude = 0;  
    var result = [];   
    var l;  
  
    for (var point in points ) {  
  
        // step 2  
        var newLatitude = Math.round(points[point][0] * 100000);  
        var newLongitude = Math.round(points[point][1] * 100000);  
  
        // step 3  
        var dy = newLatitude - latitude;  
        var dx = newLongitude - longitude;  
        latitude = newLatitude;  
        longitude = newLongitude;  
  
        // step 4 and 5  
        dy = (dy << 1) ^ (dy >> 31);  
        dx = (dx << 1) ^ (dx >> 31);  
  
        // step 6  
        var index = ((dy + dx) * (dy + dx + 1) / 2) + dy;  
  
        while (index > 0) {  
  
            // step 7  
            var rem = index & 31;  
            index = (index - rem) / 32;  
  
            // step 8  
            if (index > 0) rem += 32;  
  
            // step 9  
            result.push("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-"[rem]);  
        }  
    }  
  
    // step 10  
    return result.join("");  
}  
```  
  
<a name="TestingYourAlg"></a>   
## Testing Your Algorithm Implementation  
 The following URL is provided for you to **test your algorithm**. You can compare the compressed string computed by this URL for a small number of points to the compressed string computed by your implementation. There is no value in using this to create the compressed string in general because you are subject to the same length limitation as the Elevation API URLs.  
  
```  
http://dev.virtualearth.net/REST/v1/Elevation/PointCompression?points=lat1,long1,lat2,long2,latn,longn&key=BingMapsKey  
```  
  
 **Example TEST Request**: The following request provides a set of test points in the URL request, and the response returns a compressed string in the `value` (JSON) or `Value` (XML) field.  
  
```  
http://dev.virtualearth.net/REST/v1/Elevation/PointCompression?points=35.894309002906084,-110.72522000409663,35.893930979073048,-110.72577999904752,35.893744984641671,-110.72606003843248&key=BingMapsKey  
```  
  
 **JSON TEST Response**  
  
```  
{  
   "authenticationResultCode":"ValidCredentials",  
   "brandLogoUri":"http:\/\/dev.virtualearth.net\/Branding\/logo_powered_by.png",  
   "copyright":"Copyright © 2012 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",  
   "resourceSets":[  
      {  
         "estimatedTotal":1,  
         "resources":[  
            {  
               "__type":"CompressedPointList:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "value":"vx1vilihnM6hR7mEl2Q"  
            }  
         ]  
      }  
   ],  
   "statusCode":200,  
   "statusDescription":"OK",  
   "traceId":"31fbc5fa9724425487a63838d552ae0b"  
}  
```  
  
 **XML Test Response**  
  
```  
<Response xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">  
  <Copyright>  
    Copyright © 2012 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.  
  </Copyright>  
  <BrandLogoUri>http://dev.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>  
  <StatusCode>200</StatusCode>  
  <StatusDescription>OK</StatusDescription>  
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
  <TraceId>  
    84aafc1217a94048a396338e4cdaefdf  
  </TraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>1</EstimatedTotal>  
      <Resources>  
        <CompressedPointList>  
          <Value>vx1vilihnM6hR7mEl2Q</Value>  
        </CompressedPointList>  
      </Resources>  
    </ResourceSet>  
  </ResourceSets>  
</Response>  
  
```  
  
## See Also  
 [Using the REST Services with .NET](../rest-services/using-the-rest-services-with-net.md)   
 [JSON Data Contracts](../rest-services/json-data-contracts.md)