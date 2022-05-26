---
title: MSMapRoutingCompletionBlock Interface | Microsoft Docs
description: Describes the MSMapRoutingCompletionBlock interface for iOS and provides the interface's syntax and additional references.
ms.author: kezhang
---

# MSMapRoutingCompletionBlock Interface (iOS only)

Handles MSMapRoutingCompletionBlock returned by MapRouteFinder routing request.

>```objectivec
>typedef void (^MSMapRoutingCompletionBlock)(MSMapRouteFinderResult* _Nullable result, NSString* status);
>```

## See Also

* [MapRouteFinder](../MapRouteFinder-class.md)
* [MapRouteFinderResult](../MapRouteFinderResult-class.md)
