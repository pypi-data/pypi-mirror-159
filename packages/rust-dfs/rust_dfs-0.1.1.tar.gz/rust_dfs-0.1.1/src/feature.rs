use pyo3::prelude::*;
use pyo3::pyclass::CompareOp;
use serde::{Deserialize, Serialize};
use std::fs::{read_to_string, File};
use std::io::prelude::*;
use std::{
    collections::{HashMap, HashSet},
    fmt,
};

use crate::logical_types::LogicalTypes;

#[pyclass]
#[derive(Debug, PartialEq, Eq, Hash, Deserialize, Serialize, Clone)]
pub struct Feature {
    #[pyo3(get, set)]
    pub name: String,
    pub logical_type: LogicalTypes,
    pub semantic_type: LogicalTypes,
    #[pyo3(get, set)]
    pub base_features: Vec<Feature>,
    pub generating_primitive: Option<String>,
}

#[pymethods]
impl Feature {
    #[new]
    fn __init__(
        name: &str,
        lt: &str,
        st: &str,
        base_features: Option<Vec<Feature>>,
        generating_primitive: Option<String>,
    ) -> Self {
        Feature {
            name: name.to_string(),
            logical_type: LogicalTypes::try_from(lt).unwrap(),
            semantic_type: LogicalTypes::try_from(st).unwrap(),
            base_features: base_features.unwrap_or(vec![]),
            generating_primitive,
        }
    }
    fn __str__(&self) -> PyResult<String> {
        Ok(format!(
            "{}:{:?}:{:?}:{:?}:{:?}",
            self.name,
            self.logical_type,
            self.semantic_type,
            self.generating_primitive,
            self.base_features
                .iter()
                .map(|x| &x.name)
                .collect::<Vec<_>>()
        ))
    }
    fn __repr__(&self) -> PyResult<String> {
        Ok(format!(
            "{}:{:?}:{:?}:{:?}:{:?}",
            self.name,
            self.logical_type,
            self.semantic_type,
            self.generating_primitive,
            self.base_features
                .iter()
                .map(|x| &x.name)
                .collect::<Vec<_>>()
        ))
    }

    fn __richcmp__(&self, other: &Feature, _op: CompareOp) -> PyResult<bool> {
        // println!("{:?} == {:?}", self, other);
        Ok(self.equals(other))
    }
}

impl Feature {
    pub fn new(
        name: String,
        logical_type: LogicalTypes,
        semantic_type: LogicalTypes,
        base_features: Option<Vec<Feature>>,
    ) -> Feature {
        Feature {
            name,
            logical_type,
            semantic_type,
            base_features: base_features.unwrap_or(vec![]),
            generating_primitive: None,
        }
    }

    pub fn equals(&self, other: &Feature) -> bool {
        self == other
    }

    pub fn write_many_to_file(features: &Vec<Feature>, filename: String) {
        let a = serde_json::to_string(&features);

        match a {
            Ok(s) => {
                // let filename = format!(&filename);
                let mut file = File::create(filename).unwrap();
                // let p = format!("{}\n", s);
                file.write_all(s.as_bytes()).expect("Error writing to file");
            }
            Err(e) => println!("{}", e),
        }
    }
    pub fn write_to_file(&self) {
        let j = serde_json::to_string(self);

        println!("--- FEATURE AS JSON");
        match j {
            Ok(s) => {
                println!("{}", s);
                let filename = format!("{}.json", self.name);
                let mut file = File::create(filename).unwrap();
                let p = format!("{}\n", s);
                file.write_all(p.as_bytes()).expect("Error writing to file");
            }
            Err(e) => println!("{}", e),
        }
    }

    pub fn read_from_file(filename: String) -> Feature {
        let contents = read_to_string(filename).expect("Something went wrong reading the file");
        let feature: Feature = serde_json::from_str(&contents[..]).unwrap();
        return feature;
    }
}

impl fmt::Display for Feature {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{} : {:?}", self.name, self.logical_type)
    }
}

pub fn get_features_by_type(features: &Vec<Feature>) -> HashMap<LogicalTypes, HashSet<&Feature>> {
    let mut features_by_type: HashMap<LogicalTypes, HashSet<&Feature>> = HashMap::new();

    for feature in features {
        let logical_type = feature.logical_type;
        let features_of_type = features_by_type
            .entry(logical_type)
            .or_insert(HashSet::new());
        features_of_type.insert(feature);

        let semantic_type = feature.semantic_type;
        let features_of_type = features_by_type
            .entry(semantic_type)
            .or_insert(HashSet::new());
        features_of_type.insert(feature);
    }

    features_by_type.insert(LogicalTypes::Any, HashSet::from_iter(features.iter()));

    return features_by_type;
}

pub fn generate_fake_features(n_features: i32) -> Vec<Feature> {
    let mut features: Vec<Feature> = vec![Feature::new(
        "idx".to_string(),
        LogicalTypes::Integer,
        LogicalTypes::Index,
        None,
    )];

    for i in 0..(n_features - 1) {
        let name = format!("F_{}", i);
        let logical_type = LogicalTypes::Integer;
        let semantic_type = LogicalTypes::Numeric;
        let base_features = None;
        let feature = Feature::new(name, logical_type, semantic_type, base_features);
        features.push(feature);
    }
    // (0..n_features)
    //     .map(|i| {
    //         let name = format!("F_{i}");
    //         Feature::new(name, LogicalTypes::Integer, LogicalTypes::Numeric, None)
    //     })
    //     .collect()

    return features;
}

#[cfg(test)]
mod tests {

    use crate::logical_types::LogicalTypes;

    use super::Feature;

    #[test]
    fn test() {
        let f1 = Feature::new(
            "idx".to_string(),
            LogicalTypes::Integer,
            LogicalTypes::Index,
            None,
        );

        let f2 = Feature::new(
            "idx".to_string(),
            LogicalTypes::Integer,
            LogicalTypes::Index,
            None,
        );

        println!("Equal? {}", f1 == f2);
    }
}
