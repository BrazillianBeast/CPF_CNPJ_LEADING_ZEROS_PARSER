import re

def cnpj_to_numbers(formatted_cnpj):
    """Converts a formatted CNPJ to a string of 11 numbers"""
    if isinstance(formatted_cnpj, float) or isinstance(formatted_cnpj, int):
        return str(int(formatted_cnpj)).zfill(14)
    else:
        return re.sub(r'\W', '', formatted_cnpj).zfill(14)

def cpf_to_numbers(formatted_cpf):
    """Converts a formatted CPF to a string of 11 numbers"""
    if isinstance(formatted_cpf, float) or isinstance(formatted_cpf, int):
        return str(int(formatted_cpf)).zfill(11)
    else:
        return re.sub(r'\W', '', formatted_cpf).zfill(11)
    
if __name__ == "__main__":
    CPF = cpf_to_numbers(7323474223)
    print(CPF)