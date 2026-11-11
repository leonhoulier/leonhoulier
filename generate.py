from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
p=Path(__file__).parent/'assets'
f=lambda n:ImageFont.truetype(str(p/'instrument-sans-regular.ttf'),n)
im=Image.new('RGB',(1200,560),'#002FA7');d=ImageDraw.Draw(im)
d.text((58,38),'Léon Houlier',font=f(36),fill='#F6F5F2')
for i,line in enumerate(['I build brands, software,','and the systems that','help them grow.']):
 d.text((52,152+i*94),line,font=f(88),fill='#F6F5F2')
d.text((58,494),'leonhoulier.com',font=f(25),fill='#F6F5F2')
d.text((953,494),'Bangalore, India',font=f(25),fill='#F6F5F2')
im.save(p/'hero.png')
s=(p/'signature-original.svg').read_text().replace('<g ', '<rect width="1080" height="540" fill="#F6F5F2"/><g ',1)
(p/'signature.svg').write_text(s)
