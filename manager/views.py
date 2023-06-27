from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from manager.models import Student,Application,Employee
import os

baseData = {
	'schoolName':'My School'
}

# Create your views here.
def home(request):
	return render(request,'home.html',context=baseData)

def newAdmission(request):
	if request.method == "POST":
		applicationType = request.POST.get('type')
		name = request.POST.get('name')
		father = request.POST.get('fname')
		cls = request.POST.get('cls')
		phone = request.POST.get('phone')
		aadhar = request.POST.get('aadhar')
		if applicationType == "Student":
			appliedAs = "Student"
			appliedFor = cls
		else:
			appliedAs = "Employee"
			appliedFor = applicationType
		application = Application(name = name,father=father,appliedAs=appliedAs,appliedFor=appliedFor,phone=phone,aadhar=aadhar)
		application.save()
		return render(request,'admissionsuccess.html',context=baseData)
	return render(request,'admissionform.html',context=baseData)

def staffLogin(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username,password=password)
		if user is None:
			messages.error(request,'Invalid Username/Password Try Again ! ')
		else:
			login(request,user)
			return redirect('/dashboard')
	return render(request,'login.html',context=baseData)

def showAbout(request):
	return render(request,'about.html',context=baseData)

def dashboard(request):
	if request.user.is_authenticated:
		return render(request,'dashboard.html',context=baseData)
	else:
		return render(request,'autherror.html',context=baseData)

def showfeestruct(request):
	return render(request,'feestruct.html',context=baseData)

def logoutUser(request):
	logout(request)
	return redirect('/')

def removeStudent(request,adm):
	if request.user.is_authenticated:
		for s in Student.objects.all():
			if s.adm == adm:
				s.delete()
				break
		return redirect('/dashboard')
	else:
		return render(request,'autherror.html',context=baseData)


def removeEmployee(request,id):
	if request.user.is_authenticated:
		for e in Employee.objects.all():
			if e.uid == id:
				e.delete()
				break
		return redirect('/dashboard')
	else:
		return render(request,'autherror.html',context=baseData)


def getObj(appid):
	for i in Application.objects.all():
		if i.id == int(appid):
			return i


def approveApplication(request,appid):
	if request.user.is_authenticated:
		obj = getObj(appid)
		if obj.appliedAs == "Student":
			student = Student(adm=obj.id,name=obj.name,father=obj.father,phone=obj.father,aadhar=obj.aadhar,cls=obj.appliedFor)
			student.save()
		else:
			employee = Employee(uid=obj.id,name=obj.name,father=obj.father,phone=obj.father,aadhar=obj.aadhar,job=obj.appliedFor)
			employee.save()
		obj.delete()
		return redirect('/dashboard')
	else:
		return render(request,'autherror.html',context=baseData)


def showStudentsList(request):
	if request.user.is_authenticated:
		data = []
		for i in Student.objects.all():
			data.append({'adm':i.adm,'name':i.name,'father':i.father,'phone':i.phone,'aadhar':i.aadhar,'cls':i.cls})
		baseData['studentsData'] = data
		return render(request,'studentlist.html',baseData)
	else:
		return render(request,'autherror.html',context=baseData) 


def showApplicationsList(request):
	if request.user.is_authenticated:
		data = []
		for i in Application.objects.all():
			data.append({'num':i.id,'name':i.name,'father':i.father,'phone':i.phone,'aadhar':i.aadhar,'appliedAs':i.appliedAs,'appliedFor':i.appliedFor})
		baseData['applicationsData'] = data
		return render(request,'applicationlist.html',baseData)
	else:
		return render(request,'autherror.html',context=baseData) 


def showStaffList(request):
	if request.user.is_authenticated:
		data = []
		for i in Employee.objects.all():
			data.append({'id':i.uid,'name':i.name,'father':i.father,'phone':i.phone,'aadhar':i.aadhar,'work':i.job})
		baseData['staffData'] = data
		return render(request,'stafflist.html',baseData)
	else:
		return render(request,'autherror.html',context=baseData) 