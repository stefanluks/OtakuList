from django.shortcuts import render
from .models import Usuario, Avaliacao, Lista, Obra, Feed, Seguidores

def FeedConfig(usuario):
    seguindo = list(Seguidores.objects.filter(segue = usuario))
    lista = []
    print(seguindo)
    for segue in seguindo:
        for news in list(Feed.objects.filter(autor = segue.seguido)):
            lista.append(news)
    return lista

def Home(request):
    usuario = None
    listas = []
    feed = []
    if request.user.is_authenticated:
        usuario = Usuario.objects.get(user=request.user)
        listas = list(Lista.objects.filter(autor = usuario))
        feed = FeedConfig(usuario)
    return render(request, 'home.html', {
        "titulo": "Pagina inicial",
        "user":usuario,
        "obras":Obra.objects.all(),
        'listas':listas,
        "len_listas":len(listas),
        "feed": feed
    })

def Perfil(request, user):
    usuario = None
    if request.user.is_authenticated:
        usuario = Usuario.objects.get(user__username = user)
    return render(request, 'perfil.html', {"user":usuario})


def ListaView(request, id):
    usuario = None
    listas = []
    feed = []
    if request.user.is_authenticated:
        usuario = Usuario.objects.get(user=request.user)
        listas = list(Lista.objects.filter(autor = usuario))
        principal = Lista.objects.get(pk=id)
    return render(request, 'conteudo_lista.html', {
        "titulo": "Lista: "+principal.titulo,
        "user":usuario,
        "obras":Obra.objects.all(),
        'listas':listas,
        "len_listas":len(listas),
        'lista_principal': principal,
    })
    
def GetDados(model, id):
    match model:
        case "Usuario":
            return Usuario.objects.get(pk=id)
        case "Seguidores":
            return Seguidores.objects.get(pk=id)
        case "Obra":
            return Obra.objects.get(pk=id)
        case "Avaliacao":
            return Avaliacao.objects.get(pk=id)
        case "Lista":
            return Lista.objects.get(pk=id)
        case "Feed":
            return Feed.objects.get(pk=id)

def OpenNews(request, idFeed):
    usuario = None
    listas =[]
    novidade = Feed.objects.get(pk=idFeed)
    classe, idItem = novidade.referencia.split("+")
    if request.user.is_authenticated:
        usuario = Usuario.objects.get(user=request.user)
        listas = list(Lista.objects.filter(autor = usuario))
    return render(request, 'news.html', {
        "titulo": "NOvidade",
        "listas":listas,
        "len_listas":len(listas),
        "user":usuario,
        "obras":Obra.objects.all(),
        "novidade": GetDados(classe, idItem)
    })