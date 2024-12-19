class BaseError(Exception):
    pass

class DocumentNotUniqueError(BaseError):
    def __init__(self, document):
        self.document = document
        self.message = f"O documento '{document}' já está em uso."
        super().__init__(self.message)

class RecordNotFoundError(BaseError):
    def __init__(self, record_type, record_id):
        self.record_type = record_type
        self.record_id = record_id
        self.message = f"{record_type} com ID {record_id} não existe."
        super().__init__(self.message)

class InvalidCepError(BaseError):
    def __init__(self, cep):
        self.cep = cep
        self.message = f"O CEP '{cep}' não é válido."
        super().__init__(self.message)

class OrphanageAlreadyExistsError(BaseError):
    def __init__(self, address, number, state, cep):
        self.address = address
        self.number = number
        self.state = state
        self.cep = cep
        self.message = f"Orfanato com cep {cep} , endereço '{address}', número '{number}' e estado '{state}' já está cadastrado."
        super().__init__(self.message)