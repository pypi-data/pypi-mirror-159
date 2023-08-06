# Travel-time Maps by Speed: Learning Project

Take in data input (.csv), generate heatmaps based on speed condition with printed timestamps

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all requirements

```bash
pip install -r /path/to/requirements.txt
```

## As Package

``` bash
pip install traveltimemap
```

## As Library

```python
import timestamp

# returns heatmap with travel time statistics & direction
map_direction('path/to/data.csv')

# returns heatmap with travel time statistics
get_timestamp('path/to/data.csv')

# returns heatmap
get_map('path/to/data.csv')

# save to build directory
map = get_map('path/to/data.csv')
save_map(map, name='map-name')
```
## Demo


<img width="1264" alt="demo" src="./demo.png">




