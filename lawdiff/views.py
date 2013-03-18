from django.shortcuts import render_to_response, get_object_or_404, redirect
from wordiff.models import GramRankings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
	rankings_list = GramRankings.objects.all().order_by("-date_created")
	try:
		page = request.GET.get("page")
	except:
		page = 1
	paginator = Paginator(rankings_list, 10)

	try:
		rankings = paginator.page(page)
	except PageNotAnInteger:
		rankings = paginator.page(1)
	except EmptyPage:
		paginator.page(paginator.num_pages)

	return render_to_response("index.html", {"rankings": rankings})
