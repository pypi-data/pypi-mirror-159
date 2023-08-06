langtranslator
===============
This module allows you to translate your program to different languages.
This is done by making a json with all the translations. For further information read the usage chapter.

Installing
============

.. code-block:: bash

    pip install langtranslator

Usage
=====

JSON File:
.. code-block:: bash

    {
        "info": {"languages": ["en", "ger", "fr"]},
        "translations": {
            "string1": {"en": "This is a string.", "ger": "Das ist ein String.", "fr": "I dont know frech."},
            "string2": {"en": "test", "ger": "abc", "fr": "bonjour"}
        }
    }

In info you specify the languages that are translated.
In translations you specify the different translated strings.

Python:
.. code-block:: bash

    # How to initialize the module:
    from langtranslator import langtranslator
    translator = langtranslator("filename.json", "language")
    
    # How to get strings in the specified language:
    translator.get("stringKey")