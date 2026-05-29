'use client'

import React, { useState, useEffect } from 'react'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Badge } from '@/components/ui/badge'
import Link from 'next/link'
import { Lead, LeadStatus } from '@/types'
import { getScoreColor, getScoreLabel } from '@/lib/scoring'
import { getLeads } from '@/lib/supabase'

const statusColors: Record<LeadStatus, string> = {
  'New': 'bg-blue-500',
  'Contacted': 'bg-yellow-500',
  'Follow-up Sent': 'bg-orange-500',
  'Interested': 'bg-green-500',
  'Sample Sent': 'bg-purple-500',
  'Proposal Sent': 'bg-pink-500',
  'Closed': 'bg-emerald-500',
  'Not Interested': 'bg-gray-500',
}

export default function LeadsPage() {
  const [searchTerm, setSearchTerm] = useState('')
  const [leads, setLeads] = useState<Lead[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetchLeads()
  }, [])

  const fetchLeads = async () => {
    try {
      setLoading(true)
      const data = await getLeads()
      setLeads(data || [])
    } catch (error) {
      console.error('Error fetching leads:', error)
    } finally {
      setLoading(false)
    }
  }

  const filteredLeads = leads.filter(lead =>
    lead.apartment_name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    lead.city.toLowerCase().includes(searchTerm.toLowerCase()) ||
    lead.state.toLowerCase().includes(searchTerm.toLowerCase())
  )

  return (
    <div className="container mx-auto py-8">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold">Leads</h1>
        <Button asChild>
          <Link href="/leads/new">Add New Lead</Link>
        </Button>
      </div>

      <Card className="mb-6">
        <CardContent className="pt-6">
          <Input
            placeholder="Search leads by name, city, or state..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="max-w-md"
          />
        </CardContent>
      </Card>

      {leads.length === 0 ? (
        <Card>
          <CardContent className="pt-6 text-center py-12">
            <p className="text-muted-foreground mb-4">No leads yet. Add your first lead to get started.</p>
            <Button asChild>
              <Link href="/leads/new">Add New Lead</Link>
            </Button>
          </CardContent>
        </Card>
      ) : (
        <div className="grid gap-4">
          {filteredLeads.map((lead) => (
            <Card key={lead.id}>
              <CardContent className="pt-6">
                <div className="flex justify-between items-start">
                  <div className="flex-1">
                    <div className="flex items-center gap-2 mb-2">
                      <h3 className="text-lg font-semibold">{lead.apartment_name}</h3>
                      <Badge className={statusColors[lead.status as LeadStatus]}>
                        {lead.status}
                      </Badge>
                    </div>
                    <p className="text-sm text-muted-foreground mb-2">
                      {lead.address}, {lead.city}, {lead.state}
                    </p>
                    <div className="flex items-center gap-4 text-sm">
                      <span className="flex items-center gap-1">
                        <span className={`w-3 h-3 rounded-full ${getScoreColor(lead.lead_score)}`} />
                        Score: {lead.lead_score} ({getScoreLabel(lead.lead_score)})
                      </span>
                      {lead.estimated_unit_count && (
                        <span>{lead.estimated_unit_count} units</span>
                      )}
                      {lead.pet_friendly && (
                        <span className="text-green-600">Pet Friendly</span>
                      )}
                    </div>
                  </div>
                  <div className="flex gap-2">
                    <Button variant="outline" size="sm" asChild>
                      <Link href={`/leads/${lead.id}`}>View</Link>
                    </Button>
                    <Button variant="outline" size="sm" asChild>
                      <Link href={`/outreach?leadId=${lead.id}`}>Outreach</Link>
                    </Button>
                  </div>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
      )}
    </div>
  )
}