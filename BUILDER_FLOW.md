# The Guided "Build Your Keepsake" Experience

This is the step-by-step, picture-driven buying flow Sue wants:

> **Step 1 — Choose your keepsake:** Christmas Tree · Thanksgiving Turkey · Easter Egg
> (if Tree → pick Small / Medium / Large / Extra Large)
> **Step 2 — Personalize:** pick figures (with photos), choose their colors, set how many of each,
> and type a name for every one. Price updates as you go.

It shows pictures, prices, and walks the customer through it — not plain product pages.

---

## What builds this (important)
A product CSV can't create a guided, visual builder — that's a **storefront experience**. You build
it with **two pieces**:

1. **A "Step 1" landing page** — 3 big image tiles (Tree / Turkey / Egg) with prices, each linking to
   that product. (Build with the free **Shopify page editor** or a page-builder like **PageFly**.)
2. **A visual product-options app on each product** for "Step 2" — shows figure **photos**, **color
   swatches**, **quantity per figure**, **name fields**, and **adds price per figure**.

### Recommended app
- **Globo Product Options** — free/low-cost, supports **image swatches**, **quantity**, **conditional
  fields**, and **add-on pricing**. Best value for this.
- **Kickflip** (paid) — if you want the polished, true step-by-step builder with a live picture
  preview that updates as they choose. Nicer look, more setup.

> Start with **Globo**. It does everything below; upgrade to Kickflip later if you want the fancy
> live-preview look.

---

## STEP 1 — Choose your keepsake (landing page)
A page titled **"Build Your Keepsake"** with three image cards:

| Card (photo) | Label | Starting price | Links to |
|---|---|---|---|
| Christmas tree photo | **Christmas Family Tree** | from **$16.99** | Tree product |
| Turkey photo | **Thanksgiving Pilgrim Turkey** | from **$24.99** | Turkey product |
| Easter egg photo | **Easter Egg Keepsake** | from **$24.99** | Egg product |

Put this page in the main menu as **"Build Your Keepsake"** and feature it on the homepage.

---

## STEP 2 — Personalize (per base product, via the options app)

### 🎄 Christmas Family Tree
- **Tree Size** (Shopify variant): Small $16.99 · Medium $19.99 · Large $21.99 · Extra Large $23.99
- Then an app option set with these figures — each shows a **photo**, lets the customer set **how
  many**, and reveals a **name box per figure**. **Each figure = $9.99.**

| Figure | Customer chooses | Then |
|---|---|---|
| **Santa Head** | how many | a name for each |
| **Dog Face** | color: Black / White / Grey / Brown / Tan + how many | a name for each |
| **Cat Face** | color: Black / White / Grey / Brown / Tan + how many | a name for each |
| **Angel** | hair: Black / Brown / Blond / Bald + how many | a name for each |

- Plus **"Family name for the star"** (text box) — the topper wording.

### 🦃 Thanksgiving Pilgrim Turkey ($24.99 base)
- App option set with two pilgrim types, each shows a **photo**, **how many**, and a **name box per
  pilgrim**. **Each pilgrim = $9.99.**

| Figure | Customer chooses | Then |
|---|---|---|
| **Boy Pilgrim** (black hat) | how many | a name for each |
| **Girl Pilgrim** (white bonnet) | how many | a name for each |

### 🐰 Easter Egg Keepsake ($24.99 base)
- App option set with two bunny colors, each shows a **photo**, **how many**, and a **name box per
  bunny**. **Each bunny = $9.99.**

| Figure | Customer chooses | Then |
|---|---|---|
| **Blue Bunny** | how many | a name for each |
| **Pink Bunny** | how many | a name for each |
| Plus "Wording on the egg" | — | text box (default "Happy Easter" or family name) |

---

## How to set up "how many of each + a name for each" in Globo
For each figure, the cleanest pattern:
1. Add an **Image Swatch** option for the figure/color (so the photo shows).
2. Add a **Quantity** or number dropdown: "How many [Santa heads]?" → set **+$9.99 each**.
3. Add **conditional text fields** "Name #1 … Name #8" that appear based on the quantity chosen
   (Name #3 shows only if quantity ≥ 3, etc.).
4. Repeat per figure type. Group them under a heading like **"Step 2: Add Your Family."**

This makes the total climb as people are added, and every name comes through on the order so Sue
knows exactly what to letter.

---

## Pricing recap (all in the CSV)
- **Trees:** S $16.99 · M $19.99 · L $21.99 · XL $23.99 (base)
- **Centerpieces:** Turkey $24.99 · Egg $24.99
- **Figures:** Santa / Dog Face / Cat Face / Pilgrim / Bunny = **$9.99 each** · **Angel = $11.50**
- **Family Star** $6.99 · **Home & Tree Ornament** $13.99 (base + figures)
- **Shipping:** flat $9.99, free over $75

> Note: Angel is currently **$11.50** while the other figures are **$9.99** — say the word and I'll
> match it to $9.99.

---

## Build checklist
- [ ] Import the products CSV (done if products show in Shopify)
- [ ] Install **Globo Product Options**
- [ ] Tree: confirm size variants; build the Step-2 figure option set (Santa/Dog/Cat/Angel)
- [ ] Turkey: build pilgrim option set (Boy/Girl + quantities + names)
- [ ] Egg: build bunny option set (Blue/Pink + quantities + names + egg wording)
- [ ] Upload figure **photos** into the app swatches (so customers see them)
- [ ] Create the **"Build Your Keepsake"** landing page (3 image tiles) and add to the menu
- [ ] Test the full flow + place a test order to confirm names/quantities come through
