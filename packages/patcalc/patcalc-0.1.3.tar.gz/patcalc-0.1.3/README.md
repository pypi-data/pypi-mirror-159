# patcalc
*Basic arithmetics calculator with memory*

## Installation

`pip install calc_pck`

## Usage

```
>>> from patcalc import Calculator
>>> c = Calculator()
>>> c.add(10)  # Adds 10.0 to memory
10.0
>>> c.subs(-5) # Adds 10.0 to memory
15.0
>>> c.subs(5)  # Adds 10.0 to memory
10.0
>>> c.mult(2)  # Adds 10.0 to memory
20.0
>>> c.div(5)   # Adds 10.0 to memory
4.0
>>> c.root()   # Root from current memory value 4.0
2.0
>>> c.root(25) # Reset memory value to 0.0 and gives the root of the argument
25.0
>>> c.reset()  # Reset memory to 0.0

```

## License
MIT
