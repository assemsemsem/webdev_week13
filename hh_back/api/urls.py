from django.urls import path


from api.viewss.crud import company_list, company_detail, vacancy_detail, vacancy_list, company_vacancies
#from api.viewss.crud import CompanyList, VacancyList, CompanyVacancies, VacancyDetails, CompanyDetails
from api.viewss.cbv import CompanyList, VacancyList, CompanyVacancies, VacancyDetails, CompanyDetails
from api.viewss.fbv import company_list, company_detail, company_vacancies, vacancy_list, vacancy_detail

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path ('login/', obtain_jwt_token),
    path('companies/', CompanyList.as_view()),
    path('companies/<int:pk>/', CompanyDetails.as_view()),
    path('companies/<int:company_id>/vacancies/', CompanyVacancies.as_view()),
    path('vacancies/', VacancyList.as_view()),
    path('vacancies/<int:pk>/', VacancyDetails.as_view())
]