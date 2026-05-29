# Apartment Outreach Agent - Project Summary

## Overview

A comprehensive SaaS-style sales dashboard for apartment lead management, built for a dog waste bag supplier to find apartment complexes, score them as leads, generate personalized outreach emails, track follow-ups, and manage deals.

## Tech Stack

- **Framework**: Next.js 14 (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **Authentication**: Supabase Auth
- **Database**: Supabase PostgreSQL
- **UI Components**: Radix UI primitives with custom styling

## Project Structure

```
apartment-outreach-agent/
├── app/                          # Next.js App Router
│   ├── layout.tsx               # Root layout
│   ├── page.tsx                 # Dashboard (home)
│   ├── globals.css              # Global styles
│   ├── leads/
│   │   ├── page.tsx             # Leads list
│   │   └── new/
│   │       └── page.tsx         # Add new lead
│   ├── lead-finder/
│   │   └── page.tsx             # Find apartments by city/state
│   ├── outreach/
│   │   └── page.tsx             # Email generation
│   ├── follow-ups/
│   │   └── page.tsx             # Follow-up tracking
│   ├── proposals/
│   │   └── page.tsx             # Proposal management
│   ├── analytics/
│   │   └── page.tsx             # Analytics dashboard
│   └── settings/
│       └── page.tsx             # Settings
├── components/
│   ├── layout/
│   │   ├── Sidebar.tsx          # Navigation sidebar
│   │   └── DashboardLayout.tsx  # Layout wrapper
│   ├── dashboard/
│   │   └── DashboardPage.tsx    # Dashboard content
│   ├── leads/
│   │   ├── LeadsPage.tsx        # Leads list component
│   │   └── AddLeadPage.tsx      # Add lead form
│   ├── lead-finder/
│   │   └── LeadFinderPage.tsx   # Lead finder component
│   ├── outreach/
│   │   └── OutreachPage.tsx     # Email generation
│   ├── follow-ups/
│   │   └── FollowUpsPage.tsx    # Follow-up tracking
│   ├── proposals/
│   │   └── ProposalsPage.tsx    # Proposal management
│   ├── analytics/
│   │   └── AnalyticsPage.tsx    # Analytics display
│   ├── settings/
│   │   └── SettingsPage.tsx     # Settings form
│   └── ui/                      # Reusable UI components
│       ├── button.tsx
│       ├── card.tsx
│       ├── input.tsx
│       ├── textarea.tsx
│       ├── label.tsx
│       ├── badge.tsx
│       ├── switch.tsx
│       └── select.tsx
├── lib/                         # Utility functions
│   ├── utils.ts                 # Helper functions (cn)
│   ├── supabase.ts              # Supabase client & CRUD
│   ├── scoring.ts               # Lead scoring algorithm
│   ├── email-generator.ts       # Email templates
│   └── proposal-generator.ts    # Proposal generation
├── types/                       # TypeScript types
│   ├── index.ts                 # Main types
│   └── database.ts              # Database types
├── supabase/
│   └── schema.sql               # Database schema
├── package.json                 # Dependencies
├── next.config.js               # Next.js config
├── tailwind.config.js           # Tailwind config
├── tsconfig.json              # TypeScript config
├── postcss.config.js            # PostCSS config
├── .env.local.example           # Environment template
├── README.md                    # Basic readme
├── SETUP.md                     # Setup instructions
└── PROJECT_SUMMARY.md           # This file
```

## Features Implemented

### 1. Dashboard
- Overview of key metrics (total leads, active leads, emails sent, closed deals)
- Quick access to add new leads
- Recent leads and activity overview

### 2. Leads Management
- View all leads with search/filter
- Add new leads with comprehensive details:
  - Apartment name, address, city, state
  - Website, phone, email
  - Property manager name and company
  - Estimated unit count
  - Pet-friendly status
  - Dog park/pet station availability
  - Luxury property flag
  - Local distance
  - Visible management contact
  - Notes
- Lead scoring display (1-100)
- Status tracking with color-coded badges

### 3. Lead Finder
- Search for apartment complexes by city and state
- (Ready for integration with real estate API)

### 4. Outreach
- Generate personalized cold emails
- Generate follow-up emails
- Create proposal emails
- Save email drafts (no automatic sending in v1)
- Email preview and editing

### 5. Follow-Ups
- Track scheduled follow-ups
- View follow-up status (pending, completed, cancelled)
- Link to leads

### 6. Proposals
- Three pricing tiers:
  - **Basic**: $99/month + $0.50/unit
  - **Standard**: $199/month + $0.75/unit
  - **Premium**: $399/month + $1.25/unit
- Feature comparison
- Proposal status tracking

### 7. Analytics
- Leads added
- Emails sent
- Replies received
- Samples sent
- Closed deals
- Projected monthly revenue
- Charts (ready for data integration)

### 8. Settings
- Company information
- Email templates
- User preferences

## Lead Scoring System (1-100)

| Criteria | Weight | Description |
|----------|--------|-------------|
| Pet Friendly | 20 pts | Properties that allow pets |
| Unit Count | 25 pts | More units = higher score (200+ = full, 100-199 = 75%, 50-99 = 50%, <50 = 25%) |
| Dog Park | 15 pts | Has dog park or pet station |
| Luxury Property | 10 pts | High-end/luxury apartments |
| Local Distance | 15 pts | Closer properties score higher (<5mi = full, 5-15mi = 75%, 15-30mi = 50%, >30mi = 25%) |
| Visible Contact | 15 pts | Management contact info available |

**Score Colors:**
- 80-100: Green (Excellent)
- 60-79: Yellow (Good)
- 40-59: Orange (Fair)
- 0-39: Red (Poor)

## Lead Status Workflow

1. **New** → Initial lead added
2. **Contacted** → First outreach sent
3. **Follow-up Sent** → Follow-up email sent
4. **Interested** → Lead expressed interest
5. **Sample Sent** → Product samples sent
6. **Proposal Sent** → Pricing proposal sent
7. **Closed** → Deal won
8. **Not Interested** → Lead declined

## Database Schema

### Tables

**leads**
- id (uuid, primary key)
- apartment_name (text)
- address (text)
- website (text)
- phone (text)
- email (text)
- property_manager_name (text)
- management_company (text)
- estimated_unit_count (integer)
- pet_friendly (boolean)
- has_dog_park (boolean)
- is_luxury (boolean)
- local_distance (numeric)
- has_visible_contact (boolean)
- notes (text)
- lead_score (integer)
- status (text)
- city (text)
- state (text)
- created_at (timestamp)
- updated_at (timestamp)
- user_id (uuid, foreign key)

**emails**
- id (uuid, primary key)
- lead_id (uuid, foreign key)
- subject (text)
- body (text)
- type (text: cold, follow-up, proposal)
- status (text: draft, sent, replied)
- created_at (timestamp)
- user_id (uuid, foreign key)

**follow_ups**
- id (uuid, primary key)
- lead_id (uuid, foreign key)
- scheduled_date (timestamp)
- notes (text)
- status (text: pending, completed, cancelled)
- created_at (timestamp)
- user_id (uuid, foreign key)

**proposals**
- id (uuid, primary key)
- lead_id (uuid, foreign key)
- pricing_tier (text: basic, standard, premium)
- monthly_price (numeric)
- unit_price (numeric)
- status (text: draft, sent, accepted, rejected)
- created_at (timestamp)
- user_id (uuid, foreign key)

### Security
- Row Level Security (RLS) enabled on all tables
- Users can only access their own data
- Policies for SELECT, INSERT, UPDATE, DELETE

## Email Templates

### Cold Email
- Personalized greeting with property manager name
- Reference to pet-friendly policies
- Mention of dog park facilities (if applicable)
- Product offerings list
- Unit count-based pricing mention
- Call to action for 15-minute call
- Sample offer

### Follow-Up Email
- Reference to previous email
- Free sample offer
- No-obligation quote promise
- Flexible payment terms
- Cost savings statistics
- P.S. with local reference

### Proposal Email
- Custom proposal details
- Pricing tier breakdown
- Included services list
- Next steps outline
- Contact information

## Getting Started

See `SETUP.md` for detailed installation and configuration instructions.

Quick start:
```bash
npm install
# Configure .env.local with Supabase credentials
npm run dev
```

## Next Steps for Production

1. **Authentication**: Implement full Supabase Auth flow
2. **API Integration**: Connect to real estate APIs for lead finding
3. **Email Sending**: Integrate with email service (SendGrid, etc.)
4. **Charts**: Add Recharts for analytics visualization
5. **Testing**: Add unit and integration tests
6. **Deployment**: Deploy to Vercel or similar platform

## License

MIT License - See LICENSE file for details.