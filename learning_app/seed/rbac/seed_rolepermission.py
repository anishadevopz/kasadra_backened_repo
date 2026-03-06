import asyncio
from sqlalchemy import select
from database.db import async_session
from models.rbac.roles import Role
from models.rbac.permission import Permission
from models.rbac.role_permission import RolePermission

# -----------------------------
# Predefined Roles
# -----------------------------
ROLES = ["Admin", "Instructor", "Student"]

# -----------------------------
# Predefined Permissions
# -----------------------------
PERMISSIONS = [
    ("student_create", "Create student"),
    ("student_view", "View student"),
    ("student_update", "Update student"),
    ("student_delete", "Delete student"),
    ("instructor_create", "Create instructor"),
    ("instructor_view", "View instructor"),
    ("instructor_update", "Update instructor"),
    ("instructor_delete", "Delete instructor"),
    ("course_create", "Create course"),
    ("course_view", "View course"),
    ("course_update", "Update course"),
    ("course_delete", "Delete course"),
    ("lesson_create", "Create lesson"),
    ("lesson_view", "View lesson"),
    ("lesson_update", "Update lesson"),
    ("lesson_delete", "Delete lesson"),
]

async def seed_roles_permissions():
    async with async_session() as session:
        # -----------------------------
        # Insert Roles
        # -----------------------------
        for role_name in ROLES:
            result = await session.execute(select(Role).where(Role.name == role_name))
            role = result.scalar_one_or_none()
            if not role:
                role = Role(name=role_name)
                session.add(role)
                await session.flush()  # get the role.id after insert

        # -----------------------------
        # Insert Permissions
        # -----------------------------
        for perm_name, desc in PERMISSIONS:
            result = await session.execute(select(Permission).where(Permission.name == perm_name))
            permission = result.scalar_one_or_none()
            if not permission:
                permission = Permission(name=perm_name, description=desc)
                session.add(permission)
                await session.flush()  # get the permission.id after insert

        await session.commit()

        print("✅ Roles and Permissions seeded successfully")

if __name__ == "__main__":
    asyncio.run(seed_roles_permissions())