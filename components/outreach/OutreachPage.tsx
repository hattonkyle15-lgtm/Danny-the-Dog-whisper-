'use client'

import React, { useState } from 'react'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Textarea } from '@/components/ui/textarea'
import { Label } from '@/components/ui/label'
import { Input } from '@/components/ui/input'

export default function OutreachPage() {
  const [leadId, setLeadId] = useState('')
  const [emailType, setEmailType] = useState('cold')
  const [subject, setSubject] = useState('')
  const [body, setBody] = useState('')

  const handleGenerate = () => {
    // In a real app, this would call the email generator
    setSubject(`Sample ${emailType} email subject`)
    setBody(`This is a sample ${emailType} email body.\n\nIn a real application, this would be personalized based on the lead information.`)
  }

  const handleSaveDraft = () => {
    alert('Email draft saved! In a real app, this would save to the database.')
  }

  return (
    <div className="container mx-auto py-8">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold">Outreach</h1>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <Card>
          <CardHeader>
            <CardTitle>Generate Email</CardTitle>
          </CardHeader>
          <CardContent className="space-y-6">
            <div className="space-y-2">
              <Label htmlFor="leadId">Lead ID</Label>
              <Input
                id="leadId"
                value={leadId}
                onChange={(e) => setLeadId(e.target.value)}
                placeholder="Enter lead ID"
              />
            </div>
            
            <div className="space-y-2">
              <Label htmlFor="emailType">Email Type</Label>
              <select
                id="emailType"
                value={emailType}
                onChange={(e) => setEmailType(e.target.value)}
                className="w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background"
              >
                <option value="cold">Cold Email</option>
                <option value="follow-up">Follow-up Email</option>
                <option value="proposal">Proposal Email</option>
              </select>
            </div>
            
            <Button onClick={handleGenerate} disabled={!leadId}>
              Generate Email
            </Button>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Email Draft</CardTitle>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="space-y-2">
              <Label htmlFor="subject">Subject</Label>
              <Input
                id="subject"
                value={subject}
                onChange={(e) => setSubject(e.target.value)}
                placeholder="Email subject"
              />
            </div>
            
            <div className="space-y-2">
              <Label htmlFor="body">Body</Label>
              <Textarea
                id="body"
                value={body}
                onChange={(e) => setBody(e.target.value)}
                placeholder="Email body"
                rows={10}
              />
            </div>
            
            <div className="flex justify-end space-x-2">
              <Button variant="outline">Preview</Button>
              <Button onClick={handleSaveDraft}>Save Draft</Button>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}