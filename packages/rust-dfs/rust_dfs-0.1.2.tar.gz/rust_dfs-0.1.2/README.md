# Deep Feature Synthesis in Rust

This is a project to implement the [Deep Feature Synthesis](https://github.com/alteryx/featuretools/blob/main/featuretools/synthesis/dfs.py) algorithm in Rust.

## Running in Python

Create virtualenv
```
python -m venv .env
source .env/bin/activate
pip install maturin
pip install featuretools
pip install pandas
```

Ensure `Cargo.toml` is configured

```toml
[lib]
name = "rust_dfs"
crate-type = ["cdylib"]
```

Run `maturin`

```
maturin develop
```

Using from python

```python
# Import Featuretools, rust_dfs, and some other utility functions
import featuretools as ft
from py.utils import *
import rust_dfs

# Generate a fake dataset with 2 Integer columns
df = generate_fake_dataframe(
    n_rows=10,
    col_defs=[
        ("Integer", 2),
        # ("Boolean", 2),
    ]
)

# pick some primitives
f_primitives = [
    ft.primitives.GreaterThan,
    ft.primitives.LessThan
]

# or use all of them
# f_primitives = list(ft.primitives.utils.get_transform_primitives().values())

# convert datafame to an entityset
es = df_to_es(df)

# run dfs with features_only=True
ft_feats = ft.dfs(
    entityset=es, 
    target_dataframe_name="nums", 
    trans_primitives=f_primitives, 
    features_only=True,
    max_depth=1
)

# ft_feats = [<Feature: F_0>, <Feature: F_1>, <Feature: F_0 > F_1>, <Feature: F_1 > F_0>]

# Convert back into a format that we can use to compare with rust
c_feats = convert_features(ft_feats)

# Now run using Rust

# convert featuretools primitives to rust primitives
r_primitives = convert_primitives(f_primitives)

# convert dataframe to rust features
r_features = dataframe_to_features(es.dataframes[0])

# generate engineered features using Rust (create new features only)
r_derived_feats = rust_dfs.generate_features(r_features, r_primitives)

# r_derived_feats = [GreaterThan_F_0_F_1 : Unknown : Unknown, GreaterThan_F_1_F_0 : Unknown : Unknown]
```

## Run `main.rs`

To run as a rust binary:

```
cargo run --no-default-features
```