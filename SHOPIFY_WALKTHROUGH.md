# Shopify Click-by-Click Walkthrough

Follow this with Shopify open on your computer. Each step says exactly what to click and type.
If a screen doesn't match, screenshot it and I'll adjust. Work top to bottom.

> **Goal:** the guided "Build Your Keepsake" flow — Step 1 pick Tree/Turkey/Egg, Step 2 personalize
> with figure photos, colors, quantities, and a name for each.

---

## PART 0 — Before you start
- [ ] Products imported (you've done this — you should see Personalized Family Christmas Tree, etc.)
- [ ] Product photos converted to JPG and uploaded (see `PHOTO_MAP.md`)
- [ ] You're logged into **admin.shopify.com**

---

## PART 1 — Install the options app (Globo)

1. In Shopify admin left menu, scroll down and click **Apps**.
2. Click **Shopify App Store** (opens a new tab).
3. In the search bar type: **Globo Product Options**.
4. Click the app named **"Product Options, Variant Option" by Globo**.
5. Click **Install** → **Install** again to confirm. It returns you to your admin with the app open.
6. If it shows a plan screen, choose the **Free** plan to start.

You now have an **"Options"** area you'll use below. Leave this tab open.

---

## PART 2 — The Christmas Tree (the main one)

### 2A. Confirm the size dropdown
1. Left menu → **Products** → click **Personalized Family Christmas Tree**.
2. Scroll to **Variants**. You should see **Small / Medium / Large / Extra Large** with prices
   ($16.99 / $19.99 / $21.99 / $23.99). That's your size picker — nothing to change.
3. Scroll up to **Media** and confirm a tree photo is there (add one if not).

### 2B. Build the "Add Your Family" options (in Globo)
1. Open the **Globo Product Options** app (the tab from Part 1, or Apps → Globo).
2. Click **Create option set** (or **Add option set**).
3. Name it: **Tree – Add Your Family**.
4. Under "Apply to," choose **Specific products** → search and select **Personalized Family
   Christmas Tree**. Save.

Now add the figures. For **each** figure below, click **Add option** and set it up:

**Option 1 — Santa Heads**
- Option type: **Quantity** (or "Dropdown" with numbers 0–8 if no quantity type)
- Label: **How many Santa heads?**
- Price add-on: **$9.99** per unit → turn ON "add price"
- Save.

**Option 2 — Santa names** (one set of name boxes)
- Option type: **Text field**
- Label: **Santa head names (one per line)**
- Help text: "Type each name on its own line."
- *(Simple version: one box for all names. Fancy version below in Part 5.)*
- Save.

**Option 3 — Dog Face**
- Add option → type **Image swatch** (or **Dropdown**)
- Label: **Add a Dog Face?**
- Values: **None, Black, White, Grey, Brown, Tan**
- Price add-on on each color (except None): **$9.99**
- Save. Then add a **Text field** labeled **Dog's name** right after it.

**Option 4 — Cat Face**
- Same as Dog: Image swatch / Dropdown
- Label: **Add a Cat Face?**
- Values: **None, Black, White, Grey, Brown, Tan** → **$9.99** each
- Save. Add a **Text field** labeled **Cat's name**.

**Option 5 — Angel**
- Image swatch / Dropdown
- Label: **Add an Angel?**
- Values: **None, Black hair, Brown hair, Blond, Bald** → **$11.50** each
- Save. Add a **Text field** labeled **Angel's name**.

**Option 6 — Star wording**
- Text field
- Label: **Family name for the star topper**
- Mark **Required**.
- Save.

5. Click **Save** on the option set.

### 2C. Test it
1. Go to **Online Store → Themes → ... → Preview** (or open the product on your live store).
2. Open the Tree product. You should see the size dropdown + all the options.
3. Pick a size, add 4 Santa heads, type names, add a dog → confirm the **price goes up** and
   **Add to cart** works.

---

## PART 3 — The Thanksgiving Turkey

1. Globo app → **Create option set** → name **Turkey – Add Pilgrims** → apply to **Personalized
   Pilgrim Turkey** → Save.
2. Add option → **Quantity** → label **How many Boy pilgrims? (black hat)** → **$9.99** each.
3. Add **Text field** → label **Boy pilgrim names (one per line)**.
4. Add option → **Quantity** → label **How many Girl pilgrims? (white bonnet)** → **$9.99** each.
5. Add **Text field** → label **Girl pilgrim names (one per line)**.
6. Save. Make sure the Turkey product has a **photo** (Media).

---

## PART 4 — The Easter Egg

1. Globo app → **Create option set** → name **Egg – Add Bunnies** → apply to **Personalized Easter
   Egg Keepsake** → Save.
2. Add option → **Quantity** → label **How many Blue bunnies?** → **$9.99** each.
3. Add **Text field** → **Blue bunny names (one per line)**.
4. Add option → **Quantity** → label **How many Pink bunnies?** → **$9.99** each.
5. Add **Text field** → **Pink bunny names (one per line)**.
6. Add option → **Text field** → label **Wording on the egg** → help text: 'Default "Happy Easter," or your family name.'
7. Save. Confirm the Egg product has a **photo**.

---

## PART 5 — (Optional, nicer) A name box per figure
If you want a separate name box that appears for each figure instead of one "one per line" box:
1. In the option set, after the quantity option, add **Text fields** named **Name #1, Name #2 … Name #8**.
2. On each, set a **Condition / Logic rule**: "show this field only if [How many Santa heads?] is
   greater than or equal to 1, 2, 3…" matching its number.
3. Globo's **Conditional logic** is under each option's settings ("Add condition").
This gives the exact "4 heads = 4 name boxes" behavior. Do the simple one-box version first if you
want to launch fast.

---

## PART 6 — Step 1 page: "Build Your Keepsake"

1. Left menu → **Online Store → Pages → Add page**.
2. Title: **Build Your Keepsake**.
3. In the content box, add three sections (use the image + link buttons in the editor), OR add a
   simple line for each with a photo and a button/link:
   - **Christmas Family Tree — from $16.99** → link to the Tree product
   - **Thanksgiving Pilgrim Turkey — from $24.99** → link to the Turkey product
   - **Easter Egg Keepsake — from $24.99** → link to the Egg product
   *(To link a product: in the editor, select the text/image → click the link icon → search the
   product.)*
4. Save.
5. Add it to your menu: **Online Store → Navigation → Main menu → Add menu item** → name **Build
   Your Keepsake** → link to the page → Save.
6. (Nice touch) **Online Store → Themes → Customize** → on the homepage add an **Image with text**
   or **Collage** section featuring the three keepsakes, linking to the page.

> Want it prettier with real "step 1 / step 2" tiles? Install **PageFly** (free plan) and build the
> Build Your Keepsake page with image cards — tell me and I'll write those steps too.

---

## PART 7 — Shipping

1. **Settings → Shipping and delivery → Manage rates** (under your shipping zone).
2. Add rate → **Flat rate** → name **Standard Shipping** → **$9.99**.
3. Add rate → **Free shipping** → name **Free over $75** → set condition **"Based on order price" →
   minimum $75**.
4. Save. (For pickup: **Settings → Shipping → Local pickup** → enable for your location.)

---

## PART 8 — Final checks before going live
- [ ] Each product (Tree/Turkey/Egg) has a photo and its option set shows on the storefront
- [ ] Adding figures **raises the price** correctly
- [ ] Place a **test order** and confirm the **names + quantities** appear on the order
- [ ] "Build Your Keepsake" page is in the menu
- [ ] Shipping shows $9.99 (and free over $75) at checkout
- [ ] When ready: **Online Store → Preferences** → remove the password to go live

---

## If you get stuck
Screenshot the screen you're on (or tell me the app/section name) and I'll give you the exact next
click. The most common snags: the option doesn't show (check it's applied to the right product),
or the price doesn't add (check "add price" is ON for that option).
