"""Builds one luxury sample page per shop.

python3 build/build.py preview   -> build/preview/<slug>.html (full-size images, for checking)
python3 build/build.py           -> <slug>/index.html (images resized by Netlify Image CDN)
"""
import html
import os
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(__file__))
from data import SHOPS, PICKS  # noqa: E402
from data6 import SHOPS6, PICKS6  # noqa: E402
from data7 import SHOPS7, THEMES7, FONTS7, KIND7  # noqa: E402
from data8 import SHOPS8, THEMES8, FONTS8, KIND8  # noqa: E402
SHOPS = {**SHOPS, **SHOPS6, **SHOPS7, **SHOPS8}
PICKS = {**PICKS, **PICKS6, **{k: {'hero': 0, 'posts': [1, 2, 3, 4], 'stories': [5, 6], 'extra': 18} for k in {**SHOPS7, **SHOPS8}}}
ONLY = sys.argv[2:] if len(sys.argv) > 2 else None

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODE = "preview" if len(sys.argv) > 1 and sys.argv[1] == "preview" else "prod"

SENDER = {
    "name": "Bisi Adenipekun",
    "co": "Autonna",
    "email": "bisi@getautonna.com",
    "addr": "155 Willowbrook Blvd, Ste 110 #6926, Wayne, NJ 07470",
}


def img(src, w):
    if MODE == "preview":
        return src
    return "/.netlify/images?url=" + urllib.parse.quote(src, safe="") + f"&w={w}&q=74&fm=webp"


def e(s):
    return html.escape(s, quote=True)


FONTS = {
    "dorsis": "family=Bodoni+Moda:ital,opsz,wght@0,6..96,400;0,6..96,600;1,6..96,400&family=Mulish:wght@400;600",
    "florals": "family=Italiana&family=Manrope:wght@400;600",
    "spa": "family=Gilda+Display&family=Nunito+Sans:opsz,wght@6..12,400;6..12,600",
    "boxing": "family=Anton&family=Archivo:wght@400;600",
    "coffee": "family=Fraunces:ital,opsz,wght,SOFT@0,9..144,400,100;0,9..144,600,100;1,9..144,400,100&family=DM+Sans:opsz,wght@9..40,400;9..40,600",
    "prime": "family=Bebas+Neue&family=Barlow:wght@400;600",
    "labon": "family=Libre+Caslon+Display&family=Karla:wght@400;600",
    "nneka": "family=Playfair+Display:ital,wght@0,400;1,400&family=Jost:wght@400;600",
    "dojo": "family=Oswald:wght@500&family=Source+Sans+3:wght@400;600",
    "fe": "family=Cormorant+Garamond:ital,wght@0,500;1,500&family=Lato:wght@400;700",
    "paw": "family=Fredoka:wght@500;600&family=Nunito:wght@400;700",
    "legrand": "family=Libre+Baskerville:ital@0;1&family=Work+Sans:wght@400;600",
    "yo": "family=Gloock&family=Quicksand:wght@400;600",
    "bb": "family=Marcellus&family=Jost:wght@400;600",
    "nabod": "family=Cinzel:wght@500&family=Montserrat:wght@400;600",
}

BASE_CSS = """
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:400 17px/1.65 var(--body);-webkit-font-smoothing:antialiased}
img{display:block;max-width:100%}
a{color:inherit}
:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
.bar{display:flex;justify-content:space-between;gap:16px;padding:18px clamp(20px,5vw,64px);font-size:14px;color:var(--muted)}
.bar strong{font-weight:600;color:var(--ink)}
.wrap{max-width:1240px;margin:0 auto;padding:0 clamp(20px,5vw,64px)}
.intro{max-width:760px;margin:0 auto;padding:clamp(56px,9vw,112px) clamp(20px,5vw,64px) 24px;text-align:center}
.intro .lead{font:400 clamp(22px,2.6vw,30px)/1.4 var(--display);margin:0}
.made{display:inline-block;text-align:left;font-size:15px;color:var(--muted);max-width:640px}
.made summary{cursor:pointer;color:var(--ink);font-weight:600;list-style-position:inside}
.made p{margin:10px 0 0}
.set{padding:clamp(48px,7vw,96px) 0 0}
.set-head{display:flex;align-items:baseline;justify-content:space-between;gap:24px;flex-wrap:wrap;margin-bottom:22px;padding-bottom:14px;border-bottom:1px solid var(--line)}
.set-head h2{margin:0;font:400 clamp(28px,3.4vw,44px)/1.1 var(--display)}
.set-head p{margin:0;color:var(--muted);font-size:15px}
.grid{display:grid;gap:var(--gap)}
.grid.p{grid-template-columns:repeat(4,1fr)}
.grid.p figure:first-child{grid-column:span 2;grid-row:span 2}
.grid.p.flip figure:first-child{grid-column:3 / span 2;grid-row:1 / span 2}
.grid.s{grid-template-columns:repeat(5,1fr)}
.grid.four{grid-template-columns:repeat(4,1fr)}
.grid.trio{grid-template-columns:repeat(3,1fr);align-items:stretch;max-width:960px;margin:0 auto}
.more{display:flex;flex-direction:column;justify-content:center;padding:clamp(24px,3vw,40px);border:1px solid var(--line);border-radius:var(--radius);background:var(--soft)}
.more-n{margin:0 0 12px;font:400 clamp(40px,4.5vw,64px)/1 var(--display);color:var(--accent)}
.more p:last-child{margin:0;color:var(--muted)}
figure{margin:0}
.shot{all:unset;display:block;width:100%;cursor:zoom-in;position:relative;overflow:hidden;border-radius:var(--radius);background:var(--soft)}
.shot:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
.shot img{width:100%;height:100%;object-fit:cover;aspect-ratio:4/5}
.grid.s .shot img,.grid.trio .shot img{aspect-ratio:9/16}
.grid.p figure:first-child .shot,.grid.p figure:first-child .shot img{height:100%}
.grid.p figure:first-child{display:flex;flex-direction:column}
.grid.p figure:first-child .shot{flex:1}
figcaption{padding:10px 2px 0;font-size:14px;color:var(--muted)}
.offer{margin:clamp(72px,10vw,140px) auto 0;padding:clamp(48px,7vw,88px) clamp(20px,5vw,64px);text-align:center;background:var(--panel);color:var(--panel-ink)}
.offer h2{margin:0 0 18px;font:400 clamp(32px,4.4vw,58px)/1.08 var(--display)}
.offer p{max-width:600px;margin:0 auto 14px}
.price{display:flex;justify-content:center;gap:clamp(24px,6vw,72px);margin:34px 0 36px;flex-wrap:wrap}
.price div{min-width:140px}
.price b{display:block;font:400 clamp(30px,3.4vw,42px)/1 var(--display)}
.price span{font-size:14px;opacity:.75}
.cta{display:inline-block;padding:16px 30px;background:var(--cta);color:var(--cta-ink);text-decoration:none;font-weight:600;border-radius:var(--btn-radius)}
.cta:hover{filter:brightness(1.08)}
.offer .small{font-size:14px;opacity:.75;margin-top:16px}
footer{padding:48px clamp(20px,5vw,64px) 64px;text-align:center;font-size:13px;line-height:1.8;color:var(--muted)}
dialog{border:0;padding:0;background:transparent;max-width:min(92vw,1100px);max-height:94vh}
dialog::backdrop{background:rgba(0,0,0,.86)}
dialog img{max-height:84vh;width:auto;margin:0 auto;border-radius:4px}
dialog .lb-bar{display:flex;justify-content:space-between;align-items:center;gap:16px;padding:12px 2px 0;color:#fff;font:400 15px/1.4 var(--body)}
dialog button{font:600 14px var(--body);background:#fff;color:#000;border:0;border-radius:999px;padding:9px 18px;cursor:pointer}
@media (max-width:820px){
 .grid.p{grid-template-columns:repeat(2,1fr)}
 .grid.p figure:first-child,.grid.p.flip figure:first-child{grid-column:1 / span 2;grid-row:auto}
 .grid.s{grid-template-columns:repeat(2,1fr)}
 .grid.four{grid-template-columns:repeat(2,1fr)}
 .grid.trio{grid-template-columns:repeat(2,1fr)}
 .more{grid-column:1 / span 2}
}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
"""

THEME_CSS = {
    "dorsis": """
:root{--bg:#F2E8D8;--ink:#2A1517;--muted:#6E5A55;--accent:#5B1621;--gilt:#B08D57;--soft:#E6D8C2;--line:#D7C4A8;
--panel:#5B1621;--panel-ink:#F2E8D8;--cta:#B08D57;--cta-ink:#2A1517;--display:'Bodoni Moda',Didot,serif;--body:'Mulish',system-ui,sans-serif;--gap:14px;--radius:2px;--btn-radius:2px}
.bar{background:var(--accent);color:#E7D3BE}.bar strong{color:#F2E8D8}
.hero{display:grid;grid-template-columns:1fr 1.05fr;min-height:min(92vh,860px);background:var(--accent);color:#F2E8D8}
.hero .copy{display:flex;flex-direction:column;justify-content:center;padding:clamp(40px,6vw,96px)}
.hero h1{margin:0;font:400 clamp(64px,9.5vw,148px)/.92 var(--display);letter-spacing:-.01em}
.hero .line{margin:26px 0 0;font:italic 400 clamp(22px,2.4vw,32px)/1.3 var(--display);color:#DCC08F}
.hero .place{margin-top:40px;font-size:15px;color:#E7D3BE}
.hero .frame{position:relative;padding:clamp(20px,3vw,40px)}
.hero .frame img{width:100%;height:100%;object-fit:cover}
.hero .frame::after{content:"";position:absolute;inset:calc(clamp(20px,3vw,40px) + 14px);border:1px solid rgba(220,192,143,.8);pointer-events:none}
.shot{outline:1px solid var(--line);outline-offset:5px}
figcaption{font:italic 400 16px/1.4 var(--display);color:var(--ink);text-align:center;padding-top:14px}
@media (max-width:820px){.hero{grid-template-columns:1fr}.hero .frame{height:110vw}}
""",
    "florals": """
:root{--bg:#160F10;--ink:#F3E6E2;--muted:#B9A3A0;--accent:#EBC8C4;--soft:#24191A;--line:#3A2A2B;
--panel:#EBC8C4;--panel-ink:#3B0D17;--cta:#5E0F1E;--cta-ink:#F7E9E6;--display:'Italiana',Didot,serif;--body:'Manrope',system-ui,sans-serif;--gap:10px;--radius:0;--btn-radius:0}
.hero{position:relative;display:grid;grid-template-columns:44% 56%;min-height:min(94vh,900px);overflow:hidden}
.hero .copy{position:relative;z-index:2;display:flex;flex-direction:column;justify-content:center;padding:clamp(32px,5vw,80px)}
.hero h1{margin:0;font:400 clamp(64px,9vw,150px)/.9 var(--display);margin-right:-30%;color:#F7E9E6}
.hero .line{margin:30px 0 0;max-width:30ch;color:var(--muted)}
.hero .place{margin-top:12px;color:var(--accent);font-size:15px}
.hero .pic img{width:100%;height:100%;object-fit:cover}
.hero .pic{position:relative}
.hero .pic::before{content:"";position:absolute;inset:0;background:linear-gradient(90deg,#160F10 0%,rgba(22,15,16,0) 38%)}
.set-head h2{font-size:clamp(34px,4.2vw,58px)}
figcaption{letter-spacing:.01em}
.offer h2{font-size:clamp(40px,5.6vw,76px)}
@media (max-width:820px){.hero{grid-template-columns:1fr}.hero .pic{height:110vw;order:-1}.hero .pic::before{background:linear-gradient(0deg,#160F10 0%,rgba(22,15,16,0) 45%)}.hero h1{margin-right:0}.hero .copy{margin-top:-28vw}}
""",
    "spa": """
:root{--bg:#FBF7F4;--ink:#3D1E3B;--muted:#7C6479;--accent:#7A4A7A;--soft:#EFE6F2;--line:#E7DCE8;
--panel:#3D1E3B;--panel-ink:#F6EEF6;--cta:#E4D2EC;--cta-ink:#3D1E3B;--display:'Gilda Display',Georgia,serif;--body:'Nunito Sans',system-ui,sans-serif;--gap:18px;--radius:22px;--btn-radius:999px}
.hero{text-align:center;padding:clamp(40px,6vw,80px) clamp(20px,5vw,64px) 0;background:linear-gradient(#FBF7F4,#F1E8F3)}
.hero h1{margin:0 auto;max-width:12ch;font:400 clamp(54px,8vw,120px)/.98 var(--display)}
.hero .line{margin:18px auto 0;max-width:60ch;color:var(--muted)}
.hero .arch{width:min(520px,82vw);margin:clamp(36px,5vw,56px) auto 0;border-radius:999px 999px 0 0;overflow:hidden;aspect-ratio:4/5;box-shadow:0 30px 80px -40px rgba(61,30,59,.45)}
.hero .arch img{width:100%;height:100%;object-fit:cover}
figcaption{text-align:center}
.set-head{border-bottom:0;justify-content:center;text-align:center;flex-direction:column;align-items:center;gap:6px}
.offer{border-radius:clamp(28px,4vw,48px);max-width:1112px;margin-left:clamp(12px,3vw,64px);margin-right:clamp(12px,3vw,64px)}
@media (min-width:1240px){.offer{margin-left:auto;margin-right:auto}}
""",
    "boxing": """
:root{--bg:#000;--ink:#EDEAE4;--muted:#A8A39B;--accent:#C8102E;--soft:#141414;--line:#262626;
--panel:#C8102E;--panel-ink:#fff;--cta:#fff;--cta-ink:#000;--display:'Anton',Impact,sans-serif;--body:'Archivo',system-ui,sans-serif;--gap:4px;--radius:0;--btn-radius:0}
.ropes{height:18px;background:linear-gradient(#C8102E 0 33%,#EDEAE4 33% 66%,#1E3A8A 66%)}
.ropes.thin{height:9px;margin-top:clamp(48px,7vw,96px)}
.hero{position:relative;min-height:min(96vh,940px);display:flex;align-items:flex-end;overflow:hidden}
.hero img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 30%;filter:grayscale(.15) contrast(1.05)}
.hero::after{content:"";position:absolute;inset:0;background:linear-gradient(0deg,#000 4%,rgba(0,0,0,.25) 60%,rgba(0,0,0,.55))}
.hero .copy{position:relative;z-index:2;padding:clamp(28px,5vw,72px)}
.hero h1{margin:0;font:400 clamp(60px,10vw,168px)/.95 var(--display);text-transform:uppercase;max-width:9ch}
.hero .line{margin:22px 0 0;color:#D8D3CB;max-width:44ch}
.hero .place{color:#fff;font-weight:600;margin-top:8px}
.set-head{border-bottom:0}
.set-head h2{text-transform:uppercase;font-size:clamp(38px,5vw,72px);letter-spacing:.01em}
.shot img{filter:contrast(1.03)}
figcaption{padding:8px 0 4px;font-size:13px}
.intro .lead{font:400 clamp(26px,3vw,40px)/1.15 var(--display);text-transform:uppercase}
.offer h2{text-transform:uppercase;font-size:clamp(44px,6.5vw,96px)}
.offer{margin-top:0}
.price b{font-size:clamp(40px,4.6vw,64px)}
""",
    "coffee": """
:root{--bg:#1C110B;--ink:#F1E3CC;--muted:#BCA88E;--accent:#E8973A;--soft:#2A1A11;--line:#3A281B;
--panel:#E8973A;--panel-ink:#1C110B;--cta:#1C110B;--cta-ink:#F1E3CC;--display:'Fraunces',Georgia,serif;--body:'DM Sans',system-ui,sans-serif;--gap:14px;--radius:6px;--btn-radius:999px}
.hero{display:grid;grid-template-columns:1fr 1fr;align-items:center;gap:clamp(24px,4vw,64px);padding:clamp(40px,6vw,88px) clamp(20px,5vw,64px);min-height:min(90vh,860px);max-width:1360px;margin:0 auto}
.hero h1{margin:0;font:400 clamp(52px,7vw,108px)/.98 var(--display);font-variation-settings:"SOFT" 100}
.hero h1 em{display:block;font-style:italic;color:var(--accent)}
.hero .line{margin:26px 0 0;color:var(--muted);max-width:40ch}
.hero .place{margin-top:10px;color:var(--ink);font-weight:600}
.turntable{position:relative;aspect-ratio:1;width:100%;max-width:620px;justify-self:center}
.record{position:absolute;top:4%;right:0;width:86%;aspect-ratio:1;border-radius:50%;
background:radial-gradient(circle,#E8973A 0 15%,#1a1a1a 15.4% 16.5%,transparent 16.6%),repeating-radial-gradient(circle,#0d0d0d 0 1.6px,#1c1c1c 1.6px 3.2px);
box-shadow:0 30px 70px -30px #000;animation:spin 9s linear infinite}
.record::after{content:"";position:absolute;inset:0;border-radius:50%;background:conic-gradient(from 30deg,transparent 0 40deg,rgba(255,255,255,.08) 60deg,transparent 80deg 220deg,rgba(255,255,255,.06) 240deg,transparent 260deg)}
.sleeve{position:absolute;left:0;bottom:0;width:62%;aspect-ratio:4/5;overflow:hidden;border-radius:4px;box-shadow:0 30px 60px -24px #000}
.sleeve img{width:100%;height:100%;object-fit:cover}
@keyframes spin{to{transform:rotate(360deg)}}
.set-head h2{font-style:italic}
.offer{border-radius:0}
@media (max-width:820px){.hero{grid-template-columns:1fr}.turntable{max-width:440px}}
""",
}


GENERIC = """
.hero.full{position:relative;min-height:min(94vh,900px);display:flex;align-items:flex-end;overflow:hidden;background:#000}
.hero.full>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 35%}
.hero.full::after{content:"";position:absolute;inset:0;background:linear-gradient(0deg,var(--bg) 3%,rgba(0,0,0,.2) 55%,rgba(0,0,0,.5))}
.hero.full .copy{position:relative;z-index:2;padding:clamp(28px,5vw,72px);max-width:1100px}
.hero.split{display:grid;grid-template-columns:1fr 1fr;align-items:center;gap:clamp(24px,5vw,80px);padding:clamp(32px,5vw,80px) clamp(20px,5vw,64px);max-width:1360px;margin:0 auto;min-height:min(90vh,860px)}
.hero.split .pic{position:relative}
.hero.split .pic img{width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:var(--radius)}
.hero.arch{text-align:center;padding:clamp(40px,6vw,80px) clamp(20px,5vw,64px) 0}
.hero.arch .pic{width:min(500px,82vw);margin:clamp(32px,5vw,56px) auto 0;border-radius:var(--arch);overflow:hidden;aspect-ratio:4/5}
.hero.arch .pic img{width:100%;height:100%;object-fit:cover}
.hero h1{margin:0;font:400 var(--h1)/1 var(--display)}
.hero .line{margin:22px 0 0;color:var(--muted);max-width:44ch}
.hero.arch .line{margin-left:auto;margin-right:auto}
.hero .place{margin-top:8px;font-weight:600}
@media (max-width:820px){.hero.split{grid-template-columns:1fr}.hero.split .pic{order:-1}}
"""

THEME_CSS.update({
 "prime": """:root{--bg:#0B0B0B;--ink:#F2F2F2;--muted:#A9A9A9;--accent:#FF6A13;--soft:#161616;--line:#2A2A2A;--panel:#FF6A13;--panel-ink:#0B0B0B;--cta:#0B0B0B;--cta-ink:#fff;
--display:'Bebas Neue',Impact,sans-serif;--body:'Barlow',system-ui,sans-serif;--gap:6px;--radius:0;--btn-radius:0;--h1:clamp(72px,12vw,200px)}
.hero h1{font-style:italic;line-height:.9}.hero .place{color:var(--accent)}.set-head h2{font-size:clamp(40px,5vw,76px)}.offer h2{font-size:clamp(48px,7vw,110px)}
.set-head{border-bottom:3px solid var(--accent)}""",
 "labon": """:root{--bg:#F7F0E6;--ink:#43271C;--muted:#7D6455;--accent:#B3262E;--soft:#EDE2D2;--line:#DCCBB4;--panel:#43271C;--panel-ink:#F7F0E6;--cta:#B3262E;--cta-ink:#fff;
--display:'Libre Caslon Display',Georgia,serif;--body:'Karla',system-ui,sans-serif;--gap:16px;--radius:4px;--btn-radius:999px;--h1:clamp(52px,6.4vw,96px)}
.hero.split .pic::after{content:"";position:absolute;inset:-14px 14px 14px -14px;border:1px solid var(--accent);z-index:-1}
.hero .place{color:var(--accent)}""",
 "nneka": """:root{--bg:#FBEEF0;--ink:#5A1730;--muted:#8E5B6B;--accent:#B88A3E;--soft:#F5DDE2;--line:#EBCBD2;--panel:#5A1730;--panel-ink:#FBEEF0;--cta:#E8C77F;--cta-ink:#3B0E1F;
--display:'Playfair Display',Georgia,serif;--body:'Jost',system-ui,sans-serif;--gap:16px;--radius:18px;--btn-radius:999px;--h1:clamp(50px,7vw,104px);--arch:50%}
.hero h1{font-style:italic}.hero.arch .pic{border:6px solid #fff;box-shadow:0 0 0 1px var(--accent),0 30px 70px -40px rgba(90,23,48,.5)}""",
 "dojo": """:root{--bg:#0A0A0A;--ink:#F4F1EC;--muted:#A6A19A;--accent:#D21F26;--soft:#161616;--line:#2B2B2B;--panel:#F4F1EC;--panel-ink:#0A0A0A;--cta:#D21F26;--cta-ink:#fff;
--display:'Oswald',Impact,sans-serif;--body:'Source Sans 3',system-ui,sans-serif;--gap:6px;--radius:0;--btn-radius:0;--h1:clamp(56px,9vw,150px)}
.hero h1{text-transform:uppercase;line-height:.95}.hero .copy{border-left:10px solid var(--accent);padding-left:clamp(24px,4vw,56px)}
.set-head h2{text-transform:uppercase}.offer h2{text-transform:uppercase}""",
 "fe": """:root{--bg:#EEF2EA;--ink:#2E3A2B;--muted:#62705D;--accent:#D9692A;--soft:#E1E8DB;--line:#CFD9C8;--panel:#2E3A2B;--panel-ink:#EEF2EA;--cta:#D9692A;--cta-ink:#fff;
--display:'Cormorant Garamond',Georgia,serif;--body:'Lato',system-ui,sans-serif;--gap:14px;--radius:999px 999px 8px 8px;--btn-radius:999px;--h1:clamp(52px,6.6vw,100px)}
.hero h1{font-style:italic;color:var(--accent)}.shot{border-radius:8px}.hero.split .pic img{border-radius:999px 999px 8px 8px}""",
 "paw": """:root{--bg:#FFFBEA;--ink:#1F2A12;--muted:#55603F;--accent:#6FAE1F;--soft:#F1F6DD;--line:#E2EBC4;--panel:#8DC63F;--panel-ink:#1F2A12;--cta:#FFC72C;--cta-ink:#1F2A12;
--display:'Fredoka',system-ui,sans-serif;--body:'Nunito',system-ui,sans-serif;--gap:16px;--radius:24px;--btn-radius:999px;--h1:clamp(46px,6.4vw,92px);--arch:50%}
.hero.arch{background:radial-gradient(circle at 50% 100%,#DDF0B8 0 40%,transparent 41%)}.hero h1{max-width:16ch;margin:0 auto}
.hero.arch .pic{border:10px solid #FFC72C}""",
 "legrand": """:root{--bg:#F3E9DC;--ink:#3B2416;--muted:#76604F;--accent:#8B5A2B;--soft:#E9DBC8;--line:#D9C6AE;--panel:#3B2416;--panel-ink:#F3E9DC;--cta:#C89B5E;--cta-ink:#2A180D;
--display:'Libre Baskerville',Georgia,serif;--body:'Work Sans',system-ui,sans-serif;--gap:14px;--radius:3px;--btn-radius:3px;--h1:clamp(44px,5.6vw,84px)}
.hero.split .pic img{box-shadow:24px 24px 0 var(--soft)}.hero .place{color:var(--accent)}""",
 "yo": """:root{--bg:#FAF7F0;--ink:#2F4A35;--muted:#6B7D6E;--accent:#7FA285;--soft:#EEF1E8;--line:#DDE4D6;--panel:#2F4A35;--panel-ink:#FAF7F0;--cta:#E9C9C6;--cta-ink:#2F4A35;
--display:'Gloock',Georgia,serif;--body:'Quicksand',system-ui,sans-serif;--gap:16px;--radius:12px;--btn-radius:999px;--h1:clamp(56px,8vw,124px);--arch:999px 999px 12px 12px}""",
 "bb": """:root{--bg:#F6F0E8;--ink:#3A2A20;--muted:#7A6A5D;--accent:#B08D57;--soft:#EDE4D8;--line:#DED1BF;--panel:#3A2A20;--panel-ink:#F6F0E8;--cta:#B08D57;--cta-ink:#fff;
--display:'Marcellus',Georgia,serif;--body:'Jost',system-ui,sans-serif;--gap:14px;--radius:2px;--btn-radius:2px;--h1:clamp(44px,5.4vw,80px)}
.hero.split .pic{padding:14px;border:1px solid var(--accent)}""",
 "nabod": """:root{--bg:#070707;--ink:#EDE3CF;--muted:#A89C86;--accent:#C9A45C;--soft:#141210;--line:#2C261C;--panel:#141210;--panel-ink:#EDE3CF;--cta:#C9A45C;--cta-ink:#070707;
--display:'Cinzel',Georgia,serif;--body:'Montserrat',system-ui,sans-serif;--gap:10px;--radius:0;--btn-radius:0;--h1:clamp(44px,6.4vw,100px)}
.hero h1{color:var(--accent)}.shot{outline:1px solid var(--line)}.offer{border-top:1px solid var(--accent);border-bottom:1px solid var(--accent)}""",
})
THEME_CSS.update(THEMES7)
THEME_CSS.update(THEMES8)
FONTS.update(FONTS7)
FONTS.update(FONTS8)
KIND = {**KIND7, **KIND8, "prime": "full", "dojo": "full", "nabod": "full", "labon": "split", "fe": "split", "legrand": "split", "bb": "split",
        "nneka": "arch", "paw": "arch", "yo": "arch"}


def hero(shop, s):
    t = s["theme"]
    h = s["sections"]
    hi = PICKS[shop]["hero"]
    first = [it for sec in h for it in sec[3]][hi]
    src = img(first["src"], 1600)
    alt = e(first["alt"])
    name, line, place = e(s["name"]), e(s["hero_line"]), e(s["place"])
    if t in KIND:
        k = KIND[t]
        copy = f'<div class="copy"><h1>{line}</h1><p class="line">Social images made for {name}.</p><p class="place">{place}</p></div>'
        if k == "full":
            return f'<section class="hero full"><img src="{src}" alt="{alt}" fetchpriority="high">{copy}</section>'
        if k == "split":
            return f'<section class="hero split">{copy}<div class="pic"><img src="{src}" alt="{alt}" fetchpriority="high"></div></section>'
        return (f'<section class="hero arch"><h1>{line}</h1><p class="line">Social images made for {name}, {place}.</p>'
                f'<div class="pic"><img src="{src}" alt="{alt}" fetchpriority="high"></div></section>')
    if t == "dorsis":
        return f'''<section class="hero"><div class="copy"><h1>D'Orsi's</h1><p class="line">{line}</p>
<p class="place">Social images made for {name} in {place}</p></div>
<div class="frame"><img src="{src}" alt="{alt}" fetchpriority="high"></div></section>'''
    if t == "florals":
        return f'''<section class="hero"><div class="copy"><h1>{line}</h1>
<p class="line">Social images of your bouquets, made for {name}.</p><p class="place">{place}</p></div>
<div class="pic"><img src="{src}" alt="{alt}" fetchpriority="high"></div></section>'''
    if t == "spa":
        return f'''<section class="hero"><h1>{line}</h1>
<p class="line">Social images made for {name}, {place}.</p>
<div class="arch"><img src="{src}" alt="{alt}" fetchpriority="high"></div></section>'''
    if t == "boxing":
        return f'''<section class="hero"><img src="{src}" alt="{alt}" fetchpriority="high"><div class="copy"><h1>{line}</h1>
<p class="line">Social images made for {name}.</p><p class="place">{place}</p></div></section><div class="ropes"></div>'''
    if t == "coffee":
        return f'''<section class="hero"><div><h1>Good Coffee. <em>Good Music.</em> Good Company.</h1>
<p class="line">Social images made for {name}, from your menu and your record-badge logo.</p><p class="place">{place}</p></div>
<div class="turntable" aria-hidden="false"><div class="record" aria-hidden="true"></div><div class="sleeve"><img src="{src}" alt="{alt}" fetchpriority="high"></div></div></section>'''


def page(slug, s):
    t = s["theme"]
    pk = PICKS[slug]
    allit = [it for sec in s["sections"] for it in sec[3]]
    flat = lambda i: allit[i]
    def fig(it, kind):
        return (f'<figure><button class="shot" type="button" data-full="{e(img(it["src"], 1800))}" data-cap="{e(it["cap"])}">'
                f'<img loading="lazy" decoding="async" src="{e(img(it["src"], 900 if kind == "p" else 700))}" alt="{e(it["alt"])}"></button>'
                f'<figcaption>{e(it["cap"])}</figcaption></figure>')
    posts = "".join(fig(flat(i), "p") for i in pk["posts"])
    stories = "".join(fig(flat(i), "s") for i in pk["stories"])
    extra = pk.get("extra", 25 - 1 - len(pk["posts"]) - len(pk["stories"]))
    teaser = (f'<div class="more"><p class="more-n">{extra} more</p><p>Banners, story covers and product shots for your holiday posts are ready.'
              f' Reply to our email and we\'ll send them, with a free 30-second video.</p></div>')
    rope = '<div class="ropes thin"></div>' if t == "boxing" else ""
    sets = [f'<section class="set wrap"><div class="set-head"><h2>Feed posts</h2><p>Ready to post, with your own words on them.</p></div>'
            f'<div class="grid four">{posts}</div></section>',
            f'{rope}<section class="set wrap"><div class="set-head"><h2>Story covers</h2><p>Vertical, for Instagram and Facebook Stories.</p></div>'
            f'<div class="grid trio">{stories}{teaser}</div></section>']
    subj = urllib.parse.quote(f"{s['short']} - free video")
    boxing_rope = '<div class="ropes thin"></div>' if t == "boxing" else ""
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Made for {e(s["name"])} by Autonna Studio</title>
<meta name="description" content="Sample social images made for {e(s["name"])}, {e(s["place"])}. Free to keep.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?{FONTS[t]}&display=swap" rel="stylesheet">
<style>{BASE_CSS}{GENERIC if t in KIND else ""}{THEME_CSS[t]}</style>
</head>
<body>
<header class="bar"><span><strong>Autonna Studio</strong></span><span>Made for {e(s["name"])}</span></header>
{hero(slug, s)}
<section class="intro"><p class="lead">{e(s["intro"])}</p>
</section>
<main>{"".join(sets)}</main>
{boxing_rope}<section class="offer">
<h2>Want a short video too?</h2>
<p>We'll make {e(s["short"])} one 30-second video for Instagram and Facebook, free. If you like it, pay what you think it's worth.</p>
<a class="cta" href="mailto:{SENDER["email"]}?subject={subj}">Email Bisi about a free video</a>
<p class="small">{SENDER["email"]}. Want the full-size files, or the other images? Just ask.</p>
</section>
<footer>{SENDER["name"]}, {SENDER["co"]}<br>{SENDER["addr"]}<br>
Sample images made for {e(s["name"])}. Autonna is not affiliated with {e(s["name"])}.<br>
Don't want to hear from us? Reply "no thanks" to our email and we won't contact you again.</footer>
<dialog id="lb" aria-label="Image viewer"><img alt=""><div class="lb-bar"><span></span><button type="button">Close</button></div></dialog>
<script>
(()=>{{const d=document.getElementById('lb'),im=d.querySelector('img'),cap=d.querySelector('span');
document.querySelectorAll('.shot').forEach(b=>b.addEventListener('click',()=>{{im.src=b.dataset.full;im.alt=b.querySelector('img').alt;cap.textContent=b.dataset.cap;d.showModal();}}));
d.querySelector('button').addEventListener('click',()=>d.close());
d.addEventListener('click',ev=>{{if(ev.target===d)d.close();}});}})();
</script>
</body>
</html>
'''


def main():
    for slug, s in SHOPS.items():
        if ONLY and slug not in ONLY:
            continue
        if MODE == "preview":
            out = os.path.join(ROOT, "build", "preview", f"{slug}.html")
        else:
            out = os.path.join(ROOT, slug, "index.html")
        os.makedirs(os.path.dirname(out), exist_ok=True)
        open(out, "w").write(page(slug, s))
        print("wrote", out)


if __name__ == "__main__":
    main()
