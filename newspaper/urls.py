# main urls
from django.conf.urls import patterns, include, url
from django.contrib import admin

import homepage.views
import sections.views
import newspaper.views
from django.views.generic import TemplateView


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'newspaper.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^$', homepage.views.homepage),
                       # url(r'^categories/(?P<category_url>[\w-]+)', sections.views.category_page, name='category_page'),
                       #add year to article url
                       url(r'^admin', include(admin.site.urls)),
                       url(r'^articles/', include('articles.urls')),
                       url(r'^contributors/', include('contributors.urls')),
                       url(r'^contact', newspaper.views.about_page),
                       url(r'^advertise', TemplateView.as_view(template_name="advertise.html")),
                       url(r'^about', newspaper.views.about_page),
                       url(r'^(?P<section_url>[\w-]+)', sections.views.section_page, name='section_page'),
                       #hardcode sections into here
                       )
