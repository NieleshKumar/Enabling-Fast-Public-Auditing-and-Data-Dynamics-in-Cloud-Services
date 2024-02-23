from django.shortcuts import render, redirect
from django.contrib import messages
from userapp.models import Userregister, Uploadfiles, Auditrequest


# templates
INDEXPAGE = "index.html"
CSPLOGINPAGE = "csplogin.html"
CSPHOMEPAGE = "csphome.html"
USERDETAILSPAGE = "userdetails.html"
CLOUDFILESPAGE = "cloudfiles.html"
AUDITREQUESTPAGE = "auditrequest.html"
GENERATEDPROOFPAGE = "generateprrof.html"
EDITFILEPAGE = "editfile.html"
# Create your views here.

def index(req):
    return render(req, INDEXPAGE)

def csp(req):
    if req.method == "POST":
        useremail = req.POST['useremail']
        userpassword = req.POST['userpassword']
        if useremail == "csp@gmail.com" and userpassword == "csp":
            return render(req, CSPHOMEPAGE)
        else:
            messages.warning(req, "Invalid credentials")
            return render(req, CSPLOGINPAGE)
    return render(req, CSPLOGINPAGE)


def useractivation(req):
    data = Userregister.objects.filter(status="pending")
    return render(req, "useractivation.html", {'data': data})


def activeuser(req, id):
    dc = Userregister.objects.get(id=id)
    dc.status = "active"
    dc.save()
    return redirect("useractivation")


def userdetails(req):
    dc = Userregister.objects.all()
    return render(req, USERDETAILSPAGE, {'dc': dc})


def cloudfiles(req):

    dc = Uploadfiles.objects.all()
    return render(req, CLOUDFILESPAGE, {'dc': dc})


def auditrequests(req):
    dc = Auditrequest.objects.filter(status="Challenged Cloud")
    return render(req, AUDITREQUESTPAGE, {'dc': dc})


def generateproof(req, id):
    dc = Auditrequest.objects.get(id=id)
    dc.status = "Proof Generated"
    dc.save()
    return redirect("auditrequests")
    # return render(req, GENERATEDPROOFPAGE, {'dc': dc})


def editfile(req, id, filename):
    print(id, filename)
    file_path1 = f"static\Block1\{filename}"  # Correctly format the file path
    f1 = open(file_path1, "r")
    f1data = f1.read()
    print(f1data)

    file_path2 = f"static\Block2\{filename}"
    f2 = open(file_path2, "r")
    f2data = f2.read()
    print(f2data)

    file_path3 = f"static\Block3\{filename}"
    f3 = open(file_path3, "r")
    f3data = f3.read()
    print(f3data)

    file_path4 = f"static\Block4\{filename}"
    f4 = open(file_path4, "r")
    f4data = f4.read()
    print(f4data)
    return render(req, EDITFILEPAGE, {"filename": filename, "id": id, "data1": f1data, "data2": f2data, "data3": f3data, "data4": f4data})


def updatecontent(req):
    if req.method == "POST":
        id = req.POST['id']
        filename = req.POST['filename']

        block1 = req.POST['block1']
        block2 = req.POST['block2']
        block3 = req.POST['block3']
        block4 = req.POST['block4']

        file_path1 = f"static/Block1/{filename}"
        f1 = open(file_path1, "r")
        data1 = f1.read()
        
        newdata1 =data1.replace(data1, block1)
        
        with open(file_path1, 'w') as fp:
            fp.write(newdata1)
            

        file_path2 = f"static/Block2/{filename}"
        f2 = open(file_path2, "r")
        data2 = f2.read()
        newdata2 =data2.replace(data2, block2)
        
        with open(file_path2, 'w') as fp:
            fp.write(newdata2)

        file_path3 = f"static/Block3/{filename}"
        f3 = open(file_path3, "r")
        data3 = f3.read()
        
        newdata3 =data3.replace(data3, block3)
        
        with open(file_path3, 'w') as fp:
            fp.write(newdata3)

        file_path4 = f"static/Block4/{filename}"
        f4 = open(file_path4, "r")
        data4 = f4.read()
        
        newdata4 =data4.replace(data4, block4)
        
        with open(file_path4, 'w') as fp:
            fp.write(newdata4)

        if data1 == block1:
            pass
        else:
            dc = Auditrequest.objects.get(id=id)
            dc.proofcheck = "failed"
            dc.save()
        if data2 == block2:
            pass
        else:
            dc = Auditrequest.objects.get(fileid=id)
            dc.proofcheck = "failed"
            dc.save()
        if data3 == block3:
            pass
        else:
            dc = Auditrequest.objects.get(fileid=id)
            dc.proofcheck = "failed"
            dc.save()
        if data4==block4:
            pass
        else:
            dc = Auditrequest.objects.get(fileid=id)
            dc.proofcheck = "failed"
            dc.save()
        # file_path2 = f"static/Block2/{filename}"
        # read_file(file_path2)

        # file_path3 = f"static/Block3/{filename}"
        # read_file(file_path3)

        # file_path4 = f"static/Block4/{filename}"
        # read_file(file_path4)

        print(id, filename, block1, block2, block3, block4)

        return redirect("cloudfiles")


# def read_file(file_path):
#     try:
#         with open(file_path, "r") as file:
#             file_data = file.read()
#             print(file_data)
#             return redirect("cloudfiles")
#     except FileNotFoundError:
#         print(f"File not found: {file_path}")
#         return f"File not found: {file_path}"
#     except Exception as e:
#         print(f"Error reading file: {file_path}, {e}")
#         return "Error reading file: {file_path}, {e}"
