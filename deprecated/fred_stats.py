import requests

api_key = "6f87a4be50cef4ad00bd25a16db9f1b0"

url = "https://api.stlouisfed.org/fred/series/observations?api_key=6f87a4be50cef4ad00bd25a16db9f1b0&series_id=GNPCA&file_type=json&realtime_start=2025-01-01&realtime_end=2025-09-22"

payload = {}
headers = {
  'Cookie': 'ak_bmsc=CDB47C4C4DAD78F1D6F0F2FD8D655F3D~000000000000000000000000000000~YAAQmWRCF+fc01CZAQAA+qEydB3Q8NgJ+a6cplRGWg6g27uJSqtjcZcbpXS9jiVhuOAZDmRlmBpHrOfrbN7LPLFl5exep1PaVbn3dKrlCngU+FVWHxyPOhGOvAXhQIn0GvygCihnhJ1M/xioH7pPSHc/+j6RdUTqQIzXuorIAt59hhWy2PHxRhLL1FownynJKS0HiDQ1LFNw/nE5bnLVCB7N6glFMdZt1fMK1/LWhxwy+okewWn8/oLk5OFP1QlxslcWptxe5g+niV3ARAKG+l+/s1rAyLR8l20Xmfr8zPs8MrcJR4hytTukhdiO9Z1ialb2dzZy5+qxrAuBH+gY6LKzE6qmArD5+1lLsit1jdTpsg==; bm_sv=9FD406B6B9506819314C6A10E073F54C~YAAQmWRCFx191lCZAQAAZ2ZDdB0QwNCLICcwWIftUVXaczgE8HYv70ZappW1s4F+D5GWjJN4qLIJn2zO2LTeZNWq3cUTOmV4cQ+ZNuBahJyYEwe9AneC9wLIl2I6z2TAWyzekFppvWtiVUCeBqXpN634mm0MJ7rDF49Eer5lwXXRayaZc6ZqUeO/uiG0hhFMm34Npsqv1W6dTnlZPU61dk4X/D8G4HiCj60cQrH5QCj2c1rZxl3NGByu4yBwfjSLC8+47Q==~1'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
