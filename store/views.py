from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


def product_list(request):
    products = Product.objects.all()

    # simple recommender (example)
    recommended = Product.objects.filter(category="Electronics")[:3]

    return render(request, 'store/product_list.html', {
        'products': products,
        'recommended': recommended
    })


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            product = form.save(commit=False)

            # simple AI-style tagging logic
            tags = []
            if "phone" in product.name.lower():
                tags.append("mobile")
            if "laptop" in product.name.lower():
                tags.append("computer")

            product.tags = tags
            product.save()

            return redirect('/')
    else:
        form = ProductForm()

    return render(request, 'store/add_product.html', {'form': form})