import { Lead } from '@/types'

interface ScoringCriteria {
  pet_friendly: number
  estimated_unit_count: number
  has_dog_park: number
  is_luxury: number
  local_distance: number
  has_visible_contact: number
}

const WEIGHTS: ScoringCriteria = {
  pet_friendly: 20,
  estimated_unit_count: 25,
  has_dog_park: 15,
  is_luxury: 10,
  local_distance: 15,
  has_visible_contact: 15,
}

export function calculateLeadScore(lead: Partial<Lead>): number {
  let score = 0

  // Pet friendly (20 points)
  if (lead.pet_friendly) {
    score += WEIGHTS.pet_friendly
  }

  // Estimated unit count (25 points max)
  if (lead.estimated_unit_count) {
    if (lead.estimated_unit_count >= 200) {
      score += WEIGHTS.estimated_unit_count
    } else if (lead.estimated_unit_count >= 100) {
      score += WEIGHTS.estimated_unit_count * 0.75
    } else if (lead.estimated_unit_count >= 50) {
      score += WEIGHTS.estimated_unit_count * 0.5
    } else {
      score += WEIGHTS.estimated_unit_count * 0.25
    }
  }

  // Has dog park or pet station (15 points)
  if (lead.has_dog_park) {
    score += WEIGHTS.has_dog_park
  }

  // Luxury property (10 points)
  if (lead.is_luxury) {
    score += WEIGHTS.is_luxury
  }

  // Local distance (15 points max - closer is better)
  if (lead.local_distance !== undefined && lead.local_distance !== null) {
    if (lead.local_distance <= 5) {
      score += WEIGHTS.local_distance
    } else if (lead.local_distance <= 15) {
      score += WEIGHTS.local_distance * 0.75
    } else if (lead.local_distance <= 30) {
      score += WEIGHTS.local_distance * 0.5
    } else {
      score += WEIGHTS.local_distance * 0.25
    }
  }

  // Visible property management contact (15 points)
  if (lead.has_visible_contact) {
    score += WEIGHTS.has_visible_contact
  }

  return Math.round(score)
}

export function getScoreColor(score: number): string {
  if (score >= 80) return 'bg-green-500'
  if (score >= 60) return 'bg-yellow-500'
  if (score >= 40) return 'bg-orange-500'
  return 'bg-red-500'
}

export function getScoreLabel(score: number): string {
  if (score >= 80) return 'Excellent'
  if (score >= 60) return 'Good'
  if (score >= 40) return 'Fair'
  return 'Poor'
}