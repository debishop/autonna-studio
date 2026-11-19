"""Generate data8.py for wave 2 from sprint/w2 specs + urls."""
import json, re, sys, unicodedata
sys.path.insert(0, '/home/claude/sprint/w2')
exec(open('/home/claude/sprint/w2/specs.py').read())
U = {int(l.split()[0]): l.split()[1] for l in open('/home/claude/sprint/w2/urls.txt')}
B = 'https://d8j0ntlcm91z4.cloudfront.net/user_3Esk8OYU2FjG0AiTaNIrZKS91Pk/hf_'

META = {
 'e-e-flowers': ('E&E Flowers', 'E&E Flowers', 'Edison, NJ', 'eandeflowers@gmail.com', 'Weddings, birthdays, balloons & fruit baskets.', 'eeflowers', 'split',
   ('#FBF8F5', '#2F3A2F', '#B96A7B', '#F4E9EC', '#E8DCDF', '#2F3A2F', '#fff', 'family=Cormorant+Garamond:wght@600&family=Jost:wght@400;600', 'Cormorant Garamond', 'Jost')),
 'juice-hub': ('Juice Hub', 'Juice Hub', 'Rahway, NJ', 'info@juicehubnj.com', 'Cold-pressed juices, smoothies & acai bowls.', 'juicehub', 'arch',
   ('#FFFBF2', '#1F3B1F', '#F07B12', '#FFF0DA', '#F6E2C2', '#2E7D32', '#fff', 'family=Shrikhand&family=Nunito:wght@400;700', 'Shrikhand', 'Nunito')),
 'soul-bowls': ('Soul Bowls', 'Soul Bowls', 'Metuchen, NJ', 'soulbowlsnj@gmail.com', 'Acai bowls, smoothies & Soul Brew.', 'soulbowls', 'split',
   ('#F8F4EE', '#3A2340', '#6B3A78', '#EFE5EF', '#E3D5E3', '#5C7D3A', '#fff', 'family=Fraunces:wght@600&family=Karla:wght@400;700', 'Fraunces', 'Karla')),
 'nj-dog-barbers': ('NJ Dog Barbers', 'NJ Dog Barbers', 'Sayreville, NJ', 'njdogbarbers@gmail.com', 'Baths, haircuts, nails & de-shedding.', 'dogbarbers', 'full',
   ('#F6F7FB', '#14213D', '#C1272D', '#E8ECF5', '#D3DAE9', '#C1272D', '#fff', 'family=Alfa+Slab+One&family=Barlow:wght@400;600', 'Alfa Slab One', 'Barlow')),
 'house-of-flowers': ('House of Flowers', 'House of Flowers', 'Linden, NJ', 'houseofflowersnj@gmail.com', 'Roses and fresh arrangements, delivered.', 'hof', 'split',
   ('#FBF5F3', '#3B1016', '#A3142B', '#F6E3E5', '#EBCFD3', '#A3142B', '#fff', 'family=Playfair+Display:wght@600&family=Lato:wght@400;700', 'Playfair Display', 'Lato')),
 'cindys-flowers': ("Cindy's Flowers & Gift Shop", "Cindy's Flowers", 'Colonia, NJ', 'contact_us@cindys-flowers.com', 'Wreaths, custom arrangements & gifts.', 'cindys', 'arch',
   ('#F9F8F3', '#2F3A2B', '#7A6A9B', '#EEEBF3', '#DEDAE6', '#5E7A55', '#fff', 'family=Libre+Caslon+Display&family=Lato:wght@400;700', 'Libre Caslon Display', 'Lato')),
 'torres-cafe': ('Torres Cafe', 'Torres Cafe', 'Perth Amboy, NJ', 'torrescafepr@gmail.com', 'Puerto Rican home cooking.', 'torres', 'full',
   ('#FFF8EC', '#3A1F12', '#C2541E', '#FBE9CF', '#F1D6AE', '#2F6B2F', '#fff', 'family=Abril+Fatface&family=Karla:wght@400;700', 'Abril Fatface', 'Karla')),
 'pampered-paws': ('Pampered Paws', 'Pampered Paws', 'Rahway, NJ', 'dellspamperedpaws@gmail.com', 'Grooming for dogs and cats.', 'pampered', 'arch',
   ('#F7FAFD', '#22324A', '#D46A92', '#EAF1F9', '#D8E4F1', '#5A8BC4', '#fff', 'family=Playfair+Display:wght@600&family=Quicksand:wght@400;600', 'Playfair Display', 'Quicksand')),
 'kuchies': ("Kuchie's Alpine Florist", "Kuchie's", 'Perth Amboy, NJ', 'rfkuchie@comcast.net', 'Fresh flowers and holiday centerpieces.', 'kuchies', 'split',
   ('#FAF7F2', '#2B2A1E', '#8E1B22', '#F1E7DE', '#E2D6C9', '#2F4A35', '#fff', 'family=Cormorant+Garamond:ital,wght@1,600&family=Jost:wght@400;600', 'Cormorant Garamond', 'Jost')),
 'la-belle-creme': ('La Belle Crème', 'La Belle Crème', 'Woodbridge, NJ', 'labellecremebakery@gmail.com', 'Birthday, chocolate and celebration cakes.', 'belle', 'arch',
   ('#FDF6F5', '#4A2B2B', '#B8865B', '#F8E6E6', '#EFD5D5', '#B8865B', '#fff', 'family=Bodoni+Moda:wght@600&family=Jost:wght@400;600', 'Bodoni Moda', 'Jost')),
 'mosaic': ('Mosaic Wellness and Beauty', 'Mosaic', 'Woodbridge, NJ', 'contact@mosaicnj.com', 'Hair salon, massage & Japanese Head Spa.', 'mosaic', 'split',
   ('#F6F2EC', '#3A342C', '#8A7A5C', '#ECE5DA', '#DDD3C4', '#6E7F63', '#fff', 'family=Cormorant+Garamond:wght@600&family=Jost:wght@400;600', 'Cormorant Garamond', 'Jost')),
 'shades': ('Shades Barbershop & Nails', 'Shades', 'Iselin, NJ', 'shadesnewjersey@gmail.com', 'Fresh fades, beard trims, manicures & pedicures.', 'shades', 'full',
   ('#141210', '#F3EADB', '#C9A25A', '#211D19', '#3A332B', '#C9A25A', '#141210', 'family=DM+Serif+Display&family=Inter:wght@400;600', 'DM Serif Display', 'Inter')),
 'breeds': ('Breeds Spa Salon', 'Breeds', 'Colonia, NJ', 'breedsspasalon@gmail.com', 'Baths, haircuts, nails & de-shedding.', 'breeds', 'arch',
   ('#F5FBF8', '#1E3A33', '#2E9C83', '#E3F3EE', '#CBE7DE', '#2E9C83', '#fff', 'family=Fredoka:wght@600&family=Nunito:wght@400;700', 'Fredoka', 'Nunito')),
 'spaw-and-stay': ('Spaw and Stay', 'Spaw and Stay', 'Avenel, NJ', 'spawandstay@gmail.com', 'Grooming and a cozy place to stay.', 'spaw', 'split',
   ('#FAF6EF', '#3A2E22', '#A0703C', '#F1E7D8', '#E3D5C0', '#5E7D4A', '#fff', 'family=Fraunces:wght@600&family=Nunito:wght@400;700', 'Fraunces', 'Nunito')),
 'venus-detailing': ('Venus Auto Detailing', 'Venus', 'Avenel, NJ', 'venusdetailing@gmail.com', 'Interior and exterior detailing.', 'venus', 'full',
   ('#0E0C12', '#EFEAF6', '#A779E9', '#1A1622', '#2E2740', '#A779E9', '#0E0C12', 'family=Bebas+Neue&family=Barlow:wght@400;600', 'Bebas Neue', 'Barlow')),
 'ak-studios': ('AK Studios Barbershop', 'AK Studios', 'Metuchen, NJ', 'AKstudio.nj@hotmail.com', 'Haircuts and beard trims.', 'akstudios', 'split',
   ('#F7F6F3', '#111111', '#A8834A', '#ECEAE4', '#DAD6CC', '#111111', '#fff', 'family=DM+Serif+Display&family=Inter:wght@400;600', 'DM Serif Display', 'Inter')),
 'laxmi-flowers': ('Laxmi Flowers', 'Laxmi Flowers', 'Edison, NJ', 'laxmiflowers.edison@gmail.com', 'Fresh flowers and bouquets.', 'laxmi', 'arch',
   ('#FFF9F2', '#3A1414', '#C0242E', '#FCEBDD', '#F3D7C2', '#E0A400', '#3A1414', 'family=Playfair+Display:ital,wght@1,600&family=Work+Sans:wght@400;600', 'Playfair Display', 'Work Sans')),
}
EMAILPICK = {}
SHOPS8, THEMES8, FONTS8, KIND8 = {}, {}, {}, {}
idx = 0
for slug, look, shots in S:
    name, short, place, email, hero_line, th, kind, (bg, ink, acc, soft, line, cta, ctaink, fam, disp, body) = META[slug]
    items, labeled = [], []
    for j, (ar, scene, h, sub) in enumerate(shots):
        cap = h if h else scene[0].upper() + scene[1:]
        items.append({'src': B + U[idx] + '.png', 'cap': cap, 'alt': scene})
        if h and j in (1, 2, 4):
            labeled.append([re.sub(r'[^a-z0-9]+', '-', unicodedata.normalize('NFKD', h).encode('ascii','ignore').decode().lower()).strip('-'), j])
        idx += 1
    SHOPS8[slug] = {'name': name, 'short': short, 'place': place, 'theme': th, 'hero_line': hero_line,
                    'intro': "We made these images from your services and your own words. They're yours to keep and post, free.",
                    'sections': [['All', '', 'p', items]], 'email': email}
    THEMES8[th] = (f":root{{--bg:{bg};--ink:{ink};--muted:{ink}b3;--accent:{acc};--soft:{soft};--line:{line};--panel:{soft};--panel-ink:{ink};"
                   f"--cta:{cta};--cta-ink:{ctaink};--display:'{disp}',Georgia,serif;--body:'{body}',system-ui,sans-serif;--gap:12px;--radius:6px;"
                   f"--btn-radius:999px;--h1:clamp(46px,6.2vw,96px);--arch:999px 999px 10px 10px}}\n.hero .place{{color:var(--accent)}}")
    FONTS8[th] = fam
    KIND8[th] = kind
    EMAILPICK[slug] = labeled
assert idx == 119
with open('/home/claude/autonna-studio/build/data8.py', 'w') as f:
    f.write('# Wave 2 shops (generated by gen8.py)\n')
    for n, v in [('SHOPS8', SHOPS8), ('THEMES8', THEMES8), ('FONTS8', FONTS8), ('KIND8', KIND8), ('EMAIL8', EMAILPICK)]:
        f.write(f'{n} = {json.dumps(v, ensure_ascii=False, indent=1)}\n')
print('ok', {k: v for k, v in EMAILPICK.items()})
