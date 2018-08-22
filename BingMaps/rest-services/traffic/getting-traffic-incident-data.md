---
title: "Getting Traffic Incident Data | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: b2b6f5bd-53d2-47ce-9578-7aacffb47b60
caps.latest.revision: 8
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Getting Traffic Incident Data

You can get traffic incident information along a route using the [Routes](routes/index.md) and for a geographical area by using the [Traffic](traffic/index.md). Traffic incident information is provided in two ways:  
  
- Traffic incident details including description, severity, location, type of incident.  
  
- Traffic location codes that specify incident information for a road segment or specific location as a code, such as 120-15918. A subscription is typically required to interpret and use the traffic location codes.  
  
 For traffic coverage by country, see [Bing Maps Traffic Coverage](../coverage/bing-maps-traffic-coverage.md).  
  
## Traffic incident information along a route (Routes API)

Each route segment (itinerary item) returned by the Routes API may include a set of traffic location codes and a set of warnings that specify traffic incident information along that part of the route. The warnings include a description of the incident, the severity, and a warning type, such as Accident or BlockedRoad. To see a list of the warning types, see [Warning Types](../routes/warning-types.md).  
  
There is no specific correlation between traffic location codes and warnings. For example, an itinerary item can contain traffic location codes without corresponding warnings.  
  
The following is an example of an itinerary item that contains both warnings and traffic location codes.  
  
```json
{  
   "itineraryItems":[  
      {  
         "compassDirection":"south",  
         "details":[  
            {  
               "compassDegrees":180,  
               "endPathIndices":[  
                  1  
               ],  
               "locationCodes":[  
                  "114-08912",  
                  "114-08911"  
               ],  
               "maneuverType":"DepartStart",  
               "mode":"Driving",  
               "names":[  
                  "44TH Ave W"  
               ],  
               "roadType":"Arterial",  
               "startPathIndices":[  
                  0  
               ]  
            }  
         ],  
         "exit":"",  
         "iconType":"Auto",  
         "instruction":{  
            "maneuverType":"DepartStart",  
            "text":"Depart 44TH Ave W toward 192ND St SW"  
         },  
         "maneuverPoint":{  
            "type":"Point",  
            "coordinates":[  
               47.825321,  
               -122.292407  
            ]  
         },  
         "sideOfStreet":"Unknown",  
         "tollZone":"",  
         "towardsRoadName":"192ND St SW",  
         "transitTerminus":"",  
         "travelDistance":1.029,  
         "travelDuration":97,  
         "travelMode":"Driving"  
      },  
      {  
         "compassDirection":"southwest",  
         "details":[  
            {  
               "compassDegrees":217,  
               "endPathIndices":[  
                  6  
               ],  
               "maneuverType":"TakeRampRight",  
               "mode":"Driving",  
               "roadType":"Ramp",  
               "startPathIndices":[  
                  1  
               ]  
            },  
            {  
               "compassDegrees":241,  
               "endPathIndices":[  
                  91  
               ],  
               "locationCodes":[ "114-04212", "114N04212", "114-04211", "114N04211", "114N04207", "114-04195" ],  
               "maneuverType":"Merge",  
               "mode":"Driving",  
               "names":[  
                  "I-5 South"  
               ],  
               "roadShieldRequestParameters":{  
                  "bucket":50402,  
                  "shields":[  
                     {  
                        "labels":[  
                           "5"  
                        ],  
                        "roadShieldType":1  
                     }  
                  ]  
               },  
               "roadType":"LimitedAccessHighway",  
               "startPathIndices":[  
                  6  
               ]  
            }  
         ],  
         "exit":"",  
         "iconType":"Auto",  
         "instruction":{  
            "maneuverType":"RampThenHighwayRight",  
            "text":"Take ramp right for I-5 South"  
         },  
         "maneuverPoint":{  
            "type":"Point",  
            "coordinates":[  
               47.816019,  
               -122.292332  
            ]  
         },  
         "sideOfStreet":"Unknown",  
         "tollZone":"",  
         "transitTerminus":"",  
         "travelDistance":24.323,  
         "travelDuration":908,  
         "travelMode":"Driving",  
         "warnings":[ { "severity":"Minor", "text":"Minor Congestion: slow 1st Av\/Northgate Way (#173) to Express Lanes Southern Entrance\/Exit", "warningType":"Congestion" } ]  
      }  
   ]  
}  
```  
  
## Traffic incident information within a geographical area (Traffic API)

The [Traffic API](index.md) returns a list of traffic incidents in a geographical area and provides incident details and traffic location codes. Traffic incident details include information such as the incident description, severity, location, road closures, type of incident, time of incident and detours. See [Traffic Incident Data](traffic-incident-data.md) for a list of the incident details that may be returned. Traffic incidents reported by the Traffic API include common traffic problems, such as accidents and disabled vehicles, as well as other potential causes of traffic, such as sports events.  
  
 To use the Traffic API, you must specify an area defined as a bounding box. A bounding box is a set of longitudes and latitudes that define an area. See [Location and Area Types](../common-parameters-and-types/location-and-area-types.md) for more information about a bounding box.  
  
 The following is an example of traffic incident information returned in a JSON Traffic API response.  
  
```json
{  
   "__type":"TrafficIncident:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",  
   "point":{  
      "type":"Point",  
      "coordinates":[  
         38.64829,  
         -94.36405  
      ]  
   },  
   "congestion":"",  
   "description":"in both directions between MO-2\/MO-7 and MO-291\/Cantrell Rd - construction",  
   "detour":"",  
   "end":"\/Date(1316217600000)\/",  
   "incidentId":214828828,  
   "lane":"Total Lanes lane blocked",  
   "lastModified":"\/Date(1310385750290)\/",  
   "roadClosed":false,  
   "severity":2,  
   "start":"\/Date(1310126400000)\/",  
   "toPoint":{  
      "type":"Point",  
      "coordinates":[  
         38.65831,  
         -94.36706  
      ]  
   },  
   "locationCodes":[  
      "119+05041",  
      "119+05042",  
      "119-05041",  
      "119-05042",  
      "119N05041",  
      "119N05042",  
      "119P05041",  
      "119P05042"  
   ],  
   "type":9,  
   "verified":true  
}
```