from database import Database
from helper.writeAJson import writeAJson
from productAnalyzer import ProductAnalyzer

db = Database(database="mercado", collection="produtos")
db.resetDatabase()

productAnalyzer = ProductAnalyzer(db)
productAnalyzer.TotalVendasPorDia()
productAnalyzer.ProdutoMaisVendido() 