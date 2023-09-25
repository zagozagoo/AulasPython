#usando a lista principal, crie outras 3 e separe os times em primeira, segunda e terceira:
data = ['1_flamengo', '2_palmeiras', '1_athletico', '2_internacional', '3_são paulo', '3_bahia', '1_grêmio', '2_coritiba', '1_vasco', '3_ponte preta', '2_fotaleza']

data_sorted = data.copy()
data_sorted.sort()

primeira = [x for x in data_sorted if "1_" in x]
primeira = [x[2:] for x in primeira]
primeira = [x.capitaliz() for x in primeira]

segunda = [x for x in data_sorted if "2_" in x]
segunda = [x[2:] for x in segunda]
segunda = [x.capitaliz() for x in segunda]

terceira = [x for x in data_sorted if "3_" in x]
terceira = [x[2:] for x in terceira]
terceira = [x.capitaliz() for x in terceira]