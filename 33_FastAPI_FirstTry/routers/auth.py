from fastapi import Depends, HTTPException
from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlmodel import Session, select
from starlette import status

from ..db import get_session
from ..schema import User, User_DBModel


# 1. Create a router to support token fetching endpoint
URL_PREFIX="/auth"
router = APIRouter(prefix=URL_PREFIX)

# 2. Instead of security, create an oauth2_scheme to delegate authentication to PasswordBearer
#security = HTTPBasic()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{URL_PREFIX}/token")


# 3. Depend on the token and this returns the token sent by the client
# i.e. when this function is called, client should've already logged in
# at the token URL and received the token.

#def get_current_user(credentials: HTTPBasicCredentials = Depends(security),
def get_current_user(token: str = Depends(oauth2_scheme),
                     session: Session = Depends(get_session)) -> User:

    
    # 4. For this demo the token will just contain the username
    # So, we select th User_DBModel, whose username matches the token
    # and return that object.

    #query = select(User_DBModel).where(User_DBModel.username == credentials.username)
    query = select(User_DBModel).where(User_DBModel.username == token)
    user = session.exec(query).first()
    if user:
        return User.model_validate(user)
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Username or password incorrect",
            headers={"WWW-Authenticate": "Bearer"},
        )


# Token Generation
@router.post("/token")  # URL will be "/auth/token"
async def login(form_data: OAuth2PasswordRequestForm = Depends(),
                # We say Depends w/o args, but the 'form_data' object is specified
                # to be OAuth2PasswordRequestForm.
                # Its init requires 'username' and 'password', which should be sent as Form() inputs
                session: Session = Depends(get_session)):
    query = select(User_DBModel).where(User_DBModel.username == form_data.username)
    user = session.exec(query).first()
    if user and user.verify_password(form_data.password):
        # return structure has 'token_type' as 'bearer', which is as per OAuth specifications.
        # Here we return the actual username in plaintext, which is not prod standard
        # Instead, we should use something more secure here, like JSON Web Tokens.
        return {"access_token": user.username, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=400, detail="Incorrect username or password")