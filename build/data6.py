"""Shops 6-15: 7 images each (0 hero, 1-4 feed posts, 5-6 story covers)."""
CF = "https://d8j0ntlcm91z4.cloudfront.net/user_3Esk8OYU2FjG0AiTaNIrZKS91Pk/hf_20261118_"


def seven(items):
    return [("All", "", "p", [{"src": CF + f + ".png", "cap": c, "alt": a} for f, c, a in items])]


SHOPS6 = {
    "prime-boxing": {
        "name": "Prime Boxing & Fitness", "short": "Prime Boxing", "place": "Avenel, NJ", "theme": "prime",
        "hero_line": "Knockout Fitness.",
        "intro": "We made these images from your classes and your own words. They're yours to keep and post, free.",
        "sections": seven([
            ("184557_647f23d0-30c0-472d-80cc-dec46f79bd46", "Gloves up", "Black and orange boxing gloves bursting through chalk dust"),
            ("184556_db766dc8-1ffd-414c-8558-f9f87f1e0328", "Knockout Fitness", "Banner: Knockout Fitness, gloves hanging on the ropes"),
            ("184555_edf61f81-5a05-40bc-9e2a-5a8f351dea12", "Women's Boxing 18+", "Banner: Women's Boxing 18+, gloves, wraps and a jump rope"),
            ("184555_cb1ecfe9-23a5-4fdf-ba80-558fc581ac89", "The gym", "Dark gym with heavy bags and a ring, orange lights"),
            ("184554_f1101030-f6d3-4290-acb3-e70c657eb7f9", "Boxing for Youth", "Banner: Boxing for Youth, small and large gloves by the ring"),
            ("184557_c9e4cf10-5a50-4854-9736-cb25ab2f67f2", "Now Open", "Story cover: Now Open, Welcome to the Fight"),
            ("184557_f1501ee3-c5c9-4c89-b9d9-a8ea915b019e", "Personal Training", "Story cover: Personal Training, focus mitts on the ring apron"),
        ]),
    },
    "la-bon": {
        "name": "La Bon Bake Shoppes", "short": "La Bon", "place": "Woodbridge, NJ", "theme": "labon",
        "hero_line": "Every bite is a delightful celebration.",
        "intro": "We made these images from this month's menu and your own words. They're yours to keep and post, free.",
        "sections": seven([
            ("184554_c30a467a-9d51-4b48-8657-c218eed6723a", "Pumpkin Whoopie Pie", "Pumpkin whoopie pie floating in a burst of crumbs"),
            ("184554_7f52cc9e-dcf9-4dd8-84ef-714d4aafaaa9", "Celebrate Thanksgiving with La Bon", "Banner: Celebrate Thanksgiving with La Bon, a table of pies"),
            ("184554_f0f3f146-19e5-4da6-be8c-e13db2f38149", "Cranberry Harvest Sourdough", "Banner: Cranberry Harvest Sourdough, sliced on a board"),
            ("184555_2900df80-9d7f-47e9-8bff-f47f7cd564c3", "Cupcake of the Month", "Banner: Chocolate Hazelnut cupcake of the month"),
            ("184558_7bdf21e1-47da-4006-8ed2-764cedc1b52b", "Pumpkin cheesecake", "Pumpkin cheesecake beside a La Bon box"),
            ("184631_17c59fef-3586-447c-b2e5-d3478db56b87", "Every Bite Is a Delightful Celebration", "Story cover: a case of pies, cakes and cupcakes"),
            ("184634_cce12803-93f7-427c-84e1-bc36abfe2aed", "Pumpkin Whoopie Pie", "Story cover: Pumpkin Whoopie Pie, product of the month"),
        ]),
    },
    "nnekas": {
        "name": "Nneka's Bakery", "short": "Nneka's", "place": "Woodbridge, NJ", "theme": "nneka",
        "hero_line": "Handcrafted daily to perfection.",
        "intro": "We made these images from your own cakes and cookies. They're yours to keep and post, free.",
        "sections": seven([
            ("184633_dc7a5aaf-f2d9-4d16-924f-ac74cc43f2b4", "Red Velvet Dessert Cake", "Slice of red velvet cake floating in a burst of crumbs"),
            ("185356_5a0326d0-15c7-49be-84c3-9762ddf81473", "Black & Gold Birthday Cake", "Ivory cake with black and gold spheres and gold leaf"),
            ("184634_59c4cc33-4b93-4106-822f-b529ccfdc274", "Celebration Cakes", "Banner: Celebration Cakes, a champagne cake"),
            ("185355_5b827904-77b1-49b7-b827-9a1bf7c1977c", "Luxury Box Cake", "Banner: Luxury Box Cake with roses and gold leaf"),
            ("184633_4f8cbd79-a797-447b-b81d-7c83dddbdeab", "Strawberry Crunch Cookies", "Banner: Strawberry Crunch Cookies, love at first bite"),
            ("184631_109fcf65-a564-425c-9e7e-3ba2789da7c0", "Banana Pudding Cake", "Story cover: Banana Pudding Cake, this month's chef special"),
            ("184633_402e3a7a-fa94-488c-aa6e-60679316e1a3", "Handcrafted daily to perfection", "Story cover: a display of cupcakes and desserts"),
        ]),
    },
    "woodbridge-martial-arts": {
        "name": "Woodbridge Martial Arts", "short": "Woodbridge Martial Arts", "place": "Woodbridge, NJ", "theme": "dojo",
        "hero_line": "Respect. Focus. Integrity.",
        "intro": "We made these images from your classes and your own words. They're yours to keep and post, free.",
        "sections": seven([
            ("184634_7f7122d0-6676-460e-b7d3-8d8c7a75104e", "The black belt", "A black belt falling onto a folded white uniform"),
            ("184634_72143c3c-287a-47c4-9f9b-3fe7e2919cb8", "Respect. Focus. Integrity.", "Banner: Respect. Focus. Integrity. A uniform on the dojo mat"),
            ("184635_c7267863-c8f8-49df-863d-3ddecb70bf3b", "Become Calm Under Pressure", "Banner: Become Calm Under Pressure, a heavy bag under a light"),
            ("184701_b51f8d5f-c178-4e93-8d59-e51e8a432a80", "Every belt", "Your sign above a rack of coloured belts"),
            ("184657_9e0b56fe-2ef1-4e05-afdc-90c133d20d0c", "Kids Martial Arts", "Banner: Kids Martial Arts, small and large uniforms"),
            ("184657_12e1dc70-ed7b-4705-9786-d2ad8673ed30", "Get a Free Class", "Story cover: Get a Free Class, the dojo doors open"),
            ("184659_2ef659a1-20de-4830-898f-7866368013ce", "Built on Discipline", "Story cover: Built on Discipline, belts on the wall"),
        ]),
    },
    "floral-expressions": {
        "name": "Floral Expressions", "short": "Floral Expressions", "place": "Woodbridge, NJ", "theme": "fe",
        "hero_line": "The best and freshest flowers in Woodbridge.",
        "intro": "We made these images from your own arrangements. They're yours to keep and post, free.",
        "sections": seven([
            ("184657_a56e59a9-8673-413f-950f-4c79a07df1d3", "Fall arrangement", "Fall lilies and roses in a wooden box, petals in the air"),
            ("184700_dc73aa4a-3f31-41b8-a05c-081747a805d3", "Fall Flowers", "Banner: Fall Flowers, sunflowers and roses in a green jug"),
            ("184659_2abadf65-903b-4346-bd30-fd39145d7824", "Pumpkin arrangement", "Fall flowers arranged in a pumpkin on a porch"),
            ("184659_71c374d2-3eaf-4736-82fe-11cdcf538aa6", "Floral Expressions", "Banner: the best and freshest flowers in Woodbridge"),
            ("184701_329a3ce6-44cf-4273-8b4b-65ac054a0da9", "Christmas Flowers", "Banner: Christmas Flowers, hand delivered in Woodbridge"),
            ("184658_56664452-19e1-4f98-a32f-91ee81643f99", "Deal of the Day", "Story cover: Deal of the Day bouquet"),
            ("184700_4a8405cd-0eff-4da3-8095-fa3379ac471b", "Make your next occasion memorable", "Story cover: a birthday bouquet with a gift"),
        ]),
    },
    "golden-paw": {
        "name": "Golden Paw Spa", "short": "Golden Paw", "place": "Woodbridge, NJ", "theme": "paw",
        "hero_line": "We treat your pets as if they were our own.",
        "intro": "We made these images from your grooming services and your own words. They're yours to keep and post, free.",
        "sections": seven([
            ("184659_52ea0a27-dbd7-47b9-9e18-29327df0cade", "The shake", "A doodle shaking off water after a bath"),
            ("184733_8d7678a8-eb4a-48cf-a5c2-7ce467e12cac", "We Treat Your Pets As If They Were Our Own", "Banner: a groomed cocker spaniel on the table"),
            ("184734_2fd8f78e-eabf-462f-bf3f-45f7be0f0589", "De-Shedding", "Banner: De-Shedding, a husky beside a pile of brushed fur"),
            ("184735_be48c7aa-a628-4bc2-82a1-f9f6c36f810b", "Bath time", "A poodle in the tub with a Golden Paw Spa towel"),
            ("184735_73d0a587-f6ec-43b7-a554-16175fc10d72", "Full Groom", "Banner: Full Groom, a shih tzu beside grooming tools"),
            ("184733_daea1bad-b396-4bc3-8686-0cca53990902", "Professional Pet Grooming", "Story cover: your logo and a golden retriever"),
            ("184732_6fa4f2d9-a8ca-4d71-aded-34d9542f1a7e", "Natural treats & supplies", "Story cover: shelves of treats and supplies"),
        ]),
    },
    "legrand": {
        "name": "LeGrand Coffee House", "short": "LeGrand", "place": "Woodbridge, NJ", "theme": "legrand",
        "hero_line": "Coffee. Comfort. Satisfaction.",
        "intro": "We made these images from your menu, your logo and your coffee bags. They're yours to keep and post, free.",
        "sections": seven([
            ("184732_287a0ae0-4605-430f-9f3a-10baa4378847", "The latte", "A latte with heart art in a burst of coffee beans"),
            ("184734_564baa5c-ccf3-4fc1-97f7-e52ffe85d5bc", "Coffee. Comfort. Satisfaction.", "Banner: a cappuccino in a LeGrand cup with pastries"),
            ("184735_7eed709a-cf4b-42d0-9b66-4ac0b6fcac2a", "Brazil, 12 oz", "Your Brazil coffee bag with roasted beans"),
            ("184736_732bdc3e-b8f6-40b0-ba08-0d1e1a3de243", "Our Signature Roasts", "Banner: five bowls of roasted beans"),
            ("184733_6e4d95f1-e1ed-4e68-b11e-365f9ea86346", "A seat by the window", "Espresso, tea and pastries by the window"),
            ("184734_27e62635-8869-4da6-b0c0-4270043e28ad", "Open 7 days", "Story cover: Open 7 days, 7 AM to 4 PM"),
            ("184757_4a293196-6cbc-48c5-a5f4-6dd9b41a3e0a", "Order our coffee online", "Story cover: a coffee bag in a shipping box"),
        ]),
    },
    "awesomeyos": {
        "name": "AwesomeYo's Kitchen", "short": "AwesomeYo's", "place": "Metuchen, NJ", "theme": "yo",
        "hero_line": "Baked with love.",
        "intro": "We made these images from your own cakes. They're yours to keep and post, free.",
        "sections": seven([
            ("184757_2624c055-ff11-412b-b0a8-9b8272ec66e2", "Wedding cake", "A white rose wedding cake with petals in the air"),
            ("184759_1f47de56-9556-4e3a-a158-c7364f79b442", "Baked with love", "Banner: Baked with love, a gold drip cake"),
            ("184757_e8fa9fe4-1e29-4b07-8ceb-84dd5451138d", "Sculpted cakes", "A cake sculpted as a stack of gift boxes"),
            ("184759_0961d92b-f753-4203-a4b4-785c82c483a5", "Let us be a part of your special event!", "Banner: a celebration dessert table"),
            ("184758_9ef14ea2-9cf4-4f64-9a6a-1e9479bca06a", "The details", "Close-up of a white rose and gold edge on a cake"),
            ("184804_4862666c-7344-4891-8d8b-f435f6386847", "Custom Cakes", "Story cover: Custom Cakes, 50 Pearl St, Metuchen"),
            ("184756_b89b2c77-f422-413a-91ce-0783a322671f", "From birthday parties to weddings", "Story cover: a birthday cake and a wedding cake"),
        ]),
    },
    "beauty-boutique": {
        "name": "The Beauty Boutique Off Main", "short": "The Beauty Boutique", "place": "Woodbridge, NJ", "theme": "bb",
        "hero_line": "Hair, facials, lashes and nails, off Main.",
        "intro": "We made these images from your services and your own boutique. They're yours to keep and post, free.",
        "sections": seven([
            ("184757_bc160d8c-2267-444b-ae5b-c970e83dc04a", "Your boutique", "The Beauty Boutique Off Main at golden hour"),
            ("184800_dbefac35-a18e-4c7d-adac-dd622a9180a7", "Japanese Head Spa", "Banner: Japanese Head Spa, a spa bed with steam"),
            ("184759_bbed6f02-afcd-472f-b3c6-cf5a70b7e717", "Facials", "Skincare on a marble tray with your card"),
            ("184756_4952576d-4eae-4b28-ac34-233cdca3e66c", "Lash Extensions", "Banner: Lash Extensions, classic, hybrid and volume"),
            ("184819_228b6784-8ffb-43fd-8e95-c16afcdc38ed", "Nails", "Nail polish in nude and rose on marble"),
            ("184815_84dfe1a6-aa55-44b2-bfe4-7a946c128665", "Beauty salon in Woodbridge, New Jersey.", "Story cover: a styling chair and arched mirror"),
            ("184819_a6006537-b4f5-4cee-8306-7f914b75e183", "Book Now", "Story cover: Book Now, your monogram on the wall"),
        ]),
    },
    "nabod": {
        "name": "NABOD Studio", "short": "NABOD", "place": "Woodbridge, NJ", "theme": "nabod",
        "hero_line": "The full NABOD experience.",
        "intro": "We made these images from your services and your own studio look. They're yours to keep and post, free.",
        "sections": seven([
            ("184818_275feeeb-a09a-4586-99cd-9e6131e33a6e", "The chair", "A black and gold barber chair in a gold spotlight"),
            ("184819_7eb9f0f1-2b4f-40ed-a470-71f9ba47a61b", "VIP Haircut", "Banner: VIP Haircut, gold tools on black velvet"),
            ("184818_dabe9d72-7d60-4507-9b31-3e261e871840", "Eucalyptus hot towel", "A steaming hot towel and a badger brush"),
            ("184816_973b55cf-6539-40d9-ae46-23b6b2abfd6d", "The full NABOD experience", "Banner: a row of black chairs and gold mirrors"),
            ("185355_16b3d49f-8983-4694-b007-b89b7f363a0e", "Razor neck shave", "A straight razor and shaving foam on black marble"),
            ("184816_3a20c74c-fd92-4e5c-adda-ebd7b8d64461", "Walk-ins welcome", "Story cover: Walk-ins welcome, the studio door at night"),
            ("184820_2831be85-24f5-40bb-90a7-f3e78692b2b0", "Book your appointment", "Story cover: your gold crest on a black wall"),
        ]),
    },
}

PICKS6 = {k: {"hero": 0, "posts": [1, 2, 3, 4], "stories": [5, 6], "extra": 18} for k in SHOPS6}

EMAIL6 = {  # three photos attached to each email: (name, flat index)
    "prime-boxing": [("knockout-fitness", 1), ("womens-boxing", 2), ("now-open", 5)],
    "la-bon": [("whoopie-pie", 0), ("thanksgiving", 1), ("cranberry-sourdough", 2)],
    "nnekas": [("red-velvet", 0), ("luxury-box-cake", 3), ("strawberry-crunch", 4)],
    "woodbridge-martial-arts": [("respect-focus-integrity", 1), ("kids-martial-arts", 4), ("free-class", 5)],
    "floral-expressions": [("fall-flowers", 1), ("pumpkin", 2), ("christmas-flowers", 4)],
    "golden-paw": [("pets-our-own", 1), ("de-shedding", 2), ("full-groom", 4)],
    "legrand": [("latte", 0), ("coffee-comfort", 1), ("signature-roasts", 3)],
    "awesomeyos": [("wedding-cake", 0), ("baked-with-love", 1), ("special-event", 3)],
    "beauty-boutique": [("storefront", 0), ("head-spa", 1), ("lash-extensions", 3)],
    "nabod": [("chair", 0), ("vip-haircut", 1), ("full-experience", 3)],
}
