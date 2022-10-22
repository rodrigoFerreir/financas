import '../styles/globals.css'
import type { AppProps } from 'next/app'
import { AuthProvider } from '../hooks/AuthContext'

function MyApp({ Component, pageProps }: AppProps) {
  return (
    //@ts-ignore
    <AuthProvider>
      <Component {...pageProps} />
    </AuthProvider>
  )
}

export default MyApp
