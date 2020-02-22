from django.shortcuts import render, HttpResponse


def hello(request, nome, idade):
    return HttpResponse('<h1>Olá Mundo!! {} de {} anos Hello World!!</h1>'.format(nome, idade))
