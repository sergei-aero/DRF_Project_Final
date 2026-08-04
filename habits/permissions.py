from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user

class IsOwner(permissions.BasePermission):
    """
    Разрешает доступ только владельцу объекта.
    Для public_list разрешено всем авторизованным.
    """
    def has_permission(self, request, view):
        # Для public_list достаточно аутентификации
        if view.action == 'public_list':
            return request.user and request.user.is_authenticated
        # Для остальных действий – только авторизованные
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Если это public_list, то объекты не проверяются (но на всякий случай)
        if view.action == 'public_list':
            return True
        # Разрешаем только владельцу (и для чтения, и для изменения)
        return obj.user == request.user



