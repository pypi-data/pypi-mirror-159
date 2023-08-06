use crate::{feature::Feature, logical_types::LogicalTypes};
use itertools::Itertools;

pub fn generate_combinations<'a>(
    features: Vec<(&'a LogicalTypes, &'a Feature)>,
    n: usize,
    is_commutative: bool,
) -> Vec<Vec<(&LogicalTypes, &'a Feature)>> {
    if is_commutative {
        features.iter().cloned().combinations(n).collect_vec()
    } else {
        features.iter().cloned().permutations(n).collect_vec()
    }
}

#[cfg(test)]
mod tests {
    use super::generate_combinations;
    use crate::{feature::Feature, logical_types::LogicalTypes};
    #[test]
    fn test_generate_combinations() {
        let fa_1 = Feature::new(
            "FA_1".to_string(),
            LogicalTypes::Boolean,
            LogicalTypes::Categorical,
            None,
        );
        let fa_2 = Feature::new(
            "FA_2".to_string(),
            LogicalTypes::Boolean,
            LogicalTypes::Categorical,
            None,
        );
        let fa_3 = Feature::new(
            "FA_3".to_string(),
            LogicalTypes::Boolean,
            LogicalTypes::Categorical,
            None,
        );

        let features = vec![
            (&LogicalTypes::Boolean, &fa_1),
            (&LogicalTypes::Boolean, &fa_2),
            (&LogicalTypes::Boolean, &fa_3),
        ];
        let actual = generate_combinations(features, 2, true);

        let expected = vec![
            vec![
                (&LogicalTypes::Boolean, &fa_1),
                (&LogicalTypes::Boolean, &fa_2),
            ],
            vec![
                (&LogicalTypes::Boolean, &fa_1),
                (&LogicalTypes::Boolean, &fa_3),
            ],
            vec![
                (&LogicalTypes::Boolean, &fa_2),
                (&LogicalTypes::Boolean, &fa_3),
            ],
        ];

        assert_eq!(actual, expected);
    }
}
