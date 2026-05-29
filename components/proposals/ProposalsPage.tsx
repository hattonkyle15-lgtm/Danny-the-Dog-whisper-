'use client'

import React, { useState } from 'react'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Badge } from '@/components/ui/badge'
import { PRICING_TIERS } from '@/lib/proposal-generator'

export default function ProposalsPage() {
  const [proposals, setProposals] = useState([
    {
      id: '1',
      leadName: 'Sunset Apartments',
      tier: 'standard',
      monthlyPrice: 299,
      status: 'sent',
    },
  ])

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'draft': return 'bg-gray-500';
      case 'sent': return 'bg-blue-500';
      case 'accepted': return 'bg-green-500';
      case 'rejected': return 'bg-red-500';
      default: return 'bg-gray-500';
    }
  }

  return (
    <div className="container mx-auto py-8">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold">Proposals</h1>
        <Button>Create Proposal</Button>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-8">
        {Object.entries(PRICING_TIERS).map(([key, tier]) => (
          <Card key={key}>
            <CardHeader>
              <CardTitle>{tier.name}</CardTitle>
            </CardHeader>
            <CardContent>
              <p className="text-2xl font-bold mb-2">${tier.basePrice}/mo</p>
              <p className="text-sm text-muted-foreground mb-4">${tier.unitPrice}/unit</p>
              <p className="text-sm mb-4">{tier.description}</p>
              <ul className="space-y-2 text-sm">
                {tier.features.map((feature, index) => (
                  <li key={index} className="flex items-center">
                    <span className="mr-2">✓</span>
                    {feature}
                  </li>
                ))}
              </ul>
            </CardContent>
          </Card>
        ))}
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Recent Proposals</CardTitle>
        </CardHeader>
        <CardContent>
          {proposals.length === 0 ? (
            <p className="text-muted-foreground">No proposals created yet.</p>
          ) : (
            <div className="space-y-4">
              {proposals.map((proposal) => (
                <div key={proposal.id} className="flex items-center justify-between p-4 border rounded-lg">
                  <div>
                    <h3 className="font-medium">{proposal.leadName}</h3>
                    <p className="text-sm text-muted-foreground">
                      {PRICING_TIERS[proposal.tier]?.name} - ${proposal.monthlyPrice}/mo
                    </p>
                  </div>
                  <div className="flex items-center space-x-2">
                    <Badge className={getStatusColor(proposal.status)}>
                      {proposal.status.charAt(0).toUpperCase() + proposal.status.slice(1)}
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