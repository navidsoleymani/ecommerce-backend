def get_user_info(user_id):
    from users.services import get_user_info as service

    return service(user_id)
