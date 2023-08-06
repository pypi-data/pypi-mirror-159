ferret
========

|pypi badge| |docs badge|

.. |pypi badge| image:: https://img.shields.io/pypi/v/ferret-xai.svg
    :target: https://pypi.python.org/pypi/ferret-xai
    :alt: Latest PyPI version

.. |Docs Badge| image:: https://readthedocs.org/projects/ferret/badge/?version=latest
    :alt: Documentation Status
    :scale: 100%
    :target: https://ferret.readthedocs.io/en/latest/?version=latest

A python package for benchmarking interpretability techniques.

* Free software: MIT license
* Documentation: https://ferret.readthedocs.io.

.. code-block:: python

    from transformers import AutoModelForSequenceClassification, AutoTokenizer
    from ferret import Benchmark

    model = AutoModelForSequenceClassification.from_pretrained("bert-base-cased")
    tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

    bench = Benchmark(model, tokenizer)
    explanations = bench.explain("You look stunning!")
    bench.show_table(explanations)


Features
--------

**ferret** builds on top of the transformers library. The library supports explanations using:

* Gradients
* Integrated Gradinets
* Gradient x Input word embeddings
* SHAP
* LIME


**TODOs**

* Possibility to run on select device ("cpu", "cuda")
* Sample-And-Occlusion explanations
* Discretized Integrated Gradients: https://arxiv.org/abs/2108.13654

Credits
-------

This package was created with Cookiecutter and the *audreyr/cookiecutter-pypackage* project template.

- Cookiecutter: https://github.com/audreyr/cookiecutter
- `audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
