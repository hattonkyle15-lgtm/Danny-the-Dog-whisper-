'use client'

import React, { useState } from 'react'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Textarea } from '@/components/ui/textarea'
import { Label } from '@/components/ui/label'
import { Switch } from '@/components/ui/switch'
import { useRouter } from 'next/navigation'
import { calculateLeadScore } from '@/lib/scoring'
import { createLead } from '@/lib/supabase'

export default function AddLeadPage() {
  const router = useRouter()
  const [loading, setLoading] = useState(false)
  const [formData, setFormData] = useState({
    apartment_name: '',
    address: '',
    city: '',
    state: '',
    website: '',
    phone: '',
    email: '',
    property_manager_name: '',
    management_company: '',
    estimated_unit_count: '',
    pet_friendly: false,
    has_dog_park: false,
    is_luxury: false,
    local_distance: '',
    has_visible_contact: false,
    notes: '',
  })

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target
    setFormData(prev => ({ ...prev, [name]: value }))
  }

  const handleSwitchChange = (name: string) => (checked: boolean) => {
    setFormData(prev => ({ ...prev, [name]: checked }))
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    
    try {
      // Get current user
      const { data: { user } } = await import('@/lib/supabase').then(m => m.supabase.auth.getUser())
      
      if (!user) {
        throw new Error('User not authenticated')
      }
      
      // Calculate lead score
      const leadData = {
        ...formData,
        estimated_unit_count: formData.estimated_unit_count ? parseInt(formData.estimated_unit_count) : undefined,
        local_distance: formData.local_distance ? parseFloat(formData.local_distance) : undefined,
        lead_score: calculateLeadScore(formData),
        status: 'New',
        user_id: user.id,
      }
      
      await createLead(leadData)
      router.push('/leads')
    } catch (error) {
      console.error('Error creating lead:', error)
      alert('Failed to create lead. Please try again.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="container mx-auto py-8">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold">Add New Lead</h1>
        <Button variant="outline" onClick={() => router.back()}>Cancel</Button>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Apartment Complex Details</CardTitle>
        </CardHeader>
        <CardContent>
          <form onSubmit={handleSubmit} className="space-y-6">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div className="space-y-2">
                <Label htmlFor="apartment_name">Apartment Name *</Label>
                <Input
                  id="apartment_name"
                  name="apartment_name"
                  value={formData.apartment_name}
                  onChange={handleChange}
                  required
                />
              </div>
              
              <div className="space-y-2">
                <Label htmlFor="address">Address *</Label>
                <Input
                  id="address"
                  name="address"
                  value={formData.address}
                  onChange={handleChange}
                  required
                />
              </div>
              
              <div className="space-y-2">
                <Label htmlFor="city">City *</Label>
                <Input
                  id="city"
                  name="city"
                  value={formData.city}
                  onChange={handleChange}
                  required
                />
              </div>
              
              <div className="space-y-2">
                <Label htmlFor="state">State *</Label>
                <Input
                  id="state"
                  name="state"
                  value={formData.state}
                  onChange={handleChange}
                  required
                />
              </div>
              
              <div className="space-y-2">
                <Label htmlFor="website">Website</Label>
                <Input
                  id="website"
                  name="website"
                  value={formData.website}
                  onChange={handleChange}
                  type="url"
                />
              </div>
              
              <div className="space-y-2">
                <Label htmlFor="phone">Phone</Label>
                <Input
                  id="phone"
                  name="phone"
                  value={formData.phone}
                  onChange={handleChange}
                  type="tel"
                />
              </div>
              
              <div className="space-y-2">
                <Label htmlFor="email">Email</Label>
                <Input
                  id="email"
                  name="email"
                  value={formData.email}
                  onChange={handleChange}
                  type="email"
                />
              </div>
              
              <div className="space-y-2">
                <Label htmlFor="property_manager_name">Property Manager Name</Label>
                <Input
                  id="property_manager_name"
                  name="property_manager_name"
                  value={formData.property_manager_name}
                  onChange={handleChange}
                />
              </div>
              
              <div className="space-y-2">
                <Label htmlFor="management_company">Management Company</Label>
                <Input
                  id="management_company"
                  name="management_company"
                  value={formData.management_company}
                  onChange={handleChange}
                />
              </div>
              
              <div className="space-y-2">
                <Label htmlFor="estimated_unit_count">Estimated Unit Count</Label>
                <Input
                  id="estimated_unit_count"
                  name="estimated_unit_count"
                  value={formData.estimated_unit_count}
                  onChange={handleChange}
                  type="number"
                  min="0"
                />
              </div>
              
              <div className="space-y-2">
                <Label htmlFor="local_distance">Local Distance (miles)</Label>
                <Input
                  id="local_distance"
                  name="local_distance"
                  value={formData.local_distance}
                  onChange={handleChange}
                  type="number"
                  step="0.1"
                  min="0"
                />
              </div>
            </div>
            
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div className="flex items-center space-x-2">
                <Switch
                  id="pet_friendly"
                  checked={formData.pet_friendly}
                  onCheckedChange={handleSwitchChange('pet_friendly')}
                />
                <Label htmlFor="pet_friendly">Pet Friendly</Label>
              </div>
              
              <div className="flex items-center space-x-2">
                <Switch
                  id="has_dog_park"
                  checked={formData.has_dog_park}
                  onCheckedChange={handleSwitchChange('has_dog_park')}
                />
                <Label htmlFor="has_dog_park">Has Dog Park/Pet Station</Label>
              </div>
              
              <div className="flex items-center space-x-2">
                <Switch
                  id="is_luxury"
                  checked={formData.is_luxury}
                  onCheckedChange={handleSwitchChange('is_luxury')}
                />
                <Label htmlFor="is_luxury">Luxury Property</Label>
              </div>
              
              <div className="flex items-center space-x-2">
                <Switch
                  id="has_visible_contact"
                  checked={formData.has_visible_contact}
                  onCheckedChange={handleSwitchChange('has_visible_contact')}
                />
                <Label htmlFor="has_visible_contact">Visible Management Contact</Label>
              </div>
            </div>
            
            <div className="space-y-2">
              <Label htmlFor="notes">Notes</Label>
              <Textarea
                id="notes"
                name="notes"
                value={formData.notes}
                onChange={handleChange}
                rows={4}
              />
            </div>
            
            <div className="flex justify-end space-x-4 pt-4">
              <Button variant="outline" type="button" onClick={() => router.back()}>
                Cancel
              </Button>
              <Button type="submit">Save Lead</Button>
            </div>
          </form>
        </CardContent>
      </Card>
    </div>
  )
}