from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import include, patterns, url
from django.contrib import admin
from .views import QuizListView, CategoriesListView,\
    ViewQuizListByCategory, QuizUserProgressView, QuizMarkingList,\
    QuizMarkingDetail, QuizDetailView, QuizTake

from . import views2

urlpatterns = patterns('',
			#url(r'^test/$', views.post_list, name='post_list'),
			url(r'^photo/$', views2.single_photo, name='view_single_photo'),
			url(r'^photo/(?P<photo_id>\d+)$', views2.single_photo2, name='view_single_photo2'),
			url(r'^admin/', include(admin.site.urls)),
                       url(regex=r'^$',
                           view=QuizListView.as_view(),
                           name='quiz_index'),
                       url(regex=r'^category/$',
                           view=CategoriesListView.as_view(),
                           name='quiz_category_list_all'),

                       url(regex=r'^category/(?P<category_name>[\w|\W-]+)/$',
                           view=ViewQuizListByCategory.as_view(),
                           name='quiz_category_list_matching'),

                       url(regex=r'^progress/$',
                           view=QuizUserProgressView.as_view(),
                           name='quiz_progress'),

                       url(regex=r'^marking/$',
                           view=QuizMarkingList.as_view(),
                           name='quiz_marking'),

                       url(regex=r'^marking/(?P<pk>[\d.]+)/$',
                           view=QuizMarkingDetail.as_view(),
                           name='quiz_marking_detail'),

                       #  passes variable 'quiz_name' to quiz_take view
                       url(regex=r'^(?P<slug>[\w-]+)/$',
                           view=QuizDetailView.as_view(),
                           name='quiz_start_page'),

                       url(regex=r'^(?P<quiz_name>[\w-]+)/take/$',
                           view=QuizTake.as_view(),
                           name='quiz_question'),
) + static('static_files', document_root=settings.MEDIA_ROOT) 

#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
