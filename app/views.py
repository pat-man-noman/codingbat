from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def rounded(request, number1):
    print(number1)
    if int(number1) >= 90 and int(number1) <= 110:
            return HttpResponse(True)
    elif int(number1) >= 190 and int(number1) <= 210:
          return HttpResponse(True)
    else:
        return HttpResponse(False)
def letters(request, letters):
        letter1 = ""
        letter2 = ""
        for character in str(letters):
                letter1 += character
                letter2 += letter1
        return HttpResponse(letter2)
def pet(request, pet):
        return HttpResponse(pet.count('cat') == pet.count("dog"))
def long_sum(request,a,b,c):
       values = [int(a),int(b),int(c)]
       counts = {x:values.count(x) for x in values}
       return HttpResponse(sum(x for x in values if counts[x] == 1))