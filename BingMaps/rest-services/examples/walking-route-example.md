---
title: "Walking Route Example | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 4f924f37-12ee-4f21-a1df-2bb3a228587e
caps.latest.revision: 11
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Walking Route Example
This example returns a walking route from the Eiffel Tower to the Louvre Museum in Paris, France. The route is optimized for distance. Responses are shown for both XML and JSON formats.  
  
```  
http://dev.virtualearth.net/REST/V1/Routes/Walking?wp.0=Eiffel%20Tower&wp.1=louvre%20museum&optmz=distance&output=xml&key=BingMapsKey  
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
                  48.858623,  
                  2.293761,  
                  48.862928,  
                  2.335222  
               ],  
               "id":"v65,h-1816995113,i0,a0,cen-US,dAAAAAAAAAAA1,y0,s1,m2,o2,t0,w-81XBGczNAA1~A5QlvVABsgEYAADgAfQb-j4A0~RWlmZmVsIFRvd2VyLCBQYXJpcywgRnJhbmNl0~~~,w-uVXBIcjNQA1~A5QlvVDDAAYYAADgAQAAAAAA0~TG91dnJlLCBQYXJpcywgRnJhbmNl0~~~,k1",  
               "distanceUnit":"Kilometer",  
               "durationUnit":"Second",  
               "routeLegs":[  
                  {  
                     "actualEnd":{  
                        "type":"Point",  
                        "coordinates":[  
                           48.86274,  
                           2.335222  
                        ]  
                     },  
                     "actualStart":{  
                        "type":"Point",  
                        "coordinates":[  
                           48.858623,  
                           2.293965  
                        ]  
                     },  
                     "alternateVias":[  
  
                     ],  
                     "cost":0,  
                     "description":"",  
                     "endLocation":{  
                        "bbox":[  
                           48.859371,  
                           2.33046,  
                           48.863522,  
                           2.33995  
                        ],  
                        "name":"Louvre, Paris, France",  
                        "point":{  
                           "type":"Point",  
                           "coordinates":[  
                              48.86272,  
                              2.3352  
                           ]  
                        },  
                        "address":{  
                           "adminDistrict":"IdF",  
                           "adminDistrict2":"Paris",  
                           "countryRegion":"France",  
                           "formattedAddress":"Louvre, Paris, France",  
                           "locality":"Paris",  
                           "landmark":"Louvre"  
                        },  
                        "confidence":"High",  
                        "entityType":"Museum",  
                        "geocodePoints":[  
                           {  
                              "type":"Point",  
                              "coordinates":[  
                                 48.86272,  
                                 2.3352  
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
                           "compassDirection":"northeast",  
                           "details":[  
                              {  
                                 "compassDegrees":54,  
                                 "endPathIndices":[  
                                    2  
                                 ],  
                                 "maneuverType":"DepartStart",  
                                 "mode":"Walking",  
                                 "roadType":"WalkingPath",  
                                 "startPathIndices":[  
                                    0  
                                 ]  
                              }  
                           ],  
                           "exit":"",  
                           "iconType":"Walk",  
                           "instruction":{  
                              "formattedText":null,  
                              "maneuverType":"DepartStart",  
                              "text":"Depart from Eiffel Tower, Paris, France"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 48.858623,  
                                 2.293965  
                              ]  
                           },  
                           "sideOfStreet":"Unknown",  
                           "tollZone":"",  
                           "towardsRoadName":"Allée Jean Paulhan",  
                           "transitTerminus":"",  
                           "travelDistance":0.07,  
                           "travelDuration":50,  
                           "travelMode":"Walking"  
                        },  
                        {  
                           "compassDirection":"northwest",  
                           "details":[  
                              {  
                                 "compassDegrees":54,  
                                 "endPathIndices":[  
                                    4  
                                 ],  
                                 "maneuverType":"TurnRight",  
                                 "mode":"Walking",  
                                 "roadType":"WalkingPath",  
                                 "startPathIndices":[  
                                    2  
                                 ]  
                              },  
                              {  
                                 "compassDegrees":303,  
                                 "endPathIndices":[  
                                    5  
                                 ],  
                                 "maneuverType":"TurnLeft",  
                                 "mode":"Walking",  
                                 "names":[  
                                    "Allée Paul Deschanel"  
                                 ],  
                                 "roadType":"WalkingPath",  
                                 "startPathIndices":[  
                                    4  
                                 ]  
                              }  
                           ],  
                           "exit":"",  
                           "iconType":"Walk",  
                           "instruction":{  
                              "formattedText":null,  
                              "maneuverType":"TurnRightThenTurnLeft",  
                              "text":"Turn right, and then immediately turn left onto Allée Paul Deschanel"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 48.85905,  
                                 2.293761  
                              ]  
                           },  
                           "sideOfStreet":"Unknown",  
                           "tollZone":"",  
                           "transitTerminus":"",  
                           "travelDistance":0.16,  
                           "travelDuration":114,  
                           "travelMode":"Walking"  
                        },  
                        {  
                           "compassDirection":"northeast",  
                           "details":[  
                              {  
                                 "compassDegrees":53,  
                                 "endPathIndices":[  
                                    10  
                                 ],  
                                 "maneuverType":"TurnRight",  
                                 "mode":"Walking",  
                                 "names":[  
                                    "Quai Branly"  
                                 ],  
                                 "roadType":"Highway",  
                                 "startPathIndices":[  
                                    5  
                                 ]  
                              }  
                           ],  
                           "exit":"",  
                           "iconType":"Walk",  
                           "instruction":{  
                              "formattedText":null,  
                              "maneuverType":"TurnRight",  
                              "text":"Turn right onto Quai Branly"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 48.860123,  
                                 2.295011  
                              ]  
                           },  
                           "sideOfStreet":"Unknown",  
                           "tollZone":"",  
                           "transitTerminus":"",  
                           "travelDistance":0.557,  
                           "travelDuration":401,  
                           "travelMode":"Walking"  
                        },  
                        {  
                           "compassDirection":"east",  
                           "details":[  
                              {  
                                 "compassDegrees":84,  
                                 "endPathIndices":[  
                                    17  
                                 ],  
                                 "locationCodes":[  
                                    "F32-51763",  
                                    "F32-51762"  
                                 ],  
                                 "maneuverType":"KeepStraight",  
                                 "mode":"Walking",  
                                 "names":[  
                                    "Quai d'Orsay"  
                                 ],  
                                 "roadType":"Highway",  
                                 "startPathIndices":[  
                                    10  
                                 ]  
                              }  
                           ],  
                           "exit":"",  
                           "iconType":"Walk",  
                           "instruction":{  
                              "formattedText":null,  
                              "maneuverType":"KeepStraight",  
                              "text":"Keep straight onto Quai d'Orsay"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 48.862263,  
                                 2.301518  
                              ]  
                           },  
                           "sideOfStreet":"Unknown",  
                           "tollZone":"",  
                           "transitTerminus":"",  
                           "travelDistance":1.302,  
                           "travelDuration":937,  
                           "travelMode":"Walking"  
                        },  
                        {  
                           "compassDirection":"east",  
                           "details":[  
                              {  
                                 "compassDegrees":100,  
                                 "endPathIndices":[  
                                    19  
                                 ],  
                                 "locationCodes":[  
                                    "F32-51762"  
                                 ],  
                                 "maneuverType":"RoadNameChange",  
                                 "mode":"Walking",  
                                 "names":[  
                                    "Quai Anatole France"  
                                 ],  
                                 "roadType":"Highway",  
                                 "startPathIndices":[  
                                    17  
                                 ]  
                              }  
                           ],  
                           "exit":"",  
                           "iconType":"Walk",  
                           "instruction":{  
                              "formattedText":null,  
                              "maneuverType":"RoadNameChange",  
                              "text":"Road name changes to Quai Anatole France"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 48.862579,  
                                 2.319033  
                              ]  
                           },  
                           "sideOfStreet":"Unknown",  
                           "tollZone":"",  
                           "transitTerminus":"",  
                           "travelDistance":0.416,  
                           "travelDuration":299,  
                           "travelMode":"Walking"  
                        },  
                        {  
                           "compassDirection":"northeast",  
                           "details":[  
                              {  
                                 "compassDegrees":36,  
                                 "endPathIndices":[  
                                    21  
                                 ],  
                                 "maneuverType":"TurnLeft",  
                                 "mode":"Walking",  
                                 "names":[  
                                    "Passerelle Léopold Sédar Senghor"  
                                 ],  
                                 "roadType":"WalkingPath",  
                                 "startPathIndices":[  
                                    19  
                                 ]  
                              }  
                           ],  
                           "exit":"",  
                           "iconType":"Walk",  
                           "instruction":{  
                              "formattedText":null,  
                              "maneuverType":"TurnLeft",  
                              "text":"Turn left onto Passerelle Léopold Sédar Senghor"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 48.861131,  
                                 2.324182  
                              ]  
                           },  
                           "sideOfStreet":"Unknown",  
                           "tollZone":"",  
                           "transitTerminus":"",  
                           "travelDistance":0.196,  
                           "travelDuration":140,  
                           "travelMode":"Walking"  
                        },  
                        {  
                           "compassDirection":"east",  
                           "details":[  
                              {  
                                 "compassDegrees":108,  
                                 "endPathIndices":[  
                                    24  
                                 ],  
                                 "maneuverType":"TurnRight",  
                                 "mode":"Walking",  
                                 "names":[  
                                    "Terrasse du Bord de l'Eau"  
                                 ],  
                                 "roadType":"WalkingPath",  
                                 "startPathIndices":[  
                                    21  
                                 ]  
                              }  
                           ],  
                           "exit":"",  
                           "iconType":"Walk",  
                           "instruction":{  
                              "formattedText":null,  
                              "maneuverType":"TurnRight",  
                              "text":"Turn right onto Terrasse du Bord de l'Eau"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 48.862703,  
                                 2.325368  
                              ]  
                           },  
                           "sideOfStreet":"Unknown",  
                           "tollZone":"",  
                           "transitTerminus":"",  
                           "travelDistance":0.247,  
                           "travelDuration":177,  
                           "travelMode":"Walking"  
                        },  
                        {  
                           "compassDirection":"northeast",  
                           "details":[  
                              {  
                                 "compassDegrees":41,  
                                 "endPathIndices":[  
                                    28  
                                 ],  
                                 "maneuverType":"TurnLeft",  
                                 "mode":"Walking",  
                                 "roadType":"WalkingPath",  
                                 "startPathIndices":[  
                                    24  
                                 ]  
                              }  
                           ],  
                           "exit":"",  
                           "iconType":"Walk",  
                           "instruction":{  
                              "formattedText":null,  
                              "maneuverType":"TurnLeft",  
                              "text":"Turn left onto path"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 48.86171,  
                                 2.32841  
                              ]  
                           },  
                           "sideOfStreet":"Unknown",  
                           "tollZone":"",  
                           "transitTerminus":"",  
                           "travelDistance":0.165,  
                           "travelDuration":118,  
                           "travelMode":"Walking"  
                        },  
                        {  
                           "compassDirection":"east",  
                           "details":[  
                              {  
                                 "compassDegrees":108,  
                                 "endPathIndices":[  
                                    30  
                                 ],  
                                 "maneuverType":"TurnRight",  
                                 "mode":"Walking",  
                                 "roadType":"WalkingPath",  
                                 "startPathIndices":[  
                                    28  
                                 ]  
                              },  
                              {  
                                 "compassDegrees":107,  
                                 "endPathIndices":[  
                                    32  
                                 ],  
                                 "maneuverType":"KeepStraight",  
                                 "mode":"Walking",  
                                 "names":[  
                                    "Jardin du Carrousel"  
                                 ],  
                                 "roadType":"WalkingPath",  
                                 "startPathIndices":[  
                                    30  
                                 ]  
                              }  
                           ],  
                           "exit":"",  
                           "iconType":"Walk",  
                           "instruction":{  
                              "formattedText":null,  
                              "maneuverType":"TurnRight",  
                              "text":"Turn right onto Jardin du Carrousel"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 48.862799,  
                                 2.329579  
                              ]  
                           },  
                           "sideOfStreet":"Unknown",  
                           "tollZone":"",  
                           "transitTerminus":"",  
                           "travelDistance":0.239,  
                           "travelDuration":171,  
                           "travelMode":"Walking"  
                        },  
                        {  
                           "compassDirection":"east",  
                           "details":[  
                              {  
                                 "compassDegrees":107,  
                                 "endPathIndices":[  
                                    35  
                                 ],  
                                 "maneuverType":"KeepStraight",  
                                 "mode":"Walking",  
                                 "roadType":"WalkingPath",  
                                 "startPathIndices":[  
                                    32  
                                 ]  
                              }  
                           ],  
                           "exit":"",  
                           "iconType":"Walk",  
                           "instruction":{  
                              "formattedText":null,  
                              "maneuverType":"KeepStraight",  
                              "text":"Keep straight onto path"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 48.861861,  
                                 2.332529  
                              ]  
                           },  
                           "sideOfStreet":"Unknown",  
                           "tollZone":"",  
                           "transitTerminus":"",  
                           "travelDistance":0.038,  
                           "travelDuration":27,  
                           "travelMode":"Walking"  
                        },  
                        {  
                           "compassDirection":"northeast",  
                           "details":[  
                              {  
                                 "compassDegrees":40,  
                                 "endPathIndices":[  
                                    37  
                                 ],  
                                 "maneuverType":"KeepLeft",  
                                 "mode":"Walking",  
                                 "roadType":"WalkingPath",  
                                 "startPathIndices":[  
                                    35  
                                 ]  
                              }  
                           ],  
                           "exit":"",  
                           "iconType":"Walk",  
                           "instruction":{  
                              "formattedText":null,  
                              "maneuverType":"KeepLeft",  
                              "text":"Keep left onto path"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 48.861861,  
                                 2.33298  
                              ]  
                           },  
                           "sideOfStreet":"Unknown",  
                           "tollZone":"",  
                           "transitTerminus":"",  
                           "travelDistance":0.026,  
                           "travelDuration":18,  
                           "travelMode":"Walking"  
                        },  
                        {  
                           "compassDirection":"east",  
                           "details":[  
                              {  
                                 "compassDegrees":90,  
                                 "endPathIndices":[  
                                    40  
                                 ],  
                                 "maneuverType":"KeepRight",  
                                 "mode":"Walking",  
                                 "roadType":"WalkingPath",  
                                 "startPathIndices":[  
                                    37  
                                 ]  
                              }  
                           ],  
                           "exit":"",  
                           "iconType":"Walk",  
                           "instruction":{  
                              "formattedText":null,  
                              "maneuverType":"KeepRight",  
                              "text":"Keep right onto path"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 48.862048,  
                                 2.33313  
                              ]  
                           },  
                           "sideOfStreet":"Unknown",  
                           "tollZone":"",  
                           "transitTerminus":"",  
                           "travelDistance":0.041,  
                           "travelDuration":29,  
                           "travelMode":"Walking"  
                        },  
                        {  
                           "compassDirection":"east",  
                           "details":[  
                              {  
                                 "compassDegrees":82,  
                                 "endPathIndices":[  
                                    44  
                                 ],  
                                 "maneuverType":"KeepRight",  
                                 "mode":"Walking",  
                                 "roadType":"WalkingPath",  
                                 "startPathIndices":[  
                                    40  
                                 ]  
                              }  
                           ],  
                           "exit":"",  
                           "iconType":"Walk",  
                           "instruction":{  
                              "formattedText":null,  
                              "maneuverType":"KeepRight",  
                              "text":"Keep right toward Place du Carrousel"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 48.862118,  
                                 2.333581  
                              ]  
                           },  
                           "sideOfStreet":"Unknown",  
                           "tollZone":"",  
                           "transitTerminus":"",  
                           "travelDistance":0.125,  
                           "travelDuration":90,  
                           "travelMode":"Walking"  
                        },  
                        {  
                           "compassDirection":"northeast",  
                           "details":[  
                              {  
                                 "compassDegrees":45,  
                                 "endPathIndices":[  
                                    45  
                                 ],  
                                 "maneuverType":"TurnLeft",  
                                 "mode":"Walking",  
                                 "names":[  
                                    "Place du Carrousel"  
                                 ],  
                                 "roadType":"MajorRoad",  
                                 "startPathIndices":[  
                                    44  
                                 ]  
                              }  
                           ],  
                           "exit":"",  
                           "iconType":"Walk",  
                           "instruction":{  
                              "formattedText":null,  
                              "maneuverType":"TurnLeft",  
                              "text":"Turn left onto Place du Carrousel"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 48.862419,  
                                 2.3349  
                              ]  
                           },  
                           "sideOfStreet":"Unknown",  
                           "tollZone":"",  
                           "transitTerminus":"",  
                           "travelDistance":0.045,  
                           "travelDuration":32,  
                           "travelMode":"Walking"  
                        },  
                        {  
                           "compassDirection":"northeast",  
                           "details":[  
                              {  
                                 "compassDegrees":45,  
                                 "endPathIndices":[  
                                    45  
                                 ],  
                                 "maneuverType":"ArriveFinish",  
                                 "mode":"Walking",  
                                 "names":[  
                                    "Place du Carrousel"  
                                 ],  
                                 "roadType":"MajorRoad",  
                                 "startPathIndices":[  
                                    45  
                                 ]  
                              }  
                           ],  
                           "exit":"",  
                           "hints":[  
                              {  
                                 "hintType":null,  
                                 "text":"If you reach Rue de Rohan, you've gone too far"  
                              }  
                           ],  
                           "iconType":"Walk",  
                           "instruction":{  
                              "formattedText":null,  
                              "maneuverType":"ArriveFinish",  
                              "text":"Arrive at Louvre, Paris, France"  
                           },  
                           "maneuverPoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 48.86274,  
                                 2.335222  
                              ]  
                           },  
                           "sideOfStreet":"Unknown",  
                           "tollZone":"",  
                           "transitTerminus":"",  
                           "travelDistance":0,  
                           "travelDuration":0,  
                           "travelMode":"Walking"  
                        }  
                     ],  
                     "routeRegion":"EU",  
                     "routeSubLegs":[  
                        {  
                           "endWaypoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 48.86272,  
                                 2.3352  
                              ],  
                              "description":"Louvre, Paris, France",  
                              "isVia":false,  
                              "locationIdentifier":"3|148|37|189|80|195|0|6|24|0|0|224|1|0|0|0|0|0|48.86274,2.335222",  
                              "routePathIndex":45  
                           },  
                           "startWaypoint":{  
                              "type":"Point",  
                              "coordinates":[  
                                 48.858601,  
                                 2.29398  
                              ],  
                              "description":"Eiffel Tower, Paris, France",  
                              "isVia":false,  
                              "locationIdentifier":"3|148|37|189|80|1|178|1|24|0|0|224|1|244|27|250|62|0|48.858623,2.293965",  
                              "routePathIndex":0  
                           },  
                           "travelDistance":3.627,  
                           "travelDuration":2611  
                        }  
                     ],  
                     "startLocation":{  
                        "bbox":[  
                           48.82963,  
                           2.235303,  
                           48.887571,  
                           2.352657  
                        ],  
                        "name":"Eiffel Tower, Paris, France",  
                        "point":{  
                           "type":"Point",  
                           "coordinates":[  
                              48.858601,  
                              2.29398  
                           ]  
                        },  
                        "address":{  
                           "adminDistrict":"IdF",  
                           "adminDistrict2":"Paris",  
                           "countryRegion":"France",  
                           "formattedAddress":"Eiffel Tower, Paris, France",  
                           "locality":"Paris",  
                           "landmark":"Eiffel Tower"  
                        },  
                        "confidence":"High",  
                        "entityType":"Monument",  
                        "geocodePoints":[  
                           {  
                              "type":"Point",  
                              "coordinates":[  
                                 48.858601,  
                                 2.29398  
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
                     "travelDistance":3.627,  
                     "travelDuration":2611  
                  }  
               ],  
               "travelDistance":3.627,  
               "travelDuration":2611,  
               "travelDurationTraffic":2611  
            }  
         ]  
      }  
   ],  
   "statusCode":200,  
   "statusDescription":"OK",  
   "traceId":"6f839bb7358543ed93ca4cf7a3bc8f62 "  
}  
```  
  
 **XML Response**  
  
 Add output=xml to the URL above to get the XML response.  
  
```  
<?xml version="1.0" encoding="utf-8"?>  
<Response xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">  
  <Copyright>Copyright © 2014 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>  
  <BrandLogoUri>http://dev.virtualearth.net/Branding/logo_powered_by.png</BrandLogoUri>  
  <StatusCode>200</StatusCode>  
  <StatusDescription>OK</StatusDescription>  
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>  
  <TraceId>6a5c2eacdb04422d91978bf9e3a3bd73 </TraceId>  
  <ResourceSets>  
    <ResourceSet>  
      <EstimatedTotal>1</EstimatedTotal>  
      <Resources>  
        <Route>  
          <Id>v65,h-1816995113,i0,a0,cen-US,dAAAAAAAAAAA1,y0,s1,m2,o2,t0,w-81XBGczNAA1~A5QlvVABsgEYAADgAfQb-j4A0~RWlmZmVsIFRvd2VyLCBQYXJpcywgRnJhbmNl0~~~,w-uVXBIcjNQA1~A5QlvVDDAAYYAADgAQAAAAAA0~TG91dnJlLCBQYXJpcywgRnJhbmNl0~~~,k1</Id>  
          <BoundingBox>  
            <SouthLatitude>48.858623</SouthLatitude>  
            <WestLongitude>2.293761</WestLongitude>  
            <NorthLatitude>48.862928</NorthLatitude>  
            <EastLongitude>2.335222</EastLongitude>  
          </BoundingBox>  
          <DistanceUnit>Kilometer</DistanceUnit>  
          <DurationUnit>Second</DurationUnit>  
          <TravelDistance>3.627</TravelDistance>  
          <TravelDuration>2611</TravelDuration>  
          <TravelDurationTraffic>2611</TravelDurationTraffic>  
          <RouteLeg>  
            <TravelDistance>3.627</TravelDistance>  
            <TravelDuration>2611</TravelDuration>  
            <Cost>0</Cost>  
            <ActualStart>  
              <Latitude>48.858623</Latitude>  
              <Longitude>2.293965</Longitude>  
            </ActualStart>  
            <ActualEnd>  
              <Latitude>48.86274</Latitude>  
              <Longitude>2.335222</Longitude>  
            </ActualEnd>  
            <StartLocation>  
              <Name>Eiffel Tower, Paris, France</Name>  
              <Point>  
                <Latitude>48.858601</Latitude>  
                <Longitude>2.29398</Longitude>  
              </Point>  
              <BoundingBox>  
                <SouthLatitude>48.82963</SouthLatitude>  
                <WestLongitude>2.235303</WestLongitude>  
                <NorthLatitude>48.887571</NorthLatitude>  
                <EastLongitude>2.352657</EastLongitude>  
              </BoundingBox>  
              <EntityType>Monument</EntityType>  
              <Address>  
                <AdminDistrict>IdF</AdminDistrict>  
                <AdminDistrict2>Paris</AdminDistrict2>  
                <CountryRegion>France</CountryRegion>  
                <FormattedAddress>Eiffel Tower, Paris, France</FormattedAddress>  
                <Locality>Paris</Locality>  
                <Landmark>Eiffel Tower</Landmark>  
              </Address>  
              <Confidence>High</Confidence>  
              <MatchCode>Good</MatchCode>  
              <GeocodePoint>  
                <Latitude>48.858601</Latitude>  
                <Longitude>2.29398</Longitude>  
                <CalculationMethod>Rooftop</CalculationMethod>  
                <UsageType>Display</UsageType>  
              </GeocodePoint>  
            </StartLocation>  
            <EndLocation>  
              <Name>Louvre, Paris, France</Name>  
              <Point>  
                <Latitude>48.86272</Latitude>  
                <Longitude>2.3352</Longitude>  
              </Point>  
              <BoundingBox>  
                <SouthLatitude>48.859371</SouthLatitude>  
                <WestLongitude>2.33046</WestLongitude>  
                <NorthLatitude>48.863522</NorthLatitude>  
                <EastLongitude>2.33995</EastLongitude>  
              </BoundingBox>  
              <EntityType>Museum</EntityType>  
              <Address>  
                <AdminDistrict>IdF</AdminDistrict>  
                <AdminDistrict2>Paris</AdminDistrict2>  
                <CountryRegion>France</CountryRegion>  
                <FormattedAddress>Louvre, Paris, France</FormattedAddress>  
                <Locality>Paris</Locality>  
                <Landmark>Louvre</Landmark>  
              </Address>  
              <Confidence>High</Confidence>  
              <MatchCode>Good</MatchCode>  
              <GeocodePoint>  
                <Latitude>48.86272</Latitude>  
                <Longitude>2.3352</Longitude>  
                <CalculationMethod>Rooftop</CalculationMethod>  
                <UsageType>Display</UsageType>  
              </GeocodePoint>  
            </EndLocation>  
            <ItineraryItem>  
              <TravelMode>Walking</TravelMode>  
              <TravelDistance>0.07</TravelDistance>  
              <TravelDuration>50</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>48.858623</Latitude>  
                <Longitude>2.293965</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="DepartStart">Depart from Eiffel Tower, Paris, France</Instruction>  
              <CompassDirection>northeast</CompassDirection>  
              <Detail>  
                <ManeuverType>DepartStart</ManeuverType>  
                <StartPathIndex>0</StartPathIndex>  
                <EndPathIndex>2</EndPathIndex>  
                <CompassDegrees>54</CompassDegrees>  
                <Mode>Walking</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>WalkingPath</RoadType>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Walk</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <TowardsRoadName>Allée Jean Paulhan</TowardsRoadName>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Walking</TravelMode>  
              <TravelDistance>0.16</TravelDistance>  
              <TravelDuration>114</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>48.85905</Latitude>  
                <Longitude>2.293761</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="TurnRightThenTurnLeft">Turn right, and then immediately turn left onto Allée Paul Deschanel</Instruction>  
              <CompassDirection>northwest</CompassDirection>  
              <Detail>  
                <ManeuverType>TurnRight</ManeuverType>  
                <StartPathIndex>2</StartPathIndex>  
                <EndPathIndex>4</EndPathIndex>  
                <CompassDegrees>54</CompassDegrees>  
                <Mode>Walking</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>WalkingPath</RoadType>  
              </Detail>  
              <Detail>  
                <ManeuverType>TurnLeft</ManeuverType>  
                <StartPathIndex>4</StartPathIndex>  
                <EndPathIndex>5</EndPathIndex>  
                <Name>Allée Paul Deschanel</Name>  
                <CompassDegrees>303</CompassDegrees>  
                <Mode>Walking</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>WalkingPath</RoadType>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Walk</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Walking</TravelMode>  
              <TravelDistance>0.557</TravelDistance>  
              <TravelDuration>401</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>48.860123</Latitude>  
                <Longitude>2.295011</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="TurnRight">Turn right onto Quai Branly</Instruction>  
              <CompassDirection>northeast</CompassDirection>  
              <Detail>  
                <ManeuverType>TurnRight</ManeuverType>  
                <StartPathIndex>5</StartPathIndex>  
                <EndPathIndex>10</EndPathIndex>  
                <Name>Quai Branly</Name>  
                <CompassDegrees>53</CompassDegrees>  
                <Mode>Walking</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>Highway</RoadType>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Walk</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Walking</TravelMode>  
              <TravelDistance>1.302</TravelDistance>  
              <TravelDuration>937</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>48.862263</Latitude>  
                <Longitude>2.301518</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="KeepStraight">Keep straight onto Quai d'Orsay</Instruction>  
              <CompassDirection>east</CompassDirection>  
              <Detail>  
                <ManeuverType>KeepStraight</ManeuverType>  
                <StartPathIndex>10</StartPathIndex>  
                <EndPathIndex>17</EndPathIndex>  
                <Name>Quai d'Orsay</Name>  
                <CompassDegrees>84</CompassDegrees>  
                <Mode>Walking</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>Highway</RoadType>  
                <LocationCode>F32-51763</LocationCode>  
                <LocationCode>F32-51762</LocationCode>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Walk</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Walking</TravelMode>  
              <TravelDistance>0.416</TravelDistance>  
              <TravelDuration>299</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>48.862579</Latitude>  
                <Longitude>2.319033</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="RoadNameChange">Road name changes to Quai Anatole France</Instruction>  
              <CompassDirection>east</CompassDirection>  
              <Detail>  
                <ManeuverType>RoadNameChange</ManeuverType>  
                <StartPathIndex>17</StartPathIndex>  
                <EndPathIndex>19</EndPathIndex>  
                <Name>Quai Anatole France</Name>  
                <CompassDegrees>100</CompassDegrees>  
                <Mode>Walking</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>Highway</RoadType>  
                <LocationCode>F32-51762</LocationCode>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Walk</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Walking</TravelMode>  
              <TravelDistance>0.196</TravelDistance>  
              <TravelDuration>140</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>48.861131</Latitude>  
                <Longitude>2.324182</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="TurnLeft">Turn left onto Passerelle Léopold Sédar Senghor</Instruction>  
              <CompassDirection>northeast</CompassDirection>  
              <Detail>  
                <ManeuverType>TurnLeft</ManeuverType>  
                <StartPathIndex>19</StartPathIndex>  
                <EndPathIndex>21</EndPathIndex>  
                <Name>Passerelle Léopold Sédar Senghor</Name>  
                <CompassDegrees>36</CompassDegrees>  
                <Mode>Walking</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>WalkingPath</RoadType>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Walk</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Walking</TravelMode>  
              <TravelDistance>0.247</TravelDistance>  
              <TravelDuration>177</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>48.862703</Latitude>  
                <Longitude>2.325368</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="TurnRight">Turn right onto Terrasse du Bord de l'Eau</Instruction>  
              <CompassDirection>east</CompassDirection>  
              <Detail>  
                <ManeuverType>TurnRight</ManeuverType>  
                <StartPathIndex>21</StartPathIndex>  
                <EndPathIndex>24</EndPathIndex>  
                <Name>Terrasse du Bord de l'Eau</Name>  
                <CompassDegrees>108</CompassDegrees>  
                <Mode>Walking</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>WalkingPath</RoadType>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Walk</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Walking</TravelMode>  
              <TravelDistance>0.165</TravelDistance>  
              <TravelDuration>118</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>48.86171</Latitude>  
                <Longitude>2.32841</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="TurnLeft">Turn left onto path</Instruction>  
              <CompassDirection>northeast</CompassDirection>  
              <Detail>  
                <ManeuverType>TurnLeft</ManeuverType>  
                <StartPathIndex>24</StartPathIndex>  
                <EndPathIndex>28</EndPathIndex>  
                <CompassDegrees>41</CompassDegrees>  
                <Mode>Walking</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>WalkingPath</RoadType>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Walk</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Walking</TravelMode>  
              <TravelDistance>0.239</TravelDistance>  
              <TravelDuration>171</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>48.862799</Latitude>  
                <Longitude>2.329579</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="TurnRight">Turn right onto Jardin du Carrousel</Instruction>  
              <CompassDirection>east</CompassDirection>  
              <Detail>  
                <ManeuverType>TurnRight</ManeuverType>  
                <StartPathIndex>28</StartPathIndex>  
                <EndPathIndex>30</EndPathIndex>  
                <CompassDegrees>108</CompassDegrees>  
                <Mode>Walking</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>WalkingPath</RoadType>  
              </Detail>  
              <Detail>  
                <ManeuverType>KeepStraight</ManeuverType>  
                <StartPathIndex>30</StartPathIndex>  
                <EndPathIndex>32</EndPathIndex>  
                <Name>Jardin du Carrousel</Name>  
                <CompassDegrees>107</CompassDegrees>  
                <Mode>Walking</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>WalkingPath</RoadType>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Walk</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Walking</TravelMode>  
              <TravelDistance>0.038</TravelDistance>  
              <TravelDuration>27</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>48.861861</Latitude>  
                <Longitude>2.332529</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="KeepStraight">Keep straight onto path</Instruction>  
              <CompassDirection>east</CompassDirection>  
              <Detail>  
                <ManeuverType>KeepStraight</ManeuverType>  
                <StartPathIndex>32</StartPathIndex>  
                <EndPathIndex>35</EndPathIndex>  
                <CompassDegrees>107</CompassDegrees>  
                <Mode>Walking</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>WalkingPath</RoadType>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Walk</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Walking</TravelMode>  
              <TravelDistance>0.026</TravelDistance>  
              <TravelDuration>18</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>48.861861</Latitude>  
                <Longitude>2.33298</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="KeepLeft">Keep left onto path</Instruction>  
              <CompassDirection>northeast</CompassDirection>  
              <Detail>  
                <ManeuverType>KeepLeft</ManeuverType>  
                <StartPathIndex>35</StartPathIndex>  
                <EndPathIndex>37</EndPathIndex>  
                <CompassDegrees>40</CompassDegrees>  
                <Mode>Walking</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>WalkingPath</RoadType>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Walk</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Walking</TravelMode>  
              <TravelDistance>0.041</TravelDistance>  
              <TravelDuration>29</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>48.862048</Latitude>  
                <Longitude>2.33313</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="KeepRight">Keep right onto path</Instruction>  
              <CompassDirection>east</CompassDirection>  
              <Detail>  
                <ManeuverType>KeepRight</ManeuverType>  
                <StartPathIndex>37</StartPathIndex>  
                <EndPathIndex>40</EndPathIndex>  
                <CompassDegrees>90</CompassDegrees>  
                <Mode>Walking</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>WalkingPath</RoadType>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Walk</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Walking</TravelMode>  
              <TravelDistance>0.125</TravelDistance>  
              <TravelDuration>90</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>48.862118</Latitude>  
                <Longitude>2.333581</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="KeepRight">Keep right toward Place du Carrousel</Instruction>  
              <CompassDirection>east</CompassDirection>  
              <Detail>  
                <ManeuverType>KeepRight</ManeuverType>  
                <StartPathIndex>40</StartPathIndex>  
                <EndPathIndex>44</EndPathIndex>  
                <CompassDegrees>82</CompassDegrees>  
                <Mode>Walking</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>WalkingPath</RoadType>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Walk</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Walking</TravelMode>  
              <TravelDistance>0.045</TravelDistance>  
              <TravelDuration>32</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>48.862419</Latitude>  
                <Longitude>2.3349</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="TurnLeft">Turn left onto Place du Carrousel</Instruction>  
              <CompassDirection>northeast</CompassDirection>  
              <Detail>  
                <ManeuverType>TurnLeft</ManeuverType>  
                <StartPathIndex>44</StartPathIndex>  
                <EndPathIndex>45</EndPathIndex>  
                <Name>Place du Carrousel</Name>  
                <CompassDegrees>45</CompassDegrees>  
                <Mode>Walking</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>MajorRoad</RoadType>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Walk</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <ItineraryItem>  
              <TravelMode>Walking</TravelMode>  
              <TravelDistance>0</TravelDistance>  
              <TravelDuration>0</TravelDuration>  
              <ManeuverPoint>  
                <Latitude>48.86274</Latitude>  
                <Longitude>2.335222</Longitude>  
              </ManeuverPoint>  
              <Instruction maneuverType="ArriveFinish">Arrive at Louvre, Paris, France</Instruction>  
              <CompassDirection>northeast</CompassDirection>  
              <Hint>If you reach Rue de Rohan, you've gone too far</Hint>  
              <Detail>  
                <ManeuverType>ArriveFinish</ManeuverType>  
                <StartPathIndex>45</StartPathIndex>  
                <EndPathIndex>45</EndPathIndex>  
                <Name>Place du Carrousel</Name>  
                <CompassDegrees>45</CompassDegrees>  
                <Mode>Walking</Mode>  
                <PreviousEntityId>0</PreviousEntityId>  
                <NextEntityId>0</NextEntityId>  
                <RoadType>MajorRoad</RoadType>  
              </Detail>  
              <Exit />  
              <TollZone />  
              <TransitTerminus />  
              <TripId>0</TripId>  
              <IconType>Walk</IconType>  
              <Time>0001-01-01T00:00:00</Time>  
              <TransitStopId>0</TransitStopId>  
              <SideOfStreet>Unknown</SideOfStreet>  
            </ItineraryItem>  
            <RouteSubLeg>  
              <TravelDistance>3.627</TravelDistance>  
              <TravelDuration>2611</TravelDuration>  
              <StartWaypoint>  
                <Latitude>48.858601</Latitude>  
                <Longitude>2.29398</Longitude>  
                <Description>Eiffel Tower, Paris, France</Description>  
                <IsVia>false</IsVia>  
                <LocationIdentifier>3|148|37|189|80|1|178|1|24|0|0|224|1|244|27|250|62|0|48.858623,2.293965</LocationIdentifier>  
                <RoutePathIndex>0</RoutePathIndex>  
              </StartWaypoint>  
              <EndWaypoint>  
                <Latitude>48.86272</Latitude>  
                <Longitude>2.3352</Longitude>  
                <Description>Louvre, Paris, France</Description>  
                <IsVia>false</IsVia>  
                <LocationIdentifier>3|148|37|189|80|195|0|6|24|0|0|224|1|0|0|0|0|0|48.86274,2.335222</LocationIdentifier>  
                <RoutePathIndex>45</RoutePathIndex>  
              </EndWaypoint>  
            </RouteSubLeg>  
            <StartTime>0001-01-01T00:00:00</StartTime>  
            <EndTime>0001-01-01T00:00:00</EndTime>  
            <Description />  
            <RouteRegion>EU</RouteRegion>  
          </RouteLeg>  
        </Route>  
      </Resources>  
    </ResourceSet>  
  </ResourceSets>  
</Response>  
```  
  
## See Also  
 [Using the REST Services with .NET](../using-the-rest-services-with-net.md)   
 [JSON Data Contracts](../json-data-contracts.md)