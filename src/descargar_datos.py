import requests, zipfile, io, pathlib

URL = "https://www.inegi.org.mx/contenidos/programas/enigh/nc/2024/microdatos/enigh2024_ns_concentradohogar_csv.zip"
destino = pathlib.Path("data/raw")
destino.mkdir(parents=True, exist_ok=True)

r = requests.get(URL, timeout=300)
r.raise_for_status()
zipfile.ZipFile(io.BytesIO(r.content)).extractall(destino)
print("Listo:", sorted(p.name for p in destino.iterdir()))