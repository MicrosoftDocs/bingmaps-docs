---
title: "MapRouteRestrictions Enumeration | Microsoft Docs"
ms.author: "kezhang"
---

# MapRouteRestrictions Enumeration

Specifies the restrictions applied to a route. This enumeration provides values for certain parameters of some overloads of the GetDrivingRoute method.

This enumeration allows a bitwise combination of its member values.

**Android**

>```java
>public @interface MapRouteRestrictions {
>  int NONE = 0;
>  int HIGHWAYS = 1;
>  int TOLLROADS = 1 << 1;
>  int FERRIES = 1 << 2;
>  int TUNNELS = 1 << 3;
>  int DIRTROADS = 1 << 4;
>  int MOTORAIL = 1 << 5;
>}
>```

**iOS**

>```objectivec
>typedef NS_OPTIONS(NSUInteger, MSMapRouteRestrictions) {
>    MSMapRouteRestrictionsNone = 0,
>    MSMapRouteRestrictionsHighways = 1,
>    MSMapRouteRestrictionsTollRoads = 2,
>    MSMapRouteRestrictionsFerries = 4,
>    MSMapRouteRestrictionsTunnels = 8,
>    MSMapRouteRestrictionsDirtRoads = 16,
>    MSMapRouteRestrictionsMotorail = 32
>};
>```

## Values

### None

No restrictions are applied to the route.

### Highway

Avoid the use highways in the route.

### TollRoads

Avoid the use of toll roads in the route.

### Ferries

Avoid the use of ferries in the route.

### Tunnels

Avoid the use of tunnels in the route.

### DirtRoads

Avoid the use of dirt roads in the route.

### Motorail

Avoid the use of motorail train services in the route.

## See Also

* [MapRouteFinder](maproutefinder-class.md)
* [MapRouteDrivingOptions](maproutedrivingoptions-class.md)