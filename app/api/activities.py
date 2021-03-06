import typing as t

from fastapi import APIRouter, Depends, status
from starlette.responses import JSONResponse
from core.auth import get_current_active_user
from db.session import get_db
from db.schemas.activity import Activity, CreateOrUpdateActivity
from db.crud.activity_log import get_user_activities, create_user_activity, delete_activity

activity_router = r = APIRouter()


@r.get(
    "/{user_id}",
    response_model=t.List[Activity],
    response_model_exclude_none=True,
    name="activities:all-user-activities"
)
def activity_list(
    user_id: int,
    db=Depends(get_db)
):
    """
    Get all user activities
    """
    try:
        return get_user_activities(db, user_id)
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=f'{str(e)}')


@r.post(
    "/{user_id}",
    response_model=Activity,
    response_model_exclude_none=True,
    name="activities:create-activity"
)
def activity_create(
    user_id: int,
    activity: CreateOrUpdateActivity,
    db=Depends(get_db),
    current_user=Depends(get_current_active_user)
):
    """
    Create user activity
    """
    try:
        if (current_user.id == user_id):
            return create_user_activity(db, user_id, activity)
        else:
            return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content="user ids do not match for current user")
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=f'{str(e)}')


@r.delete(
    "/{id}",
    response_model=Activity,
    response_model_exclude_none=True,
    name="activities:delete-activity"
)
def activity_delete(
    id: int,
    db=Depends(get_db),
    current_user=Depends(get_current_active_user)
):
    """
    delete user activity
    """
    try:
        return delete_activity(db, id, current_user.id)
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=f'{str(e)}')
