from django.shortcuts import render, redirect
from userapp.models import Userregister, Auditrequest
from userapp.models import Uploadfiles
from django.contrib import messages

# templates
INDEXPAGE = "index.html"
TPALOGINPAGE = "tpalogin.html"
TPAHOMEPAGE = "tpahome.html"
USERSPAGE = "users.html"
INTEGRITYPAGE = "integrity.html"
VIEWMETADATAPAGE = "viewmeta.html"
CHALLENGECLOUDPAGE = "challengecloud.html"
ALLAUDITSPAGE = "allaudits.html"
# Create your views here.

def index(req):
    return render(req, INDEXPAGE)

def tpa(req):
    if req.method == "POST":
        useremail = req.POST['useremail']
        userpassword = req.POST['userpassword']
        if useremail == "tpa@gmail.com" and userpassword == "tpa":
            return render(req, TPAHOMEPAGE)
        else:
            return render(req, TPALOGINPAGE)
    return render(req, TPALOGINPAGE)


def users(req):
    dc = Userregister.objects.all()
    return render(req, USERSPAGE, {'dc': dc})


def integrity(req):
    dc = Auditrequest.objects.filter(status="waiting")
    print(dc)
    return render(req, INTEGRITYPAGE, {'dc': dc})


def viewmetadata(req, fileid):
    dc = Uploadfiles.objects.filter(id=fileid)
    # data = [(i.id, i.user_email, i.inputfilename, i.filename, i.uploadeddate, i.hashcodeone, i.hashcodetwo,
    #          i.hashcodethree, i.hashcodefour, i.keyone, i.keytwo, i.keythree, i.keyfour) for i in dc]
    return render(req, VIEWMETADATAPAGE, {'dc': dc})


def challengecloud(req, id):
    print(id)
    dc = Auditrequest.objects.get(id=id, status="waiting")
    dc.status = "Challenged Cloud"
    dc.save()
    return redirect("integrity")


def challengestatus(req):
    dc = Auditrequest.objects.filter(proofcheck="waiting")
    return render(req, CHALLENGECLOUDPAGE, {'dc': dc})


def checkuser(req, fileid):
    try:
        dc = Auditrequest.objects.get(fileid=fileid, status="Proof Generated")
        dc.proofcheck = 'success'
        dc.save()
        return redirect("challengestatus")
    except:
        
        
        messages.warning(req, "Integrity check failed")
        return redirect("challengestatus")


def allaudits(req):
    dc = Auditrequest.objects.filter()
    return render(req, ALLAUDITSPAGE, {'dc': dc})
