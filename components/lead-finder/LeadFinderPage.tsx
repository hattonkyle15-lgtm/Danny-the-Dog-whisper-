'use client'

import React, { useState } from 'react'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'

export default function LeadFinderPage() {
  const [city, setCity] = useState('')
  const [state, setState] = useState('')
  const [isSearching, setIsSearching] = useState(false)

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault()
    if (!city.trim() || !state.trim()) return
    
    setIsSearching(true)
    // In a real app, this would call an API to find apartment complexes
    setTimeout(() => {
      setIsSearching(false)
      alert(`Searching for apartments in ${city}, ${state}. In a real app, this would return results.`)
    }, 1000)
  }

  return (
    <div className="container mx-auto py-8">
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold">Lead Finder</h1>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Find Apartment Complexes</CardTitle>
        </CardHeader>
        <CardContent>
          <form onSubmit={handleSearch} className="space-y-6">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div className="space-y-2">
                <Label htmlFor="city">City *</Label>
                <Input
                  id="city"
                  value={city}
                  onChange={(e) => setCity(e.target.value)}
                  placeholder="Enter city"
                  required
                />
              </div>
              
              <div className="space-y-2">
                <Label htmlFor="state">State *</Label>
                <Input
                  id="state"
                  value={state}
                  onChange={(e) => setState(e.target.value)}
                  placeholder="Enter state"
                  required
                />
              </div>
            </div>
            
            <div className="flex justify-end">
              <Button type="submit" disabled={isSearching}>
                {isSearching ? 'Searching...' : 'Find Apartments'}
              </Button>
            </div>
          </form>
        </CardContent>
      </Card>

      <Card className="mt-6">
        <CardHeader>
          <CardTitle>Search Results</CardTitle>
        </CardHeader>
        <CardContent>
          <p className="text-muted-foreground">Enter a city and state to find apartment complexes. Results will appear here.</p>
        </CardContent>
      </Card>
    </div>
  )
}