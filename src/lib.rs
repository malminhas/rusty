use pyo3::prelude::*;
use pyo3::exceptions::PyValueError;

/// Formats the sum of two numbers as a string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

/// Adds 1 to the input integer.
#[pyfunction]
fn add_one(x: i32) -> PyResult<i32> {
    Ok(x + 1)
}

fn _factorial(n: u128) -> u128 {
    if n <= 1 {
        return n
    } else {
        return n * _factorial(n - 1)
    }
}

/// Calculates the factorial of a number.
#[pyfunction]
fn factorial(n: u128) -> PyResult<u128> {
    if n == 0 {
        Ok(1)
    } else if n > 34 {
        // Adding a simple guard to avoid overflow for very large numbers
        Err(PyErr::new::<PyValueError, _>("Factorial is too large to compute"))
    } else {
        Ok(_factorial(n))
    }
}

/// A Python module implemented in Rust.
#[pymodule]
fn rusty(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    m.add_function(wrap_pyfunction!(add_one, m)?)?;
    m.add_function(wrap_pyfunction!(factorial, m)?)?;
    Ok(())
}