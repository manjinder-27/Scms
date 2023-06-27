from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from manager.models import Student,Application

baseData = {
	'schoolName':'My School'
}

# Create your views here.
def home(request):
	return render(request,'home.html',context=baseData)

def newAdmission(request):
	if request.method == "POST":
		if len(Application.objects.all()) > 0:
			id = str(int(Application.objects.last().appId) + 1)
		else:
			id = "1"
		firstName = request.POST.get('fname')
		lastName = request.POST.get('lname')
		cls = request.POST.get('cls')
		phone = request.POST.get('phone')
		father = request.POST.get('father')
		application = Application(appId=id,firstName = firstName,lastName=lastName,studentClass = cls,phoneNumber=phone,fatherName=father)
		application.save()
		data = {}
		data['appid'] = id
		data['schoolName'] = baseData['schoolName']
		return render(request,'admissionsuccess.html',context=data)
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
		data1 = []
		for i in Student.objects.all():
			data1.append({'admNum':i.admNum,'firstName':i.firstName,'lastName':i.lastName,'fatherName':i.fatherName,'phoneNumber':i.phoneNumber,'studentClass':i.studentClass})
		data2 = []
		for i in Application.objects.all():
			data2.append({'appId':i.appId,'firstName':i.firstName,'lastName':i.lastName,'fatherName':i.fatherName,'phoneNumber':i.phoneNumber,'studentClass':i.studentClass})
		data = {
			'studentsData':data1,
			'applicationsData':data2
		}
		data['schoolName'] = baseData['schoolName']
		return render(request,'dashboard.html',context=data)
	else:
		return render(request,'autherror.html',context=baseData)

def showfeestruct(request):
	return render(request,'feestruct.html',context=baseData)

def logoutUser(request):
	logout(request)
	return redirect('/')

def removeStudent(request,admNum):
	if request.user.is_authenticated:
		for s in Student.objects.all():
			if s.admNum == admNum:
				s.delete()
				break
		return redirect('/dashboard')
	else:
		return render(request,'autherror.html',context=baseData)

def getObj(id):
	for i in Application.objects.all():
		if i.appId == id:
			return i

def approveApplication(request,appid):
	if request.user.is_authenticated:
		if len(Student.objects.all()) > 0:
			num = int(Student.objects.last().admNum) + 1
		else:
			num = "9001"
		obj = getObj(appid)
		admnum = "0" + str(num)
		firstName = obj.firstName
		lastName = obj.lastName
		cls = obj.studentClass
		phone = obj.phoneNumber
		father = obj.fatherName
		student = Student(admNum=admnum,firstName = firstName,lastName=lastName,studentClass = cls,phoneNumber=phone,fatherName=father)
		student.save()
		obj.delete()
		return redirect('/dashboard')
	else:
		return render(request,'autherror.html',context=baseData)