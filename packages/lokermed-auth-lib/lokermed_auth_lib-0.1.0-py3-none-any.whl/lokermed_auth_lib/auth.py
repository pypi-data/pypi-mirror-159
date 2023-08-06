# ===== Module & Library

from http import HTTPStatus
from fastapi import APIRouter, HTTPException, Security
import jwt
from fastapi.param_functions import Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from bson.objectid import ObjectId
from datetime import datetime, timedelta
from enum import Enum
from typing import Any, Dict, List, Optional
# from config.config import ALGORITHM, BASE_URL, SECRET_KEY
from pydantic.fields import Field
# from config.config import SECRET_KEY, ALGORITHM, TOKEN_EXPIRED_IN_MINUTES
from config import config

route_credential = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{config.BASE_URL}/v1/auth/login")

# ===== Header

# ===== Function

# ===== Class
class UnauthorizedException(HTTPException):
    def __init__(
        self,
        detail: Any = None,
        header: Optional[Dict[str, Any]] = None,
    ) -> None:
        super().__init__(
            status_code=HTTPStatus.UNAUTHORIZED.value,
            detail=detail,
            headers=header,
        )

class ObjectIdStr(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if type(v) == str:
            v = ObjectId(v)
        if not isinstance(v, ObjectId):
            raise ValueError("Not a valid ObjectId")
        return str(v)


class DefaultBase(BaseModel):
    create_time: datetime = None
    creator_id: ObjectIdStr = None

    update_time: datetime = None
    editor_id: ObjectIdStr = None

    is_delete: bool = False
    delete_by: ObjectIdStr = None
    delete_time: datetime = None

class RoleType(str, Enum):
    JOB_SEEKER = "JOB_SEEKER"
    JOB_OPORTUNITY = "JOB_OPORTUNITY"
    ADMIN = "ADMIN"

    @classmethod
    def list(cls):
        return list(map(lambda c: str(c.value).replace("_", " ").title(), cls))


class TierType(str, Enum):
    FREE = "FREE"
    SILVER = "SILVER"
    GOLD = "GOLD"
    PLATINUM = "PLATINUM"

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class AbilityBase(BaseModel):
    ability: List[str] = None
    subject: str = None


class AnalyticBase(BaseModel):
    first_login_date: datetime = None
    last_login_date: datetime = None
    last_reset_password_date: datetime = None

    login_count: int = 0
    reset_password_count: int = 0

    first_login: bool = True


class SsoUserBase(DefaultBase):
    full_name: str = None
    username: str = None
    email: str = None
    password: str = None
    phone: str = None
    role: str = None
    tier: TierType = TierType.FREE

    active: bool = False
    avatar: str = 'require("@/assets/images/avatars/13-small.png")'
    analytic: AnalyticBase = AnalyticBase()

    firebase: str = None

    ability: List = []

class JwtToken(SsoUserBase):
    id: str = None
    exp: int = 1000


# ===== Main
async def mytoken(token: str = Depends(oauth2_scheme)):
    return token

async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Insert description here
    """

    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
        data_token = JwtToken(**payload)
    except jwt.PyJWTError as err:
        raise UnauthorizedException(
            "Sesi telah berakhir, silahkan login kembali!",
            {"WWW-Authenticate": "Bearer"},
        )
    return data_token.dict(exclude_unset=True)


async def get_current_token(token: str = Depends(oauth2_scheme)):
    """
    Insert description here
    """

    return token

async def create_access_token(data: JwtToken, expires_delta: int = config.TOKEN_EXPIRED_IN_MINUTES):
    """
    Insert description here
    """

    if expires_delta:
        expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    data.exp = expire

    encoded_jwt = jwt.encode(data.dict(exclude_unset=True), config.SECRET_KEY, config.ALGORITHM)
    return encoded_jwt