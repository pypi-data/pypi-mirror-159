"""
SKOS Codelist Reader
--------------------

Read some information from a CSV-W `skos:ConceptScheme`.
"""
import logging
import re
from pathlib import Path
from typing import Tuple, Set
from uritemplate import variables

from csvcubed.utils.csvw import get_first_table_schema
from csvcubed.utils.iterables import first


_logger = logging.getLogger(__name__)


def extract_code_list_concept_scheme_info(
    code_list_csvw_path: Path,
) -> Tuple[str, str, str]:
    """
    :return: the (:obj:`csv_url_or_relative_path`, :obj:`concept_scheme_uri`, :obj:`concept_uri_template`) from a
      CSV-W representing a `skos:ConceptScheme`.

      `concept_uri_template` uses the standard `notation` uri template variable even if the underlying file uses a
       different column name.
    """
    table_schema_result = get_first_table_schema(code_list_csvw_path)
    if table_schema_result is None:
        raise ValueError(f"Unable to find tableSchema in {code_list_csvw_path}")

    csv_url_or_relative_path, table_schema = table_schema_result
    if csv_url_or_relative_path is None:
        raise ValueError(
            f"{code_list_csvw_path} is missing `url` property for code list table."
        )

    columns = table_schema.get("columns", [])

    in_scheme_column = first(columns, lambda c: c.get("propertyUrl") == "skos:inScheme")
    if in_scheme_column is None:
        raise ValueError(f"{code_list_csvw_path} is missing `skos:inScheme` column.")

    concept_scheme_uri = in_scheme_column.get("valueUrl")
    if concept_scheme_uri is None:
        raise ValueError(f"{code_list_csvw_path} is missing concept scheme's URI.")

    about_url = table_schema.get("aboutUrl")
    if about_url is None:
        raise ValueError(f"{code_list_csvw_path} is missing `aboutUrl` property.")

    variables_in_about_url: Set[str] = {v for v in variables(about_url)}
    if len(variables_in_about_url) != 1:
        raise ValueError(
            "Unexpected number of variables in aboutUrl Template. "
            + f"Expected 1, found {len(variables_in_about_url)}"
        )

    variable_name_in_about_url = first(variables_in_about_url)
    assert variable_name_in_about_url is not None

    if variable_name_in_about_url != "notation":
        _logger.debug(
            'Replacing variable name "%s" in URI template with "notation" for consistency.',
            variable_name_in_about_url,
        )
        about_url = re.sub(
            "\\{(.?)" + re.escape(variable_name_in_about_url) + "\\}",
            "{\\1notation}",
            about_url,
        )

    return csv_url_or_relative_path, concept_scheme_uri, about_url
