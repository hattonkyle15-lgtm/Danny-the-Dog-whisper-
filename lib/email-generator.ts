import { Lead } from '@/types'

export function generateColdEmail(lead: Lead): { subject: string; body: string } {
  const managerName = lead.property_manager_name || 'Property Manager'
  const apartmentName = lead.apartment_name
  
  const subject = `Eco-Friendly Dog Waste Solutions for ${apartmentName}`
  
  const body = `Dear ${managerName},

I hope this email finds you well. My name is [Your Name], and I represent [Your Company], a leading supplier of eco-friendly dog waste bags and pet station solutions.

I recently came across ${apartmentName} and was impressed by ${lead.pet_friendly ? 'your pet-friendly policies' : 'your property'}. I noticed ${lead.has_dog_park ? 'you have excellent dog park facilities' : 'you cater to pet owners'}, and I believe our products could enhance your resident experience while supporting your sustainability goals.

We specialize in:
- Biodegradable dog waste bags
- Durable pet waste stations
- Custom branding options
- Bulk pricing for properties of all sizes

${lead.estimated_unit_count ? `With ${lead.estimated_unit_count} units, we can offer competitive pricing starting at just $X per unit per month.` : 'We offer competitive pricing tailored to properties of all sizes.'}

Would you be open to a brief 15-minute call next week to discuss how we can support ${apartmentName}? I'd be happy to send samples for your review.

Best regards,
[Your Name]
[Your Company]
[Your Phone]
[Your Email]`

  return { subject, body }
}

export function generateFollowUpEmail(lead: Lead, previousEmailDate: string): { subject: string; body: string } {
  const managerName = lead.property_manager_name || 'Property Manager'
  const apartmentName = lead.apartment_name
  
  const subject = `Following up: Eco-Friendly Dog Waste Solutions for ${apartmentName}`
  
  const body = `Dear ${managerName},

I hope you're doing well. I wanted to follow up on my email from ${previousEmailDate} regarding eco-friendly dog waste solutions for ${apartmentName}.

I understand you're busy, so I'll keep this brief. We're currently offering:

✓ Free sample packs for qualified properties
✓ No-obligation quotes within 24 hours
✓ Flexible payment terms

${lead.estimated_unit_count ? `For a property with ${lead.estimated_unit_count} units, our clients typically see a 20-30% cost savings compared to traditional suppliers.` : 'Our clients typically see 20-30% cost savings compared to traditional suppliers.'}

If you're interested, I can send a sample pack this week. No strings attached.

Would a quick call on Tuesday or Wednesday work for you?

Best regards,
[Your Name]
[Your Company]
[Your Phone]
[Your Email]

P.S. We're currently working with several properties in ${lead.city} and would love to add ${apartmentName} to our growing list of partners.`

  return { subject, body }
}

export function generateProposalEmail(lead: Lead, proposal: { pricing_tier: string; monthly_price: number; unit_price: number }): { subject: string; body: string } {
  const managerName = lead.property_manager_name || 'Property Manager'
  const apartmentName = lead.apartment_name
  
  const subject = `Custom Proposal for ${apartmentName} - Dog Waste Solutions`
  
  const body = `Dear ${managerName},

Thank you for your interest in our dog waste solutions for ${apartmentName}. I'm excited to present our custom proposal for your property.

PROPOSAL DETAILS:
━━━━━━━━━━━━━━━━━━━━━━━
Property: ${apartmentName}
Pricing Tier: ${proposal.pricing_tier.charAt(0).toUpperCase() + proposal.pricing_tier.slice(1)}
Monthly Investment: $${proposal.monthly_price.toFixed(2)}
Per Unit Cost: $${proposal.unit_price.toFixed(2)}

INCLUDES:
• Premium biodegradable waste bags
• ${proposal.pricing_tier === 'basic' ? '1' : proposal.pricing_tier === 'standard' ? '2' : '4'} pet waste stations
• Monthly restocking service
• 24/7 customer support
• Custom branding available

NEXT STEPS:
1. Review the attached detailed proposal
2. Schedule a site visit (if desired)
3. Sign agreement and schedule installation

I'm available to answer any questions you may have. Would you like to schedule a call to discuss?

Best regards,
[Your Name]
[Your Company]
[Your Phone]
[Your Email]`

  return { subject, body }
}