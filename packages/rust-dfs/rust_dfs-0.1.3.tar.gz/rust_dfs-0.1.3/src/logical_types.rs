use serde::{Deserialize, Serialize};
use strum_macros::EnumIter;

#[derive(Debug, PartialEq, Eq, Hash, EnumIter, Copy, Clone, Serialize, Deserialize)]
pub enum LogicalTypes {
    Boolean,
    BooleanNullable,
    Address,
    Age,
    AgeFractional,
    Categorical,
    Datetime,
    Double,
    Integer,
    IntegerNullable,
    PostalCode,
    Unknown,
    Ordinal,
    EmailAddress,
    LatLong,
    URL,
    NaturalLanguage,

    // Semantic Tags
    Numeric,
    TimeIndex,
    ForeignKey,
    DateOfBirth,
    Index,

    //Other - Hack
    Any,
}

impl TryFrom<&str> for LogicalTypes {
    type Error = ();

    fn try_from(v: &str) -> Result<Self, Self::Error> {
        match v {
            "Boolean" => Ok(LogicalTypes::Boolean),
            "BooleanNullable" => Ok(LogicalTypes::BooleanNullable),
            "Address" => Ok(LogicalTypes::Address),
            "Age" => Ok(LogicalTypes::Age),
            "AgeFractional" => Ok(LogicalTypes::AgeFractional),
            "Categorical" => Ok(LogicalTypes::Categorical),
            "Datetime" => Ok(LogicalTypes::Datetime),
            "Double" => Ok(LogicalTypes::Double),
            "Integer" => Ok(LogicalTypes::Integer),
            "IntegerNullable" => Ok(LogicalTypes::IntegerNullable),
            "PostalCode" => Ok(LogicalTypes::PostalCode),
            "Unknown" => Ok(LogicalTypes::Unknown),
            "Ordinal" => Ok(LogicalTypes::Ordinal),
            "EmailAddress" => Ok(LogicalTypes::EmailAddress),
            "LatLong" => Ok(LogicalTypes::LatLong),
            "URL" => Ok(LogicalTypes::URL),
            "NaturalLanguage" => Ok(LogicalTypes::NaturalLanguage),

            // Semantic Tags
            "Numeric" => Ok(LogicalTypes::Numeric),
            "TimeIndex" => Ok(LogicalTypes::TimeIndex),
            "ForeignKey" => Ok(LogicalTypes::ForeignKey),
            "DateOfBirth" => Ok(LogicalTypes::DateOfBirth),
            "Index" => Ok(LogicalTypes::Index),

            //Other - Hack
            "Any" => Ok(LogicalTypes::Any),
            _ => Err(()),
        }
    }
}
