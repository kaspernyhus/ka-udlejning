from django.shortcuts import render

def show_stats(request):
  context = {}
  return render(request, 'statistik/stats.html', context)