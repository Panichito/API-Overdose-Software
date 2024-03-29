from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='home-page'),
    path('about/', About, name='about-page'),
    path('contact/', Contact, name='contact-page'),
    path('api/newuser', register_newuser),
    path('api/authenticate', authenticate_app),
    path('api/all-caretaker', all_caretaker),
    path('api/all-medicine', all_medicine),
    path('api/post-record', post_record),
    path('api/update-profile/<int:UID>', update_profile),
    path('api/ask-caretakerid/<int:UID>', ask_caretakerid),
    path('api/get-care-status/<int:UID>', get_care_status),
    path('api/switch-care-status/<int:UID>', switch_care_status),
    path('api/get-mypatient/<int:CID>', get_mypatient),
    path('api/request-caretaker/<int:UID>', request_service),
    path('api/medicine-info/<int:MID>', get_medinfo),
    path('api/get-user-records/<int:UID>', get_user_records),
    path('api/update-record/<int:RID>', update_record),
    path('api/delete-record/<int:RID>', delete_record),
    path('api/user-alerts/<int:UID>', get_all_alerts),
    path('api/record-alerts/<int:RID>', get_specific_alerts),
    path('api/add-alert', add_alert),
    path('api/update-alert/<int:AID>', update_alert),
    path('api/delete-alert/<int:AID>', delete_alert),
    path('api/add-history', add_history),
    path('api/get-user-history/<int:UID>', get_user_history),
    path('api/delete-history/<int:AID>', delete_history),
    path('api/latest-history', ask_latest_history),
    path('api/refresh-alerts', refresh_alerts),

    # path for todolist
    path('api/all-todolist/', all_todolist),
    path('api/post-todolist', post_todolist),
    path('api/update-todolist/<int:TID>', update_todolist),
    path('api/delete-todolist/<int:TID>', delete_todolist),

    #### path for event register app #####
    path('api/all-event/', all_event),
    path('api/post-enroll', post_enroll),
    path('api/delete-enroll/<int:UID>/<int:EID>', delete_enroll),
    path('api/ask-enroll/<int:UID>/<int:EID>', ask_enroll),
]
