# Sales Enablement Platform

A comprehensive sales enablement platform with lead management, email generation, proposal creation, and analytics.

## Table of Contents

1. [Installation](#installation)
2. [Supabase Setup](#supabase-setup)
3. [Database Schema](#database-schema)
4. [Environment Variables](#environment-variables)
5. [Running the Application](#running-the-application)
6. [Deployment to Vercel](#deployment-to-vercel)
7. [Testing Features](#testing-features)

## Installation

### Prerequisites

- Node.js (version 16 or higher)
- npm or yarn
- Git

### Steps

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd sales-enablement-platform
   ```

2. Install dependencies:
   ```bash
   npm install
   # or
   yarn install
   ```

3. Create a `.env.local` file in the root directory (see [Environment Variables](#environment-variables) section)

## Supabase Setup

1. Go to [Supabase](https://supabase.io/) and create a new project
2. Choose your organization and enter a project name
3. Select a region closest to your users
4. Set a strong database password
5. Click "Create new project" and wait for it to be provisioned

### Supabase Configuration

After your project is created:

1. Go to Project Settings > API
2. Copy the Project URL and anon/public keys
3. Add these to your `.env.local` file

## Database Schema

The application requires the following tables in your Supabase database:

### users
```sql
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  full_name VARCHAR(255),
  role VARCHAR(50) DEFAULT 'user',
  created_at TIMESTAMP DEFAULT NOW()
);
```

### leads
```sql
CREATE TABLE leads (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255),
  company VARCHAR(255),
  phone VARCHAR(50),
  status VARCHAR(50) DEFAULT 'new',
  source VARCHAR(100),
  assigned_to UUID REFERENCES users(id),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);
```

### emails
```sql
CREATE TABLE emails (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  lead_id UUID REFERENCES leads(id),
  subject VARCHAR(255),
  content TEXT,
  status VARCHAR(50) DEFAULT 'draft',
  sent_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW()
);
```

### proposals
```sql
CREATE TABLE proposals (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  lead_id UUID REFERENCES leads(id),
  title VARCHAR(255),
  content TEXT,
  status VARCHAR(50) DEFAULT 'draft',
  sent_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW()
);
```

### analytics
```sql
CREATE TABLE analytics (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  event_type VARCHAR(100),
  user_id UUID REFERENCES users(id),
  lead_id UUID REFERENCES leads(id),
  metadata JSONB,
  created_at TIMESTAMP DEFAULT NOW()
);
```

## Environment Variables

Create a `.env.local` file in the root directory with the following variables:

```
NEXT_PUBLIC_SUPABASE_URL=your_supabase_project_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key
SUPABASE_SERVICE_ROLE_KEY=your_supabase_service_role_key
```

## Running the Application

1. Make sure you have completed the setup steps above
2. Run the development server:
   ```bash
   npm run dev
   # or
   yarn dev
   ```

3. Open [http://localhost:3000](http://localhost:3000) in your browser

## Deployment to Vercel

1. Push your code to a GitHub repository
2. Go to [Vercel](https://vercel.com/) and sign up/sign in
3. Click "New Project" and import your GitHub repository
4. Configure the project settings:
   - Framework Preset: Next.js
   - Root Directory: ./
5. Add environment variables in the Vercel dashboard:
   - NEXT_PUBLIC_SUPABASE_URL
   - NEXT_PUBLIC_SUPABASE_ANON_KEY
   - SUPABASE_SERVICE_ROLE_KEY
6. Click "Deploy" and wait for the build to complete
7. Your application will be available at the provided URL

## Testing Features

### Login
1. Navigate to the login page
2. Enter valid credentials or use "Sign in with Google" if configured
3. Verify successful redirection to the dashboard

### Leads Management
1. Navigate to the leads section
2. Create a new lead with sample data
3. Verify the lead appears in the leads list
4. Edit lead information and verify updates
5. Delete a lead and confirm removal

### Email Generation
1. Go to a lead's detail page
2. Click "Generate Email" button
3. Verify email draft is created with appropriate content
4. Edit the email content
5. Send the email and verify status change

### Proposals
1. Navigate to the proposals section
2. Create a new proposal for a lead
3. Add content to the proposal
4. Save as draft and verify it appears in drafts
5. Send the proposal and verify status change

### Analytics
1. Perform various actions in the application (creating leads, sending emails, etc.)
2. Navigate to the analytics dashboard
3. Verify that events are being tracked and displayed correctly
4. Check different time ranges and filters

---

For additional support, please contact the development team.