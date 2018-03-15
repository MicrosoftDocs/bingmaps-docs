---
title: "Isochrone Example | Microsoft Docs"
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: fb2bec77-ad33-4740-8deb-6655509ca929
caps.latest.revision: 3
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---
# Isochrone Example
The following example shows how to request an isochrone.

In this case, consider a delivery company that has some electric vehicles in their fleet that have a maximum range of 100 miles on a fully charged battery. The company would like to determine which customer delivery locations the electric vehicles can reach and return back to the shop without having to recharge the vehicle battery. The company can use the resulting isochrone to assign the electric vehicles to only customer deliveries that are within the isochrone polygon.

* maxDistance: 50 miles (100 miles round trip)
* distanceUnit: mile
* optimize: distance
* travelMode: driving
* waypoint: Delivery company's shop latitude/longitude

**HTTP GET Request URL**

```
https://dev.virtualearth.net/REST/v1/Routes/Isochrones?waypoint=31.520759,-97.133597&maxDistance=50&distanceUnit=mile&optimize=distance&travelMode=driving&key=BingMapsKey
```

Responses are shown for both XML and JSON formats.

**JSON Response**

```JSON
{
    "authenticationResultCode": "ValidCredentials",
    "brandLogoUri": "http:\/\/veplat2.maps.live-int.com\/Branding\/logo_powered_by.png",
    "copyright": "Copyright © 2017 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.",
    "resourceSets": [{
        "estimatedTotal": 1,
        "resources": [{
            "__type": "IsochroneResponse:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1",
            "polygons": [{
                "coordinates": [
                    [
                        [32.19802, -97.09152],
                        [32.17197, -97.05196],
                        [32.16111, -97.02786],
                        [32.1298, -97.01473],
                        [32.11995, -96.98134],
                        [32.130604, -96.96546],
                        [32.14522, -96.94716],
                        [32.14929, -96.93339],
                        [32.14496, -96.93288],
                        [32.1289, -96.88526],
                        [32.11647, -96.82458],
                        [32.1011, -96.79898],
                        [32.08558, -96.77308],
                        [32.07064, -96.75143],
                        [32.06282, -96.75296],
                        [32.04652, -96.6738],
                        [32.03475, -96.64905],
                        [32.02999, -96.62503],
                        [32.03322, -96.61778],
                        [32.03715, -96.59747],
                        [32.03239, -96.57689],
                        [32.028827, -96.56338],
                        [32.028777, -96.56333],
                        [32.01661, -96.5636],
                        [31.99841, -96.57638],
                        [31.99226, -96.55694],
                        [31.98357, -96.56532],
                        [31.9599, -96.57733],
                        [31.94065, -96.5296],
                        [31.92597, -96.52978],
                        [31.91202, -96.52789],
                        [31.9103, -96.53131],
                        [31.89636, -96.53509],
                        [31.8785, -96.53163],
                        [31.85495, -96.51552],
                        [31.84651, -96.48801],
                        [31.82473, -96.4691],
                        [31.81276, -96.45049],
                        [31.80351, -96.43839],
                        [31.7833, -96.42488],
                        [31.77396, -96.44353],
                        [31.7534, -96.43915],
                        [31.7494, -96.4276],
                        [31.72852, -96.41914],
                        [31.72002, -96.4061],
                        [31.69614, -96.37849],
                        [31.68104, -96.36315],
                        [31.67012, -96.36656],
                        [31.65303, -96.39232],
                        [31.64965, -96.40241],
                        [31.62804, -96.39527],
                        [31.62173, -96.41425],
                        [31.59631, -96.40659],
                        [31.58578, -96.39114],
                        [31.57497, -96.38122],
                        [31.56219, -96.38775],
                        [31.54394, -96.37746],
                        [31.52641, -96.36267],
                        [31.50925, -96.3422],
                        [31.49733, -96.35742],
                        [31.49078, -96.35726],
                        [31.47488, -96.39137],
                        [31.45125, -96.41397],
                        [31.43415, -96.40848],
                        [31.42223, -96.42427],
                        [31.40892, -96.41586],
                        [31.40153, -96.42706],
                        [31.37708, -96.47376],
                        [31.37553, -96.47416],
                        [31.36009, -96.50634],
                        [31.34406, -96.51062],
                        [31.33216, -96.51581],
                        [31.30426, -96.54621],
                        [31.29069, -96.53346],
                        [31.2835, -96.50902],
                        [31.27132, -96.52127],
                        [31.25765, -96.54503],
                        [31.23679, -96.55818],
                        [31.21721, -96.62007],
                        [31.21526, -96.61977],
                        [31.19771, -96.59607],
                        [31.17628, -96.60292],
                        [31.16469, -96.58668],
                        [31.14793, -96.60033],
                        [31.13745, -96.60883],
                        [31.12047, -96.61511],
                        [31.10979, -96.63897],
                        [31.10022, -96.65075],
                        [31.07394, -96.69429],
                        [31.06423, -96.68996],
                        [31.05183, -96.68906],
                        [31.04225, -96.68933],
                        [31.01569, -96.80244],
                        [31.00713, -96.80226],
                        [30.98597, -96.80507],
                        [30.97981, -96.75877],
                        [30.96994, -96.78084],
                        [30.94222, -96.77337],
                        [30.93809, -96.77113],
                        [30.91627, -96.84297],
                        [30.911773, -96.84613],
                        [30.89408, -96.90268],
                        [30.88373, -96.94491],
                        [30.85611, -96.93547],
                        [30.84449, -96.95831],
                        [30.84051, -96.98222],
                        [30.83884, -96.98834],
                        [30.85369, -96.99783],
                        [30.89464, -97.01604],
                        [30.893, -97.03478],
                        [30.8899, -97.06536],
                        [30.88299, -97.06819],
                        [30.8993, -97.0842],
                        [30.90401, -97.11581],
                        [30.93039, -97.13299],
                        [30.89178, -97.15051],
                        [30.89062, -97.15096],
                        [30.90133, -97.184303],
                        [30.8987, -97.18536],
                        [30.89329, -97.21446],
                        [30.89474, -97.21936],
                        [30.88165, -97.24136],
                        [30.8892, -97.26222],
                        [30.896115, -97.285505],
                        [30.88043, -97.2877],
                        [30.88339, -97.31973],
                        [30.88072, -97.33337],
                        [30.88234, -97.33948],
                        [30.89266, -97.37069],
                        [30.89141, -97.38463],
                        [30.86705, -97.40041],
                        [30.8674, -97.40352],
                        [30.88195, -97.41257],
                        [30.88422, -97.40544],
                        [30.91142, -97.40732],
                        [30.92553, -97.54642],
                        [30.92779, -97.54327],
                        [30.95618, -97.5544],
                        [30.96717, -97.57187],
                        [30.9783, -97.57886],
                        [30.99293, -97.5657],
                        [31.00328, -97.56221],
                        [31.01618, -97.53444],
                        [31.04221, -97.60463],
                        [31.05259, -97.62072],
                        [31.072, -97.62925],
                        [31.08376, -97.63682],
                        [31.10105, -97.63027],
                        [31.10622, -97.64355],
                        [31.12944, -97.62099],
                        [31.1389, -97.62794],
                        [31.14615, -97.61498],
                        [31.16588, -97.69124],
                        [31.1738, -97.66823],
                        [31.19613, -97.66045],
                        [31.2126, -97.71932],
                        [31.22858, -97.74342],
                        [31.232, -97.7373],
                        [31.24751, -97.74771],
                        [31.26558, -97.76419],
                        [31.28921, -97.76597],
                        [31.28991, -97.82133],
                        [31.3164, -97.87164],
                        [31.33154, -97.88469],
                        [31.33378, -97.88974],
                        [31.35601, -97.88922],
                        [31.37609, -97.88734],
                        [31.38092, -97.90871],
                        [31.40445, -97.90946],
                        [31.41356, -97.91704],
                        [31.42433, -97.92239],
                        [31.44128, -97.92304],
                        [31.46291, -97.9422],
                        [31.46331, -97.9296],
                        [31.478, -97.8921],
                        [31.50437, -97.88418],
                        [31.51635, -97.89753],
                        [31.52184, -97.8896],
                        [31.53997, -97.83481],
                        [31.5503, -97.82206],
                        [31.56581, -97.84267],
                        [31.58896, -97.84731],
                        [31.59325, -97.82083],
                        [31.62173, -97.85867],
                        [31.62245, -97.85694],
                        [31.63798, -97.85352],
                        [31.65116, -97.8213],
                        [31.66658, -97.76932],
                        [31.69214, -97.77527],
                        [31.69633, -97.82028],
                        [31.71832, -97.8139],
                        [31.73601, -97.81737],
                        [31.74685, -97.81354],
                        [31.75816, -97.81907],
                        [31.77974, -97.78879],
                        [31.78643, -97.80058],
                        [31.80084, -97.7676],
                        [31.82345, -97.75001],
                        [31.82919, -97.77288],
                        [31.85326, -97.75476],
                        [31.86199, -97.76111],
                        [31.86826, -97.74387],
                        [31.884842, -97.734425],
                        [31.89711, -97.70974],
                        [31.91813, -97.71839],
                        [31.93822, -97.70673],
                        [31.94586, -97.72703],
                        [31.96325, -97.6945],
                        [31.97468, -97.68772],
                        [31.9859, -97.61479],
                        [32.00812, -97.61525],
                        [32.01526, -97.61017],
                        [32.027413, -97.572067],
                        [32.05513, -97.52428],
                        [32.05647, -97.52255],
                        [32.07762, -97.52238],
                        [32.07878, -97.50822],
                        [32.08196, -97.5],
                        [32.0168, -97.48798],
                        [32.00821, -97.47198],
                        [32.03947, -97.45023],
                        [32.03856, -97.43701],
                        [32.09788, -97.40958],
                        [32.11059, -97.40036],
                        [32.11489, -97.40273],
                        [32.13716, -97.25741],
                        [32.14701, -97.27669],
                        [32.1578, -97.26331],
                        [32.17424, -97.26758],
                        [32.18778, -97.25792],
                        [32.18783, -97.25787],
                        [32.18453, -97.24656],
                        [32.1781, -97.23397],
                        [32.17775, -97.20329],
                        [32.16973, -97.18574],
                        [32.20383, -97.17696],
                        [32.19802, -97.09152]
                    ]
                ]
            }]
        }]
    }],
    "statusCode": 200,
    "statusDescription": "OK",
    "traceId": "834a708de20b429c895a519bcd76205d|EAP8083229|7.7.0.0|"
}
```

**XML Response**

Add *&output=xml* to the URL above to get the XML response.

```XML
<?xml version="1.0" encoding="utf-8"?><Response xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://schemas.microsoft.com/search/local/ws/rest/v1">
  <Copyright>Copyright © 2017 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.</Copyright>
  <BrandLogoUri>http://veplat2.maps.live-int.com/Branding/logo_powered_by.png</BrandLogoUri>
  <StatusCode>200</StatusCode>
  <StatusDescription>OK</StatusDescription>
  <AuthenticationResultCode>ValidCredentials</AuthenticationResultCode>
  <TraceId>71b0c7a084bb4768b58062496a42ee19|EAP8083228|7.7.0.0|</TraceId>
  <ResourceSets>
    <ResourceSet>
      <EstimatedTotal>1</EstimatedTotal>
      <Resources>
        <Resource xsi:type="IsochroneResponse">
          <Polygons>
            <Polygon>
              <Coordinates>
                <ArrayOfArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.19802</double>
                    <double>-97.09152</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.17197</double>
                    <double>-97.05196</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.16111</double>
                    <double>-97.02786</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.1298</double>
                    <double>-97.01473</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.11995</double>
                    <double>-96.98134</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.130604</double>
                    <double>-96.96546</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.14522</double>
                    <double>-96.94716</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.14929</double>
                    <double>-96.93339</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.14496</double>
                    <double>-96.93288</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.1289</double>
                    <double>-96.88526</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.11647</double>
                    <double>-96.82458</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.1011</double>
                    <double>-96.79898</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.08558</double>
                    <double>-96.77308</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.07064</double>
                    <double>-96.75143</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.06282</double>
                    <double>-96.75296</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.04652</double>
                    <double>-96.6738</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.03475</double>
                    <double>-96.64905</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.02999</double>
                    <double>-96.62503</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.03322</double>
                    <double>-96.61778</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.03715</double>
                    <double>-96.59747</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.03239</double>
                    <double>-96.57689</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.028827</double>
                    <double>-96.56338</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.028777</double>
                    <double>-96.56333</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.01661</double>
                    <double>-96.5636</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.99841</double>
                    <double>-96.57638</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.99226</double>
                    <double>-96.55694</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.98357</double>
                    <double>-96.56532</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.9599</double>
                    <double>-96.57733</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.94065</double>
                    <double>-96.5296</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.92597</double>
                    <double>-96.52978</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.91202</double>
                    <double>-96.52789</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.9103</double>
                    <double>-96.53131</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.89636</double>
                    <double>-96.53509</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.8785</double>
                    <double>-96.53163</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.85495</double>
                    <double>-96.51552</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.84651</double>
                    <double>-96.48801</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.82473</double>
                    <double>-96.4691</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.81276</double>
                    <double>-96.45049</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.80351</double>
                    <double>-96.43839</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.7833</double>
                    <double>-96.42488</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.77396</double>
                    <double>-96.44353</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.7534</double>
                    <double>-96.43915</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.7494</double>
                    <double>-96.4276</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.72852</double>
                    <double>-96.41914</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.72002</double>
                    <double>-96.4061</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.69614</double>
                    <double>-96.37849</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.68104</double>
                    <double>-96.36315</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.67012</double>
                    <double>-96.36656</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.65303</double>
                    <double>-96.39232</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.64965</double>
                    <double>-96.40241</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.62804</double>
                    <double>-96.39527</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.62173</double>
                    <double>-96.41425</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.59631</double>
                    <double>-96.40659</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.58578</double>
                    <double>-96.39114</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.57497</double>
                    <double>-96.38122</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.56219</double>
                    <double>-96.38775</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.54394</double>
                    <double>-96.37746</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.52641</double>
                    <double>-96.36267</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.50925</double>
                    <double>-96.3422</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.49733</double>
                    <double>-96.35742</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.49078</double>
                    <double>-96.35726</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.47488</double>
                    <double>-96.39137</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.45125</double>
                    <double>-96.41397</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.43415</double>
                    <double>-96.40848</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.42223</double>
                    <double>-96.42427</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.40892</double>
                    <double>-96.41586</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.40153</double>
                    <double>-96.42706</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.37708</double>
                    <double>-96.47376</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.37553</double>
                    <double>-96.47416</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.36009</double>
                    <double>-96.50634</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.34406</double>
                    <double>-96.51062</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.33216</double>
                    <double>-96.51581</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.30426</double>
                    <double>-96.54621</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.29069</double>
                    <double>-96.53346</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.2835</double>
                    <double>-96.50902</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.27132</double>
                    <double>-96.52127</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.25765</double>
                    <double>-96.54503</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.23679</double>
                    <double>-96.55818</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.21721</double>
                    <double>-96.62007</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.21526</double>
                    <double>-96.61977</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.19771</double>
                    <double>-96.59607</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.17628</double>
                    <double>-96.60292</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.16469</double>
                    <double>-96.58668</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.14793</double>
                    <double>-96.60033</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.13745</double>
                    <double>-96.60883</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.12047</double>
                    <double>-96.61511</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.10979</double>
                    <double>-96.63897</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.10022</double>
                    <double>-96.65075</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.07394</double>
                    <double>-96.69429</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.06423</double>
                    <double>-96.68996</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.05183</double>
                    <double>-96.68906</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.04225</double>
                    <double>-96.68933</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.01569</double>
                    <double>-96.80244</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.00713</double>
                    <double>-96.80226</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.98597</double>
                    <double>-96.80507</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.97981</double>
                    <double>-96.75877</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.96994</double>
                    <double>-96.78084</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.94222</double>
                    <double>-96.77337</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.93809</double>
                    <double>-96.77113</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.91627</double>
                    <double>-96.84297</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.911773</double>
                    <double>-96.84613</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.89408</double>
                    <double>-96.90268</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.88373</double>
                    <double>-96.94491</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.85611</double>
                    <double>-96.93547</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.84449</double>
                    <double>-96.95831</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.84051</double>
                    <double>-96.98222</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.83884</double>
                    <double>-96.98834</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.85369</double>
                    <double>-96.99783</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.89464</double>
                    <double>-97.01604</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.893</double>
                    <double>-97.03478</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.8899</double>
                    <double>-97.06536</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.88299</double>
                    <double>-97.06819</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.8993</double>
                    <double>-97.0842</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.90401</double>
                    <double>-97.11581</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.93039</double>
                    <double>-97.13299</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.89178</double>
                    <double>-97.15051</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.89062</double>
                    <double>-97.15096</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.90133</double>
                    <double>-97.184303</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.8987</double>
                    <double>-97.18536</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.89329</double>
                    <double>-97.21446</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.89474</double>
                    <double>-97.21936</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.88165</double>
                    <double>-97.24136</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.8892</double>
                    <double>-97.26222</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.896115</double>
                    <double>-97.285505</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.88043</double>
                    <double>-97.2877</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.88339</double>
                    <double>-97.31973</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.88072</double>
                    <double>-97.33337</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.88234</double>
                    <double>-97.33948</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.89266</double>
                    <double>-97.37069</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.89141</double>
                    <double>-97.38463</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.86705</double>
                    <double>-97.40041</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.8674</double>
                    <double>-97.40352</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.88195</double>
                    <double>-97.41257</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.88422</double>
                    <double>-97.40544</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.91142</double>
                    <double>-97.40732</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.92553</double>
                    <double>-97.54642</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.92779</double>
                    <double>-97.54327</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.95618</double>
                    <double>-97.5544</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.96717</double>
                    <double>-97.57187</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.9783</double>
                    <double>-97.57886</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>30.99293</double>
                    <double>-97.5657</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.00328</double>
                    <double>-97.56221</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.01618</double>
                    <double>-97.53444</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.04221</double>
                    <double>-97.60463</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.05259</double>
                    <double>-97.62072</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.072</double>
                    <double>-97.62925</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.08376</double>
                    <double>-97.63682</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.10105</double>
                    <double>-97.63027</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.10622</double>
                    <double>-97.64355</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.12944</double>
                    <double>-97.62099</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.1389</double>
                    <double>-97.62794</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.14615</double>
                    <double>-97.61498</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.16588</double>
                    <double>-97.69124</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.1738</double>
                    <double>-97.66823</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.19613</double>
                    <double>-97.66045</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.2126</double>
                    <double>-97.71932</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.22858</double>
                    <double>-97.74342</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.232</double>
                    <double>-97.7373</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.24751</double>
                    <double>-97.74771</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.26558</double>
                    <double>-97.76419</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.28921</double>
                    <double>-97.76597</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.28991</double>
                    <double>-97.82133</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.3164</double>
                    <double>-97.87164</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.33154</double>
                    <double>-97.88469</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.33378</double>
                    <double>-97.88974</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.35601</double>
                    <double>-97.88922</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.37609</double>
                    <double>-97.88734</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.38092</double>
                    <double>-97.90871</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.40445</double>
                    <double>-97.90946</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.41356</double>
                    <double>-97.91704</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.42433</double>
                    <double>-97.92239</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.44128</double>
                    <double>-97.92304</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.46291</double>
                    <double>-97.9422</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.46331</double>
                    <double>-97.9296</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.478</double>
                    <double>-97.8921</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.50437</double>
                    <double>-97.88418</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.51635</double>
                    <double>-97.89753</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.52184</double>
                    <double>-97.8896</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.53997</double>
                    <double>-97.83481</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.5503</double>
                    <double>-97.82206</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.56581</double>
                    <double>-97.84267</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.58896</double>
                    <double>-97.84731</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.59325</double>
                    <double>-97.82083</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.62173</double>
                    <double>-97.85867</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.62245</double>
                    <double>-97.85694</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.63798</double>
                    <double>-97.85352</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.65116</double>
                    <double>-97.8213</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.66658</double>
                    <double>-97.76932</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.69214</double>
                    <double>-97.77527</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.69633</double>
                    <double>-97.82028</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.71832</double>
                    <double>-97.8139</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.73601</double>
                    <double>-97.81737</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.74685</double>
                    <double>-97.81354</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.75816</double>
                    <double>-97.81907</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.77974</double>
                    <double>-97.78879</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.78643</double>
                    <double>-97.80058</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.80084</double>
                    <double>-97.7676</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.82345</double>
                    <double>-97.75001</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.82919</double>
                    <double>-97.77288</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.85326</double>
                    <double>-97.75476</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.86199</double>
                    <double>-97.76111</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.86826</double>
                    <double>-97.74387</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.884842</double>
                    <double>-97.734425</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.89711</double>
                    <double>-97.70974</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.91813</double>
                    <double>-97.71839</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.93822</double>
                    <double>-97.70673</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.94586</double>
                    <double>-97.72703</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.96325</double>
                    <double>-97.6945</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.97468</double>
                    <double>-97.68772</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>31.9859</double>
                    <double>-97.61479</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.00812</double>
                    <double>-97.61525</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.01526</double>
                    <double>-97.61017</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.027413</double>
                    <double>-97.572067</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.05513</double>
                    <double>-97.52428</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.05647</double>
                    <double>-97.52255</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.07762</double>
                    <double>-97.52238</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.07878</double>
                    <double>-97.50822</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.08196</double>
                    <double>-97.5</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.0168</double>
                    <double>-97.48798</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.00821</double>
                    <double>-97.47198</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.03947</double>
                    <double>-97.45023</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.03856</double>
                    <double>-97.43701</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.09788</double>
                    <double>-97.40958</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.11059</double>
                    <double>-97.40036</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.11489</double>
                    <double>-97.40273</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.13716</double>
                    <double>-97.25741</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.14701</double>
                    <double>-97.27669</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.1578</double>
                    <double>-97.26331</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.17424</double>
                    <double>-97.26758</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.18778</double>
                    <double>-97.25792</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.18783</double>
                    <double>-97.25787</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.18453</double>
                    <double>-97.24656</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.1781</double>
                    <double>-97.23397</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.17775</double>
                    <double>-97.20329</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.16973</double>
                    <double>-97.18574</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.20383</double>
                    <double>-97.17696</double>
                  </ArrayOfDouble>
                  <ArrayOfDouble>
                    <double>32.19802</double>
                    <double>-97.09152</double>
                  </ArrayOfDouble>
                </ArrayOfArrayOfDouble>
              </Coordinates>
            </Polygon>
          </Polygons>
        </Resource>
      </Resources>
    </ResourceSet>
  </ResourceSets>
</Response>
```

## See Also

* [Using the REST Services with .NET](../rest-services/using-the-rest-services-with-net.md)
