'use client'

import React, { useState, useEffect } from 'react'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Badge } from '@/components/ui/badge'
import { supabase } from '@/lib/supabase'

export default function FollowUpsPage() {
  const [followUps, setFollowUps] = useState<any[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetchFollowUps()
  }, [])

  const fetchFollowUps = async () => {
    try {
      const { data, error } = await supabase
        .from('follow_ups')
        .select('*')
        .order('scheduled_date', { ascending: true })
      
      if (error) throw error
      
      // In a real implementation, we would join with leads table to get lead names
      const followUpsWithLeadInfo = data.map(followUp => ({
        ...followUp,
        leadName: 'Lead Name', // This would come from joined data
      }))
      
      setFollowUps(followUpsWithLeadInfo)
    } catch (error) {
      console.error('Error fetching follow-ups:', error)
    } finally {
      setLoading(false)
    }
  }

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'pending': return 'bg-yellow-500';
      case 'completed': return 'bg-green-500';
      case 'cancelled': return 'bg-gray-500';
      default: return 'bg-gray-500';
    }
  }

  return (
    <div className="container mx-auto py-8">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold">Follow-Ups</h1>
        <Button>Add Follow-Up</Button>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Scheduled Follow-Ups</CardTitle>
        </CardHeader>
        <CardContent>
          {followUps.length === 0 ? (
            <p className="text-muted-foreground">No follow-ups scheduled.</p>
          ) : (
            <div className="space-y-4">
              {followUps.map((followUp) => (
                <div key={followUp.id} className="flex items-center justify-between p-4 border rounded-lg">
                  <div>
                    <h3 className="font-medium">{followUp.leadName}</h3>
                    <p className="text-sm text-muted-foreground">Scheduled for {followUp.scheduledDate}</p>
                  </div>
                  <div className="flex items-center space-x-2">
                    <Badge className={getStatusColor(followUp.status)}>
                      {followUp.status.charAt(0).toUpperCase() + followUp.status.slice(1)}
                    </Badge>
                    <Button variant="outline" size="sm">View</Button>
                  </div>
                </div>
              ))}
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  )
}