import typing as t

from fastapi import APIRouter, Depends, status
from starlette.responses import JSONResponse
from core.auth import get_current_active_user
from db.crud.dao import create_dao, edit_dao, get_all_daos, get_dao, delete_dao
from db.session import get_db

from db.schemas.dao import CreateOrUpdateDao, Dao, DaoBasic

dao_router = r = APIRouter()


@r.get(
    "/",
    response_model=t.List[DaoBasic],
    response_model_exclude_none=True,
    name="dao:all-dao"
)
def dao_list(
    db=Depends(get_db),
):
    """
    Get all dao
    """
    try:
        return get_all_daos(db)
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=f'{str(e)}')


@r.get(
    "/{id}",
    response_model=Dao,
    response_model_exclude_none=True,
    name="dao:get-dao"
)
def dao_get(
    id: int,
    db=Depends(get_db),
):
    """
    Get dao
    """
    try:
        return get_dao(db, id)
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=f'{str(e)}')


@r.post("/", response_model=Dao, response_model_exclude_none=True, name="dao:create")
def dao_create(
    dao: CreateOrUpdateDao,
    db=Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    """
    Create a new dao (draft)
    """
    try:
        return create_dao(db, dao)
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=f'{str(e)}')


@r.put(
    "/{id}",
    response_model=Dao,
    response_model_exclude_none=True,
    name="dao:edit-dao"
)
def dao_edit(
    id: int,
    dao: CreateOrUpdateDao,
    db=Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    """
    edit existing dao
    """
    try:
        return edit_dao(db, id, dao)
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=f'{str(e)}')


@r.delete(
    "/{id}",
    response_model=Dao,
    response_model_exclude_none=True,
    name="dao:delete-dao"
)
def dao_delete(
    id: int,
    db=Depends(get_db),
    current_user=Depends(get_current_active_user),
):
    """
    delete dao
    """
    try:
        return delete_dao(db, id)
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=f'{str(e)}')
