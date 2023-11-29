def get_user_info(user_id):
    from users.models import UserModel

    try:
        obj_dict = UserModel.objects.values(
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'last_login',
            'date_joined',
        ).get(id=user_id)
        return obj_dict
    except UserModel.DoesNotExist:
        return None
