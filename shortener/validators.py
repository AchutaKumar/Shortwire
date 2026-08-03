from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def is_valid_url(value:str) -> bool:
    validator = URLValidator(schemes=['http','https'])
    try:
        validator(value)
        return True
    except ValidationError:
        return False