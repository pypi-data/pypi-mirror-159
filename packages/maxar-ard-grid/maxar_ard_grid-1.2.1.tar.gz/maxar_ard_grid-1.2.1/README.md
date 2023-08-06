## maxar-ard-grid

Tools and utils for the Maxar ARD Grid system and COG tiles.

For more information on the grid and ARD see the [main documentation page](https://ard.maxar.com/docs/about/)

### Installation

Using pip:

```
pip install maxar-ard-grid 
```


### The ARD Grid

Maxar ARD uses a grid system based on UTM zones. Each zone is divided using a quadkey scheme that divides the zone into useful grid **cells**.

At the 12th zoom level each cell is 5km square. We use these cells as a boundary to subset image strips into **tiles**. The image tiles are Cloud Optimized Geotiffs stored in S3. The tiffs use a normalized resolution of approximately 30cm. The size and resolution of the tiffs maps to 16,384 pixels inside of each cell (the COGS are generated with an additional 512 pixel apron outside of the cell boundary). Because 16,384 is a power of two, it can be further subdivided with quadkeys along pixel boundaries.

At the 18th zoom level we have a cell that is 256 pixels in size. This is a convenient size for a chip. Each chip therefore has a unique quadkey describing its bounding box. Fetching image data for this cell will alway retrieve the same square on the earth. Because 256 is also a power of two, that means every pixel also has a unique quadkey identifier on the globe.

This library does not access these tiles. It is only intended to handle the grid and its cells.


### The Basics of the ARD Grid

#### Finding grid cells

To find out which grid cells cover an area, use the `covers()` function:

```pycon
>>> from maxar_ard_grid import covers
>>> geom = 'POINT(40 -120)'
>>> covers(geom)
<generator object covers at 0x11d9dfe08>>
```

The `covers` function returns a generator of Cell objects. Unless specified the Cells will be generated at grid zoom level 12 to match the COG tiles. These two are equivalent:

```pycon
>>> covers(geom)
>>> covers(geom, zoom=12)
```

The following are acceptable formats for the input geometry:

- Objects using the Python Geospatial Interface 
- Shapely geometries
- ARD Cells
- ARD Cell IDs
- GeoJSON-like geometry dicts
- GeoJSON-like feature dicts
- Well Know Text (WKT)

Geometries are assumed to be in the WGS84 coordinate system. If the geometry is in a different coordinate system or projection, it can be specified using the `src_proj` keyword. Acceptable inputs are PyProj `CRS` objects or EPSG codes (as strings or integers):

```pycon
>>> geom = 'POINT(243900 4432069)'
>>> covers(geom, src_proj=32611) # UTM 11N
```

When finding the cells covered by a given cell, always use the cell object or identifier. Using a cell's bounds or geospatial interface as an input will return unwanted cells that share edges. It is also possible to use the `Cell.get_children_at_zoom()` to calculate the same cells.

#### Working with Cells

Each cell in a zone's grid has a unique quadkey identifier. When combined with the the zone's UTM number the result is a unique cell on Earth. These cell IDs use the following format:

`Z{zone}-{quadkey}`

An example is `Z08-03201333302`.

Note that the zone number is zero padded to two digits. Quadkeys can start with the digit 0 so they should always be represented as strings. The length of a quadkey is equal to the cell's zoom level.

A specific cell can be initialized using either a Cell ID, or a combination of quadkey and zone:

```pycon
>>> from maxar_ard_grid import Cell
>>> c = Cell('Z08-03201333302')
>>> c = Cell('03201333302', zone=8)
```

A cell initialized with another cell will return an equivalent cell. This is useful for working with an input that can either be a Cell or a cell ID - you can create a Cell using the input instead of having to check the input type

```pycon
>>> c = Cell('Z08-03201333302')
>>> d = Cell(c)
>>> c == d
True
```

Identifying attributes:

```pycon
>>> c.id
'Z08-03201333302'

>>> c.quadkey
'03201333302'

>>> c.zone
8

>>> c.zoom
11

>>> c.hemisphere
'N'

>>> c.proj
'EPSG:32608'
```

Geospatial attributes:

```pycon
>>> c.bounds
[ <xmin, ymin, xmax, ymax in UTM> ]

>>> from shapely.geometry import shape
>>> shape(c) # Python Geospatial Interface support
<Shapely.geometry.polygon>   

>>> c.geom_WGS84
<Shapely.geometry.polygon> #in WGS84


>>> c.to_feature()
{'type': 'Feature', 
    'properties': {
        'id': <cell id> 
    }, 
    'geometry': <geometry in WGS84>
}

>>> c.to_GeoJSON()
'{"type": "Feature", 
    "properties": {
        "id": <cell id> 
    }, 
    "geometry": <geometry in WGS84>
}'

```

Finding related cells in the quadkey structure:

```pycon
>>> c.parent
<Cell Z08-0320133330>

>>> c.get_parent_at_zoom(9)
<Cell Z08-032013333>

>>> c.children
[<Cell Z08-03201333300>, <Cell Z08-03201333301>, <Cell Z08-03201333302>, <Cell Z08-03201333303>]

>>> c.get_children_at_zoom(18)
< generator of zoom 18 Cells >

>>> c.neighbor('E') # cell to the east
<Cell Z08-03201333303>

>>> c.neighbors
{'N': <Cell Z08-03201333300>, 'NE': <Cell Z08-03201333301>, 'E': <Cell Z08-03201333303>, 'SE': <Cell Z08-03201333321>, 'S': <Cell Z08-03201333320>, 'SW': <Cell Z08-03201333231>, 'W': <Cell Z08-03201333213>, 'NW': <Cell Z08-03201333211>}

```

Overloaded operators include `==` and `in`. Cell objects are equivalent if they represent the same cell on earth. `in` overloads `__contains__` to check if a cell is a descendent of a given cell, which is also equivalent to being spatially contained.

```pycon
>>> Cell('Z08-03201333302') == Cell('03201333302', zone=8) 
True

>>> Cell('Z08-03201333302') in Cell('Z08-032013') 
True
```
