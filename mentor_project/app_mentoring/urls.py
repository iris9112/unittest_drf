from django.urls import path

from .views import *


urlpatterns = [
    # nodes urls
    path(
        'nodes/<int:pk>/',
        NodeAPIView.as_view(),
        name=NodeAPIView.name,
    ),

    path(
        'nodes/<int:pk>/users/',
        UsersByNodeListAPIView.as_view(),
        name=UsersByNodeListAPIView.name,
    ),
    
    # mentoring urls
    # path(
    #     'mentoring/<int:pk_mentoring>/',
    #     MentoringAPIView.as_view(),
    #     name=MentoringAPIView.name,
    # ),

    # path(
    #     'mentoring/user/<slug:username>/',
    #     MentoringByUserListView.as_view(),
    #     name=MentoringByUserListView.name,
    # ),

    # path(
    #     'mentoring/nodo/<int:pk>/',
    #     MentoringByNodeListView.as_view(),
    #     name=MentoringByNodeListView.name,
    # ),

    # path(
    #     'mentoring/',
    #     MentoringCreateView.as_view(),
    #     name=MentoringCreateView.name,
    # ),    

]