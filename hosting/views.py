from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Domain, Server
from .forms import DomainForm, ServerForm
from customers.models import Customer
from django.template.loader import render_to_string
from django.http import JsonResponse


# =========================
# Domain CRUD
# =========================

def domain_list(request):
    search = request.GET.get('search', '')
    client = request.GET.get('client', '')
    status = request.GET.get('status', '')
    from_date = request.GET.get('from_date', '')
    to_date = request.GET.get('to_date', '')

    domains = Domain.objects.select_related('client').all().order_by('-id')
    clients = Customer.objects.all()

    if search:
        domains = domains.filter(domain_name__icontains=search)

    if client:
        domains = domains.filter(client_id=client)

    if status:
        domains = domains.filter(status=status)

    if from_date:
        domains = domains.filter(start_date__gte=from_date)

    if to_date:
        domains = domains.filter(end_date__lte=to_date)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        html = render_to_string('hosting/search_domain.html', {'domains': domains}, request=request)
        return JsonResponse({
            'html': html,
            'total_domains': domains.count(),
            'active_domains': domains.filter(status='active').count(),
            'inactive_domains': domains.filter(status='inactive').count(),
        })

    context = {
        'domains': domains,
        'clients': clients,
        'total_domains': domains.count(),
        'active_domains': domains.filter(status='active').count(),
        'inactive_domains': domains.filter(status='inactive').count(),
    }
    return render(request, 'hosting/domain_list.html', context)



def domain_create(request):
    if request.method == 'POST':
        form = DomainForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Domain created successfully.')
            return redirect('hosting:domain_list')
    else:
        form = DomainForm()

    context = {
        'form': form,
        'page_title': 'Create Domain'
    }
    return render(request, 'hosting/domain_form.html', context)


def domain_update(request, pk):
    domain = get_object_or_404(Domain, pk=pk)

    if request.method == 'POST':
        form = DomainForm(request.POST, instance=domain)
        if form.is_valid():
            form.save()
            messages.success(request, 'Domain updated successfully.')
            return redirect('hosting:domain_list')
    else:
        form = DomainForm(instance=domain)

    context = {
        'form': form,
        'page_title': 'Update Domain'
    }
    return render(request, 'hosting/domain_form.html', context)


def domain_delete(request, pk):
    domain = get_object_or_404(Domain, pk=pk)

    domain.delete()
    messages.success(request, 'Domain deleted successfully.')
    return redirect('hosting:domain_list')

   

# =========================
# Server CRUD
# =========================
def server_list(request):
    search = request.GET.get('search', '')
    status = request.GET.get('status', '')
    provider = request.GET.get('provider', '')
    from_date = request.GET.get('from_date', '')
    to_date = request.GET.get('to_date', '')

    servers = Server.objects.all().order_by('-id')

    if search:
        servers = servers.filter(server_name__icontains=search)

    if status:
        servers = servers.filter(status=status)

    if provider:
        servers = servers.filter(provider__icontains=provider)

    if from_date:
        servers = servers.filter(start_date__gte=from_date)

    if to_date:
        servers = servers.filter(end_date__lte=to_date)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        html = render_to_string('hosting/search_server.html', {'servers': servers}, request=request)
        return JsonResponse({
            'html': html,
            'total_servers': servers.count(),
            'active_servers': servers.filter(status='active').count(),
            'inactive_servers': servers.filter(status='inactive').count(),
        })

    context = {
        'servers': servers,
        'total_servers': servers.count(),
        'active_servers': servers.filter(status='active').count(),
        'inactive_servers': servers.filter(status='inactive').count(),
    }
    return render(request, 'hosting/server_list.html', context)



def server_create(request):
    if request.method == 'POST':
        form = ServerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Server created successfully.')
            return redirect('hosting:server_list')
    else:
        form = ServerForm()

    context = {
        'form': form,
        'page_title': 'Create Server'
    }
    return render(request, 'hosting/server_form.html', context)


def server_update(request, pk):
    server = get_object_or_404(Server, pk=pk)

    if request.method == 'POST':
        form = ServerForm(request.POST, instance=server)
        if form.is_valid():
            form.save()
            messages.success(request, 'Server updated successfully.')
            return redirect('hosting:server_list')
    else:
        form = ServerForm(instance=server)

    context = {
        'form': form,
        'page_title': 'Update Server'
    }
    return render(request, 'hosting/server_form.html', context)


def server_delete(request, pk):
    server = get_object_or_404(Server, pk=pk)

    server.delete()
    messages.success(request, 'Server deleted successfully.')
    return redirect('hosting:server_list')
