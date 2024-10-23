# rusty
Rust-based Python module experiments.

## Installing Rust
Follow the instructions [here](https://www.rust-lang.org/tools/install) to download and install the official compiler for the Rust programming language, and its package manager, Cargo.
```
$ curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```
Exit the shell, restart terminal.  You should be able to check the version of the `rustc` compiler as follows:
```
$ rusty % rustc --version
rustc 1.82.0 (f6e511eec 2024-10-15)
```

## Installing Maturin
```
$ mkdir rusty
$ cd rusty
$ mkvirtualenv rusty
(rusty) $ pip install maturin
```
We’re going to use [PyO3](https://github.com/PyO3/pyo3) to bind Python and Rust together.   We will do this using [maturin]() to simplify the process.
Maturin allows you to:
> build and publish crates with pyo3, cffi and uniffi bindings as well as Rust binaries as Python packages with minimal configuration. 
```
(rusty) $ maturin init
You should see the following structure created by default:
(rusty) $ ls -R 
Cargo.toml	pyproject.toml	src
./src:
lib.rs
```
Here is what it creates by default:
```
use pyo3::prelude::*;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

/// A Python module implemented in Rust.
#[pymodule]
fn rusty2(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    Ok(())
}
```
Now we can try to modify this default module implementation to incorporate the `add_one` function presented in the Rust London meetup on 22.10.24 by [David Seddon](https://github.com/seddonym):

![IMG_5302](https://github.com/user-attachments/assets/68488794-6c3f-4149-883c-19c090593164)

as the following wrapped function added to the module:
```
/// Adds 1 to the input integer.
#[pyfunction]
fn add_one(x: i32) -> PyResult<i32> {
    Ok(x + 1)
}
...
    m.add_function(wrap_pyfunction!(add_one, m)?)?;
```
The code in [lib.rs](src/lib.rs) includes `add_one` and also a `factorial` implementation.  Now we can build this into a python module using maturin as follows:
```
(rusty) $ maturin develop                    
🔗 Found pyo3 bindings
🐍 Found CPython 3.11 at /Users/malm/.virtualenvs/rusty/bin/python
📡 Using build options features from pyproject.toml
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.01s
📦 Built wheel for CPython 3.11 to /var/folders/bb/9r_ys971201g8f0zpkp20t8c0000gn/T/.tmpRr6jcT/rusty-0.1.0-cp311-cp311-macosx_11_0_arm64.whl
✏️  Setting installed package as editable
🛠 Installed rusty-0.1.0
```
And run the accompanying [test_rusty.py](test_rusty.py) test code which compares timings between Python and Python implementations of `factorial`:
```
(rusty) $ python test_rusty.py               
time for rust code: 0.92 sec
time for python code: 2.35 sec
Rust implementation is 2.56 times faster than Python one
```
