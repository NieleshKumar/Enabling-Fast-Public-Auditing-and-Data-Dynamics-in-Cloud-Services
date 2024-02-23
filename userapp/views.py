from django.shortcuts import render, redirect
from .models import Userregister, Uploadfiles, Auditrequest
from django.contrib import messages
import hashlib
from django.core.files.base import ContentFile
import os
from django.core.files.storage import default_storage


# Templates
INDEXPAGE = "index.html"
USERLOGIN = "userlog.html"
USERREGISTRATIONPAGE = "userregister.html"
USERHOMEPAGE = "userhome.html"
UPLOADFILESPAGE = "uploadfiles.html"
MYFILESPAGE = "myfiles.html"
AUDITFILEPAGE = "auditfile.html"
AUDITMYFILESPAGE = "auditmyfiles.html"
# REGISTRATIONPAGE = "userregister.html"
# Create your views here.


def index(req):
    return render(req, INDEXPAGE)


def userlogin(req):
    if req.method == "POST":
        user_email = req.POST['useremail']
        user_password = req.POST['userpassword']
        dc = Userregister.objects.filter(
            user_email=user_email, user_password=user_password, status='active').exists()
        if dc:
            req.session['user_email'] = user_email
            return render(req, USERHOMEPAGE)
        else:
            messages.warning(req, "Invalid details")
            return render(req, USERLOGIN, {'login': 'login'})
    return render(req, USERLOGIN, {'login': 'login'})


def useregister(req):
    if req.method == "POST":
        user_name = req.POST['username']
        user_email = req.POST['useremail']
        user_password = req.POST['password']
        user_contact = req.POST['contact']
        user_address = req.POST['address']
        dc = Userregister.objects.filter(
            user_email=user_email, user_password=user_password).exists()
        if dc:
            messages.warning(req, "Details already exists")
            return render(req, USERREGISTRATIONPAGE, {'login': 'register'})
        else:
            dc = Userregister(user_name=user_name, user_email=user_email,
                              user_password=user_password, user_contact=user_contact, user_address=user_address)
            dc.save()
            return render(req, USERREGISTRATIONPAGE, {'login': 'login'})
    return render(req, USERREGISTRATIONPAGE, {'login': 'register'})


def uploadfiles(req):
    if req.method == "POST":
        filename = req.POST['file']
        filedetails = req.FILES['filedetails']
        myfilename = filedetails.name
        path = default_storage.save(os.path.join(
            "static/files/", myfilename), ContentFile(filedetails.read()))

        # Access the saved file's path
        saved_path = default_storage.url(path)

        # Print or use the saved path as needed
        print("File saved at:", saved_path)
        print("========================")
        filedata = open("static/files/" + filedetails.name, "r")
        myfiledata = filedata.read()
        print(myfiledata)
        datalen = int(len(myfiledata))
        print(datalen)
        splitdata = 4
        data = datalen // splitdata
        print(data)

        dataone = myfiledata[0:data]

        hashcode256 = hashlib.sha256(dataone.encode())
        hash2561 = hashcode256.hexdigest()
        hashcode1 = hashlib.sha1(dataone.encode())
        hash11 = hashcode1.hexdigest()
        print("Part 1:", dataone)

        f = open("static/Block1/"+myfilename, "w")
        f.write(dataone)
        f.close()

        datatwo = myfiledata[data:data*2]

        hashcode256 = hashlib.sha256(datatwo.encode())
        hash2562 = hashcode256.hexdigest()
        hashcode1 = hashlib.sha1(datatwo.encode())
        hash12 = hashcode1.hexdigest()
        print("Part 2:", datatwo)

        f = open("static/Block2/"+myfilename, "w")
        f.write(datatwo)
        f.close()

        datathree = myfiledata[data*2:data*3]
        hashcode256 = hashlib.sha256(datathree.encode())
        hash2563 = hashcode256.hexdigest()
        hashcode1 = hashlib.sha1(datathree.encode())
        hash13 = hashcode1.hexdigest()
        print("Part 3:", datathree)

        f = open("static/Block3/"+myfilename, "w")
        f.write(datathree)
        f.close()

        datafour = myfiledata[data*3:data*4]
        hashcode256 = hashlib.sha256(datafour.encode())
        hash2564 = hashcode256.hexdigest()
        hashcode1 = hashlib.sha1(datafour.encode())
        hash14 = hashcode1.hexdigest()
        print("Part 4:", datafour)

        f = open("static/Block4/"+myfilename, "w")
        f.write(datafour)
        f.close()

        dc = Uploadfiles(
            user_email=req.session['user_email'],
            inputfilename=filename,
            filename=myfilename,
            hashcodeone=hash2561,
            hashcodetwo=hash2562,
            hashcodethree=hash2563,
            hashcodefour=hash2564,
            keyone=hash11,
            keytwo=hash12,
            keythree=hash13,
            keyfour=hash14)
        dc.save()
        messages.success(req, "File Uploaded successfully")
        return render(req, UPLOADFILESPAGE)
    return render(req, UPLOADFILESPAGE)


def myfiles(req):
    dc = Uploadfiles.objects.filter(user_email=req.session['user_email'])
    return render(req, MYFILESPAGE, {'dc': dc})

def deletefile(req,id):
    print(f"delete file { id}")
    data = Uploadfiles.objects.filter(id=id)
    data.delete()
    messages.success(req,"File deleted successfully")
    return redirect("myfiles")


def auditfile(req):
    dc = Uploadfiles.objects.filter(user_email=req.session['user_email'])
    return render(req, AUDITFILEPAGE, {"dc": dc})


def auditmyfiles(req, id, filename):
    print(id, filename)
    dc = Auditrequest(fileid=id, filename=filename,
                      useremail=req.session['user_email'])
    dc.save()
    return redirect("auditfile")


def audittransactions(req):
    dc = Auditrequest.objects.filter(useremail=req.session['user_email'])
    return render(req, AUDITMYFILESPAGE, {'dc': dc})
