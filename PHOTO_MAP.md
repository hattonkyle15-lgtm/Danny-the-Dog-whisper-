# Photo → Product Map

How to get Sue's product photos into Shopify, and exactly which photo goes with which product.

## Step 1 — Convert the photos (they're AVIF; Shopify needs JPG)
Shopify does **not** accept AVIF. Batch-convert all of them to **JPG** first:
- Easiest: **cloudconvert.com/avif-to-jpg** (or freeconvert.com / iloveimg.com) → select all → Convert → Download All.
- Mac: select files → right-click → **Quick Actions → Convert Image → JPEG**.
- Windows: open in **Paint** → **Save As → JPEG**.

## Step 2 — Name each JPG to match the "Save the JPG as…" column below
Naming files to match the product **handle** keeps everything organized and makes matching foolproof.

## Step 3 — Upload into Shopify
**Products → click the product → Media box → Add** → drag the matching JPG in.
Shopify allows **multiple images per product** — use the named-figure shot as the main image and a
plain tree / close-up as image 2.

> Reminder: the product CSV (`shopify_products_import.csv`) does **not** carry these images — image
> files have to be uploaded directly to each product (or hosted at a public URL and pasted into the
> CSV's `Image Src` column).

---

## The Map

> **Note:** the 7 "Family of X" trees are now **one product** — `Personalized Family Christmas
> Tree` — with Small/Medium/Large/XL size variants. So **all the named-figure tree photos go on
> that single product** as a gallery (Shopify allows many images per product). You can also assign
> a size-appropriate photo to each size **variant** (e.g., the 2-figure tree on "Small," the
> 8-figure tree on "XL"). Suggested variant assignments below.

| Save the JPG as… | Where it goes | Which photo it is |
|---|---|---|
| `family-tree-xl` | Family Tree → **XL** variant + gallery | Standing tree, **"Hatton Family"** star, ~8 named figures |
| `family-tree-large-b` | Family Tree → gallery (Large) | **"Santos Family"** star, ~7 figures |
| `family-tree-large` | Family Tree → **Large** variant | **"Santos/Harbor"** star, ~6 figures |
| `family-tree-medium` | Family Tree → **Medium** variant | **"Harbor Family"** — Grayson, Sharon, Nathen, Tracey (4) |
| `family-tree-small-b` | Family Tree → gallery (Small) | **"Yanec Family"** — Keith, Debbie, Lydia (3) |
| `family-tree-small` | Family Tree → **Small** variant | **"Yanec Family"** — Keith & Debbie (2 figures) |
| `family-tree-plain` | Family Tree → gallery / **Medium** | Plain green glitter tree (no names) — clean "this is the tree" shot |
| `family-home-tree-ornament` | Family Home & Tree Ornament | House + tree with **James/Louis/katlya** (or Louis/Janelle) |
| `personalized-santa-head-magnet` | Santa Head Figure | Single clay Santa head (grey background) |
| `personalized-dog-magnet` | Dog Magnet | 5 dogs clustered (tan/black/white/brown/grey) |
| `personalized-cat-magnet` | Cat Magnet | 5 cats clustered |
| `personalized-family-star` | Family Name Star | Yellow star — **"Hatton Family 2017"** |
| `personalized-heart-magnet` | Clay Heart Magnet | *(crop a red heart from a tree shot, or reshoot)* |
| `clay-angel-ornament` | Clay Angel Ornament | White clay angel holding a yellow star |
| `memorial-magnet` | Memorial Magnet | *(needs its own photo — see notes)* |
| `pilgrim-turkey` | Pilgrim Turkey | Turkey with pilgrims (**"Example with Pilgrims"**) |
| `personalized-pilgrim-figure` | Pilgrim Figure | The 2 pilgrims (girl bonnet + boy black hat) |
| `easter-egg-keepsake` | Easter Egg Keepsake | Teal **"Happy Easter"** egg with daisies |
| `personalized-bunny-figure` | Bunny Figure | 2 bunnies (purple bow tie + pink bow) |

> The separate size-specific gift **bundles** were folded into the configurable tree + add-ons
> (extra Santa heads $9.99, pets, hearts). No separate bundle photos needed.

---

## Notes & gaps
- **Plain green glitter trees** (the no-name shots) are great stand-ins — use one for **Family of 5**
  and as a clean second image on the other trees.
- **Heart magnet** and **memorial magnet** have no dedicated shot yet — crop one from a tree photo
  for now, or add them to the reshoot list.
- **Family of 5, 6, 7** mapping is by figure count — **count the named figures** in each photo to be
  sure it lands on the right size before uploading.

## Photo quality verdict (for later upgrades)
The white-background tree/turkey/egg shots are solid for a shop grid. To push the "premium" feel,
the shot list in **Section 21 of `SHOPIFY_REBUILD_PLAN.md`** is the upgrade path: a styled lifestyle
hero, consistent white-background product shots, macro clay-texture close-ups, and a founder/workshop
photo of Sue. Launch with what you have, then swap in better photos when you can.
