export type Json =
  | string
  | number
  | boolean
  | null
  | { [key: string]: Json | undefined }
  | Json[]

export interface Database {
  public: {
    Tables: {
      leads: {
        Row: {
          id: string
          apartment_name: string
          address: string
          website: string | null
          phone: string | null
          email: string | null
          property_manager_name: string | null
          management_company: string | null
          estimated_unit_count: number | null
          pet_friendly: boolean
          has_dog_park: boolean
          is_luxury: boolean
          local_distance: number | null
          has_visible_contact: boolean
          notes: string | null
          lead_score: number
          status: string
          city: string
          state: string
          created_at: string
          updated_at: string
          user_id: string
        }
        Insert: {
          id?: string
          apartment_name: string
          address: string
          website?: string | null
          phone?: string | null
          email?: string | null
          property_manager_name?: string | null
          management_company?: string | null
          estimated_unit_count?: number | null
          pet_friendly?: boolean
          has_dog_park?: boolean
          is_luxury?: boolean
          local_distance?: number | null
          has_visible_contact?: boolean
          notes?: string | null
          lead_score?: number
          status?: string
          city: string
          state: string
          created_at?: string
          updated_at?: string
          user_id: string
        }
        Update: {
          id?: string
          apartment_name?: string
          address?: string
          website?: string | null
          phone?: string | null
          email?: string | null
          property_manager_name?: string | null
          management_company?: string | null
          estimated_unit_count?: number | null
          pet_friendly?: boolean
          has_dog_park?: boolean
          is_luxury?: boolean
          local_distance?: number | null
          has_visible_contact?: boolean
          notes?: string | null
          lead_score?: number
          status?: string
          city?: string
          state?: string
          created_at?: string
          updated_at?: string
          user_id?: string
        }
      }
      emails: {
        Row: {
          id: string
          lead_id: string
          subject: string
          body: string
          type: string
          status: string
          created_at: string
          user_id: string
        }
        Insert: {
          id?: string
          lead_id: string
          subject: string
          body: string
          type: string
          status?: string
          created_at?: string
          user_id: string
        }
        Update: {
          id?: string
          lead_id?: string
          subject?: string
          body?: string
          type?: string
          status?: string
          created_at?: string
          user_id?: string
        }
      }
      follow_ups: {
        Row: {
          id: string
          lead_id: string
          scheduled_date: string
          notes: string | null
          status: string
          created_at: string
          user_id: string
        }
        Insert: {
          id?: string
          lead_id: string
          scheduled_date: string
          notes?: string | null
          status?: string
          created_at?: string
          user_id: string
        }
        Update: {
          id?: string
          lead_id?: string
          scheduled_date?: string
          notes?: string | null
          status?: string
          created_at?: string
          user_id?: string
        }
      }
      proposals: {
        Row: {
          id: string
          lead_id: string
          pricing_tier: string
          monthly_price: number
          unit_price: number
          status: string
          created_at: string
          user_id: string
        }
        Insert: {
          id?: string
          lead_id: string
          pricing_tier: string
          monthly_price: number
          unit_price: number
          status?: string
          created_at?: string
          user_id: string
        }
        Update: {
          id?: string
          lead_id?: string
          pricing_tier?: string
          monthly_price?: number
          unit_price?: number
          status?: string
          created_at?: string
          user_id?: string
        }
      }
    }
    Views: {
      [_ in never]: never
    }
    Functions: {
      [_ in never]: never
    }
    Enums: {
      [_ in never]: never
    }
    CompositeTypes: {
      [_ in never]: never
    }
  }
}