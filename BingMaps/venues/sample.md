---
title: "Venue JSON sample | Microsoft Docs"
description: Provides a Venue JSON code sample.
ms.custom: ""
ms.date: "05/26/2020"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: E8CF660D-4B9A-460B-BE0D-5C48E5E34572
caps.latest.revision: 3
author: "dbuerer"
ms.author: dbuerer
manager: ""
ms.service: "bing-maps"
---
# Venue JSON sample

```json
{
  "$schema": "https://venuemaps.virtualearth.net/manual/v1.1/Venue.Schema.json",
  "id": "sample-venue",
  "name": {
    "": "Sample Venue"
  },
  "isGeoPositioned": true,
  "type": "Building",
  "xy": [0,0],
  "address": {
    "addressLine": "1 Microsoft Way",
    "locality": "Redmond",
    "adminDistrict": "WA",
    "countryRegionCode": "US"
  },
  "defaultFloor": 1,
  "bbox": [-40.279,-76.302,39.483,76.591],
  "floors": [
    {
      "entities": [
        {
          "tag": "3",
          "xy": [0.144,-0.398],
          "type": "Footprint",
          "geometry": [
            {
              "closed": true,
              "x": [-76.302,49.619,76.591,-49.777],
              "y": [6.794,39.483,-7.388,-40.279]
            }
          ]
        }
      ]
    },
    {
      "display": "G",
      "name": {
        "": "Ground Level",
        "en": "G"
      },
      "entities": [
        {
          "tag": "1",
          "xy": [0.144,-0.398],
          "type": "Floor",
          "geometry": [
            {
              "closed": true,
              "x": [-76.302,49.619,76.591,-49.777],
              "y": [6.794,39.483,-7.388,-40.279]
            }
          ]
        },
        {
          "tag": "4",
          "xy": [-40.612,4.937],
          "name": {
            "": "G001"
          },
          "type": "Room",
          "geometry": [
            {
              "closed": true,
              "x": [-65.006,-42.363,-4.922,-13.382,-76.302],
              "y": [-13.254,-7.288,8.101,23.128,6.794]
            }
          ]
        },
        {
          "tag": "5",
          "xy": [-23.93,-24.588],
          "name": {
            "": "G002"
          },
          "type": "Room",
          "geometry": [
            {
              "closed": true,
              "x": [13.282,-49.777,-61.142,-38.618,4.764],
              "y": [-23.866,-40.279,-20.11,-14.323,-8.897]
            }
          ]
        },
        {
          "tag": "6",
          "xy": [31.605,7.808],
          "name": {
            "": "G003"
          },
          "type": "Room",
          "geometry": [
            {
              "closed": true,
              "x": [-4.922,12.364,4.764,13.282,76.591,49.619,-13.382],
              "y": [8.101,3.374,-8.897,-23.866,-7.388,39.483,23.128]
            }
          ]
        },
        {
          "tag": "8",
          "xy": [4.913,1.362],
          "type": "Escalator"
        }
      ]
    },
    {
      "display": "2",
      "name": {
        "": "Level 2",
        "en": "2"
      },
      "entities": [
        {
          "tag": "2",
          "xy": [31.67,7.792],
          "type": "Floor",
          "geometry": [
            {
              "closed": true,
              "x": [-13.252,13.152,76.591,49.619],
              "y": [23.162,-23.9,-7.388,39.483]
            }
          ]
        },
        {
          "tag": "7",
          "xy": [44.107,11.034],
          "name": {
            "": "2001"
          },
          "type": "Room",
          "geometry": [
            {
              "closed": true,
              "x": [11.623,49.619,76.591,38.069],
              "y": [29.619,39.483,-7.388,-17.415]
            }
          ]
        },
        {
          "tag": "9",
          "xy": [4.913,1.362],
          "type": "Escalator"
        }
      ]
    }
  ],
  "transform": [
    8.999567514436891E-06, 0.0, 0.0,
    0.0, 8.983152841195214E-06, 0.0,
    -122.139084, 47.64425, 1.0
  ]
}
```