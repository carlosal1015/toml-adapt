from toml_adapt.AllShapes import all_shapes
from toml_adapt.DocumentType import DocumentTypeEnum
import os

POETRY_TOML_CONTENTS_BEFORE = '''[build-system]
requires = [ "poetry-core>=1.0.0",]
build-backend = "poetry.core.masonry.api"

[tool.poetry]
name = "sport-activities-features"
version = "0.2.0"
description = "A minimalistic toolbox for extracting features from sport activity files"
authors = [ "iztokf <iztokf@fedoraproject.org>",]

[tool.interrogate]
ignore-init-method = true
ignore-init-module = false
ignore-magic = false
ignore-semiprivate = false
ignore-private = false
ignore-property-decorators = false
ignore-module = false
fail-under = 10
exclude = [ "setup.py", "docs", "build",]
ignore-regex = [ "^get$", "^mock_.*", ".*BaseClass.*",]
verbose = 0
quiet = false
whitelist-regex = []
color = true

[tool.poetry.dependencies]
python = "^3.6.1"
matplotlib = "^3.3.3"
geopy = "1.0"
tcxreader = "^0.3.0"
requests = "^2.25.1"
niaaml = "^1.1.1"
overpy = "^0.6"
pytest = "*"

[tool.poetry.dev-dependencies]
Sphinx = "1.1.1"
sphinx-rtd-theme = "1.1.1"
coveralls = "1.1.1"
pytest = "1.2.1"
interrogate = "1.1.1"
doesntexist = "1.1.1"'''

POETRY_TOML_CONTENTS_AFTER = '''[build-system]
requires = [ "poetry-core>=1.0.0",]
build-backend = "poetry.core.masonry.api"

[tool.poetry]
name = "sport-activities-features"
version = "0.2.0"
description = "A minimalistic toolbox for extracting features from sport activity files"
authors = [ "iztokf <iztokf@fedoraproject.org>",]

[tool.interrogate]
ignore-init-method = true
ignore-init-module = false
ignore-magic = false
ignore-semiprivate = false
ignore-private = false
ignore-property-decorators = false
ignore-module = false
fail-under = 10
exclude = [ "setup.py", "docs", "build",]
ignore-regex = [ "^get$", "^mock_.*", ".*BaseClass.*",]
verbose = 0
quiet = false
whitelist-regex = []
color = true

[tool.poetry.dependencies]
python = "^3.6.1"
matplotlib = "^3.3.3"
geopy = "1.0"
tcxreader = "^0.3.0"
requests = "^2.25.1"
niaaml = "^1.1.1"
overpy = "^0.6"
pytest = "*"
test-dependency = "1.2.3"

[tool.poetry.dev-dependencies]
Sphinx = "1.1.1"
sphinx-rtd-theme = "1.1.1"
coveralls = "1.1.1"
pytest = "1.2.1"
interrogate = "1.1.1"
doesntexist = "1.1.1"'''


def test_answer():
    TESTFILE_BEFORE: str = "___examplefile.toml"
    TESTFILE_AFTER: str = "___examplefile_after.toml"
    poetry_functions = filter(lambda shape: shape.DocumentType ==
                              DocumentTypeEnum.POETRY, all_shapes).__next__()
    with open(TESTFILE_BEFORE, "w", encoding="utf-8") as filewrite:
        filewrite.write(POETRY_TOML_CONTENTS_BEFORE)
        poetry_functions.AddDependencyFn(
            TESTFILE_BEFORE,  # Toml file
            "test-dependency",  # Dependency name
            "1.2.3"  # Dependency version
        )
    with open(TESTFILE_AFTER, "w", encoding="utf-8") as filewrite:
        filewrite.write(POETRY_TOML_CONTENTS_AFTER)
    with open(TESTFILE_BEFORE, "r", encoding="utf-8") as fileread_after:
        with open(TESTFILE_BEFORE, "r", encoding="utf-8") as fileread_should_be:
            contents_after_adapt = fileread_after.read()
            contents_should_be=fileread_should_be.read()
            assert contents_after_adapt == contents_should_be
    os.remove(TESTFILE_BEFORE)
    os.remove(TESTFILE_AFTER)
