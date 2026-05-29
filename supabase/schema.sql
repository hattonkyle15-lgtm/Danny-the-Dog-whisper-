-- Apartment Outreach Agent Database Schema

-- Enable Row Level Security
alter table if exists leads enable row level security;
alter table if exists emails enable row level security;
alter table if exists follow_ups enable row level security;
alter table if exists proposals enable row level security;

-- Leads Table
create table if not exists leads (
  id uuid default gen_random_uuid() primary key,
  apartment_name text not null,
  address text not null,
  website text,
  phone text,
  email text,
  property_manager_name text,
  management_company text,
  estimated_unit_count integer,
  pet_friendly boolean default false,
  has_dog_park boolean default false,
  is_luxury boolean default false,
  local_distance numeric,
  has_visible_contact boolean default false,
  notes text,
  lead_score integer default 0,
  status text default 'New',
  city text not null,
  state text not null,
  created_at timestamp with time zone default timezone('utc'::text, now()),
  updated_at timestamp with time zone default timezone('utc'::text, now()),
  user_id uuid references auth.users not null
);

-- Emails Table
create table if not exists emails (
  id uuid default gen_random_uuid() primary key,
  lead_id uuid references leads on delete cascade not null,
  subject text not null,
  body text not null,
  type text not null, -- 'cold', 'follow-up', 'proposal'
  status text default 'draft', -- 'draft', 'sent', 'replied'
  created_at timestamp with time zone default timezone('utc'::text, now()),
  user_id uuid references auth.users not null
);

-- Follow-ups Table
create table if not exists follow_ups (
  id uuid default gen_random_uuid() primary key,
  lead_id uuid references leads on delete cascade not null,
  scheduled_date timestamp with time zone not null,
  notes text,
  status text default 'pending', -- 'pending', 'completed', 'cancelled'
  created_at timestamp with time zone default timezone('utc'::text, now()),
  user_id uuid references auth.users not null
);

-- Proposals Table
create table if not exists proposals (
  id uuid default gen_random_uuid() primary key,
  lead_id uuid references leads on delete cascade not null,
  pricing_tier text not null, -- 'basic', 'standard', 'premium'
  monthly_price numeric not null,
  unit_price numeric not null,
  status text default 'draft', -- 'draft', 'sent', 'accepted', 'rejected'
  created_at timestamp with time zone default timezone('utc'::text, now()),
  user_id uuid references auth.users not null
);

-- Row Level Security Policies

-- Leads: Users can only see their own leads
create policy "Users can view their own leads"
  on leads for select
  using (auth.uid() = user_id);

create policy "Users can insert their own leads"
  on leads for insert
  with check (auth.uid() = user_id);

create policy "Users can update their own leads"
  on leads for update
  using (auth.uid() = user_id);

create policy "Users can delete their own leads"
  on leads for delete
  using (auth.uid() = user_id);

-- Emails: Users can only see their own emails
create policy "Users can view their own emails"
  on emails for select
  using (auth.uid() = user_id);

create policy "Users can insert their own emails"
  on emails for insert
  with check (auth.uid() = user_id);

create policy "Users can update their own emails"
  on emails for update
  using (auth.uid() = user_id);

-- Follow-ups: Users can only see their own follow-ups
create policy "Users can view their own follow-ups"
  on follow_ups for select
  using (auth.uid() = user_id);

create policy "Users can insert their own follow-ups"
  on follow_ups for insert
  with check (auth.uid() = user_id);

create policy "Users can update their own follow-ups"
  on follow_ups for update
  using (auth.uid() = user_id);

-- Proposals: Users can only see their own proposals
create policy "Users can view their own proposals"
  on proposals for select
  using (auth.uid() = user_id);

create policy "Users can insert their own proposals"
  on proposals for insert
  with check (auth.uid() = user_id);

create policy "Users can update their own proposals"
  on proposals for update
  using (auth.uid() = user_id);

-- Indexes for better performance
create index if not exists idx_leads_user_id on leads(user_id);
create index if not exists idx_leads_status on leads(status);
create index if not exists idx_leads_city on leads(city);
create index if not exists idx_leads_state on leads(state);
create index if not exists idx_emails_lead_id on emails(lead_id);
create index if not exists idx_follow_ups_lead_id on follow_ups(lead_id);
create index if not exists idx_proposals_lead_id on proposals(lead_id);