"""
Module translator.py
This module provides functions for translating text between English and French.
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translate English text to French.
    """
    french_text = MyMemoryTranslator(source="en-US", target="fr-FR").translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    Translate French text to English.
    """
    english_text = MyMemoryTranslator(source="fr-FR", target="en-US").translate(french_text)
    return english_text



