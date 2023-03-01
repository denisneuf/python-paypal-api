from enum import Enum

class EndPoint(Enum):
    PRODUCTION = "api.paypal.com"
    SANDBOX = "api.sandbox.paypal.com"

class ProductType(str, Enum):
    PHYSICAL = 'PHYSICAL'
    DIGITAL = 'DIGITAL'
    SERVICE = 'SERVICE'

class CategoryType(str, Enum):
    AC_REFRIGERATION_REPAIR = 'AC_REFRIGERATION_REPAIR'
    ACADEMIC_SOFTWARE = 'ACADEMIC_SOFTWARE'
    ACCESSORIES = 'ACCESSORIES'
    # Check how to find the whole categories in code mode