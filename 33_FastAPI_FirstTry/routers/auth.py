from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlmodel import Session, select
from starlette import status

from ..db import get_session
from ..schema import User, User_DBModel


# 4. Ask for credentials upon URL access, 
# check for user presence in db,
# and verify against the password_hash


security = HTTPBasic()


def get_current_user(credentials: HTTPBasicCredentials = Depends(security),
                     # Depending on security will make FastAPI ask for username/password upon URL access
                     # Filled in details will be sent to the server as HTTP header, 
                     # and populate the 'credentials' object here.

                     session: Session = Depends(get_session)) -> User:
    
    query = select(User_DBModel).where(User_DBModel.username == credentials.username)
    user = session.exec(query).first()
    if user and user.verify_password(credentials.password):
        return User.model_validate(user)
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Username or password incorrect",
        )