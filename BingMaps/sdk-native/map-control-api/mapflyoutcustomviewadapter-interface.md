# MapFlyoutCustomViewAdapter interface

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

## See also

* [MapFlyout](mapflyout-class.md)
