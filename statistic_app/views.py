import json
from django.shortcuts import render
import requests
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from statistic_site import settings as conf

# write json
# with open('statistic_app/cont.json', 'w') as file:
#         json.dump(response.json(), file)

def get_content():
    url = conf.BOT_URL + 'groups'
    try:
        response = requests.get(url)
    except:
        response = {'message': 'Нет ответа от бота'}
    return response
    # with open('statistic_app/cont.json', 'r') as file:
    #     content = json.load(file)
    # return content


class IndexListView(LoginRequiredMixin, View):
    login_url = 'users/login'

    def get(self, request, *args, **kwargs):
        content = get_content()
        return render(request, "statistic_app/index.html", context=content)