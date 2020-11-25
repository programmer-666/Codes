def bagilhata(sm, so):
    return 100*(sm-so)/sm*1.5 # % değer döndürür +-
o = 4
for m in range(1, 9):
    print(f"m:{m} -> a: %{bagilhata(m,o)} Hata")