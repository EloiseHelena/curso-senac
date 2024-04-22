class PontoGeografico:
     
   def __init__(self, latitude, longitude):
       self.latitude = latitude
       self.longitude = longitude
       
       
   def get_latitude(self):
    return self.latitude  
       
   def get_longitude(self):
    return self.longitude


   def set_latitude(self, nova_latitude):
     self.latitude = nova_latitude
     
   def set_longitude(self, nova_longitude):
     self.longitude = nova_longitude

if __name__ == '__main__':
    ponto = PontoGeografico (-2.98676, -58.3974)
    
# Imprime latitude e longitude 
print(f"Latitude: {ponto.get_latitude()}")

print(f"Longitude: {ponto.get_longitude()}")


#Imprime nova latitude e nova longitude
ponto.set_latitude(-29.9357)
print(f"Nova latitude: {ponto.get_latitude()}")

ponto.set_longitude(-51.0166)
print(f"Nova longitude: {ponto.get_longitude()}")


