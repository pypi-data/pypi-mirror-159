========
sentency
========


.. image:: https://img.shields.io/pypi/v/sentency.svg
        :target: https://pypi.python.org/pypi/sentency
        :alt: PYPI Status

.. image:: https://readthedocs.org/projects/sentency/badge/?version=latest
        :target: https://sentency.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




A small spaCy pipeline component for matching within document sentences using regular expressions.


* Free software: MIT license
* Documentation: https://sentency.readthedocs.io.


Features
--------

* spaCy component for sentence-by-sentence pattern matching
* Find matches with complex patterns using the power of regular expressions
* Easily convert simple keywords into valid regular expressions
* Specify matching patterns as well as patterns to ignore
* Annotate matches for NER (Named Entity Recognition) tasks

Installation
------------

.. code-block:: shell

        pip install sentency

    

Usage
--------

The following minimally complex example showcases the features of sentenCy.


.. code-block:: python

        import spacy
        from spacy import displacy

        from sentency.regex import regexize_keywords
        from sentency.sentency import Sentex

        text = """
        Screening for abdominal aortic aneurysm. 
        Impression: There is evidence of a fusiform 
        abdominal aortic aneurysm measuring 3.4 cm.
        """
        aaa_keywords = "abdominal aortic aneurysm"
        ignore_keywords = "screening aneurysm"

        keyword_regex = regexize_keywords(aaa_keywords)
        ignore_regex = regexize_keywords(ignore_keywords)

        nlp = spacy.load("en_core_web_sm")
        nlp.add_pipe(
        "sentex", config={
                "sentence_regex": keyword_regex, 
                "ignore_regex": ignore_regex,
                "annotate_ents": True,
                "label": "AAA"
                }
        )

        doc = nlp(text)

        displacy.render(doc, style="ent", options = {"ents": ["AAA"]})

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
