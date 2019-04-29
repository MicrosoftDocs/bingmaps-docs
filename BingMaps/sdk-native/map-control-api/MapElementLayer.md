
# MapElementLayer Class

Displays primitives on the map.  The z-order of a primitive is in order of insertion (last inserted object will be on the top).

**Android**

>```java
> class MapElementLayer extends MapLaye
>```

**iOS**

>```objectivec
> @interface MSMapElementLayer : MSMapLayer
>```

## Properties

### elements

The map elements in this layer. This collection may be freely modified.  
_See also:_ [MapElementCollection](MapElementCollection.md)

**Android**

>```java
> MapElementCollection getElements()
>```

**iOS**

>```objectivec
> @property (nonatomic, readonly) MSMapElementCollection *elements
>```

## See also

* [MapLayer](MapLayer.md)
* [MapElement](MapElement.md)
