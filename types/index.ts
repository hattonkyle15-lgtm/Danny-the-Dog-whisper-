export interface Lead {
  id: string
  apartment_name: string
  address: string
  website?: string
  phone?: string
  email?: string
  property_manager_name?: string
  management_company?: string
  estimated_unit_count?: number
  pet_friendly: boolean
  has_dog_park: boolean
  is_luxury: boolean
  local_distance?: number
  has_visible_contact: boolean
  notes?: string
  lead_score: number
  status: LeadStatus
  city: string
  state: string
  created_at: string
  updated_at: string
  user_id: string
}

export type LeadStatus = 
  | 'New'
  | 'Contacted'
  | 'Follow-up Sent'
  | 'Interested'
  | 'Sample Sent'
  | 'Proposal Sent'
  | 'Closed'
  | 'Not Interested'

export interface Email {
  id: string
  lead_id: string
  subject: string
  body: string
  type: 'cold' | 'follow-up'
  status: 'draft' | 'sent' | 'replied'
  created_at: string
  user_id: string
}

export interface FollowUp {
  id: string
  lead_id: string
  scheduled_date: string
  notes?: string
  status: 'pending' | 'completed' | 'cancelled'
  created_at: string
  user_id: string
}

export interface Proposal {
  id: string
  lead_id: string
  pricing_tier: 'basic' | 'standard' | 'premium'
  monthly_price: number
  unit_price: number
  status: 'draft' | 'sent' | 'accepted' | 'rejected'
  created_at: string
  user_id: string
}

export interface Analytics {
  leads_added: number
  emails_sent: number
  replies: number
  samples_sent: number
  closed_deals: number
  projected_monthly_revenue: number
}