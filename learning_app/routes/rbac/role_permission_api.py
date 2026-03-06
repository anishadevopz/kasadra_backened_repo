from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import get_session
from models.rbac.role_permission import RolePermission
from schemas.rbac.role_permission_schema import RolePermissionCreate

router = APIRouter(
    prefix="/role-permissions",
    tags=["Role Permissions"]
)

@router.post("/assign", summary="Assign a permission to a role")
async def assign_permission_to_role(
    payload: RolePermissionCreate,
    session: AsyncSession = Depends(get_session)
):
    """
    Assign a permission to a role.
    Requires:
    - role_id: ID of the role
    - permission_id: ID of the permission
    """
    role_permission = RolePermission(
        role_id=payload.role_id,
        permission_id=payload.permission_id
    )

    session.add(role_permission)
    await session.commit()

    return {"message": "Permission assigned to role"}