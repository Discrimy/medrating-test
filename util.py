REPORT_DATETIME_FORMAT = '%d.%m.%Y %H:%M'
OLD_REPORT_DATETIME_FORMAT = '%Y-%m-%dT%H:%M'


def short_if_necessary(original: str, max_symbols: int = 50) -> str:
    return original \
        if len(original) <= max_symbols \
        else original[:max_symbols] + '...'
