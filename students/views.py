from django.core import serializers
from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView, ListView, UpdateView, CreateView
from .models import Students
from .forms import Studentform

#create student view CBV
class CreateStudent(CreateView):
    model = Students
    template_name = 'students/create.html'
    form_class = Studentform
    success_url = reverse_lazy('students:list_student')

#list student view CBV
class ListStudentRegistration(ListView):
    model = Students
    template_name = 'students/list.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListStudentRegistration, self).get_context_data()
        #checking if there is data in the queryset the default value assums that we are getting data
        context['empty'] = False
        qs = self.get_queryset()
        #if no data has been found than empty will equal to true so that we can display the message
        if not qs:
            context['empty'] = True
        context['editform'] = Studentform
        return context

    def get_queryset(self):
        qs= super(ListStudentRegistration, self).get_queryset()
        #getting the value of search input that i named it q
        search = self.request.GET.get('q')
        if search:
            #if q has value then we need to filter our queryset for each fild to get matching data with the help
            #of Q to use OR  operator and icontains for case-insensitive match
            qs = qs.filter(Q(first_name__icontains=search) | Q(last_name__icontains=search) |
                      Q(date_of_birth__icontains=search) | Q(student_id__icontains=search) |
                      Q(email__icontains=search) | Q(speciality__name__icontains=search))
        return qs

#edit user ajax function
def EditStudent(request,pk):
    if request.is_ajax() and request.method == 'POST':
        #making sure that this student exists if not we return an error message
        try:
            student = Students.objects.get(pk=pk)
        except:
            return JsonResponse(data={'message': 'This Student Does Not Exits'}, status=400)
        form = Studentform(request.POST,instance=student)
        #checking if the form is valid
        if form.is_valid():
            obj = form.save()
            #serializing the object so that we can return in in json response
            data = serializers.serialize('json', [ obj, ])
            #returning sutdent data with speciality name
            return JsonResponse({'data':data,'sepciality':obj.speciality.name}, status=200)
        else:
            return JsonResponse({'data':form.errors}, status=400)

    else:
        #i only want ajax request to be received for better user experiance
        return HttpResponseRedirect(reverse_lazy('students:CreateStudent'))

#adding csrf exempt because the delete is a link and not for so it hasn't a csrf_token
@csrf_exempt
def DeleteStudent(request,pk):
    #accepting ajax requests only for better user experiance
    if request.is_ajax() and request.method == 'POST':
        #making sure that this student exists if not we return an error message
        try:
            student = Students.objects.get(pk=pk)
        except:
            return JsonResponse(data={'message':'This Student Does Not Exits'},status=400)
        #deleting the student
        student.delete()
        return JsonResponse(data={}, status=200)
    else:
        return HttpResponseRedirect(reverse_lazy('students:CreateStudent'))
