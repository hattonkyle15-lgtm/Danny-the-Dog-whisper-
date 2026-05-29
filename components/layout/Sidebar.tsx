'use client'

import React, { useState, useEffect } from 'react'
import Link from 'next/link'
import { usePathname, useRouter } from 'next/navigation'
import { Button } from '@/components/ui/button'
import { 
  Home, 
  Users, 
  MapPin, 
  Mail, 
  Calendar, 
  FileText, 
  BarChart3, 
  Settings,
  LogOut,
  User
} from 'lucide-react'
import { signOut, getCurrentUser } from '@/lib/supabase'

const navigation = [
  { name: 'Dashboard', href: '/', icon: Home },
  { name: 'Leads', href: '/leads', icon: Users },
  { name: 'Lead Finder', href: '/lead-finder', icon: MapPin },
  { name: 'Outreach', href: '/outreach', icon: Mail },
  { name: 'Follow-Ups', href: '/follow-ups', icon: Calendar },
  { name: 'Proposals', href: '/proposals', icon: FileText },
  { name: 'Analytics', href: '/analytics', icon: BarChart3 },
  { name: 'Settings', href: '/settings', icon: Settings },
]

export default function Sidebar() {
  const pathname = usePathname()
  const router = useRouter()
  const [userEmail, setUserEmail] = useState<string | null>(null)

  useEffect(() => {
    getCurrentUser().then(user => {
      setUserEmail(user?.email || null)
    })
  }, [])

  const handleLogout = async () => {
    try {
      await signOut()
      router.push('/login')
      router.refresh()
    } catch (error) {
      console.error('Error signing out:', error)
    }
  }

  return (
    <div className="flex flex-col w-64 bg-white border-r border-gray-200">
      <div className="flex items-center justify-center h-16 px-4 border-b border-gray-200">
        <h1 className="text-xl font-bold text-primary">Apartment Outreach</h1>
      </div>
      <nav className="flex-1 px-2 py-4 space-y-1">
        {navigation.map((item) => {
          const Icon = item.icon
          const isActive = pathname === item.href
          
          return (
            <Link
              key={item.name}
              href={item.href}
              className={`flex items-center px-4 py-2 text-sm font-medium rounded-md ${isActive
                ? 'bg-primary text-white'
                : 'text-gray-700 hover:bg-gray-100'
                }`}
            >
              <Icon className="w-5 h-5 mr-3" />
              {item.name}
            </Link>
          )
        })}
      </nav>
      <div className="p-4 border-t border-gray-200">
        {userEmail && (
          <div className="flex items-center gap-2 mb-3 px-2">
            <User className="w-4 h-4 text-gray-500" />
            <span className="text-sm text-gray-600 truncate">{userEmail}</span>
          </div>
        )}
        <Button 
          variant="outline" 
          className="w-full flex items-center justify-center gap-2"
          onClick={handleLogout}
        >
          <LogOut className="w-4 h-4" />
          Logout
        </Button>
      </div>
    </div>
  )
}