from django.conf.urls import url
from .views import *

urlpatterns = [
    # url(r'^$', applicant_tracker, name='applicant_tracker'),
    url(r'^add', add_candidate, name='add_candidate'),
    url(r'^deactivate/(?P<id>\d+)/$', deactivate_candidate, name='deactivate_candidate'),
    url(r'^edit/(?P<id>\d+)/$', edit_candidate, name='edit_candidate'),
    url(r'^detail/(?P<id>\d+)/$', candidate_detail, name='candidate_detail')
]