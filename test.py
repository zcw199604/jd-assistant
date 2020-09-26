import requests

headers = {
    "referer":"https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.754894437.1.5af911d9Vo9rtF&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F",
    "Cookie":"_m_h5_tk=2d9665d7e78fda1b9a8fd10d83ee7dae_1600184055474; _m_h5_tk_enc=c88bddaccc92cc08d1fe5cd6705fa365; t=6a34a35cacdc5a6be708028af0e61929; v=0; _tb_token_=75d5837385e7a; cna=N6vnF+aTWCwCAXt3ys/G4A73; xlly_s=1; _samesite_flag_=true; cookie2=10f2ccbc08bfb192a220eca98cb6c84b; sgcookie=E100EFQTcNEqYbdwRaIUdIPSxBonLcYu6XliHYzPlB1xzKHAVExFcA3VYb%2BTeXlz%2Bju%2B2yb4V%2FjfNjradPEhl2I9bw%3D%3D; unb=2337987969; uc3=id2=UUtIEnrHgUwe7g%3D%3D&lg2=VT5L2FSpMGV7TQ%3D%3D&nk2=GcuIY3P8tadb&vt3=F8dCufbCHXd3VGLG6NE%3D; csg=94fa8269; lgc=zcw199604; cookie17=UUtIEnrHgUwe7g%3D%3D; dnk=zcw199604; skt=605a1f105b1ff51d; existShop=MTYwMDE3ODg4NQ%3D%3D; uc4=id4=0%40U2lyiLOWU9zTSTcu8%2F23cABLhKM4&nk4=0%40GwJ9OG3LmeATF%2Bew3Cp8WLxBk%2Bs%3D; tracknick=zcw199604; _cc_=UtASsssmfA%3D%3D; _l_g_=Ug%3D%3D; sg=495; _nk_=zcw199604; cookie1=U%2BTppmiSFKWtYhqUPPpsfzKJKYADRKXtGbl%2FOS%2By3Ww%3D; ubn=p; mt=ci=56_1; thw=cn; ucn=center; enc=hGeVIokKkfAX0%2FWdsC4mNQMIi3fOWKE1kWVhzIxgi1ZIbxFY4zje4L8RT5w%2BhvBDoppxJMVEnN%2BUqRCA6AmfWg%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; uc1=cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&cookie15=WqG3DMC9VAQiUQ%3D%3D&existShop=false&cookie14=Uoe0bUnLwmfmoA%3D%3D&pas=0&cart_m=0&cookie21=W5iHLLyFeYZ1WM9hVnmS; tfstk=cdDVBOMq_Kp2tWw69-wNCkSVFdVAZW0ikTzzifbbjkH5ykFciUQTqnc34r7-ySf..; l=eBgJWMq7OzgwyC-UBO5Clurza77tfIOb4kPzaNbMiInca1zhtFZCnNQ4DMdJSdtfgtCjnetzg7otdRLHR3AGmyLKQQeusLPI3xvO.; isg=BBISy4Spmc203uWxsex2U1oVY9j0Ixa9dyMNG9xqWEWw77LpxLY-zRQBX8tThI5V"
}

resp = requests.get("https://qrlogin.taobao.com/newlogin/qrcode/generate.do?appName=taobao&fromSite=0",headers=headers)
#resp = requests.get("https://cart.taobao.com/trail_mini_cart.htm?callback=MiniCart.setData&t=1600179273370",headers=headers)
print(resp.text)
