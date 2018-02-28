---
title: "Driving Route Example | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: c65b5f8c-73d9-49b6-9f25-cf188cbc231f
caps.latest.revision: 13
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
---
# Driving Route Example
The following example shows how to request a driving route between two locations that minimizes the use of toll roads. Responses are shown for both XML and JSON formats.  
  
```  
http://dev.virtualearth.net/REST/V1/Routes/Driving?wp.0=redmond%2Cwa&wp.1=Issaquah%2Cwa&avoid=minimizeTolls&key=BingMapsKey  
```  
  
 **JSON Response**  
  
```  
{  
   "authenticationResultCode":"ValidCredentials",  
   "brandLogoUri":"http:\/\/dev.virtualearth.net\/Branding\/logo_powered_by.png",  
   "copyright":"Copyright © 2014 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",  
   "resourceSets":[  
      {  
         "estimatedTotal":1,  
         "resources":[  
            {  
               "__type":"Route:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
               "bbox":[  
                  47.53009,  
                  -122.189448,  
                  47.678588,  
                  -122.033799  
               ],  
               "id":"v65,h131861087,i0,a2,cen-US,dAAAAAAAAAAA1,y0,s1,m1,o1,t4,w3vM8BP_TJPU1~AnVFsCKB8g4BAADgAQAAgD8A0~UmVkbW9uZCwgV0E1~~~,w6pI5BJoNJ_U1~AnVFsCIBuhoBAADgAd709z4A0~SXNzYXF1YWgsIFdB0~~~,k1",  
               "distanceUnit":"Kilometer",  
               "durationUnit":"Second",  
               "routeLegs":[  
                  {  
                     "actualEnd":{  
                        "type":"Point",  
                        "coordinates":[  
                           47.53009,  
                           -122.033799  
                        ]  
                     },  
                     "actualStart":{  
                        "type":"Point",  
                        "coordinates":[  
                           47.678583,  
                           -122.131459  
                        ]  
                     },  
                     "alternateVias":[  
  
                     ],  
                     "cost":0,  
                     "description":"",  
                     "endLocation":{  
                        "bbox":[  
                           47.480648,  
                           -122.153313,  
                           47.5811,  
                           -121.912598  
                        ],  
                        "name":"Issaquah, WA",  
                        "point":{  
                           "type":"Point",  
                           "coordinates":[  
                              47.530102,  
                              -122.033798  
                           ]  
                        },  
                        "address":{  
                           "adminDistrict":"WA",  
                           "adminDistrict2":"King Co.",  
                           "countryRegion":"United States",  
                           "formattedAddress":"Issaquah, WA",  
                           "locality":"Issaquah"  
                        },  
                        "confidence":"High",  
                        "entityType":"PopulatedPlace",  
                        "geocodePoints":[  
                           {  
                              "type":"Point",  
                              "coordinates":[  
                                 47.530102,  
                                 -122.033798  
                              ],  
                              "calculationMethod":"Rooftop",  
                              "usageTypes":[  
                                 "Display"  
                              ]  
                           }  
                        ],  
                        "matchCodes":[  
                           "Good"  
                        ]  
                     },  
                     "itineraryItems":[  
                        {  
                           "compassDirection":"west",  
                           "details":[  
                              {  
                                 "compassDegrees":270,  
                                 "endPathIndices":[  
                                    1  
                                 ],  
                                 "maneuverType":"DepartStart",  
                                 "mode":"Driving",  
                                 "names":[  
                                    "NE 85th St"  
                                 ],  
                                 "roadType":"Street",  
                                 "startPathIndices":[  
                                    0  
                                 ]  
                              }  
                           ],  
                           "exit":"",  
                           "iconType":"Auto",  
                           "instruction":{  
                              "formattedText":null,  
                              "maneuverType":"DepartStart",  
                              "text":"Depart NE 85th St toward 154th Ave NE"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 47.678583,  
                                 -122.131459  
                              ]  
                           },  
                           "sideOfStreet":"Unknown",  
                           "tollZone":"",  
                           "towardsRoadName":"154th Ave NE",  
                           "transitTerminus":"",  
                           "travelDistance":0.243,  
                           "travelDuration":25,  
                           "travelMode":"Driving"  
                        },  
                        {  
                           "compassDirection":"south",  
                           "details":[  
                              {  
                                 "compassDegrees":179,  
                                 "endPathIndices":[  
                                    6  
                                 ],  
                                 "maneuverType":"TurnLeft",  
                                 "mode":"Driving",  
                                 "names":[  
                                    "154th Ave NE"  
                                 ],  
                                 "roadType":"Street",  
                                 "startPathIndices":[  
                                    1  
                                 ]  
                              }  
                           ],  
                           "exit":"",  
                           "iconType":"Auto",  
                           "instruction":{  
                              "formattedText":null,  
                              "maneuverType":"TurnLeft",  
                              "text":"Turn left onto 154th Ave NE"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 47.678588,  
                                 -122.134661  
                              ]  
                           },  
                           "sideOfStreet":"Unknown",  
                           "tollZone":"",  
                           "transitTerminus":"",  
                           "travelDistance":0.836,  
                           "travelDuration":88,  
                           "travelMode":"Driving"  
                        },  
                        {  
                           "compassDirection":"southeast",  
                           "details":[  
                              {  
                                 "compassDegrees":131,  
                                 "endPathIndices":[  
                                    9  
                                 ],  
                                 "locationCodes":[  
                                    "114-08476"  
                                 ],  
                                 "maneuverType":"KeepStraight",  
                                 "mode":"Driving",  
                                 "names":[  
                                    "W Lake Sammamish Pkwy NE"  
                                 ],  
                                 "roadType":"Arterial",  
                                 "startPathIndices":[  
                                    6  
                                 ]  
                              }  
                           ],  
                           "exit":"",  
                           "iconType":"Auto",  
                           "instruction":{  
                              "formattedText":null,  
                              "maneuverType":"KeepStraight",  
                              "text":"Keep straight onto W Lake Sammamish Pkwy NE"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 47.671341,  
                                 -122.13237  
                              ]  
                           },  
                           "sideOfStreet":"Unknown",  
                           "tollZone":"",  
                           "transitTerminus":"",  
                           "travelDistance":0.316,  
                           "travelDuration":19,  
                           "travelMode":"Driving"  
                        },  
                        {  
                           "compassDirection":"southwest",  
                           "details":[  
                              {  
                                 "compassDegrees":230,  
                                 "endPathIndices":[  
                                    19  
                                 ],  
                                 "locationCodes":[  
                                    "114N10641"  
                                 ],  
                                 "maneuverType":"TakeRampRight",  
                                 "mode":"Driving",  
                                 "roadType":"Ramp",  
                                 "startPathIndices":[  
                                    9  
                                 ]  
                              },  
                              {  
                                 "compassDegrees":229,  
                                 "endPathIndices":[  
                                    55  
                                 ],  
                                 "locationCodes":[  
                                    "114-04240",  
                                    "114N04240",  
                                    "114-04239",  
                                    "114N04239",  
                                    "114-04238",  
                                    "114N04238",  
                                    "114-04237",  
                                    "114N04237",  
                                    "114-04236",  
                                    "114N04236"  
                                 ],  
                                 "maneuverType":"Merge",  
                                 "mode":"Driving",  
                                 "names":[  
                                    "WA-520 West"  
                                 ],  
                                 "roadShieldRequestParameters":{  
                                    "bucket":51095,  
                                    "shields":[  
                                       {  
                                          "labels":[  
                                             "520"  
                                          ],  
                                          "roadShieldType":3  
                                       }  
                                    ]  
                                 },  
                                 "roadType":"LimitedAccessHighway",  
                                 "startPathIndices":[  
                                    19  
                                 ]  
                              }  
                           ],  
                           "exit":"",  
                           "hints":[  
                              {  
                                 "hintType":null,  
                                 "text":"7-Eleven on the corner"  
                              }  
                           ],  
                           "iconType":"Auto",  
                           "instruction":{  
                              "formattedText":null,  
                              "maneuverType":"RampThenHighwayRight",  
                              "text":"Take ramp right for WA-520 West toward Seattle"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 47.66934,  
                                 -122.129501  
                              ]  
                           },  
                           "sideOfStreet":"Unknown",  
                           "signs":[  
                              "Seattle",  
                              "WA-520 West"  
                           ],  
                           "tollZone":"",  
                           "transitTerminus":"",  
                           "travelDistance":8.035,  
                           "travelDuration":361,  
                           "travelMode":"Driving"  
                        },  
                        {  
                           "compassDirection":"south",  
                           "details":[  
                              {  
                                 "compassDegrees":308,  
                                 "endPathIndices":[  
                                    64  
                                 ],  
                                 "locationCodes":[  
                                    "114P13706"  
                                 ],  
                                 "maneuverType":"TakeRampRight",  
                                 "mode":"Driving",  
                                 "roadType":"Ramp",  
                                 "startPathIndices":[  
                                    55  
                                 ]  
                              },  
                              {  
                                 "compassDegrees":198,  
                                 "endPathIndices":[  
                                    82  
                                 ],  
                                 "locationCodes":[  
                                    "114N04137",  
                                    "114-04136",  
                                    "114N04136",  
                                    "114-04135",  
                                    "114N04135",  
                                    "114-04134",  
                                    "114N04134",  
                                    "114-04133"  
                                 ],  
                                 "maneuverType":"Merge",  
                                 "mode":"Driving",  
                                 "names":[  
                                    "I-405 South"  
                                 ],  
                                 "roadShieldRequestParameters":{  
                                    "bucket":51095,  
                                    "shields":[  
                                       {  
                                          "labels":[  
                                             "405"  
                                          ],  
                                          "roadShieldType":1  
                                       }  
                                    ]  
                                 },  
                                 "roadType":"LimitedAccessHighway",  
                                 "startPathIndices":[  
                                    64  
                                 ]  
                              }  
                           ],  
                           "exit":"",  
                           "iconType":"Auto",  
                           "instruction":{  
                              "formattedText":null,  
                              "maneuverType":"RampThenHighwayRight",  
                              "text":"Take ramp right for I-405 South toward Renton"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 47.63269,  
                                 -122.188729  
                              ]  
                           },  
                           "sideOfStreet":"Unknown",  
                           "signs":[  
                              "I-405 South",  
                              "Renton"  
                           ],  
                           "tollZone":"",  
                           "transitTerminus":"",  
                           "travelDistance":5.612,  
                           "travelDuration":223,  
                           "travelMode":"Driving",  
                           "warnings":[  
                              {  
                                 "origin":"47.616339,-122.188922",  
                                 "severity":"Moderate",  
                                 "text":"Moderate Congestion",  
                                 "to":"47.615958,-122.188922",  
                                 "warningType":"TrafficFlow"  
                              }  
                           ]  
                        },  
                        {  
                           "compassDirection":"east",  
                           "details":[  
                              {  
                                 "compassDegrees":161,  
                                 "endPathIndices":[  
                                    93  
                                 ],  
                                 "locationCodes":[  
                                    "114P13608",  
                                    "114P13614",  
                                    "114P13592"  
                                 ],  
                                 "maneuverType":"TakeRampRight",  
                                 "mode":"Driving",  
                                 "roadType":"Ramp",  
                                 "startPathIndices":[  
                                    82  
                                 ]  
                              },  
                              {  
                                 "compassDegrees":93,  
                                 "endPathIndices":[  
                                    112  
                                 ],  
                                 "locationCodes":[  
                                    "114-04111",  
                                    "114N04111",  
                                    "114-04110",  
                                    "114N04110",  
                                    "114-04109",  
                                    "114N04109",  
                                    "114-04108",  
                                    "114N04108",  
                                    "114-04107"  
                                 ],  
                                 "maneuverType":"Merge",  
                                 "mode":"Driving",  
                                 "names":[  
                                    "I-90 East"  
                                 ],  
                                 "roadShieldRequestParameters":{  
                                    "bucket":51095,  
                                    "shields":[  
                                       {  
                                          "labels":[  
                                             "90"  
                                          ],  
                                          "roadShieldType":1  
                                       }  
                                    ]  
                                 },  
                                 "roadType":"LimitedAccessHighway",  
                                 "startPathIndices":[  
                                    93  
                                 ]  
                              }  
                           ],  
                           "exit":"11",  
                           "iconType":"Auto",  
                           "instruction":{  
                              "formattedText":null,  
                              "maneuverType":"RampThenHighwayRight",  
                              "text":"At exit 11, take ramp right for I-90 East toward Spokane"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 47.586631,  
                                 -122.179309  
                              ]  
                           },  
                           "sideOfStreet":"Unknown",  
                           "signs":[  
                              "I-90 East",  
                              "Spokane"  
                           ],  
                           "tollZone":"",  
                           "transitTerminus":"",  
                           "travelDistance":12.011,  
                           "travelDuration":452,  
                           "travelMode":"Driving",  
                           "warnings":[  
                              {  
                                 "origin":"47.57808,-122.132762",  
                                 "severity":"Minor",  
                                 "text":"Minor Congestion",  
                                 "to":"47.577962,-122.132269",  
                                 "warningType":"TrafficFlow"  
                              }  
                           ]  
                        },  
                        {  
                           "compassDirection":"southeast",  
                           "details":[  
                              {  
                                 "compassDegrees":139,  
                                 "endPathIndices":[  
                                    117  
                                 ],  
                                 "maneuverType":"TakeRampRight",  
                                 "mode":"Driving",  
                                 "roadType":"Ramp",  
                                 "startPathIndices":[  
                                    112  
                                 ]  
                              }  
                           ],  
                           "exit":"17",  
                           "iconType":"Auto",  
                           "instruction":{  
                              "formattedText":null,  
                              "maneuverType":"TakeRampRight",  
                              "text":"At exit 17, take ramp right for Front St toward E Lk Sammamish Parkway SE"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 47.542632,  
                                 -122.040698  
                              ]  
                           },  
                           "sideOfStreet":"Unknown",  
                           "signs":[  
                              "E Lk Sammamish Parkway SE",  
                              "Front St"  
                           ],  
                           "tollZone":"",  
                           "transitTerminus":"",  
                           "travelDistance":0.42,  
                           "travelDuration":24,  
                           "travelMode":"Driving"  
                        },  
                        {  
                           "compassDirection":"south",  
                           "details":[  
                              {  
                                 "compassDegrees":180,  
                                 "endPathIndices":[  
                                    120  
                                 ],  
                                 "locationCodes":[  
                                    "114-10308"  
                                 ],  
                                 "maneuverType":"TurnRight",  
                                 "mode":"Driving",  
                                 "names":[  
                                    "Front St N"  
                                 ],  
                                 "roadType":"Ramp",  
                                 "startPathIndices":[  
                                    117  
                                 ]  
                              }  
                           ],  
                           "exit":"",  
                           "iconType":"Auto",  
                           "instruction":{  
                              "formattedText":null,  
                              "maneuverType":"TurnRight",  
                              "text":"Turn right onto Front St N"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 47.539912,  
                                 -122.0369  
                              ]  
                           },  
                           "sideOfStreet":"Unknown",  
                           "tollZone":"",  
                           "transitTerminus":"",  
                           "travelDistance":1.122,  
                           "travelDuration":127,  
                           "travelMode":"Driving"  
                        },  
                        {  
                           "compassDirection":"east",  
                           "details":[  
                              {  
                                 "compassDegrees":90,  
                                 "endPathIndices":[  
                                    122  
                                 ],  
                                 "locationCodes":[  
                                    "114P11405",  
                                    "114+11406"  
                                 ],  
                                 "maneuverType":"TurnLeft",  
                                 "mode":"Driving",  
                                 "names":[  
                                    "E Sunset Way"  
                                 ],  
                                 "roadType":"Arterial",  
                                 "startPathIndices":[  
                                    120  
                                 ]  
                              }  
                           ],  
                           "exit":"",  
                           "hints":[  
                              {  
                                 "hintType":null,  
                                 "text":"Shell on the corner"  
                              }  
                           ],  
                           "iconType":"Auto",  
                           "instruction":{  
                              "formattedText":null,  
                              "maneuverType":"TurnLeft",  
                              "text":"Turn left onto E Sunset Way"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 47.530128,  
                                 -122.03653  
                              ]  
                           },  
                           "sideOfStreet":"Unknown",  
                           "tollZone":"",  
                           "transitTerminus":"",  
                           "travelDistance":0.208,  
                           "travelDuration":43,  
                           "travelMode":"Driving"  
                        },  
                        {  
                           "compassDirection":"east",  
                           "details":[  
                              {  
                                 "compassDegrees":91,  
                                 "endPathIndices":[  
                                    122  
                                 ],  
                                 "locationCodes":[  
                                    "114+11406"  
                                 ],  
                                 "maneuverType":"ArriveFinish",  
                                 "mode":"Driving",  
                                 "names":[  
                                    "E Sunset Way"  
                                 ],  
                                 "roadType":"Arterial",  
                                 "startPathIndices":[  
                                    122  
                                 ]  
                              }  
                           ],  
                           "exit":"",  
                           "hints":[  
                              {  
                                 "hintType":null,  
                                 "text":"The last intersection is Rainier Blvd S"  
                              },  
                              {  
                                 "hintType":null,  
                                 "text":"If you reach 2nd Ave SE, you've gone too far"  
                              }  
                           ],  
                           "iconType":"Auto",  
                           "instruction":{  
                              "formattedText":null,  
                              "maneuverType":"ArriveFinish",  
                              "text":"Arrive at Issaquah, WA"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 47.53009,  
                                 -122.033799  
                              ]  
                           },  
                           "sideOfStreet":"Unknown",  
                           "tollZone":"",  
                           "transitTerminus":"",  
                           "travelDistance":0,  
                           "travelDuration":0,  
                           "travelMode":"Driving"  
                        }  
                     ],  
                     "routeRegion":"NAv2",  
                     "routeSubLegs":[  
                        {  
                           "endWaypoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 47.530102,  
                                 -122.033798  
                              ],  
                              "description":"Issaquah, WA",  
                              "isVia":false,  
                              "locationIdentifier":"2|117|69|176|34|1|186|26|1|0|0|224|1|222|244|247|62|0|47.53009,-122.033799",  
                              "routePathIndex":122  
                           },  
                           "startWaypoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 47.678581,  
                                 -122.131577  
                              ],  
                              "description":"Redmond, WA",  
                              "isVia":false,  
                              "locationIdentifier":"2|117|69|176|34|129|242|14|1|0|0|224|1|0|0|128|63|0|47.678583,-122.131459",  
                              "routePathIndex":0  
                           },  
                           "travelDistance":28.803,  
                           "travelDuration":1368  
                        }  
                     ],  
                     "startLocation":{  
                        "bbox":[  
                           47.626041,  
                           -122.249229,  
                           47.729954,  
                           -121.999512  
                        ],  
                        "name":"Redmond, WA",  
                        "point":{  
                           "type":"Point",  
                           "coordinates":[  
                              47.678581,  
                              -122.131577  
                           ]  
                        },  
                        "address":{  
                           "adminDistrict":"WA",  
                           "adminDistrict2":"King Co.",  
                           "countryRegion":"United States",  
                           "formattedAddress":"Redmond, WA",  
                           "locality":"Redmond"  
                        },  
                        "confidence":"High",  
                        "entityType":"PopulatedPlace",  
                        "geocodePoints":[  
                           {  
                              "type":"Point",  
                              "coordinates":[  
                                 47.678581,  
                                 -122.131577  
                              ],  
                              "calculationMethod":"Rooftop",  
                              "usageTypes":[  
                                 "Display"  
                              ]  
                           }  
                        ],  
                        "matchCodes":[  
                           "Good"  
                        ]  
                     },  
                     "travelDistance":28.803,  
                     "travelDuration":1368  
                  }  
               ],  
               "travelDistance":28.803,  
               "travelDuration":1368,  
               "travelDurationTraffic":1887  
            }  
         ]  
      }  
   ],  
   "statusCode":200,  
   "statusDescription":"OK",  
   "traceId":"f663f126aada4830b104085d80c54bab "  
}  
```  
  
 **XML Response**  
  
 You would receive the following JSON response if the output=xml parameter was set in the URL request.  
  
```  
<?xml version="1.0" encoding="utf-8"?>  
<Response xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">  
  <Copyright>Copyright © 2014 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>  
  <BrandLogoUri>http://dev.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>  
  <StatusCode>200</StatusCode>  
  <StatusDescription>OK</StatusDescription>  
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
  <TraceId>c3d88797fee3467b8b2292291498d735</TraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>1</EstimatedTotal>  
      <Resources>  
        <Route>  
          <Id>v65,h131861087,i0,a2,cen-US,dAAAAAAAAAAA1,y0,s1,m1,o1,t4,w3vM8BP_TJPU1~AnVFsCKB8g4BAADgAQAAgD8A0~UmVkbW9uZCwgV0E1~~~,w6pI5BJoNJ_U1~AnVFsCIBuhoBAADgAd709z4A0~SXNzYXF1YWgsIFdB0~~~,k1</Id>  
          <BoundingBox>  
            <SouthLatitude>47.53009</SouthLatitude>  
            <WestLongitude>-122.189448</WestLongitude>  
            <NorthLatitude>47.678588</NorthLatitude>  
            <EastLongitude>-122.033799</EastLongitude>  
          </BoundingBox>  
          <DistanceUnit>Kilometer</DistanceUnit>  
          <DurationUnit>Second</DurationUnit>  
          <TravelDistance>28.803</TravelDistance>  
          <TravelDuration>1368</TravelDuration>  
          <TravelDurationTraffic>1888</TravelDurationTraffic>  
          <RouteLeg>  
            <TravelDistance>28.803</TravelDistance>  
            <TravelDuration>1368</TravelDuration>  
            <Cost>0</Cost>  
            <ActualStart>  
              <Latitude>47.678583</Latitude>  
              <Longitude>-122.131459</Longitude>  
            </ActualStart>  
            <ActualEnd>  
              <Latitude>47.53009</Latitude>  
              <Longitude>-122.033799</Longitude>  
            </ActualEnd>  
            <StartLocation>  
              <Name>Redmond, WA</Name>  
              <Point>  
                <Latitude>47.678581</Latitude>  
                <Longitude>-122.131577</Longitude>  
              </Point>  
              <BoundingBox>  
                <SouthLatitude>47.626041</SouthLatitude>  
                <WestLongitude>-122.249229</WestLongitude>  
                <NorthLatitude>47.729954</NorthLatitude>  
                <EastLongitude>-121.999512</EastLongitude>  
              </BoundingBox>  
              <EntityType>PopulatedPlace</EntityType>  
              <Address>  
                <AdminDistrict>WA</AdminDistrict>  
                <AdminDistrict2>King Co.</AdminDistrict2>  
                <CountryRegion>United States</CountryRegion>  
                <FormattedAddress>Redmond, WA</FormattedAddress>  
                <Locality>Redmond</Locality>  
              </Address>  
              <Confidence>High</Confidence>  
              <MatchCode>Good</MatchCode>  
              <GeocodePoint>  
                <Latitude>47.678581</Latitude>  
                <Longitude>-122.131577</Longitude>  
                <CalculationMethod>Rooftop</CalculationMethod>  
                <UsageType>Display</UsageType>  
              </GeocodePoint>  
            </StartLocation>  
            <EndLocation>  
              <Name>Issaquah, WA</Name>  
              <Point>  
                <Latitude>47.530102</Latitude>  
                <Longitude>-122.033798</Longitude>  
              </Point>  
              <BoundingBox>  
                <SouthLatitude>47.480648</SouthLatitude>  
                <WestLongitude>-122.153313</WestLongitude>  
                <NorthLatitude>47.5811</NorthLatitude>  
                <EastLongitude>-121.912598</EastLongitude>  
              </BoundingBox>  
              <EntityType>PopulatedPlace</EntityType>  
              <Address>  
                <AdminDistrict>WA</AdminDistrict>  
                <AdminDistrict2>King Co.</AdminDistrict2>  
                <CountryRegion>United States</CountryRegion>  
                <FormattedAddress>Issaquah, WA</FormattedAddress>  
                <Locality>Issaquah</Locality>  
              </Address>  
              <Confidence>High</Confidence>  
              <MatchCode>Good</MatchCode>  
              <GeocodePoint>  
                <Latitude>47.530102</Latitude>  
                <Longitude>-122.033798</Longitude>  
                <CalculationMethod>Rooftop</CalculationMethod>  
                <UsageType>Display</UsageType>  
              </GeocodePoint>  
            </EndLocation>  
            <ItineraryItem>  
              <TravelMode>Driving</TravelMode>  
              <TravelDistance>0.243</TravelDistance>  
              <TravelDuration>25</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>47.678583</Latitude>  
                <Longitude>-122.131459</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="DepartStart">Depart NE 85th St toward 154th Ave NE</Instruction>  
              <CompassDirection>west</CompassDirection>  
              <Detail>  
                <ManeuverType>DepartStart</ManeuverType>  
                <StartPathIndex>0</StartPathIndex>  
                <EndPathIndex>1</EndPathIndex>  
                <Name>NE 85th St</Name>  
                <CompassDegrees>270</CompassDegrees>  
                <Mode>Driving</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>Street</RoadType>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Auto</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <TowardsRoadName>154th Ave NE</TowardsRoadName>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Driving</TravelMode>  
              <TravelDistance>0.836</TravelDistance>  
              <TravelDuration>88</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>47.678588</Latitude>  
                <Longitude>-122.134661</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="TurnLeft">Turn left onto 154th Ave NE</Instruction>  
              <CompassDirection>south</CompassDirection>  
              <Detail>  
                <ManeuverType>TurnLeft</ManeuverType>  
                <StartPathIndex>1</StartPathIndex>  
                <EndPathIndex>6</EndPathIndex>  
                <Name>154th Ave NE</Name>  
                <CompassDegrees>179</CompassDegrees>  
                <Mode>Driving</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>Street</RoadType>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Auto</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Driving</TravelMode>  
              <TravelDistance>0.316</TravelDistance>  
              <TravelDuration>19</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>47.671341</Latitude>  
                <Longitude>-122.13237</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="KeepStraight">Keep straight onto W Lake Sammamish Pkwy NE</Instruction>  
              <CompassDirection>southeast</CompassDirection>  
              <Detail>  
                <ManeuverType>KeepStraight</ManeuverType>  
                <StartPathIndex>6</StartPathIndex>  
                <EndPathIndex>9</EndPathIndex>  
                <Name>W Lake Sammamish Pkwy NE</Name>  
                <CompassDegrees>131</CompassDegrees>  
                <Mode>Driving</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>Arterial</RoadType>  
                <LocationCode>114-08476</LocationCode>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Auto</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Driving</TravelMode>  
              <TravelDistance>8.035</TravelDistance>  
              <TravelDuration>361</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>47.66934</Latitude>  
                <Longitude>-122.129501</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="RampThenHighwayRight">Take ramp right for WA-520 West toward Seattle</Instruction>  
              <CompassDirection>southwest</CompassDirection>  
              <Hint>7-Eleven on the corner</Hint>  
              <Detail>  
                <ManeuverType>TakeRampRight</ManeuverType>  
                <StartPathIndex>9</StartPathIndex>  
                <EndPathIndex>19</EndPathIndex>  
                <CompassDegrees>230</CompassDegrees>  
                <Mode>Driving</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>Ramp</RoadType>  
                <LocationCode>114N10641</LocationCode>  
              </Detail>  
              <Detail>  
                <ManeuverType>Merge</ManeuverType>  
                <StartPathIndex>19</StartPathIndex>  
                <EndPathIndex>55</EndPathIndex>  
                <Name>WA-520 West</Name>  
                <CompassDegrees>229</CompassDegrees>  
                <Mode>Driving</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>LimitedAccessHighway</RoadType>  
                <RoadShieldRequestParameters>  
                  <Bucket>51095</Bucket>  
                  <Shield>  
                    <RoadShieldType>3</RoadShieldType>  
                    <Label>520</Label>  
                  </Shield>  
                </RoadShieldRequestParameters>  
                <LocationCode>114-04240</LocationCode>  
                <LocationCode>114N04240</LocationCode>  
                <LocationCode>114-04239</LocationCode>  
                <LocationCode>114N04239</LocationCode>  
                <LocationCode>114-04238</LocationCode>  
                <LocationCode>114N04238</LocationCode>  
                <LocationCode>114-04237</LocationCode>  
                <LocationCode>114N04237</LocationCode>  
                <LocationCode>114-04236</LocationCode>  
                <LocationCode>114N04236</LocationCode>  
              </Detail>  
              <Sign>Seattle</Sign>  
              <Sign>WA-520 West</Sign>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Auto</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Driving</TravelMode>  
              <TravelDistance>5.612</TravelDistance>  
              <TravelDuration>223</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>47.63269</Latitude>  
                <Longitude>-122.188729</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="RampThenHighwayRight">Take ramp right for I-405 South toward Renton</Instruction>  
              <CompassDirection>south</CompassDirection>  
              <Warning warningType="TrafficFlow" severity="Moderate" origin="47.616339,-122.188922" to="47.615958,-122.188922">Moderate Congestion</Warning>  
              <Detail>  
                <ManeuverType>TakeRampRight</ManeuverType>  
                <StartPathIndex>55</StartPathIndex>  
                <EndPathIndex>64</EndPathIndex>  
                <CompassDegrees>308</CompassDegrees>  
                <Mode>Driving</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>Ramp</RoadType>  
                <LocationCode>114P13706</LocationCode>  
              </Detail>  
              <Detail>  
                <ManeuverType>Merge</ManeuverType>  
                <StartPathIndex>64</StartPathIndex>  
                <EndPathIndex>82</EndPathIndex>  
                <Name>I-405 South</Name>  
                <CompassDegrees>198</CompassDegrees>  
                <Mode>Driving</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>LimitedAccessHighway</RoadType>  
                <RoadShieldRequestParameters>  
                  <Bucket>51095</Bucket>  
                  <Shield>  
                    <RoadShieldType>1</RoadShieldType>  
                    <Label>405</Label>  
                  </Shield>  
                </RoadShieldRequestParameters>  
                <LocationCode>114N04137</LocationCode>  
                <LocationCode>114-04136</LocationCode>  
                <LocationCode>114N04136</LocationCode>  
                <LocationCode>114-04135</LocationCode>  
                <LocationCode>114N04135</LocationCode>  
                <LocationCode>114-04134</LocationCode>  
                <LocationCode>114N04134</LocationCode>  
                <LocationCode>114-04133</LocationCode>  
              </Detail>  
              <Sign>I-405 South</Sign>  
              <Sign>Renton</Sign>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Auto</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Driving</TravelMode>  
              <TravelDistance>12.011</TravelDistance>  
              <TravelDuration>452</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>47.586631</Latitude>  
                <Longitude>-122.179309</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="RampThenHighwayRight">At exit 11, take ramp right for I-90 East toward Spokane</Instruction>  
              <CompassDirection>east</CompassDirection>  
              <Warning warningType="TrafficFlow" severity="Minor" origin="47.57808,-122.132762" to="47.577962,-122.132269">Minor Congestion</Warning>  
              <Detail>  
                <ManeuverType>TakeRampRight</ManeuverType>  
                <StartPathIndex>82</StartPathIndex>  
                <EndPathIndex>93</EndPathIndex>  
                <CompassDegrees>161</CompassDegrees>  
                <Mode>Driving</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>Ramp</RoadType>  
                <LocationCode>114P13608</LocationCode>  
                <LocationCode>114P13614</LocationCode>  
                <LocationCode>114P13592</LocationCode>  
              </Detail>  
              <Detail>  
                <ManeuverType>Merge</ManeuverType>  
                <StartPathIndex>93</StartPathIndex>  
                <EndPathIndex>112</EndPathIndex>  
                <Name>I-90 East</Name>  
                <CompassDegrees>93</CompassDegrees>  
                <Mode>Driving</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>LimitedAccessHighway</RoadType>  
                <RoadShieldRequestParameters>  
                  <Bucket>51095</Bucket>  
                  <Shield>  
                    <RoadShieldType>1</RoadShieldType>  
                    <Label>90</Label>  
                  </Shield>  
                </RoadShieldRequestParameters>  
                <LocationCode>114-04111</LocationCode>  
                <LocationCode>114N04111</LocationCode>  
                <LocationCode>114-04110</LocationCode>  
                <LocationCode>114N04110</LocationCode>  
                <LocationCode>114-04109</LocationCode>  
                <LocationCode>114N04109</LocationCode>  
                <LocationCode>114-04108</LocationCode>  
                <LocationCode>114N04108</LocationCode>  
                <LocationCode>114-04107</LocationCode>  
              </Detail>  
              <Sign>I-90 East</Sign>  
              <Sign>Spokane</Sign>  
              <Exit>11</Exit>  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Auto</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Driving</TravelMode>  
              <TravelDistance>0.42</TravelDistance>  
              <TravelDuration>24</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>47.542632</Latitude>  
                <Longitude>-122.040698</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="TakeRampRight">At exit 17, take ramp right for Front St toward E Lk Sammamish Parkway SE</Instruction>  
              <CompassDirection>southeast</CompassDirection>  
              <Detail>  
                <ManeuverType>TakeRampRight</ManeuverType>  
                <StartPathIndex>112</StartPathIndex>  
                <EndPathIndex>117</EndPathIndex>  
                <CompassDegrees>139</CompassDegrees>  
                <Mode>Driving</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>Ramp</RoadType>  
              </Detail>  
              <Sign>E Lk Sammamish Parkway SE</Sign>  
              <Sign>Front St</Sign>  
              <Exit>17</Exit>  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Auto</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Driving</TravelMode>  
              <TravelDistance>1.122</TravelDistance>  
              <TravelDuration>127</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>47.539912</Latitude>  
                <Longitude>-122.0369</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="TurnRight">Turn right onto Front St N</Instruction>  
              <CompassDirection>south</CompassDirection>  
              <Detail>  
                <ManeuverType>TurnRight</ManeuverType>  
                <StartPathIndex>117</StartPathIndex>  
                <EndPathIndex>120</EndPathIndex>  
                <Name>Front St N</Name>  
                <CompassDegrees>180</CompassDegrees>  
                <Mode>Driving</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>Ramp</RoadType>  
                <LocationCode>114-10308</LocationCode>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Auto</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Driving</TravelMode>  
              <TravelDistance>0.208</TravelDistance>  
              <TravelDuration>43</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>47.530128</Latitude>  
                <Longitude>-122.03653</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="TurnLeft">Turn left onto E Sunset Way</Instruction>  
              <CompassDirection>east</CompassDirection>  
              <Hint>Shell on the corner</Hint>  
              <Detail>  
                <ManeuverType>TurnLeft</ManeuverType>  
                <StartPathIndex>120</StartPathIndex>  
                <EndPathIndex>122</EndPathIndex>  
                <Name>E Sunset Way</Name>  
                <CompassDegrees>90</CompassDegrees>  
                <Mode>Driving</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>Arterial</RoadType>  
                <LocationCode>114P11405</LocationCode>  
                <LocationCode>114+11406</LocationCode>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Auto</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Driving</TravelMode>  
              <TravelDistance>0</TravelDistance>  
              <TravelDuration>0</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>47.53009</Latitude>  
                <Longitude>-122.033799</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="ArriveFinish">Arrive at Issaquah, WA</Instruction>  
              <CompassDirection>east</CompassDirection>  
              <Hint>The last intersection is Rainier Blvd S</Hint>  
              <Hint>If you reach 2nd Ave SE, you've gone too far</Hint>  
              <Detail>  
                <ManeuverType>ArriveFinish</ManeuverType>  
                <StartPathIndex>122</StartPathIndex>  
                <EndPathIndex>122</EndPathIndex>  
                <Name>E Sunset Way</Name>  
                <CompassDegrees>91</CompassDegrees>  
                <Mode>Driving</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>Arterial</RoadType>  
                <LocationCode>114+11406</LocationCode>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Auto</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <RouteSubLeg>  
              <TravelDistance>28.803</TravelDistance>  
              <TravelDuration>1368</TravelDuration>  
              <StartWaypoint>  
                <Latitude>47.678581</Latitude>  
                <Longitude>-122.131577</Longitude>  
                <Description>Redmond, WA</Description>  
                <IsVia>false</IsVia>  
                <LocationIdentifier>2|117|69|176|34|129|242|14|1|0|0|224|1|0|0|128|63|0|47.678583,-122.131459</LocationIdentifier>  
                <RoutePathIndex>0</RoutePathIndex>  
              </StartWaypoint>  
              <EndWaypoint>  
                <Latitude>47.530102</Latitude>  
                <Longitude>-122.033798</Longitude>  
                <Description>Issaquah, WA</Description>  
                <IsVia>false</IsVia>  
                <LocationIdentifier>2|117|69|176|34|1|186|26|1|0|0|224|1|222|244|247|62|0|47.53009,-122.033799</LocationIdentifier>  
                <RoutePathIndex>122</RoutePathIndex>  
              </EndWaypoint>  
            </RouteSubLeg>  
            <StartTime>0001-01-01T00:00:00</StartTime>  
            <EndTime>0001-01-01T00:00:00</EndTime>  
            <Description />  
            <RouteRegion>NAv2</RouteRegion>  
          </RouteLeg>  
        </Route>  
      </Resources>  
    </ResourceSet>  
  </ResourceSets>  
</Response>  
```  
  
## See Also  
 [Using the REST Services with .NET](../rest-services/using-the-rest-services-with-net.md)   
 [JSON Data Contracts](../rest-services/json-data-contracts.md)