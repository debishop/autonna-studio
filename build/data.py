CF = "https://d8j0ntlcm91z4.cloudfront.net/user_3Esk8OYU2FjG0AiTaNIrZKS91Pk/hf_20261118_"


def load_dorsis():
    rows = [l.rstrip("\n").split("|") for l in open(__file__.replace("data.py", "dorsis.txt"))]
    imgs = [{"src": r[0], "alt": r[1], "cap": r[2].replace("&amp;", "&")} for r in rows]
    return imgs


def cf(items):
    return [{"src": CF + f + ".png", "alt": alt, "cap": cap} for f, cap, alt in items]


_d = load_dorsis()

SHOPS = {
    "dorsis": {
        "name": "D'Orsi's Bakery",
        "short": "D'Orsi's",
        "place": "Port Reading, NJ",
        "theme": "dorsis",
        "hero_line": "Your bakes, styled for the season.",
        "hero_img": 0,
        "intro": "We made these 25 images from your menu and your own product photos. They're yours to keep and post, free.",
        "made": "These are AI images set in one studio look built around your logo and colours. The red velvet, carrot cake, tiramisu, Napoleon and ring cakes were made from your own product photos. The rest are our styling of items on your menu. The printed box is a packaging idea, not your current box. Every headline uses your own words.",
        "sections": [
            ("Product heroes", "The scroll-stopping shots.", "p", _d[0:5]),
            ("Ad banners", "Ready to post, with your own words on them.", "p", _d[5:10]),
            ("Story covers", "Vertical, for Instagram and Facebook Stories.", "s", _d[10:15]),
            ("Tables", "Your bakes in the settings customers picture.", "p", _d[15:20]),
            ("Clean product shots", "Simple, for your menu and website.", "p", _d[20:25]),
        ],
    },
    "rich-florals": {
        "name": "Rich Florals",
        "short": "Rich Florals",
        "place": "Woodbridge, NJ",
        "theme": "florals",
        "hero_line": "Say it in roses.",
        "hero_img": (4, 0),
        "intro": "We made these 25 images from your own bouquets and arrangements. They're yours to keep and post, free.",
        "made": "These are AI images. Every bouquet shown was made from the real product photos in your online shop, set in one studio look built around your blush, burgundy and gold. Every headline uses your own words or your product names.",
        "sections": [
            ("Product portraits", "Your bouquets, one at a time.", "p", cf([
                ("162139_7155ecdd-1dbf-4bb9-8bf0-750d4d4d945a", "Initial Rose Bouquet", "Initial Rose Bouquet on a marble pedestal"),
                ("162147_1a627a65-6687-45f9-8dd8-44628b386909", "Golden Bouquet", "Golden Bouquet of champagne and blush roses"),
                ("162144_30fd8d8a-8c05-4960-8ef6-92de01fed034", "100 Count Rose Bouquet", "One hundred red roses in a round bouquet"),
                ("162142_b1483dc6-2293-4166-a1c9-62466e6dfb6c", "Pink Rose Statement Arrangement", "Tall pink rose statement arrangement"),
                ("162146_0a8c6a1e-3b86-4a8d-a44c-46c2b891143e", "Rich Florals Bloom Candle", "Rich Florals Bloom Candle in its box"),
            ])),
            ("Story covers", "Vertical, for Instagram and Facebook Stories.", "s", cf([
                ("162143_a84073c6-59ee-48cc-87bd-f326cb52a173", "Say It In Roses", "Story cover: Say It In Roses with the I Love You Bouquet"),
                ("162143_7bf2d159-a6d5-4353-90a0-bfafbd965655", "Zodiac Rose Bouquet", "Story cover: Zodiac Rose Bouquet"),
                ("162145_d2dfed16-6702-4bd3-995d-fdeba6e8392d", "Need Flowers Today?", "Story cover: wrapped and ready bouquets"),
                ("162145_eaae58d0-8d37-4f20-a089-171dba084a7c", "Crown Me", "Story cover: Crown Me Bouquet"),
                ("162139_18ee8b37-5741-4c68-a172-cf17be5718c6", "Big Daddy", "Story cover: Big Daddy Mens Bouquet"),
            ])),
            ("Moments", "Your bouquets where they get given.", "p", cf([
                ("162144_9f13d488-df6a-4c39-baa5-1dbaa18722b4", "The Grand Gesture", "The Grand Gesture, two vases of long-stemmed roses"),
                ("162143_16d36a19-640d-41bc-8e3a-07c5654b01db", "Birthday Number Rose Bouquet", "Birthday Number Rose Bouquet on a vanity"),
                ("162248_d7f1d9e9-85dc-4076-87f2-5af6909490d9", "Event tables", "Wedding table with pink rose centrepieces"),
                ("162248_d792b0bf-4f8b-42d7-939f-ce507e923e53", "Berry Rich Bouquet", "Berry Rich Bouquet on a car seat at night"),
                ("162251_7c2909c6-f56c-4bdb-aefa-c8998867045f", "Biggest Bouquet", "Biggest Bouquet on a blush velvet chaise"),
            ])),
            ("Ad banners", "Ready to post, with your own words on them.", "p", cf([
                ("162251_af52a7f2-a77e-4176-ad51-4547939a589c", "100 Count Rose Bouquet", "Banner: our roses make the statement"),
                ("162250_2c40c18e-1a2a-4f3f-a5f4-eab310c3dfb5", "Initial Rose Bouquet", "Banner with the Initial Rose Bouquet"),
                ("162248_cb9961b2-e67d-4dec-ad9e-a8cd3174daad", "Build Your Own Bouquet", "Banner: Build Your Own Bouquet"),
                ("162249_56ed771e-c93c-488b-9cd2-246385ed4e38", "I Love You Bouquet", "Banner: I Love You Bouquet"),
                ("162249_b8a21ee1-23ef-430d-96d9-ac8d3eba01e4", "Luxury Bouquets + Event Florist", "Banner: Luxury Bouquets + Event Florist"),
            ])),
            ("Hero shots", "Motion, petals and gold.", "p", cf([
                ("162249_41571256-792d-476d-8d9a-69a3a07ecec8", "Initial Rose Bouquet", "Initial Rose Bouquet floating in a burst of petals"),
                ("162248_c511fbff-668d-4b8d-9f2d-d142288ee5ab", "Long Stemmed Rose", "A single long-stemmed red rose floating"),
                ("162250_8be6233c-3f7c-48e5-8c39-aa6a09e31c53", "Three bouquets from above", "Three bouquets on blush velvet from above"),
                ("162249_9d1ca971-bbf1-4121-ac7e-51cd7e331cca", "I Love You Bouquet", "Close-up of the I Love You Bouquet"),
                ("162255_780a2bef-d287-4918-a76a-5f609e6f5a33", "Signature roses", "Rich Florals roses, hero shot"),
            ])),
        ],
    },
    "lavish-tails": {
        "name": "Lavish Tails Pet Spa",
        "short": "Lavish Tails",
        "place": "Woodbridge, NJ",
        "theme": "spa",
        "hero_line": "Paws on, stress off.",
        "hero_img": 0,
        "intro": "We made these 25 images around your services and your own words. They're yours to keep and post, free.",
        "made": "These are AI images, set in one calm spa look built around your clawfoot-tub logo, cream and aubergine. The pets are not your clients; they show the services on your site. Every headline uses your own words.",
        "sections": [
            ("Portraits", "Freshly groomed, one at a time.", "p", cf([
                ("162642_1214f3e7-5e4d-466e-adfe-492732049b6b", "Doodle with pink bows", "Golden doodle with pink bows on a lavender pouf"),
                ("162644_1075c48c-c7bb-472c-b0c9-1de26c9fab11", "Bath & brush", "Bichon in a clawfoot tub with bubbles"),
                ("162645_ef5df9ba-2deb-483c-88eb-cca47c4e2a1e", "Cat grooming", "Silver Persian cat on a lavender cushion"),
                ("162643_3327021b-293c-4783-a977-3524d6fa63ff", "Fresh trim", "Yorkshire terrier in a pink bandana"),
                ("162642_6674a40d-51cb-42f7-b5ff-2f292c6e682e", "Creative colour", "White poodle with pastel pink and lavender ear tips"),
            ])),
            ("Story covers", "Vertical, for Instagram and Facebook Stories.", "s", cf([
                ("162647_afbfffa6-2af8-4e7b-b4c4-c37916174331", "Paws on, stress off.", "Story cover: Paws on, stress off."),
                ("162644_65db41bc-cf05-428a-bdad-53b0174011b8", "Cat Grooming", "Story cover: Cat Grooming"),
                ("162643_4960a698-a8f2-4e76-a58f-2abaaedabc3b", "Free meet & greet", "Story cover: Free meet and greet"),
                ("162643_aa4d163b-5fdd-46b1-ade0-0d5a92bcc5c0", "100% Cageless", "Story cover: 100% Cageless"),
                ("162643_87930fef-09fc-47c7-a6ba-06c60196dfb4", "Massage & Reiki", "Story cover: Massage and Reiki"),
            ])),
            ("Inside the spa", "Daycare, overnights and quiet moments.", "p", cf([
                ("162645_b9d092cb-e0a8-4765-817b-a90af7a22ce4", "Main Street at dusk", "Pet spa window at dusk with a doodle inside"),
                ("162643_fdeb2646-5272-44d7-a02c-9318a83493d5", "Daycare nap", "Three dogs napping in a cageless daycare room"),
                ("162706_9e2da9d2-0b79-471a-86c9-d534dba4b37a", "After the bath", "Cockapoo wrapped in a lavender towel"),
                ("162707_93391e28-a02a-4ed9-8656-90f39cd98dba", "Overnights", "Terrier asleep under a lavender blanket"),
                ("162705_fc735407-6057-4b8b-a807-0aa9005b052c", "Dogs & cats", "Maltese and orange tabby on a lavender sofa"),
            ])),
            ("Ad banners", "Ready to post, with your own words on them.", "p", cf([
                ("162706_4bb5fbbd-4ff5-40be-83b6-d44dd9671975", "A spa day your pet will actually love", "Banner: A spa day your pet will actually love"),
                ("162707_3c0f978e-a3bb-441d-bc5b-ef552615ffc9", "Premium cageless grooming, daycare & spa care", "Banner: Premium cageless grooming, daycare and spa care"),
                ("162707_5f0ed492-37da-4935-8e15-7bcc88817360", "15 years of grooming craft", "Banner: 15 years of grooming craft"),
                ("162706_77d5aab2-9c37-4b31-b880-caeb4fe22346", "Dogs & cats welcome", "Banner: Dogs and cats welcome"),
                ("162705_19e5698b-b0cf-4f04-8286-6ac801dc5b34", "Calm, one-on-one attention", "Banner: Calm, one-on-one attention"),
            ])),
            ("Hero shots", "Bubbles, shakes and blow-dries.", "p", cf([
                ("162706_27428c25-0914-4d13-a5ff-fcc08e5f8206", "The shake", "Wet doodle mid-shake with droplets"),
                ("162707_0e49562e-ecac-423a-aea3-d898b952919a", "Bubble bath", "Maltese puppy in a tub with floating bubbles"),
                ("162705_292affe5-6544-40ff-b8dd-0dfd6fd6cc03", "Spa kit", "Overhead grid of pet spa towels, brushes and bows"),
                ("162707_5b703e32-7e57-4ed9-82e0-6ec9ea9a6799", "Blow-dry", "Apricot poodle with fur lifted by warm air"),
                ("162710_004a9541-c6de-46b8-8d79-af498bfaec7b", "The regulars", "Three groomed dogs in matching pink bandanas"),
            ])),
        ],
    },
    "hit-em-up": {
        "name": "Hit Em Up Boxing",
        "short": "Hit Em Up",
        "place": "Fords, NJ",
        "theme": "boxing",
        "hero_line": "Any age. All levels. One goal.",
        "hero_img": 0,
        "intro": "We made these 25 images around your gym, your programs and your own words. They're yours to keep and post, free.",
        "made": "These are AI images in one gritty look built around your HEU banner and your ring. There are no people in them, so nobody is shown who doesn't train with you. Every headline uses your own words, programs and hours from your website.",
        "sections": [
            ("The gear", "Gloves, wraps and bags.", "p", cf([
                ("162917_236de2cf-7949-4d7c-acab-7f3b9e20056a", "Gloves on the ropes", "Red gloves hanging on the ring rope under the HEU banner"),
                ("162914_135d959d-2b8c-47a6-8df5-2c9855194630", "Wraps and gloves", "Hand wraps and red gloves on a gym bench"),
                ("162914_4345cf2b-2de2-4284-9fef-f227b08256d1", "Heavy bag", "Heavy bag swinging under a spotlight"),
                ("162916_dcbda86f-cbac-4381-bfee-a96a7207f804", "Speed bag", "Speed bag mid-rebound"),
                ("162915_3ca047ec-11e6-4284-b4da-0c11dab93ef6", "Belts and trophies", "Championship belt and trophy in the ring corner"),
            ])),
            ("Story covers", "Vertical, for Instagram and Facebook Stories.", "s", cf([
                ("162914_279a6825-a79d-42f6-832e-c034bd7942d0", "Any age. All levels. One goal.", "Story cover: Any age. All levels. One goal."),
                ("162916_66c70394-95fc-4c17-8331-15e40e263476", "1-day free trial", "Story cover: 1-day free trial"),
                ("162915_5e2a1466-4ea6-4ebc-83c6-d7785fda8b34", "Youth boxing", "Story cover: Youth boxing, ages 7 and up"),
                ("162916_f0bb4dd2-2c1e-4816-bfdf-23eb36bfbe1a", "Certified coaches", "Story cover: Certified coaches"),
                ("162915_65a5d285-f27b-47d8-8605-4abd20ddb658", "Private training", "Story cover: Private training"),
            ])),
            ("The gym", "Before the 6pm class.", "p", cf([
                ("162916_505a3e41-c491-4fe9-8316-eff16b56401e", "Before class", "Empty gym with the HEU banner and heavy bags"),
                ("162918_b0865ec5-146c-4909-b1cb-f5d29553fc4b", "From the canvas", "Low view across the ring ropes"),
                ("162945_3f97b143-0f5e-4c55-a816-398ede4db0c0", "Gym bag", "Gym bag with gloves, wraps and jump rope"),
                ("162946_73f547a8-281a-4a0f-a008-f7115f895007", "Saturday 8am", "Sunrise light across the ring"),
                ("162942_10f6fc0e-d700-4106-aa08-98d687c0f551", "The trophy shelf", "Shelves of belts and trophies under the HEU banner"),
            ])),
            ("Ad banners", "Ready to post, with your own words on them.", "p", cf([
                ("162946_fe11ac11-e81f-463e-94d8-99df6eab138a", "Your journey starts at any age.", "Banner: Your journey starts at any age."),
                ("162944_64e51b65-6c7e-48c2-9ff0-0af7fd443186", "Family training discounts", "Banner: Family training discounts"),
                ("162945_a70c8a91-03e9-4a96-8fa0-324baef54277", "Classes and open gym", "Banner: Classes and open gym"),
                ("162947_0ca93212-15c9-4a04-9a1d-ef01a724ae30", "385 New Brunswick Ave", "Poster with the HEU logo and address"),
                ("162945_73215399-d2a6-4f07-89d2-834f63e14ea6", "Opening hours", "Banner with the gym's opening hours"),
            ])),
            ("Hero shots", "Impact, frozen.", "p", cf([
                ("162942_4fa7dbf0-c40a-4bee-96ad-66a7d0f53f74", "Impact", "Heavy bag at the moment of impact with chalk bursting"),
                ("162943_a9f474f6-55ff-46de-9d40-a1ae6003416f", "Gloves in the air", "Red gloves floating in a burst of chalk"),
                ("162948_58fb02fd-1b8d-446a-829c-4c85c3bd8d35", "The kit", "Boxing gear laid out in a grid from above"),
                ("162945_c7140a8a-26be-4a34-841c-5a98392a9bcb", "Knuckles", "Close-up of a worn red glove"),
                ("162950_faa058e4-f0b8-426e-9499-1f5c88a72c10", "The wrap", "Red hand wrap unfurling in the air"),
            ])),
        ],
    },
    "rnbeans": {
        "name": "R&Beans Coffee Shop",
        "short": "R&Beans",
        "place": "Avenel, NJ",
        "theme": "coffee",
        "hero_line": "Good Coffee. Good Music. Good Company.",
        "hero_img": (4, 4),
        "intro": "We made these 25 images from your menu, your logo and your own photos. They're yours to keep and post, free.",
        "made": "These are AI images in one warm look built around your record-badge logo. Every drink and bake shown is on your menu today; the Butter Love Latte, Iced Matcha and C.R.E.A.M. Brulee were made from your own photos. Smashing Pumpkins and the Pear Apple Cobbler Chai may be seasonal, so check before posting. Every headline uses your own words.",
        "sections": [
            ("The menu", "Your drinks, one at a time.", "p", cf([
                ("163420_3c7162bd-00ec-45b0-b7e6-cc81d3f3b249", "Butter Love Latte (Iced)", "Butter Love Latte in a branded cup"),
                ("163420_74043ed2-8777-47be-8aaf-40eb60c3eeca", "Iced Matcha", "Iced Matcha in a branded cup"),
                ("163420_05d4e366-c579-45ee-b2a9-33bd0925940d", "Cold Brew", "Cold Brew over ice in a branded cup"),
                ("163422_4322a639-9356-4e03-8a0a-f9e039ef3901", "C.R.E.A.M. Brulee Latte", "C.R.E.A.M. Brulee Latte with dripping cold foam"),
                ("163422_8c79b540-d2f8-4776-9208-8aab5e7c8d31", "Banana Pudding Matcha", "Banana Pudding Matcha with vanilla wafers"),
            ])),
            ("Story covers", "Vertical, for Instagram and Facebook Stories.", "s", cf([
                ("163422_1adeca49-5c59-4ed2-8f2e-7ccfba23167c", "Good Coffee. Good Music. Good Company.", "Story cover with three drinks and a turntable"),
                ("163420_0523df67-39ab-4437-8cf3-a363c1b889c0", "A record on.", "Story cover: Espresso, drip, cold brew. A record on."),
                ("163419_d109f2ca-62dc-4b15-b2d8-4cd8086b3de1", "Drumline Latte", "Story cover: Drumline Latte, Saturdays only"),
                ("163642_c10a0a7a-6959-4470-9469-2a8d8720564d", "Open at 6am", "Story cover: Open at 6am"),
                ("163420_9ccb8217-b0a9-47c6-b5f5-71b458637aab", "Smashing Pumpkins", "Story cover: Smashing Pumpkins"),
            ])),
            ("Around the shop", "Mornings, records and the office run.", "p", cf([
                ("163421_172fa111-4ada-4a19-9f4e-ef55c5bfcbe7", "Out front", "Storefront with yellow chairs and drinks"),
                ("163421_374bb9b7-b924-49b4-90dd-b932855fda27", "Record on", "Turntable with a cappuccino and croissant"),
                ("163449_7c229dfc-501d-4b63-bf47-20514e0396f1", "Box of Joe at the office", "Box of Joe on an office table"),
                ("163453_1fe6db29-e04b-416d-9af0-4439092ef428", "The first shot", "Espresso pulling at opening"),
                ("163451_197ec5e1-611a-4b60-9c3e-68dd97d4f1a3", "Croissants", "Everything, chocolate and plain croissants"),
            ])),
            ("Ad banners", "Ready to post, with your own words on them.", "p", cf([
                ("163642_22bffa13-5796-4a42-b177-8064c05468c4", "Butter Love Latte", "Banner: Butter Love Latte"),
                ("163450_b21434d3-f0f2-4fab-9e31-9f7862825ee8", "Pear Apple Cobbler Chai", "Banner: Pear Apple Cobbler Chai"),
                ("163451_879092e5-4bbb-4f31-b461-c324100adfbe", "Box of Joe", "Banner: Box of Joe"),
                ("163452_b1a2e3fc-37e5-4a56-9f6c-93d523a27f81", "The record badge", "Poster of the R&Beans logo as a vinyl record"),
                ("163449_c5a23d00-69a9-430f-bf4d-f3c04047d66c", "Snow Globe", "Banner: Snow Globe lemonade"),
            ])),
            ("Hero shots", "Splashes, pours and spinning records.", "p", cf([
                ("163450_726b8528-592f-475e-8374-cdf59bcd8284", "Cold brew splash", "Cold brew with ice bursting around it"),
                ("163449_c74b441a-a891-4b97-ad9d-c9d9c9bae041", "Espresso on vinyl", "Espresso floating on a vinyl record"),
                ("163450_73167fd5-4268-49c9-b859-517f9218b540", "The whole menu", "Drinks, croissants and cookies from above"),
                ("163451_3a71fc4c-79a5-480b-841c-5642e3f2d9d0", "Honey Nut Cheerios", "Honey Nut Cheerios latte with honey drizzle"),
                ("163455_3c829c52-aef6-40c0-b925-69cbac4382df", "The pour", "Cold foam pouring over a C.R.E.A.M. Brulee Latte"),
            ])),
        ],
    },
}
