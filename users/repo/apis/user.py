from gando.architectures.apis import BaseAPI

from users.services import get_user_info

from rest_framework.permissions import IsAuthenticated


class GetMyProfileInformationAPI(BaseAPI):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        rsp = get_user_info(request.user.id)
        if not rsp:
            self.set_status_code(404)
            return self.response()
        return self.response(output_data=rsp)
