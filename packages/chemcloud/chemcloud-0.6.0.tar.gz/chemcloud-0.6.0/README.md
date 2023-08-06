# chemcloud - A Python Client for ChemCloud

`chemcloud` is a python client that makes performing computational chemistry calculations easy, fast, and fun. All input and output data structures are based on the [QCSchema](https://molssi-qc-schema.readthedocs.io/en/latest/index.html#) specification designed by [The Molecular Sciences Software Institute](https://molssi.org). The client provides a simple, yet powerful interface to perform computational chemistry calculation using nothing but modern python and an internet connection. Compute is generously provided free of charge by the [ChemCloud](https://chemcloud.mtzlab.com) project.

Check out the [documentation](https://mtzgroup.github.io/chemcloud/).

## Requirements

- Python 3.6+
- `chemcloud` stands on the shoulders of giants. It internally depends upon [QCElemental](http://docs.qcarchive.molssi.org/projects/QCElemental/en/stable/), [httpx](https://www.python-httpx.org), and [toml](https://pypi.org/project/toml/).
- The `AtomicInput`, `Molecule`, `Model`, and `AtomicResult` models used throughout the package come directly from [QCElemental](http://docs.qcarchive.molssi.org/projects/QCElemental/en/stable/). They are included in `chemcloud.models` for your convenience.

## Installation

```sh
pip install chemcloud
```

## Example

### The Absolute Minimum

- Create a ChemCloud account at [https://chemcloud.mtzlab.com/signup](https://chemcloud.mtzlab.com/signup).
- Instantiate a client
- Configure client (only required the very first time you use `CCClient`)

```python
>>> from chemcloud import CCClient

>>> client = CCClient()
>>> client.configure() # only run the very first time you use CCClient
# See supported compute engines
>>> client.supported_engines
['psi4', 'terachem_fe', ...]
# Test connection to ChemCloud
>>> client.hello_world("Colton")
'Welcome to ChemCloud, Colton'
```

- Create a `Molecule`
- More details about the `Molecule` object can be found [here](http://docs.qcarchive.molssi.org/en/latest/basic_examples/QCElemental.html#Molecule-Parsing-and-Models) and [here](http://docs.qcarchive.molssi.org/projects/QCElemental/en/stable/model_molecule.html).
- `Molecules` can be created from [pubchem](https://pubchem.ncbi.nlm.nih.gov), local files, or using pure python.

```python
>>> from chemcloud.models import Molecule
>>> water = Molecule.from_data("pubchem:water")
```

- Specify your compute job using an `AtomicInput` object
- More details about the `AtomicInput` object can be found [here](http://docs.qcarchive.molssi.org/projects/QCElemental/en/stable/model_result.html).

```python
>>> from chemcloud.models import AtomicInput
>>> atomic_input = AtomicInput(molecule=water, model={"method": "B3LYP", "basis": "6-31g"}, driver="energy")
```

- Submit a computation, specify a target quantum chemistry engine, and get back an [AtomicResult](http://docs.qcarchive.molssi.org/projects/QCElemental/en/stable/model_result.html)

```python
>>> future_result = client.compute(atomic_input, engine="terachem_fe")
>>> future_result.status
'STARTED'

# Get result
>>> result = future_result.get()
# Successful computation
>>> result.success
True
>>> result
AtomicResult(driver='energy', model={'method': 'B3LYP', 'basis': '6-31g'}, molecule_hash='b6ec4fa')
>>> result.return_result
-76.38545794119997

# Failed computation
>>> result.success
False
# View result
>>> result
FailedOperation(error=ComputeError(error_type='input_error', error_message='QCEngine Input Error: Traceback (most recent call last):...'))
>>> from pprint import pprint
>>> pprint(result.error.error_message)
```

- Putting it all together

```python
>>> from chemcloud import CCClient
>>> from chemcloud.models import AtomicInput, Molecule

>>> client = CCClient()
>>> water = Molecule.from_data("pubchem:water")
>>> atomic_input = AtomicInput(molecule=water, model={"method": "B3LYP", "basis": "6-31g"}, driver="energy")
>>> future_result = client.compute(atomic_input, engine="terachem_fe")
>>> result = future_result.get()
>>> result
AtomicResult(driver='energy', model={'method': 'B3LYP', 'basis': '6-31g'}, molecule_hash='b6ec4fa')
>>> result.return_result
-76.38545794119997
```

## Licence

This project is licensed under the terms of the MIT license.
