from aed_ds.dictionaries.hash_table import HashTable
#from aed_ds.lists.doubly.linked.list import DoublyLinkedList
from models.user import User
from models.profissionais import Profissional
from models.utentes import Utentes

class ListController:
    def __init__(self):
        self.categorias = HashTable()
        self.categorias.insert("medicina",HashTable())
        self.categorias.insert("enfermagem",HashTable())
        self.categorias.insert("auxiliar",HashTable())
        
    def has_categoria(self, nome_categoria):
        if self.categorias.has_key(nome_categoria):
            return True
        return False
    
    def has_profissional(self,nome_categoria , nome_profissional):
        categoria = self.categorias.get(nome_categoria)
        if categoria.has_key(nome_profissional):
            return True
        return False
    
    def add_profissional(self, nome_categoria , nome_profissional):
        profissionais = self.categorias.get(nome_categoria)
        profissional = Profissional(nome_profissional) 
        profissionais.insert(nome_profissional,profissional)
    
    def has_faixa(self, faixa_etaria):
        pass

    def has_family(self, nome_familia):
        pass
    
    def exist_familia(self, nome_familia):
        pass

    def remove_user_family(self,nome_utente):
        pass
    
    def has_utente_in_table(self):
        pass

    def print_list_professionals(self):
        pass

    def print_list_users(self):
        pass

    def has_family_register(self):
        pass
    
    def print_families(self):
        pass

    def print_users_family(self,nome_familia):
        pass

    def existe_cuidado(self,nome_utente):
        pass

    def desmarcar_cuidado(self,nome_utente):
        pass

    def listar_cuidados_utente(self,nome_utente):
        pass

    def listar_cuidados_familia(self,nome_familia):
        pass
    
    def listar_cuidados_prof(self,nome_profissional):
        pass

    def has_service(self,serviço):
        pass

    def has_marked_service(self,serviço):
        pass

    def list_marked_services(self,serviço):
        pass
