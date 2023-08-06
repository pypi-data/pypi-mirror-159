from rest_framework.views import APIView

from vtb_django_utils.user_info.info import set_user_info


class SetUserInfoMixin(APIView):
    """ Достает из реквеста инфо о пользователе и кладет в переменную контекста """
    def initialize_request(self, request, *args, **kwargs):
        request = super().initialize_request(request, *args, **kwargs)
        set_user_info(request)
        return request
