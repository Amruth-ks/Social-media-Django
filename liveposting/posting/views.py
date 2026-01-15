from django.shortcuts import render, redirect, get_object_or_404
from .models import Species


def index(request):
    if request.method == "POST":
        Species.objects.create(
            name=request.POST.get("name"),
            scientific_name=request.POST.get("scientific_name"),
            description=request.POST.get("description"),
            cash_value=request.POST.get("cash_value"),
            image=request.FILES.get("image"),
        )
        return redirect("exotic")

    return render(request, "index.html")


def exotic(request):
    exotics = Species.objects.all()
    return render(request, "exotic.html", {"exotics": exotics})


def edit_species(request, id):
    species = get_object_or_404(Species, id=id)

    if request.method == "POST":
        species.name = request.POST.get("name")
        species.scientific_name = request.POST.get("scientific_name")
        species.description = request.POST.get("description")
        species.cash_value = request.POST.get("cash_value")

        if request.FILES.get("image"):
            species.image = request.FILES.get("image")

        species.save()
        return redirect("exotic")

    return render(request, "edit.html", {"species": species})


def delete_species(request, id):
    species = get_object_or_404(Species, id=id)
    species.delete()
    return redirect("exotic")
