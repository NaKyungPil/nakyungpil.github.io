import pandas as pd
import requests
code = "000270"
URL = f"https://finance.naver.com/item/main.naver?code={code}"
r = requests.get(URL)
df = pd.read_html(r.text)[3]
df = df.replace({np.nan: ""})

html = df.to_html()
print(html)
