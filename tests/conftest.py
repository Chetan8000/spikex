import pytest
import spacy
from spacy.util import get_lang_class


def pytest_addoption(parser):
    parser.addoption("--slow", action="store_true", help="include slow tests")


def pytest_runtest_setup(item):
    def getopt(opt):
        return item.config.getoption("--%s" % opt, False)

    for opt in ["slow"]:
        if opt in item.keywords and not getopt(opt):
            pytest.skip("need --%s option to run" % opt)


@pytest.fixture(scope="session")
def nlp():
    return spacy.load("en_core_web_md")


@pytest.fixture(scope="session")
def en_tokenizer():
    return get_lang_class("en")().tokenizer


@pytest.fixture(scope="session")
def en_vocab():
    return get_lang_class("en")().vocab


@pytest.fixture(scope="session")
def en_parser(en_vocab):
    nlp = get_lang_class("en")(en_vocab)
    return nlp.create_pipe("parser")
