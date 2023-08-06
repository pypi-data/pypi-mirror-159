"""
Base implementation classes for passing on inherited attributes.
"""
from abc import ABC
from datetime import date
from enum import Enum

from pydantic import BaseModel

from algoralabs.common.functions import date_to_timestamp


class BaseEnum(str, Enum):
    """
    Base class for all enum classes.

    Note: Inheriting from str is necessary to correctly serialize output of enum
    """

    pass


class Base(ABC, BaseModel):
    """
    Abstract class for all pydantic models/classes.
    """

    class Config:
        # Use enum values when using .dict() on object
        use_enum_values = True

        # Converts dates to timestamps
        json_encoders = {
            date: date_to_timestamp
        }
