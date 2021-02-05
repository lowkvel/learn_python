from django.urls import path

#from .views import polls_list, polls_detail
from .apiviews import PollList, PollDetail, ChoiceList, CreateVote, UserCreate

urlpatterns = [
    
    #path("polls/", polls_list, name="polls_list"),
    path("polls/", PollList.as_view(), name="polls_list"),
    
    #path("polls/<int:pk>/", polls_detail, name="polls_detail"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),

    #path("choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),

    #path("vote/", CreateVote.as_view(), name="create_vote"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),

    path("users/", UserCreate.as_view(), name="user_create"),
]



