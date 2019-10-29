---
title: "MapFlyoutCustomViewAdapter Interface | Microsoft Docs"
author: "bmnxplat"
---

# MapFlyoutCustomViewAdapter Interface

Interface for providing custom views for flyouts, on per-icon basis.  
If a null view is returned, the default view with flyout's title and description will be used.

>```java
> public interface MapFlyout.CustomViewAdapter
> {
>     public View getView(MapElement mapElement);
> }
>```

**iOS**

>```objectivec
> typedef UIView* _Nullable (^MSMapFlyoutCustomViewAdapter)(MSMapElement*)
>```

## Parameters

### MapElement
The map element that the flyout is being invoked on.

## See also

* [MapElement](mapelement-class.md)
* [MapFlyout](mapflyout-class.md)
