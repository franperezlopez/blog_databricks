from functools import lru_cache

_package_name_ = "product_sales_ml_etl"

@lru_cache
def get_version():
    from importlib.metadata import version
    return version(_package_name_)

@lru_cache
def get_version_metadata():
    from importlib.metadata import distribution
    import json, re
    metadata = distribution(_package_name_).metadata
    description = metadata["Description"] or metadata.get_payload()
    regex = r"^\s*```json(.*)^\s*```"
    matches = re.findall(regex, description, re.MULTILINE | re.DOTALL)[0]
    return json.loads(matches)

# environment variable for setting default log level
# LOGURU_LEVEL=[TRACE|DEBUG|INFO|SUCCESS|WARNING|ERROR|CRITICAL]
