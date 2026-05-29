import { Lead } from '@/types'

export interface PricingTier {
  name: string
  description: string
  basePrice: number
  unitPrice: number
  features: string[]
}

export const PRICING_TIERS: Record<string, PricingTier> = {
  basic: {
    name: 'Basic',
    description: 'Essential dog waste management for smaller properties',
    basePrice: 99,
    unitPrice: 0.50,
    features: [
      '1 pet waste station',
      'Biodegradable bags (500/month)',
      'Monthly restocking',
      'Email support',
    ],
  },
  standard: {
    name: 'Standard',
    description: 'Complete solution for mid-size properties',
    basePrice: 199,
    unitPrice: 0.75,
    features: [
      '2 pet waste stations',
      'Premium biodegradable bags (1000/month)',
      'Bi-weekly restocking',
      'Priority email & phone support',
      'Custom signage',
    ],
  },
  premium: {
    name: 'Premium',
    description: 'Premium solution for luxury properties',
    basePrice: 399,
    unitPrice: 1.25,
    features: [
      '4 pet waste stations',
      'Premium biodegradable bags (unlimited)',
      'Weekly restocking',
      '24/7 priority support',
      'Custom branding',
      'Dog park amenities consultation',
      'Quarterly sustainability reports',
    ],
  },
}

export function generateProposal(lead: Lead, tier: string): { monthly_price: number; unit_price: number; total_monthly: number } {
  const pricingTier = PRICING_TIERS[tier]
  const unitCount = lead.estimated_unit_count || 50
  
  const monthly_price = pricingTier.basePrice + (unitCount * pricingTier.unitPrice)
  const unit_price = monthly_price / unitCount
  
  return {
    monthly_price,
    unit_price,
    total_monthly: monthly_price,
  }
}

export function getProposalDocument(lead: Lead, tier: string): string {
  const pricingTier = PRICING_TIERS[tier]
  const proposal = generateProposal(lead, tier)
  
  return `
PROPOSAL FOR DOG WASTE MANAGEMENT SERVICES

Date: ${new Date().toLocaleDateString()}
Prepared for: ${lead.apartment_name}
Property Manager: ${lead.property_manager_name || 'N/A'}
Address: ${lead.address}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PROPOSAL DETAILS

Pricing Tier: ${pricingTier.name}
Monthly Investment: $${proposal.monthly_price.toFixed(2)}
Per Unit Cost: $${proposal.unit_price.toFixed(2)}

INCLUDED SERVICES:
${pricingTier.features.map(f => `• ${f}`).join('\n')}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TERMS & CONDITIONS

• 12-month minimum contract
• 30-day cancellation notice required
• Payment due on the 1st of each month
• Setup fee: $250 (waived with annual contract)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ACCEPTANCE

By signing below, you agree to the terms and conditions outlined in this proposal.

_________________________
Property Manager Signature

_________________________
Date

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Thank you for considering our services!

[Your Company Name]
[Your Contact Information]
`
}