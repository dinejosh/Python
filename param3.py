def cake(flav="Pine",weg="2kgs",shape="Square"):
	print("Flavour: "+flav)
	print("weight: "+weg)
	print("shape: "+shape)
	print()
cake("choc","3kgs","round")	
cake("vanilla","2Kgs")
cake("staubarry","heart")
cake(flav="staubarry",shape="heart")


#Keyword argument

def cake(flav="Pine",weg="2kgs",shape="Square",**kwargs):
	print("Flavour: "+flav)
	print("weight: "+weg)
	print("shape: "+shape)
	print(kwargs)
	print()

cake(flav="Pine",weg="2kgs",shape="Square",toppings="Almonds")

