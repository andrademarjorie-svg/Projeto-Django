class Categoria (models.Model):
    nome = models.CharField(max_lenght=50, unique=True)
    descricao = models.TextField(blanck=True, null=True)
    criada_em = models.DateTimeField(auto_now_add=True)

    def_str_(self):
    return self.nome

    