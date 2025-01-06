# tools
small everyday tool collection

## building:

### Python to C
```sh
cython foo.py --embed
gcc -Os $(python3-config --includes) foo.c -o foo $(python3-config --ldflags --embed)
```


