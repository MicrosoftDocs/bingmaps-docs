---
title: "VehicleSpec Object | Microsoft Docs"
description: Describes the VehicleSpec object, which specifies the vehicle attributes for calculating a truck route, and provides a list of attributes.
ms.custom: ""
ms.date: "02/28/2018"
ms.reviewer: ""
ms.suite: ""
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 95df5de1-933c-4f00-be2c-eb9dd63b9607
caps.latest.revision: 2
author: "rbrundritt"
ms.author: "richbrun"
manager: "stevelom"
ms.service: "bing-maps"
---

# VehicleSpec Object

[!INCLUDE [bing-maps-web-control-sdk-retirement](../../../includes/bing-maps-web-control-sdk-retirement.md)]

Specifies the vehicle attributes to use when calculating a truck route.

| **Name**                  | **Type** | **Description**                                                                                                                                            |
|---------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `dimensionUnit`             | string   | The unit of measurement of width, height, length. Can be one of the following values: <br/><br/> -   **meter** or **m** \[default\]<br/> -   **foot** or **ft**               |
| `weightUnit`                | string   | The unit of measurement of weight. Can be one of the following values. <br/><br/>-   **kilogram** or **kg** \[default\]<br/> -   **pound** or **lb**      |
| `vehicleHeight`             | number   | The height of the vehicle in the specified dimension units.                                                                                                |
| `vehicleWidth`              | number   | The width of the vehicle in the specified dimension units.                                                                                                 |
| `vehicleLength`             | number   | The length of the vehicle in the specified dimension units.                                                                                                |
| `vehicleWeight`             | number   | The weight of the vehicle in the specified weight units.                                                                                                   |
| `vehicleAxles`              | number   | The number of axles.                                                                                                                                       |
| `vehicleTrailers`           | number   | The number of trailers.                                                                                                                                    |
| `vehicleSemi`               | boolean  | Indicates if the truck is pulling a semi-trailer. Semi-trailer restrictions are mostly used in North America.                                              |
| `vehicleMaxGradient`        | boolean  | The maximum gradient the vehicle can drive measured in degrees.                                                                                            |
| `vehicleMinTurnRadius`      | number   | The minimum required radius for the vehicle to turn in the specified dimension units.                                                                      |
| `vehicleAvoidCrossWind`     | boolean  | Indicates if the vehicle shall avoid crosswinds.                                                                                                           |
| `vehicleAvoidGroundingRisk` | boolean  | Indicates if the route shall avoid the risk of grounding.                                                                                                  |
| `vehicleHazardousMaterials` | string   | A comma separated and case-sensitive list of one or more hazardous materials for which the vehicle is transporting. Possible values and their aliases are: <br/><br/> -   **Combustable** *or* **C** <br/>-   **Corrosive** *or* **Cr** <br/>-   **Explosive** *or* **E** <br/> -   **Flammable** *or* **F**<br/> -   **FlammableSolid** *or* **FS** <br/> -   **Gas** *or* **G** <br/>  -   **GoodsHarmfulToWater** *or* **WH** <br/> -   **Organic** *or* **O** <br/> -   **Other**<br/>-   **Poison** *or* **P** <br/>-   **PoisonousInhalation** *or* **PI**<br/>-   **Radioactive** *or* **R**<br/> -   **None** <br/><br/>**Example:** "WH,R,Poison"   |
| `vehicleHazardousPermits`   | string   | A comma separated and case-sensitive list of one or more hazardous materials for which the vehicle has a permit. Possible values and their aliases are: <br/>-   **AllAppropriateForLoad**<br/>  -   **Combustible** *or* **C** <br/>  -   **Corrosive** *or* **Cr** <br/>  -   **Explosive** *or* **E** <br/>  -   **Flammable** *or* **F** <br/> -   **FlammableSolid** *or* **FS**  <br/> -   **Gas** *or* **G**<br/> -   **Organic** *or* **O** <br/>-   **Poison** *or* **P **<br/> -   **PoisonousInhalation** *or* **PI**<br/>-   **Radioactive** *or* **R**<br/> -   **None** <br/><br/><br/>**Example:** "C,Explosive,Corrosive"  |

## Example

The following is an example how to specify a vehicle specification as part of a truck route request.

```javascript
directionsManager.setRequestOptions({
	routeMode: Microsoft.Maps.Directions.RouteMode.truck,
	vehicleSpec: {
		dimensionUnit: 'ft',
		weightUnit: 'lb',
		vehicleHeight: 5,
		vehicleWidth: 3.5,
		vehicleLength: 30,
		vehicleWeight: 30000,
		vehicleAxles: 3,
		vehicleTrailers: 2,
		vehicleSemi: true,
		vehicleMaxGradient: 10,
		vehicleMinTurnRadius: 15,
		vehicleAvoidCrossWind: true,
		vehicleAvoidGroundingRisk: true,
		vehicleHazardousMaterials: 'F',
		vehicleHazardousPermits: 'F'
	}
});
```

## See Also:

* [Calculate a Truck Route](../../../rest-services/routes/calculate-a-truck-route.md)
