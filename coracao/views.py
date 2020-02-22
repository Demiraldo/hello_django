from django.shortcuts import render, HttpResponse


def hello(request, nome, idade):
    return HttpResponse('<h1>Olá Mundo!! {} de {} anos Hello World!!</h1>'.format(nome, idade))


def soma(request, n1, n2):
    s = n1 + n2
    return HttpResponse('<h1>A soma entre os números é: {}</h1>'.format(s))


def multiplicacao(request, n3, n4):
    m = n3 * n4
    return HttpResponse('<h1>A multiplicação entre os números é de: {}</h1>'.format(m))


def divisao(request, n5, n6):
    d = n5 / n6
    return HttpResponse('<h1>A divisão entre os números é: {}</h1>'.format(d))


def subtracao(request, n7, n8):
    ss = n7 - n8
    return HttpResponse('<h1>A subtração entre eles é: {}</h1>'.format(ss))
