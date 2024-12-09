use pyo3::prelude::*;

mod statistics;
mod catch22;

pub const N_CATCH22: usize = 25;

#[pymodule]
#[pyo3(name = "pycatch")]
fn py_module(_py: Python, m: &Bound<PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(catch22::compute, m)?)?;
    m.add_function(wrap_pyfunction!(catch22::zscore, m)?)?;
    Ok(())
}