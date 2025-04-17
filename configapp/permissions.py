from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadPatchOnly(BasePermission):
    """
    Admin userga to'liq CRUD ruxsat.
    Teacher userga faqat GET va PATCH ruxsat.
    """

    def has_permission(self, request, view):
        user = request.user

        # Admin foydalanuvchiga barcha ruxsat
        if user.is_authenticated and user.is_admin:
            return True
        # Teacher foydalanuvchiga faqat GET va PATCH ruxsat
        elif user.is_authenticated and user.is_teacher:
            return request.method in SAFE_METHODS or request.method == 'PATCH'
        return False


class IsGetOrPatchOnly(BasePermission):
    """
    Faqat GET va PATCH metodlariga ruxsat beradi
    """

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.method == 'PATCH'
