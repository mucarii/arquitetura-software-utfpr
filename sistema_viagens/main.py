# 1. Classes para diferentes partes do sistema
class ReservaVoo:
    def reserva_voo(self, origem, destino):
        # Lógica para reservar um voo
        print(f"Reservando voo de {origem} para {destino}")
        return "Reserva de voo confirmada"


class ReservaHotel:
    def reserva_hotel(self, destino):
        # Lógica para reservar um hotel
        print(f"Reservando hotel em {destino}")
        return "Reserva de hotel confirmada"


class AluguelCarro:
    def aluguel_carro(self, destino):
        # Lógica para alugar um carro
        print(f"Alugando carro em {destino}")
        return "Aluguel de carro confirmado"


# 2. Classe Facade para simplificar a interação


class TravelFacade:
    def __init__(self):
        # Instanciamos as diferentes partes do sistema
        self.reserva_voo = ReservaVoo()
        self.reserva_hotel = ReservaHotel()
        self.aluguel_carro = AluguelCarro()

    def viagem_completa(self, origem, destino):
        # Encapsulamos o processo completo de reserva de viagem
        voo = self.reserva_voo.reserva_voo(origem, destino)
        hotel = self.reserva_hotel.reserva_hotel(destino)
        carro = self.aluguel_carro.aluguel_carro(destino)

        return {"voo": voo, "hotel": hotel, "carro": carro}


# 3. Testando o sistema

if __name__ == "__main__":
    # O cliente deseja reservar uma viagem de São Paulo para Nova York
    travel_facade = TravelFacade()
    result = travel_facade.viagem_completa("São Paulo", "Nova York")

    # Mostra o resultado da reserva
    print("\nResumo da Reserva:")
    for key, value in result.items():
        print(f"{key.capitalize()}: {value}")
