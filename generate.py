from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
p=Path(__file__).parent/'assets';(p/'buttons').mkdir(exist_ok=True)
f=lambda n:ImageFont.truetype(str(p/'instrument-sans-regular.ttf'),n)
blue='#002FA7';paper='#F6F5F2';ink='#08090B'
im=Image.new('RGB',(1200,450),blue);d=ImageDraw.Draw(im)
d.text((56,30),'Léon Houlier',font=f(34),fill=paper)
d.text((927,38),'Bangalore, India',font=f(25),fill=paper)
for i,line in enumerate(['I build brands, software,','and the systems that','help them grow.']):d.text((52,114+i*93),line,font=f(88),fill=paper)
im.save(p/'hero.png')
buttons=[('website','Visit my website',176,44,True),('projects','Projects',126,44,False),('writing','Writing',110,44,False),('linkedin','LinkedIn',128,44,False),('agency','Explore the agency',196,44,True),('report','Read the report',166,40,False),('contact','Get in touch',154,44,True)]
for slug,label,w,h,primary in buttons:
 im=Image.new('RGB',(w*2,h*2),blue if primary else paper);d=ImageDraw.Draw(im)
 if not primary:d.rectangle((0,0,w*2-1,h*2-1),outline='#B9BEC7',width=2)
 c=paper if primary else ink
 d.text((24,(h*2-31)/2-4),label,font=f(29),fill=c)
 # Consistent external arrow, independent of font glyph support.
 x=w*2-32;y=h-7;d.line((x-8,y+14,x+6,y),fill=c,width=2);d.line((x-5,y,x+6,y,x+6,y+11),fill=c,width=2)
 im.save(p/'buttons'/f'{slug}.png')
