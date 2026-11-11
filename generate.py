from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math
P=Path(__file__).parent/'assets'
P.mkdir(exist_ok=True)
B='#002FA7'; L='#D7FF57'; W='#F6F5F0'; K='#0C1221'
def font(n,bold=False): return ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Bold.ttf' if bold else '/System/Library/Fonts/Supplemental/Arial.ttf',n)
def text(d,xy,s,n=24,c=W,b=False): d.text(xy,s,font=font(n,b),fill=c)
frames=[]
for f in range(48):
 im=Image.new('RGB',(1200,480),B); d=ImageDraw.Draw(im)
 for x in range(0,1200,40):d.line((x,0,x,480),fill='#123EAF')
 for y in range(0,480,40):d.line((0,y,1200,y),fill='#123EAF')
 text(d,(42,28),'LÉON HOULIER',22,W,True);text(d,(864,28),'BANGALORE / INDIA',22,L,True)
 text(d,(38,100),'MARKETING',89,W,True)
 text(d,(38,195),'WITH A',89,W,True)
 text(d,(38,290),'TERMINAL.',89,L,True)
 d.rounded_rectangle((758,104,1158,395),radius=13,fill=K,outline='#5973A8',width=2)
 for i,c in enumerate(['#FF825D','#F7CF61',L]):d.ellipse((779+i*22,123,789+i*22,133),fill=c)
 text(d,(780,158),'$ leon --build',24,L)
 lines=['paid media + measurement','MCP tools + Mac apps','The Detail Department']
 for i,line in enumerate(lines):
  text(d,(780,207+i*42),'> '+line[:min(len(line),max(0,f*2-i*10))],21,W)
 # A continuous signal moves through three labelled nodes, without flashing.
 d.line((782,363,1125,363),fill='#496182',width=2)
 for x in [782,953,1125]:d.ellipse((x-4,359,x+4,367),fill=L)
 x=782+343*(f/47);d.ellipse((x-7,356,x+7,370),fill=L)
 text(d,(42,430),'PAID MEDIA  /  SOFTWARE  /  A VERY PARTICULAR AGENCY',20,W)
 frames.append(im)
frames[-1].save(P/'hero.png')
frames[0].save(P/'hero.gif',save_all=True,append_images=frames[1:],duration=90,loop=0,optimize=True)
im=Image.new('RGB',(1200,220),K);d=ImageDraw.Draw(im)
d.rectangle((0,0,14,220),fill=L)
text(d,(44,24),'THE DETAIL DEPARTMENT',49,W,True)
text(d,(46,96),'THE EXECUTION AGENCY FOR LUXURY BRANDS.',25,L,True)
text(d,(46,155),'Campaign operations. Measurement. Websites. AI implementation.',23,W)
im.save(P/'department.png')
print([(p.name,p.stat().st_size) for p in P.iterdir()])
