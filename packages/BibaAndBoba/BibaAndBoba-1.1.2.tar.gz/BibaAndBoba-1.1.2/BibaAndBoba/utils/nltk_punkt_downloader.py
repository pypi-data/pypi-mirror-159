"""
Important! This module downloads the punkt tokenizer from NLTK.
"""
import nltk
import ssl
import logging


def download_punkt():
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    nltk.download("punkt")
    logging.info("Successfully downloaded punkt tokenizer from NLTK.")


if __name__ == "__main__":
    download_punkt()
