# LLVM-Demangle
Pyhton wrapper around llvm::demangle.

## Requirements
- Cython
- llvm
- g++

## Install
```bash
$ pip install llvm-demangle
```
or
```bash
$ git clone https://github.com/MNayer/llvmdemangle
$ cd llvmdemangle
$ pip install .
```

## Usage
Within python
```python
>>> from llvmdemangle.demangle import llvm_demangle
>>> llvm_demangle("_Z5isinfUa9enable_ifILb1EEd")
isinf(double) [enable_if:true]
```
or via the command line interface
```bash
$ demangle _Z5isinfUa9enable_ifILb1EEd
isinf(double) [enable_if:true]
```
