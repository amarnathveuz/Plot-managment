from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
from .models import *
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import Intractive_mapSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
def index(request):
    return render(request,'super_admin/index.html')



def plot(request):
    return render(request,'super_admin/plot.html')



def property_management(request):
    data = intractive_map.objects.all()
    context = {
        'data':data
    }
    return render(request,'super_admin/property_management.html',context)


def create_property(request):

    data_list = intractive_map.objects.all()
    data_list1 = list(data_list.values_list('UnitNo_primary',flat=True))
    
    data_no = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494]
    res = [i for i in data_no if i not in data_list1]
    
    context = {
        'data_no':res
    }
    return render(request,'super_admin/create_property.html',context)

def user_management(request):
    user_data = user_Details.objects.all()
    context = {
        'user_data':user_data
    }
    return render(request,'super_admin/user_management.html',context)

def create_user(request):
    if request.method == "POST":
        name = request.POST.get("name",False)
        attachment = None
        try:
            attachment = request.FILES['attachment']
        except:
            pass
        user_type = request.POST.get("user_type",False)
        phone = request.POST.get("phone",False)
        mobile = request.POST.get("mobile",False)
        email = request.POST.get("email",False)
        empid = request.POST.get("empid",False)
        address1 = request.POST.get("address1",False)
        address2 = request.POST.get("address2",False)
        city = request.POST.get("city",False)
        state = request.POST.get("state",False)
        country = request.POST.get("country",False)
        zip = request.POST.get("zip",False)
        password_select = request.POST.get("password_select",False)
        password = ""
        if password_select == "Automatic":
            import string    
            import random
            S = 10
            password = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
        elif password_select == "Manual":
            password = request.POST.get("password",False)
        if user_type == "manager":
            if User.objects.filter(username=email).exists():
                messages.warning(request,str("An account with the given username alredy exists"))
                return redirect(request.META['HTTP_REFERER'])
            else:
                user = User.objects.create_user(email, email, password)
                user.save()
                data1 = Token.objects.create(user=user)
                save_user_data = user_Details(
                    auth_user = user,
                    name = name,
                    phone = phone,
                    email = email,
                    mobile = mobile,
                    emp_id = empid,
                    address1 = address1,
                    address2 = address2,
                    city = city,
                    state = state,
                    country = country,
                    zip = zip,
                    password_geration_type = password_select,
                    user_type = user_type,
                    atatchment =  attachment,
                    created_by = request.user

                )
                save_user_data.save()
                messages.success(request,str("password:"+str(password)))
                return redirect(request.META['HTTP_REFERER'])
        elif user_type == "salesman":
            if User.objects.filter(username=email).exists():
                messages.warning(request,str("An account with the given username alredy exists"))
                return redirect(request.META['HTTP_REFERER'])
            else:
                user = User.objects.create_user(email, email, password)
                user.save()
                data1 = Token.objects.create(user=user)
                save_user_data = user_Details.objects.create(
                    auth_user = user,
                    name = name,
                    phone = phone,
                    email = email,
                    mobile = mobile,
                    emp_id = empid,
                    address1 = address1,
                    address2 = address2,
                    city = city,
                    state = state,
                    country = country,
                    zip = zip,
                    password_geration_type = password_select,
                    user_type = user_type,
                    atatchment =  attachment,
                    created_by = request.user

                )
                manager = request.POST.get("manager")
                save_manager = user_manger_mapping(
                    user_id_id = save_user_data.id,
                    user_auth_id = save_user_data.auth_user,
                    manager_id_id = manager
                )
                save_manager.save()
                messages.success(request,str("password:"+str(password)))
                return redirect(request.META['HTTP_REFERER'])

            pass



    

        pass
    else:
        manager_data = user_Details.objects.filter(user_type="manager")
        context = {
            'manager_data':manager_data
        }
        return render(request,'super_admin/create_user.html',context)



def upload_excel(request):
    return render(request,'super_admin/upload_excel.html')
from tablib import Dataset
def simple_upload(request):
    if request.method == "POST":
        new_person = request.FILES['myfile']
        dataset = Dataset()
        if not new_person.name.endswith('xlsx'):
            messages.info('w0rong format')
            return render(request,"super_admin/upload_excel.html")
        imported_data = dataset.load(new_person.read(),format = 'xlsx')
        i = 0
        for data in imported_data:
            if i == 0:
                i = i + 1
                pass
            else:
                data = intractive_map(
                    Name = data[1],
                    Phoneno = data[3],
                    UnitNo = data[4],
                    UnitNo_primary = data[4],
                    BlockNo = data[5],
                    UnitArea = data[6],
                    LandArea = data[7],
                    UType = data[8],
                    Price = data[9],
                    Bank = data[10],
                    Status = data[11],
                    current_status = 0

                )
                data.save()

                print(data)


@api_view(['GET','POST'])
def property_list_api(request):

    data1 = intractive_map.objects.all()
    serializer = Intractive_mapSerializer(data1,many=True)
    return Response(serializer.data)
                
                
@api_view(['GET','POST'])
def property_list_api1(request,pk):
    
    print("id:::::",str(pk))
    data1 = intractive_map.objects.get(UnitNo_primary=pk)
    serializer = Intractive_mapSerializer(data1)
    return Response(serializer.data)



def property_update(request):

    if request.method == "POST":
        id = request.POST.get("id")
        Name = request.POST.get("Name")
        UnitNo = request.POST.get("UnitNo")
        Phoneno = request.POST.get("Phoneno")
        BlockNo = request.POST.get("BlockNo")
        UnitArea = request.POST.get("UnitArea")
        LandArea = request.POST.get("LandArea")
        UType = request.POST.get("UType")
        Price = request.POST.get("Price")
        Bank = request.POST.get("Bank")
        current_status = request.POST.get("current_status")
        attachment = None
        try:
            attachment = request.FILES['attachment']
            data_update_attch = intractive_map.objects.get(id=id)
            data_update_attch.attached_file = attachment
            data_update_attch.save()

        except:
            pass
        data_update = intractive_map.objects.filter(id=id).update(
            Name=Name,
            UnitNo = UnitNo,
            Phoneno = Phoneno,
            BlockNo = BlockNo,
            UnitArea = UnitArea,
            LandArea =LandArea,
            UType= UType,
            Price= Price,
            Bank =Bank,
             current_status = current_status
        )
        messages.success(request,"updated")
        return redirect(request.META['HTTP_REFERER'])
        


        

    else:    
        id = request.GET.get("id")
        data = intractive_map.objects.get(id=id)
        context = {
            'data':data
        }
        return render(request,'super_admin/property_update.html',context)



def user_edit(request):
    id = request.GET.get("id",False)
    data = user_Details.objects.get(id=id)


    all_manger = user_Details.objects.filter(user_type="manager")
    user_manger = ''
    try:
        user_manger = user_manger_mapping.objects.get(user_id_id=id)
    except:
        pass
    
    context = {
        'data':data,
        'all_manger':all_manger,
        'user_manger':user_manger
    }
    return render(request,'super_admin/user_edit.html',context)



def update_user_action(request):
    if request.method == "POST":
        updated_id = request.POST.get("updated_id",False)
        name = request.POST.get("name",False)
        user_type = request.POST.get("user_type",False)
        phone = request.POST.get("phone",False)
        mobile = request.POST.get("mobile",False)
        email = request.POST.get("email",False)
        empid = request.POST.get("empid",False)
        address1 = request.POST.get("address1",False)
        address2 = request.POST.get("address2",False)
        city = request.POST.get("city",False)
        state = request.POST.get("state",False)
        country = request.POST.get("country",False)
        zip = request.POST.get("zip",False)
        password_select = request.POST.get("password_select",False)
        manager = request.POST.get("manager",False)
        try:
            attachment = request.FILES['attachment']
            data_update_attch = user_Details.objects.get(id=updated_id)
            data_update_attch.atatchment = attachment
            data_update_attch.save()
        except:
            pass
        update_user_details = user_Details.objects.filter(id=updated_id).update(
            name=name,
            phone = phone,
            email = email,
            mobile = mobile,
            emp_id = empid,
            address1 = address1,
            address2 = address2,
            city = city,
            state = state,
            country = country,
            zip = zip,
            user_type = user_type


        )
        print("password_select:::::",str(password_select))
        if password_select == "yes":
            user_data = user_Details.objects.get(id=updated_id)
            password = request.POST.get("password",False)
            u = User.objects.get(id=user_data.auth_user.id)
            u.set_password(password)
            u.save()
        if user_type == "salesman":
            user_data = user_Details.objects.get(id=updated_id)
            try:
                check_manger = user_manger_mapping.objects.get(user_id_id=user_data.id)
                update_manager = user_manger_mapping.objects.filter(user_id_id=user_data.id).update(manager_id_id=manager)
            except:
                
                insert_manger = user_manger_mapping(
                    user_id_id = user_data.id,
                    user_auth_id_id = user_data.auth_user.id,
                    manager_id_id=manager
                )
                insert_manger.save()
                pass

        messages.success(request,"updated")
        return redirect(request.META['HTTP_REFERER'])
        
def login_action(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = authenticate(username=username, password=password)
            st = user.is_superuser
            if st == True:
                print("helloooooo")
                login(request, user)
                return redirect('home')
            else:
                user_data = user_Details.objects.get(auth_user=user)
                if user_data.user_type == "salesman":
                    login(request, user)
                    return redirect("plot")
                elif user_data.user_type == "manager":
                    login(request,user) 
                    return redirect("home")
        except:
            messages.warning(request,"invalid username and password")
            return redirect(request.META['HTTP_REFERER'])


@login_required(login_url='/')
def home(request):
    return render(request,'super_admin/home.html')



def plot(request):
    data = intractive_map.objects.all()
    context = {
        'data':data
    }
    return render(request,'super_admin/plot.html',context)



def booking_action(request):
    if request.method == "POST":
        name = request.POST.get("name",False)
        plot_id_mapping_id = request.POST.get("plot_id_mapping_id",False)
        b_id = request.POST.get("b_id",False)
        phone = request.POST.get("phone",False)
        bank = request.POST.get("bank",False)
        data_user = user_Details.objects.get(auth_user=request.user)
        data_user_manger = user_manger_mapping.objects.get(user_auth_id_id=request.user.id)
        data_save = user_request_plot.objects.create(
            auth_user=request.user,
            user_id_id = data_user.id,
            property_mapping_id_id = plot_id_mapping_id,
            name = name,
            booking_id = b_id,
            phone = phone,
            bank = bank,
            manager_id_id = data_user_manger.manager_id.id,
            read_status = 0

        )
        data_update = intractive_map.objects.filter(id=plot_id_mapping_id).update(current_status=1)
        messages.success(request,"You successfully created your booking")
        return redirect(request.META['HTTP_REFERER'])




def view_all_activity(request):
    data_user = user_Details.objects.get(auth_user=request.user)
    data = user_request_plot.objects.filter(manager_id_id=data_user.id).order_by("-id")
    context = {
        'data':data
    }
    return render(request,'super_admin/view_all_activity.html',context)



def booking_more_details(request):

    id = request.GET.get("id")
    data = user_request_plot.objects.get(id=id)
    context = {
        'data':data
    }
    return render(request,'super_admin/booking_more_details.html',context)