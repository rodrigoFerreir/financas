import React, { ReactNode } from "react"
import { useAuth } from "../hooks/AuthContext"
import { FcReadingEbook } from "react-icons/fc"
import LinkMenu from "./LinkMenu"

interface ContentProps {
    children: ReactNode
}

const Content = ({ children }: ContentProps) => {
    const { userData } = useAuth()
    return (
        <main className="bg-gray-100 dark:bg-gray-800 h-screen overflow-hidden relative">
            <div className="flex items-start justify-between">
                <div className="h-screen hidden lg:block shadow-lg relative w-80">
                    <div className="bg-white h-full dark:bg-gray-700">
                        <div className="flex items-center justify-start pt-6 ml-8">
                            <p className="font-bold dark:text-white text-xl">
                                OpenFinances
                            </p>
                        </div>
                        <nav className="mt-6">
                            <div>
                                <LinkMenu href={"/home"}>
                                    <span className="text-left">
                                        <svg width={20} height={20} fill="currentColor" viewBox="0 0 1792 1792" xmlns="http://www.w3.org/2000/svg">
                                            <path d="M1472 992v480q0 26-19 45t-45 19h-384v-384h-256v384h-384q-26 0-45-19t-19-45v-480q0-1 .5-3t.5-3l575-474 575 474q1 2 1 6zm223-69l-62 74q-8 9-21 11h-3q-13 0-21-7l-692-577-692 577q-12 8-24 7-13-2-21-11l-62-74q-8-10-7-23.5t11-21.5l719-599q32-26 76-26t76 26l244 204v-195q0-14 9-23t23-9h192q14 0 23 9t9 23v408l219 182q10 8 11 21.5t-7 23.5z">
                                            </path>
                                        </svg>
                                    </span>
                                    <span className="mx-2 text-sm font-normal">
                                        Home
                                    </span>
                                </LinkMenu>
                                <LinkMenu href={"/accounts"}>
                                    <span className="text-left">
                                        <svg width={20} height={20} fill="currentColor" viewBox="0 0 2048 1792" xmlns="http://www.w3.org/2000/svg">
                                            <path d="M1070 1178l306-564h-654l-306 564h654zm722-282q0 182-71 348t-191 286-286 191-348 71-348-71-286-191-191-286-71-348 71-348 191-286 286-191 348-71 348 71 286 191 191 286 71 348z">
                                            </path>
                                        </svg>
                                    </span>

                                    <span className="mx-2 text-sm font-normal">
                                        Lançamentos
                                        <span className="p-1 ml-4 rounded-lg w-4 h-2 bg-gray-200 text-gray-400 text-xs">
                                            0
                                        </span>
                                    </span>
                                </LinkMenu>
                                <LinkMenu href={"/reports"}>
                                    <span className="text-left">
                                        <svg width={20} height={20} fill="currentColor" viewBox="0 0 1792 1792" xmlns="http://www.w3.org/2000/svg">
                                            <path d="M1728 608v704q0 92-66 158t-158 66h-1216q-92 0-158-66t-66-158v-960q0-92 66-158t158-66h320q92 0 158 66t66 158v32h672q92 0 158 66t66 158z">
                                            </path>
                                        </svg>
                                    </span>
                                    <span className="mx-4 text-sm font-normal">
                                        Relatórios
                                    </span>
                                </LinkMenu>
                                <LinkMenu href={"/planning"}>
                                    <span className="text-left">
                                        <svg width={20} height={20} fill="currentColor" viewBox="0 0 2048 1792" xmlns="http://www.w3.org/2000/svg">
                                            <path d="M580 461q0-41-25-66t-66-25q-43 0-76 25.5t-33 65.5q0 39 33 64.5t76 25.5q41 0 66-24.5t25-65.5zm743 507q0-28-25.5-50t-65.5-22q-27 0-49.5 22.5t-22.5 49.5q0 28 22.5 50.5t49.5 22.5q40 0 65.5-22t25.5-51zm-236-507q0-41-24.5-66t-65.5-25q-43 0-76 25.5t-33 65.5q0 39 33 64.5t76 25.5q41 0 65.5-24.5t24.5-65.5zm635 507q0-28-26-50t-65-22q-27 0-49.5 22.5t-22.5 49.5q0 28 22.5 50.5t49.5 22.5q39 0 65-22t26-51zm-266-397q-31-4-70-4-169 0-311 77t-223.5 208.5-81.5 287.5q0 78 23 152-35 3-68 3-26 0-50-1.5t-55-6.5-44.5-7-54.5-10.5-50-10.5l-253 127 72-218q-290-203-290-490 0-169 97.5-311t264-223.5 363.5-81.5q176 0 332.5 66t262 182.5 136.5 260.5zm592 561q0 117-68.5 223.5t-185.5 193.5l55 181-199-109q-150 37-218 37-169 0-311-70.5t-223.5-191.5-81.5-264 81.5-264 223.5-191.5 311-70.5q161 0 303 70.5t227.5 192 85.5 263.5z">
                                            </path>
                                        </svg>
                                    </span>
                                    <span className="mx-4 text-sm font-normal">
                                        Plano de Contas
                                    </span>
                                </LinkMenu>
                            </div>
                        </nav>
                    </div>
                </div>
                <div className="flex flex-col w-full md:space-y-4">
                    <header className="w-full h-16 z-40 flex items-center justify-between">
                        <div className="block lg:hidden ml-6">
                            <button className="flex p-2 items-center rounded-full bg-white shadow text-gray-500 text-md">
                                <svg width={20} height={20} className="text-gray-400" fill="currentColor" viewBox="0 0 1792 1792" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M1664 1344v128q0 26-19 45t-45 19h-1408q-26 0-45-19t-19-45v-128q0-26 19-45t45-19h1408q26 0 45 19t19 45zm0-512v128q0 26-19 45t-45 19h-1408q-26 0-45-19t-19-45v-128q0-26 19-45t45-19h1408q26 0 45 19t19 45zm0-512v128q0 26-19 45t-45 19h-1408q-26 0-45-19t-19-45v-128q0-26 19-45t45-19h1408q26 0 45 19t19 45z">
                                    </path>
                                </svg>
                            </button>
                        </div>
                        <div className="relative z-20 flex flex-col justify-end h-full px-3 md:w-full">
                            <div className="relative p-1 flex items-center w-full space-x-4 justify-end">
                                {/* <a href="/me" className="block relative">
                                    {userData?.avatar ? <img alt="profil" src={userData?.avatar} className="mx-auto object-cover rounded-full h-10 w-10 " /> : <FcReadingEbook size={40} />}
                                </a> */}
                                <button className="flex items-center text-gray-500 dark:text-white text-md">
                                    {userData?.name}
                                    <svg width={20} height={20} className="ml-2 text-gray-400" fill="currentColor" viewBox="0 0 1792 1792" xmlns="http://www.w3.org/2000/svg">
                                        <path d="M1408 704q0 26-19 45l-448 448q-19 19-45 19t-45-19l-448-448q-19-19-19-45t19-45 45-19h896q26 0 45 19t19 45z">
                                        </path>
                                    </svg>
                                </button>
                            </div>
                        </div>
                    </header>
                    <div className="overflow-auto h-screen pb-24 px-4 md:px-6 no-scrollbar">
                        <h1 className="text-4xl font-semibold text-gray-800 dark:text-white">
                            Bem vindo, {userData?.name}
                        </h1>
                        <h2 className="text-md text-gray-400">
                            Aqui estão suas financas registradas.
                        </h2>
                        <>
                            {children}
                        </>
                    </div>
                </div>
            </div>
        </main>
    )
}

export default Content