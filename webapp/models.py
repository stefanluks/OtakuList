from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        
    nome = models.CharField("Nome do Usuario", max_length=150)
    biografia = models.TextField("Biografia do Usuario", max_length=1500, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def GetInicial(self):
        iniciais = ""
        n = self.nome.split(" ")
        for i in n:
            iniciais+=i[0]
        return iniciais
    
    def __str__(self):
        return self.nome
    

class Seguidores(models.Model):
    class Meta:
        verbose_name = "SEGUIDOR"
        verbose_name_plural = "SEGUIDORES"
        
    segue = models.ForeignKey(Usuario, related_name="User_que_Segue", on_delete=models.CASCADE)
    seguido = models.ForeignKey(Usuario, related_name="sendo_seguido", on_delete=models.CASCADE)
    
    def __str__(self):
        return '{} segue o {}'.format(self.segue.nome, self.seguido.nome)
    
    
class Obra(models.Model):
    class Meta:
        verbose_name = "Obra"
        verbose_name_plural = "Obras"
        
    nome = models.CharField("Nome do anime", max_length=250)
    resumo = models.TextField("Resumo do anime", max_length=2500, blank=True, null=True)
    tipos = (
        ("0","Anime"),
        ("1","Mangá"),
        ("2","Jogo"),
    )
    tipo = models.CharField("Tipo de obra", choices=tipos, max_length=15, default=tipos[0][1])
    
    def GetAvaliacaoAutor(self, autor):
        return list(Avaliacao.objects.filter(autor = autor))
    
    def __str__(self):
        return self.nome + " - " + str(self.tipos[int(self.tipo)][1])

    
class Avaliacao(models.Model):
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE)
    avaliacao = models.TextField("Comentarios", max_length=1500, blank=True, null=True)
    nota = models.IntegerField("Nota da obra", default=0)
    
    def __str__(self):
        if self.avaliacao:
            return '{} avaliou a obra "{}" com a nota: {} + comentario'.format(self.autor.nome, self.obra, self.nota)
        return '{} avaliou a obra "{}" com a nota: {}'.format(self.autor.nome, self.obra, self.nota)

    
class Lista(models.Model):
    titulo = models.CharField("titulo da lista", max_length=150)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE, blank=True, null=True)
    obras = models.ManyToManyField(Obra, blank=True)
    
    def getQtdItens(self):
        return len(list(self.obras.all()))
    
    def __str__(self):
        return "Lista '{}' de: [{}]".format(self.titulo, self.autor.nome)
    

class Feed(models.Model):
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    atualizacao = models.CharField("Descrição da atualizacao", max_length=250)
    referencia = models.CharField("Classe+ID", max_length=15, null=True, blank=True)
    
    def __str__(self):
        return self.autor.nome +" | news: "+self.atualizacao