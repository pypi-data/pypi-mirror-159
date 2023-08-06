# captchascraper
captcha and cloudflare bypass<br>
[get apikey](https://www.scraperapi.com/)
# Example
```py
import captchascraper

data = {"name": "captchascraper","message": "captchascraper","send_message": "投稿"}

apikey = "APIKEYHERE"

# get
captchascraper.get("https://aarrzearadiscord.000webhostapp.com/anarchy/chat/",apikey=apikey)

# post
captchascraper.post("https://aarrzearadiscord.000webhostapp.com/anarchy/chat/",apikey=apikey,data=data)

# put
captchascraper.put("https://aarrzearadiscord.000webhostapp.com/anarchy/chat/",apikey=apikey)


# patch
captchascraper.patch("https://aarrzearadiscord.000webhostapp.com/anarchy/chat/",apikey=apikey,data=data)

#delete
captchascraper.delete("https://aarrzearadiscord.000webhostapp.com/anarchy/chat/",apikey=apikey)
```
# インストールの仕方
`$ pip install captchascraper`<br>
`$ pip install git+https://github.com/zearadiscord/captchascraper`
```py
import captchascraper

print(captchascraper.get("https://google.com").status_code)
```
