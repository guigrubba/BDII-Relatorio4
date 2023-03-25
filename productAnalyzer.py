from helper.writeAJson import writeAJson
from database import Database

class ProductAnalyzer:
    def __init__(self, database: Database):
        self.db = database

    def TotalVendasPorDia(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$data_compra", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}}
        ])        
        writeAJson(result, "Total de vendas por dia")

    def ProdutoMaisVendido(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": -1}},
            {"$limit": 1}
        ])
        writeAJson(result, "Produto mais vendido")

    
    def postPokemonByWeakness(self, weakness: list):
        pokemons = self.db.collection.find({"weaknesses": {"$all": weakness}})
        writeAJson(pokemons, "pokemons_by_weakness") 
    
    def postPokemonByNumberWeakness(self, number):
        pokemons = self.db.collection.find({"weaknesses": {"$size": number}})
        writeAJson(pokemons, "pokemon_by_number_weakness")
    
    def postPokemonIntervalSpawn(self, spawn1, spawn2):
        pokemons = self.db.collection.find({"spawn_chance": {"$gt": spawn1, "$lt": spawn2}})
        writeAJson(pokemons, "pokemon_by_interval_spawn")
