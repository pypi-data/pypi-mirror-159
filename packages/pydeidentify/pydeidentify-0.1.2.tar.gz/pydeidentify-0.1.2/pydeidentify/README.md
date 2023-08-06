# pydeidentify

A Python library for easy text deidentification

## Usage

View more detailed examples at https://github.com/Lucasc-99/pydeidentify

DISCLAIMER: this pipeline is not 100% accurate, and may miss some entities

The models are also case sensitive, and may not tag entities if they are lower-case

```python

from pydeidentify import Deidentifier, DeidentifiedText

# Deidentify using this Deidentifier class
d = Deidentifier()
d_text: DeidentifiedText = d.deidentify("My name is Joe Biden, I'm from Scranton, Pennsylvania and I like to create python packages")

# View output of deidentification using DeidentifiedText class
print(d_text.original()) # My name is Joe Biden, I'm from Scranton, Pennsylvania and I like to create python packages
print(d_text) # My name is PER0, I'm from LOC0, LOC1 and I like to create python packages
print(d_text.encode_mapping) # {'Joe Biden': 'PER0', 'Scranton': 'LOC0', 'Pennsylvania': 'LOC1'}
print(d_text.decode_mapping) # {'PER0': 'Joe Biden', 'LOC0': 'Scranton', 'LOC1': 'Pennsylvania'}
print(d_text.counts) # {'PER': 1, 'ORG': 0, 'LOC': 2, 'MISC': 0}
```

## Contributing
All pull requests are welcome.

## License
[MIT](https://choosealicense.com/licenses/mit/)