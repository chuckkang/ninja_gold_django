from django.shortcuts import render, redirect, HttpResponse
import random
def index(request):
	
	if 'totalgold' not in request.session:
		request.session['totalgold']=0

	return render(request, "ninja_gold/index.html")

def process_money(request):
	
	if request.POST['building']=="farm":
		rnd = random.randint(10, 20)
		request.session['totalgold'] += rnd
	elif request.POST['building']=="cave":
		rnd = random.randint(5, 10)
		request.session['totalgold'] += rnd
	elif request.POST['building']=="house":
		rnd = random.randint(2, 5)
		request.session['totalgold'] += rnd
	elif request.POST['building']=="casino":
		rnd = random.randint(-50, 50)
		request.session['totalgold'] += rnd
	return redirect("/ninja_gold")

def clear_session(request):
	request.session.clear()
	return redirect('/ninja_gold')
