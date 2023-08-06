use pyo3::prelude::*;
use std::fmt;
use std::fs::read_to_string;

use serde::{Deserialize, Serialize};
use serde_json::Value;

use crate::logical_types::LogicalTypes;
#[pyclass]
#[derive(Debug, PartialEq, Eq, Deserialize, Serialize, Clone)]
pub struct InputType {
    pub logical_type: Option<LogicalTypes>,
    pub semantic_tag: Option<LogicalTypes>,
}

impl InputType {
    pub fn new(
        logical_type: Option<LogicalTypes>,
        semantic_tag: Option<LogicalTypes>,
    ) -> InputType {
        InputType {
            logical_type,
            semantic_tag,
        }
    }
}

#[pymethods]
impl InputType {
    #[new]
    fn __init__(lt: Option<&str>, st: Option<&str>) -> Self {
        InputType {
            logical_type: match lt {
                Some(lt) => Some(
                    LogicalTypes::try_from(lt)
                        .expect(format!("{} is not a valid logical type", lt).as_str()),
                ),
                None => None,
            },
            semantic_tag: match st {
                Some(lt) => Some(
                    LogicalTypes::try_from(lt)
                        .expect(format!("{} is not a valid logical type", lt).as_str()),
                ),
                None => None,
            },
        }
    }
    fn __str__(&self) -> PyResult<String> {
        Ok(format!("{:?}:{:?}", self.logical_type, self.semantic_tag))
    }
    fn __repr__(&self) -> PyResult<String> {
        Ok(format!("{:?}:{:?}", self.logical_type, self.semantic_tag))
    }
}
#[pyclass]
#[derive(Debug, PartialEq, Eq, Deserialize, Serialize, Clone)]
pub struct InputSet(pub Vec<InputType>);

// https://users.rust-lang.org/t/access-tuple-struct-with-one-element-more-ergonomically/27236/3
impl core::ops::Deref for InputSet {
    type Target = Vec<InputType>;

    fn deref(self: &'_ Self) -> &'_ Self::Target {
        &self.0
    }
}

#[pymethods]
impl InputSet {
    #[new]
    fn __init__(inputs: Vec<(Option<&str>, Option<&str>)>) -> Self {
        InputSet(
            inputs
                .iter()
                .map(|(lt, st)| InputType::__init__(*lt, *st))
                .collect(),
        )
    }
    fn __str__(&self) -> PyResult<String> {
        Ok(format!("{:?}", self.0))
    }
    fn __repr__(&self) -> PyResult<String> {
        Ok(format!("{:?}", self.0))
    }
}

impl InputSet {
    pub fn new(input_set: Vec<InputType>) -> InputSet {
        InputSet(input_set)
    }
}
#[pyclass]
#[derive(Debug, PartialEq, Eq, Deserialize, Serialize, Clone)]
pub struct Primitive {
    #[pyo3(get, set)]
    #[serde(alias = "type")]
    pub name: String,
    pub module: String,
    pub arguments: Value,
    pub input_types: Vec<InputSet>,
    pub return_type: InputType,
    pub function_type: String,
    pub commutative: bool,
}

#[pymethods]
impl Primitive {
    #[new]
    fn __init__(
        name: &str,
        module: &str,
        function_type: &str,
        commutative: bool,
        input_types: Vec<Vec<(Option<&str>, Option<&str>)>>,
        return_type: (Option<&str>, Option<&str>),
    ) -> Self {
        let a = input_types
            .iter()
            .map(|x| InputSet::__init__(x.clone()))
            .collect();

        let b = InputType::__init__(return_type.0, return_type.1);

        Primitive {
            name: name.to_string(),
            module: module.to_string(),
            function_type: function_type.to_string(),
            commutative,
            input_types: a,
            arguments: Value::Null,
            return_type: b,
        }
    }
    fn __str__(&self) -> PyResult<String> {
        Ok(format!(
            "{}:{}:{}:{}:{:?}",
            self.name, self.module, self.function_type, self.commutative, self.input_types
        ))
    }
    fn __repr__(&self) -> PyResult<String> {
        Ok(format!(
            "{}:{}:{}:{}:{:?}",
            self.name, self.module, self.function_type, self.commutative, self.input_types
        ))
    }
}

impl Primitive {
    // pub fn new(logical_type: LogicalTypes, name: String) -> Primitive {
    //     Primitive { logical_type, name }
    // }
    // pub fn write_to_file(&self) {
    //     let j = serde_json::to_string(self);

    //     println!("--- PRIMITIVE AS JSON");
    //     match j {
    //         Ok(s) => {
    //             println!("{}", s);
    //             let filename = format!("{}.json", self.name);
    //             let mut file = File::create(filename).unwrap();
    //             let p = format!("{}\n", s);
    //             file.write_all(p.as_bytes()).expect("Error writing to file");
    //         }
    //         Err(e) => println!("{}", e),
    //     }
    // }

    pub fn read_from_file(filename: String) -> Vec<Primitive> {
        let contents = read_to_string(filename).expect("Something went wrong reading the file");
        let primitives: Vec<Primitive> = serde_json::from_str(&contents[..]).unwrap();
        return primitives;
    }
}

impl fmt::Display for Primitive {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}", self.name)
    }
}

#[derive(Debug)]
pub struct LogicalTypeSet(Vec<LogicalTypes>);

impl LogicalTypeSet {
    pub fn new(a: Vec<LogicalTypes>) -> LogicalTypeSet {
        LogicalTypeSet(a)
    }

    pub fn add(&mut self, logical_type: LogicalTypes) {
        self.0.push(logical_type);
    }

    // fn get(&self, index: usize) -> LogicalTypes {
    // self.logical_types[index].clone()
    // }
}

#[derive(Debug)]
pub struct LogicalTypeOption(Vec<LogicalTypeSet>);

impl LogicalTypeOption {
    pub fn new(a: Vec<LogicalTypeSet>) -> LogicalTypeOption {
        // let mut size;
        let size1 = a.first().unwrap().0.len();
        for i in &a {
            if i.0.len() != size1 {
                panic!("LogicalTypeOption: different size");
            }
        }

        LogicalTypeOption(a)
    }

    // fn get(&self, index: usize) -> LogicalTypes {
    // self.logical_types[index].clone()
    // }
}

#[cfg(test)]
mod tests {
    #[test]
    fn test() {}
}
