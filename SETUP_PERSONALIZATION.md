# Personalization Setup — The "Pick a Size, Name Each Figure" Buying Flow

This is how to make the product page work exactly like you described:

> **Customer picks a tree size → chooses how many Santa heads → types a name for each one
> (Carly, Bill, Mike, Stacy) → price updates → add to cart.**

The same setup powers the **Pilgrim Turkey** (add pilgrims) and the **Easter Egg** (add bunnies).

---

## Why you need an app
Shopify's built-in product options can do the **size** (as a variant), but they **cannot**:
- show a **name box for each figure** the customer adds, or
- **add a price per figure**.

So you install one **product options app**. Both of these have a **free plan** that does conditional
name fields *and* per-option add-on pricing:

- **Globo Product Options, Variant** (recommended — strong conditional logic, free tier)
- **Hulk Product Options** (good alternative)

Install from the Shopify App Store → open the app → it adds an "Options" section to your products.

---

## The tree product is already built for this
In the import CSV, the tree is **one product** — `Personalized Family Christmas Tree` — with **4
size variants**:

| Size | For | Price |
|---|---|---|
| Small | 2–3 names | $49 |
| Medium | 4 names | $62 |
| Large | 5–6 names | $75 |
| XL | 6+ names | $89 |

The **size dropdown** comes from these variants automatically. The **name fields** come from the app
(below). *(Pricing here is by size — the figures that fit that size are included, and names are free
text. **Extra/add-on Santa heads beyond the size are $9.99 each**; pets/hearts are paid add-ons too.)*

---

## Step-by-step: build the flow on the Family Tree product

### 1. Confirm the size dropdown
Open the **Personalized Family Christmas Tree** product → under **Variants** you'll see
Small / Medium / Large / XL with their prices. That's your "pick a size" step — done.

### 2. Add the name fields (the core of what you asked for)
In the options app, create an **Option Set** and attach it to the Family Tree product. Add fields:

- **Field 1 — "How many Santa heads?"** → type: **Dropdown** → values **2, 3, 4, 5, 6, 7, 8**
  *(extra Santa heads beyond what the size includes = +$9.99 each)*
- **Field 2 — "Name on Santa #1"** → type: **Text box** → *Required*
- **Field 3 — "Name on Santa #2"** → Text box → *Required*
- **Field 4 — "Name on Santa #3"** → Text box
- …continue **through "Name on Santa #8."**

### 3. Make the name boxes appear based on the number chosen (conditional logic)
For each name box, set a **conditional rule** in the app:

- "Name on Santa #3" → **show only if** "How many Santa heads?" **is 3 or more**
- "Name on Santa #4" → show only if number **is 4 or more**
- …and so on through #8.

Now if the customer picks **4**, exactly **four** name boxes appear → they type Carly, Bill, Mike,
Stacy. Pick 6, six boxes appear. Exactly your example.

### 4. (Optional) Add the extras as paid add-ons
In the same option set, add:
- **"Add a pet?"** → Dropdown: None / Dog (+$9.99) / Cat (+$9.99) → plus a **"Pet's name"** text box
  (show only if a pet is chosen) and a **"Pet fur color"** box.
- **"Add hearts?"** → Dropdown with **+$8** each.
- **"Family name for the star"** → Text box (Required) — this is the star topper wording.

### 5. Save & preview
Open the product on your live store and walk the flow: pick **XL → 6 heads → 6 name boxes → type
names → price updates → Add to Cart.** The names ride along into the order so Sue sees exactly what
to letter on each figure.

---

## Do the same for Thanksgiving & Easter
Same idea, different figures (these use **base price + add a figure**, no size variants):

**Pilgrim Turkey**
- Option: "How many pilgrims?" (1–8) → optional +$12 each
- Conditional "Name on Pilgrim #1…#8" boxes
- "Boy or girl?" dropdown per pilgrim (black hat / white bonnet)

**Easter Egg**
- Option: "How many bunnies?" → optional +$12 each
- Conditional "Name on Bunny #1…#N" boxes
- "Boy or girl?" per bunny (purple bow tie / pink bow)
- "Wording on the egg" → Text box (default "Happy Easter," or family name)

---

## Pricing models (pick one)

**Selected: by size, figures included.** The size price covers the figures that fit that size; names
are free text. **Extra Santa heads beyond the size are $9.99 each**, and pets ($9.99) / hearts ($8) are
paid add-ons. This is the current CSV setup and works the moment you import.

> If you ever want to charge **per Santa head from the start** instead, lower the size base prices and
> set the "How many Santa heads?" dropdown to **+$9.99 each** in the app — no re-import needed.

---

## Quick checklist
- [ ] Install **Globo Product Options** (or Hulk)
- [ ] Import the CSV (tree already has Small/Medium/Large/XL)
- [ ] Build the option set: "How many Santa heads?" + Name #1–#8 (conditional)
- [ ] Add pet / heart / star-name options (extra Santa heads = $9.99 each)
- [ ] Repeat for Turkey (pilgrims) and Egg (bunnies)
- [ ] Test the full flow and place a test order to confirm names come through
