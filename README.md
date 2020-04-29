# atom position visualizer
![MD](https://github.com/m12watanabe1a/atom_pos_visualization/blob/master/MD.gif)

## Usage

- show the atom position
```
$ python3 pv.py pos.dat
```

- show and save the movie
```
$ python3 pv.py pos.dat --save
```


## Requirements
- Python3
  - matplotlib
  - numpy
- ImageMagick

## Tips
Edit the backend of matplotlib by editing ```matplotlibrc``` as following.

```matplotlibrc
backend : TkAgg
```
