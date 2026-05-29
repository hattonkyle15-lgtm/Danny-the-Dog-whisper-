# Apartment Outreach Agent - Setup Instructions

## Prerequisites

- Node.js 18+ installed
- npm or yarn package manager
- Supabase account (free tier works)

## Step 1: Clone and Install Dependencies

```bash
# Clone the repository
git clone <repository-url>
cd apartment-outreach-agent

# Install dependencies
npm install
```

## Step 2: Set Up Supabase

1. Go to [Supabase](https://supabase.com) and create a new project
2. Once your project is created, go to Project Settings > API
3. Copy the following values:
   - Project URL
   - Project API Keys > anon public
   - Project API Keys > service_role secret (keep this secure!)

## Step 3: Configure Environment Variables

1. Copy the example environment file:
   ```bash
   cp .env.local.example .env.local
   ```

2. Fill in your Supabase credentials in `.env.local`:
   ```
   NEXT_PUBLIC_SUPABASE_URL=your_project_url
   NEXT_PUBLIC_SUPABASE_ANON_KEY=your_anon_key
   SUPABASE_SERVICE_ROLE_KEY=your_service_role_key
   ```

## Step 4: Set Up Database Schema

1. In your Supabase dashboard, go to the SQL Editor
2. Create a new query
3. Copy the contents of `supabase/schema.sql` and paste it into the SQL Editor
4. Run the query to create all tables and set up Row Level Security

## Step 5: Set Up Authentication

1. In your Supabase dashboard, go to Authentication > Settings
2. Under "Site URL", add: `http://localhost:3000`
3. Under "Redirect URLs", add:
   - `http://localhost:3000/auth/callback`
   - `http://localhost:3000`

## Step 6: Run the Development Server

```bash
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

## Step 7: Create Your First User

1. Go to Authentication > Users in your Supabase dashboard
2. Click "Add user" and create a new user
3. Sign in with that user in the application

## Features Overview

### Dashboard
- Overview of leads, emails sent, and closed deals
- Quick access to add new leads

### Leads
- View all your apartment leads
- Search and filter leads
- Add new leads with comprehensive details
- Lead scoring (1-100) based on multiple criteria

### Lead Finder
- Search for apartment complexes by city and state
- (Note: In production, integrate with a real estate API)

### Outreach
- Generate personalized cold emails
- Generate follow-up emails
- Create proposal emails
- Save email drafts (no automatic sending in v1)

### Follow-Ups
- Track scheduled follow-ups
- Mark follow-ups as completed or cancelled

### Proposals
- View pricing tiers (Basic, Standard, Premium)
- Create custom proposals for leads
- Track proposal status

### Analytics
- View leads added
- Track emails sent and replies
- Monitor samples sent
- Track closed deals
- View projected monthly revenue

### Settings
- Configure company information
- Set default email templates

## Lead Scoring System

Leads are scored from 1-100 based on:

- **Pet Friendly** (20 points): Properties that allow pets
- **Estimated Unit Count** (25 points): More units = higher score
- **Has Dog Park/Pet Station** (15 points): Existing pet amenities
- **Luxury Property** (10 points): High-end properties
- **Local Distance** (15 points): Closer properties score higher
- **Visible Management Contact** (15 points): Easy to reach decision makers

## Pricing Tiers

### Basic - $99/month base + $0.50/unit
- 1 pet waste station
- 500 biodegradable bags/month
- Monthly restocking
- Email support

### Standard - $199/month base + $0.75/unit
- 2 pet waste stations
- 1000 premium bags/month
- Bi-weekly restocking
- Priority support
- Custom signage

### Premium - $399/month base + $1.25/unit
- 4 pet waste stations
- Unlimited premium bags
- Weekly restocking
- 24/7 priority support
- Custom branding
- Dog park consultation
- Quarterly sustainability reports

## Deployment

### Build for Production

```bash
npm run build
```

### Deploy to Vercel

1. Push your code to GitHub
2. Connect your repository to Vercel
3. Add environment variables in Vercel dashboard
4. Deploy!

## Troubleshooting

### Database Connection Issues
- Verify your Supabase URL and API keys are correct
- Check that Row Level Security policies are set up
- Ensure your user is authenticated

### Build Errors
- Make sure all dependencies are installed: `npm install`
- Check that TypeScript types are correct
- Verify all imports are valid

### Authentication Issues
- Check Supabase Auth settings
- Verify redirect URLs are configured correctly
- Clear browser cookies and try again

## Support

For issues or questions, please open an issue in the repository.