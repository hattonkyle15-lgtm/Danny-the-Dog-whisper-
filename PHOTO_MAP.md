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

| Save the JPG as… | Product in Shopify | Which photo it is |
|---|---|---|
| `grand-family-tree-family-of-8` | Family of 8 — Grand Tree | Standing tree, **"Hatton Family"** star, ~8 named figures |
| `family-of-seven-keepsake-tree` | Family of 7 | Standing tree, **"Santos Family"** star, ~7 figures |
| `family-of-six-keepsake-tree` | Family of 6 | Standing tree, **"Santos/Harbor"** star, ~6 figures |
| `family-of-five-keepsake-tree` | Family of 5 | *(use a plain green tree shot — see notes)* |
| `family-of-four-keepsake-tree` | Family of 4 | **"Harbor Family"** tree — Grayson, Sharon, Nathen, Tracey |
| `little-family-tree-family-of-3` | Family of 3 | **"Yanec Family"** tree — Keith, Debbie, Lydia |
| `sweetheart-tree-family-of-2` | Family of 2 — Sweetheart | **"Yanec Family"** tree — Keith & Debbie (2 figures) |
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

### Bundles (reuse existing photos)
| Product | Use the photo from… |
|---|---|
| The Couple's Keepsake Set | `sweetheart-tree-family-of-2` |
| The Family Bundle | `family-of-four-keepsake-tree` |
| The Grandparent Gift Set | `family-of-six-keepsake-tree` |
| The Heirloom Set | `grand-family-tree-family-of-8` |

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
