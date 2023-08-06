
import datetime

import rframe
from pydantic import validator, BaseModel, constr, HttpUrl
from typing import Literal, List

from ..base_schemas import XeDoc
from ..._settings import settings


class ActivityMeasurement(BaseModel):
    time: datetime.datetime
    activity: float
    uncertainty: float
    units: constr(max_length=10) = 'Bq'


class CalibrationSource(XeDoc):
    _ALIAS = 'calibration_sources'
    
    source_id: str = rframe.Index(max_length=50)
    lngs_id: constr(max_length=30) 
    kind: constr(max_length=50)
    ref: HttpUrl
    activity_measurements: List[ActivityMeasurement]
