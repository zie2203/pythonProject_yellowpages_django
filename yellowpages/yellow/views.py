from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from .models import yellowm,category,Reviews
from .forms import MyLoginForm,UserRegistrationForm,AddBusinessForm,BusinessEditForm,ReviewerRegistrationForm,ReviewsAddForm
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.auth.models import Group

# Create your views here.
def Home_Page (request):

    category_instance = category.objects.all()  # Get the category instance
    return render(request,"home_page.html",{'category': category_instance,})
def category_business_list(request, category_id):
    search_term=request.GET.get('searchpost')
    if search_term:
        #there is a valid search term,filter the list of objects with it
        home_contentlist= yellowm.objects.filter(business_name__icontains=search_term)
    else:
        home_contentlist = yellowm.objects.all()
    category_instance = category.objects.get(id=category_id)  # Get the category instance
    businesses = yellowm.objects.filter(business_category=category_instance)
    review_details = Reviews.objects.filter(yellowm__in=[category_id])
    context = {'businesses': businesses, 'category': category_instance,'review_details':review_details,"home_contentlist":home_contentlist,"search_term":search_term,}
    return render(request, 'category_business_list.html', context)

def user_login_view(request):
        print(request.method)
        if request.method == 'POST':
            login_form = MyLoginForm(request.POST)
            if login_form.is_valid():
                cleaned_data = login_form.cleaned_data
                auth_user = authenticate(request, username=cleaned_data['username'], password=cleaned_data['password'])
                if auth_user is not None:
                    login(request, auth_user)
                    return HttpResponse('<h1>Authenticated</h1>')
                else:
                    return HttpResponse('<h1>Not Authenticated</h1>')
        else:
            login_form = MyLoginForm  # if the form submission was not POST give login again

        return render(request, "useraccount/userlogin.html", {"login_form": login_form})


def register(request):
    if request.method == 'POST':
        # it'll get the posted variables from the MyLoginForm
        user_reg_form = UserRegistrationForm(request.POST)
        # checking if the post request parameters are valid
        if user_reg_form.is_valid():  #
            # receive the data,create the form,do not save it,just keep it temporarily without saving
            new_user = user_reg_form.save(commit=False)
            # set the password with cleaned data for password
            # cleaned_data will automatically be calling the form's clean_password2 function
            new_user.set_password(user_reg_form.cleaned_data['password'])
            # permanently save the new user modal data into database
            new_user.save()
            # after saving,render or display the template register_done.html
            return render(request, 'account/register_done.html', {'user_reg_form': user_reg_form})

    else:  # if the user registration form is not valid or not submitted
        # in that case give the user,the blank registration form from register.html
        user_reg_form = UserRegistrationForm()
    return render(request, "account/register.html", {"user_reg_form": user_reg_form})
@login_required
def add_business(request):
    #create an object of the form PostAddForm
    #with the post variables and also the posted image file
    add_business_form = AddBusinessForm(request.POST, request.FILES)
    #checking if the user posted the form by clicking submit
    if request.method == 'POST':
        if add_business_form.is_valid():
            #get the data,but do not save it now
            newbusiness = add_business_form.save(commit=False)
            #get the current user and add that info to the post_author field
            newbusiness.person_name = request.user
            #save the changes to database
            newbusiness.save()
            #if save successful redirect the user to home page or listing page
            return redirect('Home_Page')
        else:
            add_business_form = AddBusinessForm()#give a fresh blank form to user
            #if the user is not submitting the form render the fresh add post form
    return render(request, "account/add_business.html", {"add_business_form": add_business_form})

@login_required
def edit_business(request,passed_id):
    #with the post variables and also the posted image file
    home_contentlist=get_object_or_404(yellowm,id=passed_id)
    edit_business_form = BusinessEditForm(request.POST or None, request.FILES or None,instance=home_contentlist)
    #checking if the user posted the form by clicking submit
    if edit_business_form.is_valid():
            edit_business_form.save()
            #if save successful redirect the user to home page or listing page
            return redirect('Home_Page')

    return render(request, "account/edit_business.html", {"edit_business_form": edit_business_form})

@login_required
def delete_business(request, passed_id):
    # with the post variables and also the posted image file
    home_contentlist = get_object_or_404(yellowm, id=passed_id)
    home_contentlist.delete()
    return redirect('Home_Page')
@login_required
#define the view for adding the post
def add_review(request,passed_id):
    #create an object of the form PostAddForm
    #with the post variables and also the posted image file
    add_review_form = ReviewsAddForm(request.POST)
    #checking if the user posted the form by clicking submit
    if request.method == 'POST':
        if add_review_form.is_valid():
            #get the data,but do not save it now
            review = add_review_form.save(commit=False)
            #get the current user and add that info to the post_author field
            review.review_author = request.user
            review.id = passed_id#since post is a keyword we use the actual column name
            #save the changes to database
            review.save()
            #if save successful redirect the user to home page or listing page
            return redirect('category_business_list.html',passed_id)
        else:
            add_review_form = ReviewsAddForm()#give a fresh blank form to user
            #if the user is not submitting the form render the fresh add post form
    return render(request, "account/add_review.html", {"add_review_form": add_review_form})
def register_reviewer(request):
    if request.method == 'POST':
        # it'll get the posted variables from the MyLoginForm
        rev_reg_form = ReviewerRegistrationForm(request.POST)
        # checking if the post request parameters are valid
        if rev_reg_form.is_valid():
            #receive the data,create the form,do not save it,just keep it temporarily without saving
            new_user = rev_reg_form.save(commit=False)
            #set the password with cleaned data for password
            #cleaned_data will automatically be calling the form's clean_password2 function
            new_user.set_password(rev_reg_form.cleaned_data['password'])
            #permanently save the new user modal data into database
            new_user.save()
            reviewers_group = Group.objects.get(name='reviewers')
            new_user.groups.add(reviewers_group)
            #add the user by default to the reviewers group
            #after saving,render or display the template register_done.html
            return render(request,'account/register_done.html',{'rev_reg_form':rev_reg_form})

    else:#if the user registration form is not valid or not submitted
            #in that case give the user,the blank registration form from register.html
            rev_reg_form=ReviewerRegistrationForm()
    return render(request, "account/register_rev.html", {"rev_reg_form": rev_reg_form})