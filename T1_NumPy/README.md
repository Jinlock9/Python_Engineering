# T1: NumPy
A library specialized in array processing.

```pip install numpy```

### WHy Fast?
>The reason why Numpy can process large-scale data at high speed is that it uses **ndarray**, a multidimensional array object, as its basic data storage format. [1]

ndarray is composed of $data$ and $meta data$. ndarray places data tightly in RAM [1].

Like ndarray, if data is gathered in the same area of memory, it has the following advantages [1]:
- Array operations can be implemented in a high-speed, low-level language such as C.
- It is fast because data can be collected in CPU registers and read efficiently.
- Be able to utilize the advantages of the CPU's vectorization operation.

### basic.py
1. Able to declare data type of an array
2. Scalar of Numpy
3. Array and Matrix
4. Create ndarray
5. Set Data Type
6. Properties Examples
7. Matrix Operations

### indexing.py

### view_copy_memory.py

### ufunc.py

### broadcasting.py

### Reference
[1] 엔지니어를 위한 파이썬. 나카쿠키 켄지. 2017
