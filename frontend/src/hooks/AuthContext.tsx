import React, { createContext, useCallback, useContext, useState } from "react"
import ApiService from "../services/ApiService"
import { parseCookies, setCookie } from 'nookies'


interface TokenState {
    token: string
}
interface AuthContextState {
    token: TokenState
    userData: UserResponse | undefined
    signIn({ email, password }: LoginData): Promise<void>
    userLooged(): boolean
}
interface LoginData {
    email: string
    password: string
}

interface UserResponse {
    _id: string
    name: string
    email: string
    password: string
    avatar: string
}

const AuthContext = createContext<AuthContextState>({} as AuthContextState)
//@ts-ignore
const AuthProvider: React.FC = ({ children }) => {
    //@ts-ignore
    const [userData, setUserData] = useState<UserResponse>()
    const [token, setToken] = useState<TokenState>(() => {
        const cookie_data = parseCookies()
        if (cookie_data.open_finances_token) {
            ApiService.defaults.headers.common['Authorization'] = `Bearer ${cookie_data.open_finances_token}`
            const token = cookie_data.open_finances_token
            getUserInfo()
            return { token }
        }

        return {} as TokenState
    })
    const signIn = useCallback(async ({ email, password }: LoginData) => {
        const response = await ApiService.post('/auth/login', {
            email,
            password
        })
        const { token, dados } = response.data
        setToken(token)
        setCookie(undefined, 'open_finances_token', token, {
            maxAge: 60 * 60 // 1 hour
        })
        setUserData(dados as UserResponse)
        ApiService.defaults.headers.common['Authorization'] = `Bearer ${token}`
    }, [])

    async function getUserInfo(){
        const response = await ApiService.get('/user/me')
        setUserData(response.data.dados as UserResponse)
    }

    const userLooged = useCallback(() => {
        const cookies = parseCookies()
        return cookies.open_finances_token ? true : false
    }, [])

    return (
        <AuthContext.Provider value={{
            token,
            userData,
            signIn,
            userLooged
        }}>
            {children}
        </AuthContext.Provider>
    )
}

function useAuth(): AuthContextState {
    const context = useContext(AuthContext)
    return context

}
export { useAuth, AuthProvider }