import React, { useState, useEffect } from "react"
import Content from "../components/Content"
import ApiService from "../services/ApiService"
import { useForm, SubmitHandler } from "react-hook-form"


interface AccountsProps {
    id?: string
    title: string
    description: string
    value: number
    category: string
    type_account: string
}

const Accounts = () => {
    const [loading, setLoading] = useState(true)
    const [newAccount, setNewAccount] = useState(false)
    const [accounts, setAccounts] = useState<AccountsProps[]>([])
    const { register, handleSubmit } = useForm<AccountsProps>()
    const submit: SubmitHandler<AccountsProps> = async (data) => {
        typeof data.value === 'string' ? data.value = parseFloat(String(data.value)) : data.value
        await ApiService.post("/account/create", {
            ...data
        }).then(res => {
            console.log(res.data)
            setNewAccount(false)
        }).catch(err => {
            console.log(err)
        })
    }
    useEffect(() => {
        setLoading(true)
        async function loadAccounts() {
            await ApiService.get('/account/list')
                .then(res => {
                    setAccounts(res.data.dados)
                })
                .catch(err => {
                    console.log(err)
                }).finally(() => {
                    setLoading(false)
                })
        }
        loadAccounts()
    }, [newAccount])
    return (
        <Content>
            <div className="">
                {!loading &&
                    <>
                        {!newAccount ?
                            <>
                                <div className="mt-5">
                                    <h1 className="font-bold dark:text-white text-xl">Lançamentos</h1>
                                </div>
                                <div className="overflow-x-auto relative">
                                    <div className="ml-auto w-56">
                                        <button
                                            type="button"
                                            className="py-2 px-4  bg-indigo-600 hover:bg-indigo-700 focus:ring-indigo-500 focus:ring-offset-indigo-200 text-white w-full transition ease-in duration-200 text-center text-base font-semibold shadow-md focus:outline-none focus:ring-2 focus:ring-offset-2  rounded-lg"
                                            onClick={() => { setNewAccount(true) }}
                                        >
                                            Novo
                                        </button>
                                    </div>
                                    <table className="w-full text-sm text-left text-gray-500 dark:text-gray-400">
                                        <thead className="text-xs text-gray-900 uppercase dark:text-gray-400">
                                            <tr>
                                                <th scope="col" className="py-3 px-6">
                                                    Titulo
                                                </th>
                                                <th scope="col" className="py-3 px-6">
                                                    Descrição
                                                </th>
                                                <th scope="col" className="py-3 px-6">
                                                    Categoria
                                                </th>
                                                <th scope="col" className="py-3 px-6">
                                                    Tipo
                                                </th>
                                                <th scope="col" className="py-3 px-6">
                                                    Valor
                                                </th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            {accounts.map(item =>
                                                <tr className="bg-white dark:bg-gray-800" key={item.id}>
                                                    <th
                                                        scope="row"
                                                        className="py-4 px-6 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                                                    >
                                                        {item.title}
                                                    </th>
                                                    <td className="py-4 px-6">{item.description}</td>
                                                    <td className="py-4 px-6">{item.category}</td>
                                                    <td className="py-4 px-6">{item.type_account}</td>
                                                    <td className="py-4 px-6">{item.value}</td>
                                                </tr>
                                            )}
                                        </tbody>
                                    </table>
                                </div>
                            </> :
                            <div className="mt-5 w-auto">
                                <div className="mr-auto w-56">
                                    <button
                                        type="button"
                                        className="py-2 px-4  bg-indigo-600 hover:bg-indigo-700 focus:ring-indigo-500 focus:ring-offset-indigo-200 text-white w-full transition ease-in duration-200 text-center text-base font-semibold shadow-md focus:outline-none focus:ring-2 focus:ring-offset-2  rounded-lg"
                                        onClick={() => { setNewAccount(false) }}>
                                        Voltar
                                    </button>
                                </div>
                                <div className="ml-auto mr-auto mt-3 max-w-4xl">
                                    <form onSubmit={handleSubmit(submit)} className="bg-gray-900 dark:text-white rounded-lg shadow sm:w-full sm:mx-auto sm:overflow-hidden">
                                        <div className="px-4 py-8 sm:px-10">
                                            <div className="relative mt-6">
                                                <div className="absolute inset-0 flex items-center">
                                                    <div className="w-full border-t border-gray-300"></div>
                                                </div>
                                                <div className="relative flex justify-center text-sm leading-5">
                                                    <span className="px-2 text-gray-200 bg-gray-900">Novo Lançamento de conta</span>
                                                </div>
                                            </div>
                                            <div className="mt-6">
                                                <div className="w-full space-y-6">
                                                    <div className="grid grid-cols-2">
                                                        <div className="w-96 p-2">
                                                            <div className=" relative ">
                                                                <input
                                                                    type="text"
                                                                    className=" rounded-lg border-transparent flex-1 appearance-none border border-gray-300 w-full py-2 px-4 bg-white text-gray-700 placeholder-gray-400 shadow-sm text-base focus:outline-none focus:ring-2 focus:ring-purple-600 focus:border-transparent"
                                                                    placeholder="Titulo"
                                                                    {...register('title')}
                                                                />
                                                            </div>
                                                        </div>
                                                        <div className="w-96 p-2">
                                                            <div className="relative ">
                                                                <input
                                                                    type="number"
                                                                    step="0.01"
                                                                    className=" rounded-lg border-transparent flex-1 appearance-none border border-gray-300 w-full py-2 px-4 bg-white text-gray-700 placeholder-gray-400 shadow-sm text-base focus:outline-none focus:ring-2 focus:ring-purple-600 focus:border-transparent"
                                                                    placeholder="Valor (R$)"
                                                                    {...register('value')}
                                                                />
                                                            </div>
                                                        </div>


                                                        <div className="w-96 p-2">
                                                            <div className=" relative ">
                                                                <input
                                                                    type="text"
                                                                    id="form-account-category"
                                                                    className=" rounded-lg border-transparent flex-1 appearance-none border border-gray-300 w-full py-2 px-4 bg-white text-gray-700 placeholder-gray-400 shadow-sm text-base focus:outline-none focus:ring-2 focus:ring-purple-600 focus:border-transparent"
                                                                    placeholder="Categoria"
                                                                    {...register('category')}
                                                                />
                                                            </div>
                                                        </div>
                                                        <div className="w-96 p-2">
                                                            <div className=" relative ">
                                                                <select
                                                                    className="rounded-lg border-transparent flex-1 appearance-none border border-gray-300 w-full py-2 px-4 bg-white text-gray-700 placeholder-gray-400 shadow-sm text-base focus:outline-none focus:ring-2 focus:ring-purple-600 focus:border-transparent"
                                                                    placeholder="Tipo RECEITA/DESPESA"
                                                                    {...register('type_account')}
                                                                >
                                                                    <option
                                                                        value={'RECEITA'}
                                                                    >
                                                                        RECEITA
                                                                    </option>
                                                                    <option
                                                                        value={'DESPESA'}
                                                                    >
                                                                        DESPESA
                                                                    </option>
                                                                </select>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div className="w-full">
                                                        <div className=" relative ">
                                                            <textarea
                                                                className=" rounded-lg border-transparent flex-1 appearance-none border border-gray-300 w-full py-2 px-4 bg-white text-gray-700 placeholder-gray-400 shadow-sm text-base focus:outline-none focus:ring-2 focus:ring-purple-600 focus:border-transparent"
                                                                placeholder="Descrição"
                                                                rows={4}
                                                                {...register('description')}
                                                            />
                                                        </div>
                                                    </div>
                                                    <div className="ml-auto max-w-xs">
                                                        <span className="block w-full rounded-md shadow-sm">
                                                            <button
                                                                type="submit"
                                                                className="py-2 px-4  bg-indigo-600 hover:bg-indigo-700 focus:ring-indigo-500 focus:ring-offset-indigo-200 text-white w-full transition ease-in duration-200 text-center text-base font-semibold shadow-md focus:outline-none focus:ring-2 focus:ring-offset-2  rounded-lg "
                                                            >
                                                                Adicionar
                                                            </button>
                                                        </span>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </form>
                                </div>
                            </div>
                        }
                    </>
                }
            </div>
        </Content>
    )
}


export default Accounts